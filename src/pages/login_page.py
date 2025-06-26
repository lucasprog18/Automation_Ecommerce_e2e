from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    """Página de login — encapsula ações de autenticação no sistema."""
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    ERROR_ALERT = (By.CLASS_NAME, "alert-danger")

    def open_login_page(self, login_url):
        """Acessa a página de login usando a URL fornecida."""
        self.driver.get(login_url)

    def enter_email(self, email):
        """Preenche o campo de email no formulário de login."""
        self.fill(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Preenche o campo de senha no formulário de login."""
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Clica no botão para submeter o formulário de login."""
        self.click(self.LOGIN_BUTTON)

    def perform_login(self, email, password, login_url):
        """
        Executa o fluxo completo de login com email e senha.

        Args:
            email (str): Endereço de e-mail do usuário.
            password (str): Senha associada ao e-mail.
            login_url (str): URL da página de login.
        """
        self.open_login_page(login_url)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def login_failed(self):
        """Verifica se uma mensagem de erro de login foi exibida."""
        return self.is_element_present(self.ERROR_ALERT)
    
    def login_from_checkout(self, email, password):
        """
        Preenche o formulário de login embutido na página de checkout.
        """
        self.fill((By.ID, "input-login-email"), email)
        self.fill((By.ID, "input-login-password"), password)
        self.click((By.ID, "button-login"))

