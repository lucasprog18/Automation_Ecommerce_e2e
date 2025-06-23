from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    ERROR_ALERT = (By.CLASS_NAME, "alert-danger")

    def open_login_page(self, login_url):
        self.driver.get(login_url)

    def enter_email(self, email):
        self.fill(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def perform_login(self, email, password, login_url):
        self.open_login_page(login_url)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def login_failed(self):
        return self.is_element_present(self.ERROR_ALERT)
