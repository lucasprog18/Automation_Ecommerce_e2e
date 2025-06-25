from src.pages.login_page import LoginPage
from src.data.test_data import VALID_USER, LOGIN_URL

def test_login_success(driver):
    """
    Teste positivo de login: autentica com usuário válido e verifica redirecionamento.

    Passos:
        1. Acessa a página de login
        2. Preenche as credenciais válidas
        3. Submete o formulário
        4. Verifica se houve redirecionamento para a área da conta
    """
    login_page = LoginPage(driver)
    login_page.perform_login(
        email=VALID_USER["email"],
        password=VALID_USER["password"],
        login_url=LOGIN_URL
    )

    # Validação básica: se a URL muda para página da conta
    assert "account" in driver.current_url

