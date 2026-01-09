# TMDB Discover QA Automation Assignment

This repository contains automated test suites for the TMDB Discover demo site (https://tmdb-discover.surge.sh) using Python, Selenium, and Behave (BDD framework).

## 📋 Table of Contents

- [Tests Covered](#tests-covered)
- [Installation & Setup](#installation--setup)
- [Running Tests](#running-tests)
- [Allure Reporting](#allure-reporting)
- [Defects Covered](#defects-covered)
- [Project Structure](#project-structure)
- [Configuration](#configuration)

## 🧪 Tests Covered

### Filter Functionality
- **TC-004**: Verify Top Rated category filter works
- **TC-007**: Verify TV Shows type filter works
- **TC-008**: Verify filtering by year of release (with boundary testing)

### Pagination
- **TC-011**: Verify navigation to the next page (@smoke test)
- **TC-012**: Verify navigation to the previous page (@smoke test)
- **TC-013**: Direct page number navigation
- **TC-016**: Verify pagination behavior on the last page (known defect)

### Negative Test Scenarios
- **TC-015**: Verify behavior when accessing category via direct URL slug (known defect)
- **TC-017**: Verify year range allows same start and end year selection (bug)

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Chrome browser installed

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Arthi26AS/rr-qa-automation-assignment.git
   cd rr-qa-automation-assignment
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install additional tools for Allure reporting (optional):**
   ```bash
   # Install Allure CLI (download from https://github.com/allure-framework/allure2/releases)
   # Or use npm:
   npm install -g allure-commandline
   ```

## ▶️ Running Tests

### Run All Tests
```bash
# Run all feature tests
behave features/

# Run with verbose output
behave features/ --format=pretty
```

### Run Specific Test Suites
```bash
# Run only filter tests
behave features/filters.feature

# Run only pagination tests
behave features/pagination.feature

# Run specific scenario
behave features/pagination.feature --name "User selects last page directly"
```

### Run Smoke Tests Only
```bash
behave features/ --tags=@smoke
```

### Generate HTML Reports
Tests automatically generate HTML reports in the `reports/` folder:
- `reports/test_report.html` - Contains test results with screenshots

## 📊 Allure Reporting

### Generate Allure Results
```bash
# Run tests with Allure formatter
behave features/ --format=allure_behave.formatter:AllureFormatter --out allure-results
```

### View Allure Report
```bash
# Serve Allure report locally
allure serve allure-results

# Generate static HTML report
allure generate allure-results --clean --output allure-report
```

The Allure report will be available at `http://localhost:8080` and includes:
- Test execution timeline
- Step-by-step test details
- Screenshots for failed tests
- Historical trends
- Test categories and severity

## 🐛 Defects Covered

### 1. Access Category via Direct URL (Known Defect)
- **Description**: Direct URL access to categories (e.g., `/popular`) doesn't display results
- **Impact**: Users cannot bookmark or share direct category links
- **Status**: Known issue - test intentionally fails to document this defect
- **Test Case**: `Access category via direct URL (known defect)`

### 2. User Selects Last Page Directly (Known Defect)
- **Description**: Clicking the last page number directly doesn't work properly
- **Impact**: Users cannot navigate directly to the last page of results
- **Status**: Known issue - test intentionally fails to document this defect
- **Test Case**: `User selects last page directly (known defect)`

### 3. Year Range Same Start/End Year (Bug)
- **Description**: Application doesn't properly handle when start and end year are the same
- **Impact**: Users cannot filter content for a specific single year
- **Status**: Bug - test fails and captures screenshot for debugging
- **Test Case**: `Verify year range allows same start and end year selection`

## 📁 Project Structure

```
rr-qa-automation-assignment/
├── features/                    # BDD feature files and step definitions
│   ├── filters.feature         # Filter functionality test scenarios
│   ├── pagination.feature      # Pagination test scenarios
│   ├── steps/                  # Step definition implementations
│   │   ├── filter_steps.py
│   │   └── pagination_steps.py
│   └── environment.py          # Test setup/teardown and reporting
├── pages/                      # Page Object Model classes
│   └── discover_page.py        # TMDB Discover page interactions
├── utils/                      # Utility modules
│   ├── driver_factory.py       # WebDriver setup and configuration
│   ├── logger.py              # Logging configuration
│   └── config.py              # Configuration settings
├── reports/                    # Generated test reports and screenshots
├── logs/                       # Application logs
├── testcases/                  # Test documentation
│   ├── TestCases.md           # Comprehensive test case documentation
│   └── TestStrategy.md        # Test strategy and approach
├── allure-results/            # Allure test results
├── requirements.txt           # Python dependencies
├── allure_config.json         # Allure configuration
└── README.md                  # This file
```

## ⚙️ Configuration

### Browser Configuration
- Tests run on Chrome browser by default
- WebDriver is automatically managed by `webdriver-manager`
- Browser runs in maximized mode with disabled notifications

### Test Data
- Application URL: `https://tmdb-discover.surge.sh`
- Test categories: "Top rated", "TV Shows"
- Test years: 1900-2025 range

### Logging
- Logs are written to `logs/automation.log`
- Log levels: INFO for general execution, ERROR for failures
- Console output includes test progress and results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-test`)
3. Commit your changes (`git commit -am 'Add new test case'`)
4. Push to the branch (`git push origin feature/new-test`)
5. Create a Pull Request

## 📄 Documentation

- **[Test Cases](testcases/TestCases.md)**: Comprehensive manual test case documentation
- **[Test Strategy](testcases/TestStrategy.md)**: Testing approach and methodology

## 📞 Support

For questions or issues:
- Create an issue in the [GitHub repository](https://github.com/Arthi26AS/rr-qa-automation-assignment.git)
- Check the logs in `logs/automation.log` for detailed execution information

---

**Repository**: https://github.com/Arthi26AS/rr-qa-automation-assignment.git
