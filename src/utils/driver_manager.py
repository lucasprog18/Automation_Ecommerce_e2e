from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_driver():
    """
    Cria e retorna uma instância configurada do Chrome WebDriver para uso nos testes.

    Retorna:
        WebDriver: navegador com opções ajustadas para ambiente de automação.
    """
    options = Options()
    options.add_argument('--start-maximized')         # Abre o navegador em tela cheia
    options.add_argument('--disable-notifications')   # Bloqueia notificações do navegador
    options.add_argument('--disable-infobars')        # Remove barra de informação "Chrome está sendo controlado..."
    options.add_experimental_option("excludeSwitches", ["enable-automation"])   # Remove flag visual de automação

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver
