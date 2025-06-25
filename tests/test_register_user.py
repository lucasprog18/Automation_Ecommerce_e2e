import time
from src.pages.register_page import RegisterPage

def test_register_new_user(driver):
    """
    Teste de registro: cria uma nova conta com dados válidos e verifica sucesso.

    Passos:
        1. Acessa a página de cadastro
        2. Preenche o formulário com nome, email único, telefone e senha
        3. Submete o formulário
        4. Verifica se a mensagem de sucesso está visível
    """
    register_page = RegisterPage(driver)
    register_page.open_register_page()

    email = f"lucas_{int(time.time())}@teste.com"   # Garante e-mail único a cada execução
    register_page.register_user(
        first="Lucas",
        last="Tester",
        email=email,
        phone="11999999999",
        password="SenhaFortinha123"
    )

    assert register_page.is_registration_successful()
