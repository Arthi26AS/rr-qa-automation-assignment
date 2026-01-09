from utils.driver_factory import get_driver
from utils.logger import setup_logging
import os
import logging
import pytest

# Use named logger for better log categorization
logger = logging.getLogger("test.lifecycle")

# Store test results for HTML report
test_results = []


def before_all(context):
    """Setup logging at the start of test execution"""
    setup_logging()
    logger.info("Test execution start - Scenario heading")


def before_scenario(context, scenario):
    """Setup before each scenario"""
    logger.info(f"=== SCENARIO: {scenario.name} ===")
    logger.info("Browser launch")
    context.driver = get_driver()
    logger.info("Browser launched successfully")

    # Initialize test result
    context.test_result = {
        'name': scenario.name,
        'feature': scenario.feature.name,
        'start_time': None,
        'end_time': None,
        'status': 'unknown',
        'error': None,
        'screenshot': None
    }


def after_scenario(context, scenario):
    """Cleanup after each scenario"""
    if scenario.status == "failed":
        logger.error("Test failure / exception occurred")
        logger.error(f"Scenario failed: {scenario.name}")

        # Take screenshot
        os.makedirs("reports", exist_ok=True)
        screenshot_path = f"reports/{scenario.name}.png"
        context.driver.save_screenshot(screenshot_path)

        # Update test result
        context.test_result['status'] = 'failed'
        context.test_result['screenshot'] = screenshot_path

        # Capture the actual assertion error message
        error_msg = "Test assertion failed"
        if hasattr(scenario, 'exception') and scenario.exception:
            error_msg = str(scenario.exception)
        elif hasattr(scenario, 'error_message'):
            error_msg = scenario.error_message
        else:
            # Try to get the last step's error
            for step in scenario.steps:
                if step.status == 'failed' and hasattr(step, 'exception'):
                    error_msg = str(step.exception)
                    break

        context.test_result['error'] = error_msg

        # Add to results list
        test_results.append(context.test_result)
        logger.info(f"Added failed test result to report: {context.test_result['name']}")

        # Generate HTML report immediately for failed tests
        generate_html_report(test_results)

    else:
        logger.info(f"Scenario passed: {scenario.name}")
        context.test_result['status'] = 'passed'
        test_results.append(context.test_result)
        logger.info(f"Added passed test result to report: {context.test_result['name']}")

    logger.info("Browser teardown")
    context.driver.quit()
    logger.info("Browser closed")


def after_all(context):
    """Generate HTML report after all tests"""
    logger.info("All scenarios completed - Test execution finished")
    logger.info(f"Total test results collected: {len(test_results)}")

    # Generate simple HTML report
    if test_results:
        generate_html_report(test_results)
        logger.info(f"Generated HTML report with {len(test_results)} test results")
    else:
        logger.warning("No test results to generate HTML report")
        # Generate a basic report anyway for debugging
        generate_html_report([{
            'name': 'No tests executed',
            'feature': 'Unknown',
            'status': 'unknown',
            'error': 'No test results were collected',
            'screenshot': None
        }])


def generate_html_report(results):
    """Generate a simple HTML report with test results and screenshots"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>QA Automation Test Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .passed {{ color: green; }}
            .failed {{ color: red; }}
            .unknown {{ color: orange; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            img {{ max-width: 300px; max-height: 200px; }}
        </style>
    </head>
    <body>
        <h1>QA Automation Test Report</h1>
        <p><strong>Feature:</strong> Filter functionality</p>
        <p><strong>Total Tests:</strong> {len(results)}</p>
        <p><strong>Passed:</strong> <span class="passed">{len([r for r in results if r['status'] == 'passed'])}</span></p>
        <p><strong>Failed:</strong> <span class="failed">{len([r for r in results if r['status'] == 'failed'])}</span></p>

        <h2>Test Results</h2>
        <table>
            <tr>
                <th>Test Name</th>
                <th>Status</th>
                <th>Error Message</th>
                <th>Screenshot</th>
            </tr>
    """

    for result in results:
        status_class = result['status']
        error_msg = result['error'] or 'N/A'
        screenshot_html = f'<img src="{os.path.basename(result["screenshot"])}" alt="Screenshot">' if result['screenshot'] else 'N/A'

        html_content += f"""
            <tr>
                <td>{result['name']}</td>
                <td class="{status_class}">{result['status'].upper()}</td>
                <td>{error_msg}</td>
                <td>{screenshot_html}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    # Save HTML report
    os.makedirs("reports", exist_ok=True)
    with open("reports/test_report.html", "w") as f:
        f.write(html_content)

    logger.info("HTML test report generated: reports/test_report.html")
