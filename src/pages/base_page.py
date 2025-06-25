from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    """Classe base para todas as páginas, com métodos reutilizáveis de interação e verificação."""
    def __init__(self, driver: WebDriver):
        """
        Inicializa com a instância do WebDriver e define tempo padrão de espera.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_visible(self, locator):
        """
        Verifica se o elemento está visível na tela.

        Returns:
            bool: True se visível, False caso contrário.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False


    def click(self, locator):
        """
        Espera até o elemento estar clicável e executa o clique.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f"Elemento {locator} não clicável.")

    def fill(self, locator, text):
        """
        Limpa e preenche um campo de texto com o valor fornecido.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise Exception(f"Elemento {locator} não visível para preenchimento.")

    def get_text(self, locator):
        """
        Retorna o texto visível de um elemento localizado.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            raise Exception(f"Não foi possível obter texto do elemento {locator}.")

    def is_element_present(self, locator):
        """
        Verifica se o elemento está presente no DOM (independente de visibilidade).
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def find_all(self, locator):
        """
        Retorna todos os elementos encontrados pelo locator.
        """
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise Exception(f"Elementos {locator} não encontrados.")
        
    def type(self, locator, text):
        """
        Digita texto em um campo localizado (versão alternativa sem espera explícita).
        """
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        
    

