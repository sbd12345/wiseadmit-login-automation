from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, ":r0:")
    PASSWORD_INPUT = (By.ID, ":r1:")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_TEXT = (By.XPATH, "//div[@class='MuiStack-root css-u4p24i']")
    Dashboard_page = (By.XPATH, "//span[contains(text(),'Welcome to WiseAdmit')]")

    def open_page(self):
        self.driver.get("https://www.wiseadmit.io/applynow")

    def enter_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.LOGIN_BUTTON)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_password_visible(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.PASSWORD_INPUT)
            )
            return True
        except:
            return False

    def is_logged_in(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.Dashboard_page)
            )
            return True
        except:
            return False

    def get_error(self):
        return self.get_text(self.ERROR_TEXT)

