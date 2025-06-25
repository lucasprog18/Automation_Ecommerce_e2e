from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    """Página de produto — permite interagir com ações específicas de um item."""
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.button-cart")


    def add_to_cart(self):
        """
        Adiciona o produto ao carrinho utilizando clique via JavaScript.

        Força o scroll até o botão e executa o clique, contornando eventuais
        bloqueios de visibilidade, overlays ou animações CSS.

        Levanta uma exceção com mensagem detalhada caso a ação falhe.
        """
        try:
            element = self.driver.find_element(*self.ADD_TO_CART_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            raise Exception(f"Erro ao clicar no botão 'Add to Cart': {e}")



