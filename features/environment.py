from utils.driver_factory import get_driver
import os


def before_scenario(context, scenario):
    context.driver = get_driver()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("reports", exist_ok=True)
        screenshot_path = f"reports/{scenario.name}.png"
        context.driver.save_screenshot(screenshot_path)
    context.driver.quit()
