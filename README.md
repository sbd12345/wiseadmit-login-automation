# Five Things That Could Break the Sign-In Process in the Future

1) Changes to field locators or UI structure
  - If the email/password input IDs, XPaths, or component names change, automated tests and the sign-in flow may fail.

2) Backend API changes
  - Updates to authentication endpoints, payload structure, or error messages may cause login attempts to fail.

3) Rate-limiting or security rules
  - New throttling mechanisms, captcha requirements, or IP restrictions could block automated logins.

4) Invalid or expired test credentials
  - If the test user is removed, disabled, or password reset rules change, login will fail.

5) Network or server outages
  - Downtime, slow API response, or database connection failures can completely break login functionality.


# five improvements for the website.

1) More stable input field IDs
  - Current IDs like :r0: and :r1: are dynamically generated and unstable; they change frequently, causing automation issues.

2) More descriptive and consistent error messages
   - Errors such as “Failed to get student” should be more user-friendly and standardized.

3) Show password visibility toggle
  - Adding a “Show Password” icon improves user experience.

4) Add validation messages below each input field
  - Example:
      “Email is required”
      “Password must be at least 6 characters”

5) Add a loading indicator during authentication
   - When the login API is processing, show a spinner or “Signing in…” text to avoid user confusion.
   

# Project Overview

This project automates:
- Positive Sign-In (valid email + valid password)
Negative Sign-In scenarios:
- Invalid Email
- Invalid Password

- Verification of error messages
- Secure handling of credentials using fixtures
- Assertions for login success & failures
- HTML reporting
- POM architecture

# Project Structure
project/
│── pages/
│   ├── base_page.py
│   ├── login_page.py
│
│── tests/
│   ├── test_login.py
│
│── utils/
│   ├── driver_factory.py
│
│── data/
│   ├── testdata.yaml
│
│
│── README.md
│── requirements.txt

# Installation & Setup
1) Install Dependencies
- pip install -r requirements.txt

# Running Tests
- Run all tests = pytest
- Run a specific test = pytest tests/test_login.py

# Generating Reports
1) Generate HTML Report
- pytest --html=report.html

# Test Data
- Data store = data/testdata.yaml

# Test Cases (excel)
1) Test Case sheet
Test cases are maintained in the Excel sheet:
[data/test-cases.xlsx](./data/test-cases.xlsx)


# Prerequisites
- Python 3.10+
- Git
- Google Chrome 
- ChromeDriver (managed automatically via webdriver-manager)

# Submission Notes
- Repository: https://github.com/sbd12345/wiseadmit-login-automation
- Ensure credentials are never hardcoded in test scripts.
- HTML test report is available in report/test_login_report.html.