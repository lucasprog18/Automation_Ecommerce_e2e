from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class HomePage(BasePage):
    """Página inicial da loja — permite acesso à home e busca de produtos."""
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search .search-button > button")
    LOGIN_MENU = (By.LINK_TEXT, "Login")

    def open_home(self):
        """Navega até a URL principal da loja."""
        self.driver.get("https://ecommerce-playground.lambdatest.io/")

    def search_product(self, term):
        """
        Realiza uma busca de produto no campo de pesquisa da home.

        Args:
            term (str): Nome ou termo do produto a ser pesquisado.
        """
        self.fill(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)
    

    
