from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import logging

logger = logging.getLogger(__name__)
class DiscoverPage:

    URL = "https://tmdb-discover.surge.sh/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    def open(self):
        self.driver.get(self.URL)
        # Wait until the main content renders
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='css-']"))
        )
        # Wait for key interactive elements to be ready (page fully settled)
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='css-2b097c-container']"))
        )
        # Additional brief wait for React to complete all updates
        import time
        time.sleep(0.5)

    def select_category(self, category):
        """
        Click a category filter (e.g., Top rated) using LINK_TEXT
        """
        element = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, category))
        )
        element.click()

    def select_type(self, value):
        """
        Select type filter (Movie/TV Shows)
        Based on DOM inspection, uses React Select container class
        """
        # Click the React Select container (the dropdown itself)
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='css-2b097c-container']"))
        )
        dropdown.click()

        # Wait for dropdown options to appear and click the appropriate option
        if value == "TV Shows":
            option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-') and text()='TV Shows']"))
            )
        else:  # Movie
            option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-') and text()='Movie']"))
            )

        option.click()

        # Wait for React to update the DOM after type change
        self.wait.until(
            EC.staleness_of(option)
        )

    def get_titles(self):
        """
        Wait for movie/TV cards to load after type/category change
        Handles React rendering delay by waiting for new content
        Cards use 'flex flex-col items-center' classes, not MuiCard
        """
        # First wait for any existing cards to be removed (staleness check)
        try:
            existing_cards = self.driver.find_elements(By.CSS_SELECTOR, "div.flex.flex-col.items-center")
            if existing_cards:
                # Wait for existing cards to become stale (removed from DOM)
                WebDriverWait(self.driver, 5).until(
                    EC.staleness_of(existing_cards[0])
                )
        except:
            pass  # No existing cards found, continue

        # Now wait for new cards to appear (with shorter timeout for known defect scenarios)
        try:
            self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "div.flex.flex-col.items-center")
                )
            )
        except:
            # For known defect scenarios, return empty list if no cards found
            return []

        return self.driver.find_elements(By.CSS_SELECTOR, "div.flex.flex-col.items-center")

    def verify_year_filter_applied(self, expected_start, expected_end):
        """
        Verify that year filtering was actually applied correctly
        Returns True if the dropdowns show the expected values
        """
        try:
            all_dropdowns = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='css-1hwfws3']")
            if len(all_dropdowns) >= 4:
                actual_start = all_dropdowns[2].find_element(By.CSS_SELECTOR, "div[class*='css-1uccc91-singleValue']").text.strip()
                actual_end = all_dropdowns[3].find_element(By.CSS_SELECTOR, "div[class*='css-1uccc91-singleValue']").text.strip()

                logger.info(f"Year filter verification - Expected: {expected_start}-{expected_end}, Actual: {actual_start}-{actual_end}")

                # Check if the values match what we expected to set
                start_correct = actual_start == expected_start
                end_correct = actual_end == expected_end

                if start_correct and end_correct:
                    logger.info("✅ Year filtering applied correctly")
                    return True
                else:
                    logger.error(f"❌ Year filtering failed - Start correct: {start_correct}, End correct: {end_correct}")
                    return False
            else:
                logger.error("Could not find year dropdowns for verification")
                return False
        except Exception as e:
            logger.error(f"Error verifying year filter: {e}")
            return False

    def debug_year_values(self):
        """Debug method to check current year dropdown values"""
        try:
            all_dropdowns = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='css-1hwfws3']")
            if len(all_dropdowns) >= 4:
                start_display = all_dropdowns[2].find_element(By.CSS_SELECTOR, "div[class*='css-1uccc91-singleValue']").text.strip()
                end_display = all_dropdowns[3].find_element(By.CSS_SELECTOR, "div[class*='css-1uccc91-singleValue']").text.strip()
                logger.info(f"DEBUG - Start year: '{start_display}', End year: '{end_display}'")
                logger.info(f"DEBUG - Same year allowed: {start_display == end_display}")
            else:
                logger.warning("Could not find year dropdowns")
        except Exception as e:
            logger.error(f"Error checking year values: {e}")

    def verify_year_filtering(self, start_year, end_year):
        """
        Verify that year filtering is actually applied by checking if the year dropdowns show the selected values
        Year dropdowns are at indices 2 (start) and 3 (end)
        """
        try:
            # Re-find dropdowns to ensure we have fresh references
            all_dropdowns = self.wait.until(
                lambda driver: driver.find_elements(By.CSS_SELECTOR, "div[class*='css-1hwfws3']")
            )

            if len(all_dropdowns) >= 4:  # Need year dropdowns at indices 2 and 3
                # Get the displayed values from the year dropdowns (indices 2 and 3)
                start_display = all_dropdowns[2].find_element(By.CSS_SELECTOR, "div[class*='css-1uccc91-singleValue']").text.strip()
                end_display = all_dropdowns[3].find_element(By.CSS_SELECTOR, "div[class*='css-1uccc91-singleValue']").text.strip()

                # Verify the values match what we selected
                return start_display == start_year and end_display == end_year
            else:
                print(f"Verification - Expected at least 4 dropdowns, found {len(all_dropdowns)}")
                return False
        except Exception as e:
            print(f"Verification - Error checking year values: {e}")
            # If we can't verify, assume filtering didn't work
            return False

    def set_year_range(self, start_year, end_year):
        """
        Set year range for filtering using input fields (Katalon approach)
        Based on Katalon script: click dropdown, use input field, type year, press Enter
        """
        # Set start year using input field approach
        try:
            logger.info(f"Setting start year to {start_year}")

            # Click start year dropdown (based on Katalon XPath)
            start_dropdown = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='root']/div/aside/div/div[3]/div/div/div/div"))
            )
            start_dropdown.click()

            # Find and use the input field
            start_input = self.wait.until(
                EC.element_to_be_clickable((By.ID, "react-select-4-input"))
            )
            start_input.clear()
            start_input.send_keys(start_year)
            start_input.send_keys(Keys.ENTER)

            logger.info(f"Start year {start_year} set successfully")
            time.sleep(1.0)  # Brief wait for UI to settle

        except Exception as e:
            logger.warning(f"Could not set start year {start_year}: {e}")
            return

        # Attempt to set end year using input field approach
        try:
            logger.info(f"Attempting to set end year to {end_year}")

            # Click end year dropdown (based on Katalon XPath)
            end_dropdown = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='root']/div/aside/div/div[3]/div[2]/div/div/div"))
            )
            end_dropdown.click()

            # Find and use the input field
            end_input = self.wait.until(
                EC.element_to_be_clickable((By.ID, "react-select-5-input"))
            )
            end_input.clear()
            end_input.send_keys(end_year)
            end_input.send_keys(Keys.ENTER)

            logger.info(f"End year {end_year} set successfully")
            time.sleep(1.0)  # Brief wait for UI to settle

        except Exception as e:
            logger.warning(f"Could not set end year {end_year}: {e}")
            # This is expected if validation prevents same year selection

        # Final debug check
        try:
            final_dropdowns = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='css-1hwfws3']")
            if len(final_dropdowns) >= 4:
                final_start = final_dropdowns[2].find_element(By.CSS_SELECTOR, "div[class*='css-1uccc91-singleValue']").text.strip()
                final_end = final_dropdowns[3].find_element(By.CSS_SELECTOR, "div[class*='css-1uccc91-singleValue']").text.strip()
                logger.info(f"FINAL RESULT - Start: '{final_start}', End: '{final_end}', Same: {final_start == final_end}")
        except Exception as e:
            logger.error(f"Error in final check: {e}")

