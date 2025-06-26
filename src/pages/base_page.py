from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException


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

    def wait_for_notification_to_disappear(self):
        """
        Aguarda o desaparecimento do alerta de notificação flutuante.
        Útil para evitar sobreposição de cliques em outros elementos.
        """
        try:
            self.wait.until(EC.invisibility_of_element_located((By.ID, "notification-box-top")))
        except TimeoutException:
            pass  # Continua mesmo que leve um pouco mais

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """
        Aguarda até que o elemento esteja clicável.

        Args:
            locator (tuple): Localizador no formato (By.X, "seletor").
            timeout (int): Tempo máximo de espera em segundos.
        Returns:
            WebElement: Elemento pronto para interação.
        """
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click_if_exists(self, locator, timeout=4):
        """
        Clica no elemento se ele estiver presente e clicável dentro do tempo limite.
        Ignora silenciosamente se não aparecer.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element: WebElement = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            pass

    def select_by_visible_text(self, locator, text):
        """
        Seleciona uma opção de um dropdown pelo texto visível.

        Args:
            locator (tuple): seletor do elemento <select>
            text (str): opção que será selecionada
        """
        element = self.driver.find_element(*locator)
        Select(element).select_by_visible_text(text)

    def focus_and_fill(self, locator, value):
        """
        Dá foco no campo, insere o valor e desfoca — para disparar eventos do DOM.
        """
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        element.clear()
        element.send_keys(value)
        # dispara blur para event listeners
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('blur'))", element)

    def wait_and_select_by_visible_text(self, locator, text, timeout=10):
        """
        Aguarda até que a opção desejada esteja presente e seleciona por texto visível.
        Evita StaleElementReferenceException realocando o elemento dentro da checagem.
        """

    def scroll_into_view(self, locator):
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    





    



                
    

