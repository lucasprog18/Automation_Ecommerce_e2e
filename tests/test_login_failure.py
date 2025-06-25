from src.pages.login_page import LoginPage
from src.data.test_data import LOGIN_URL

def test_login_failure(driver):
    """
    Teste negativo de login: insere credenciais inválidas e valida exibição de mensagem de erro.

    Passos:
        1. Acessa a página de login
        2. Preenche e-mail e senha incorretos
        3. Verifica que o sistema apresenta alerta de falha na autenticação
    """
    login_page = LoginPage(driver)
    login_page.perform_login(
        email="wrong@example.com",
        password="invalid123",
        login_url=LOGIN_URL
    )

    assert login_page.login_failed()
