import pytest
import yaml
from pages.login_page import LoginPage
from utils.driver_factory import get_driver
from pathlib import Path

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def testdata():
    current_file_dir = Path(__file__).parent
    yaml_file_path = current_file_dir.parent / "data" / "testdata.yaml"
    if not yaml_file_path.exists():
        pytest.fail(f"Test data file not found at: {yaml_file_path}")

    with open(yaml_file_path, 'r') as f:
        return yaml.safe_load(f)

def test_positive_login(driver, testdata):
    page = LoginPage(driver)
    page.open_page()
    page.enter_email(testdata["valid_email"])
    assert page.is_password_visible(), "Password field did not appear after entering valid email"

    page.enter_password(testdata["valid_password"])
    assert page.is_logged_in()

def test_invalid_email(driver, testdata):
    page = LoginPage(driver)
    page.open_page()

    page.enter_email(testdata["invalid_email"])
    assert not page.is_password_visible(), "Password field should not appear for invalid email"
    assert "Failed to get student" in page.get_error()

def test_invalid_password(driver, testdata):
    page = LoginPage(driver)
    page.open_page()

    page.enter_email(testdata["valid_email"])
    assert page.is_password_visible(), "Password field did not appear after valid email"
    page.enter_password(testdata["invalid_password"])
    assert "Invalid Credentials" in page.get_error()
