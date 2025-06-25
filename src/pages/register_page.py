from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class RegisterPage(BasePage):
    """Página de registro — permite cadastrar um novo usuário no sistema."""
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-primary")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content h1")

    def open_register_page(self):
        """Acessa diretamente a página de registro de usuário."""
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

    def register_user(self, first, last, email, phone, password):
        """
        Preenche o formulário de registro com os dados fornecidos e o submete.

        Args:
            first (str): Primeiro nome.
            last (str): Sobrenome.
            email (str): Email único e válido.
            phone (str): Número de telefone.
            password (str): Senha da conta.
        """
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)
        self.type(self.TELEPHONE, phone)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, password)
        self.click(self.SUBMIT_BUTTON)

    def is_registration_successful(self):
        """Verifica se o título de sucesso da criação de conta está visível."""
        return self.is_visible(self.SUCCESS_MESSAGE)
