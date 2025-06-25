from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    """Página de carrinho — verifica se o produto foi adicionado com sucesso."""

    SUCCESS_ALERT = (By.ID, "notification-box-top")

    def is_product_added(self):
        """
        Verifica se a mensagem de sucesso ao adicionar o produto ao carrinho está visível.

        Returns:
            bool: True se a notificação de sucesso estiver presente e contiver o texto esperado.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_ALERT))
            alert_text = element.text.lower()
            print("Texto da notificação:", alert_text)
            return "success: you have added" in alert_text and "shopping cart" in alert_text
        except TimeoutException:
            return False

     
    
