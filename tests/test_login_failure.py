from src.pages.login_page import LoginPage
from src.data.test_data import LOGIN_URL

def test_login_failure(driver):
    login_page = LoginPage(driver)
    login_page.perform_login(
        email="wrong@example.com",
        password="invalid123",
        login_url=LOGIN_URL
    )

    assert login_page.login_failed()
