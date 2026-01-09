from behave import given, when, then
from pages.discover_page import DiscoverPage
import logging

logger = logging.getLogger("step.verification")


@given("user is on discover page")
def step_open_discover(context):
    context.page = DiscoverPage(context.driver)
    context.page.open()


@when('user selects "{category}" category')
def step_select_category(context, category):
    context.page.select_category(category)


@when('user selects "{type_value}" type')
def step_select_type(context, type_value):
    context.page.select_type(type_value)


@given('user accesses discover page with "{slug}" slug')
def step_open_with_slug(context, slug):
    context.driver.get(f"https://tmdb-discover.surge.sh/{slug}")
    context.page = DiscoverPage(context.driver)


@when('user sets year range from "{start_year}" to "{end_year}"')
def step_set_year_range(context, start_year, end_year):
    context.page.set_year_range(start_year, end_year)
    # Store expected values for verification
    context.year_range_start = start_year
    context.year_range_end = end_year


@then("movie results should be displayed")
def step_verify_results(context):
    logger.info("step_verify_results called")
    results = context.page.get_titles()
    logger.info(f"Found {len(results)} results")
    assert len(results) > 0, "Expected movie results but none were displayed"

    # For year range scenarios, verify that year filtering actually worked
    if hasattr(context, 'year_range_start') and hasattr(context, 'year_range_end'):
        logger.info("Verifying year range filtering worked correctly")
        year_filter_applied = context.page.verify_year_filter_applied(context.year_range_start, context.year_range_end)
        assert year_filter_applied, f"Year filtering failed - should show results for {context.year_range_start}-{context.year_range_end} only"

    # Debug: Always check year values for troubleshooting
    logger.info("About to call debug_year_values()")
    context.page.debug_year_values()
    logger.info("Finished calling debug_year_values()")
