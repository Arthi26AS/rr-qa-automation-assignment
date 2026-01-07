# Test Strategy – TMDB Discover Demo Site

## 1. Objective
The objective of this testing effort is to validate the core functionality of the TMDB Discover demo site. The focus is on verifying that filtering options and pagination work as expected and that the data displayed on the UI is consistent with the data returned by backend API calls. The strategy also considers known limitations of the demo application and includes negative test scenarios to observe system behavior under failure conditions.

---

## 2. Scope

### In Scope
- Validation of filtering options including category, title search, content type, year of release, rating, and genre.
- Verification of pagination behavior across different result pages.
- Basic validation of API responses triggered by UI interactions to ensure data consistency.
- Negative test cases based on known issues mentioned in the assignment and issues observed during testing.

### Out of Scope
- Performance or load testing.
- Security testing.
- Cross-browser compatibility testing.
- Full CI/CD pipeline implementation (only the approach will be documented).

---

## 3. Test Approach

### UI Testing
UI testing will focus on user-facing functionality such as applying filters, navigating between pages, and verifying that results update correctly. Tests will simulate real user actions to ensure the application behaves as expected under normal usage.

### API Validation
Where applicable, network calls triggered by UI actions will be observed and validated. This includes checking request parameters and basic response details to ensure that the data shown on the UI aligns with the API responses.

### Reporting
Test execution results will be generated in both console and HTML formats to provide clear visibility into passed and failed test cases. Reports will be easy to review and suitable for sharing with stakeholders.

### Logging
Logging will be added to capture key steps during test execution. This will help in understanding test flow and in troubleshooting failures without needing to rerun tests multiple times.

### Defect Reporting
For failed test cases, relevant details such as screenshots, logs, and steps to reproduce will be captured. Identified defects will be documented clearly to reflect real-world bug reporting practices.

---

## 4. Test Design Techniques
The following test design techniques will be used to ensure effective coverage without unnecessary duplication:

- Equivalence Partitioning to group similar input conditions for filters.
- Boundary Value Analysis, especially for pagination limits and year-based filtering.
- Negative Testing to validate application behavior for invalid inputs and known problem areas.

---

## 5. Deliverables
The following artifacts will be provided as part of this assignment:
- Automated test scripts covering selected functional scenarios.
- A test case document describing manual test scenarios.
- A README file explaining project setup, execution steps, and CI integration approach.
- Test execution reports and a summary of identified defects.

---

## 6. Tools and Frameworks
The automation solution will be built using commonly used and well-supported tools to keep the setup simple and maintainable:

- Programming Language: Python
- Test Framework: Pytest
- UI Automation: Selenium or Playwright
- API Validation: Requests library
- Reporting: Pytest-HTML or Allure
- Logging: Python logging module

---

## 7. CI Integration Approach
Although CI integration will not be implemented as part of this assignment, the intended approach would involve using a CI tool such as GitHub Actions or Jenkins. The pipeline would install dependencies, execute tests in headless mode, and generate test reports. Test results and reports would be archived for review after each run.
