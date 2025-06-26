from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CartPage(BasePage):
    """Página de carrinho — acessa a tela 'View Cart' a partir do topo do site."""

    SUCCESS_ALERT = (By.ID, "notification-box-top")
    CART_ICON = (By.ID, "entry_217825")  # ID do container superior que segura o dropdown de carrinho
    VIEW_CART_BUTTON = (By.LINK_TEXT, "View Cart")
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")
    
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
        
    def go_to_cart(self):
        """
        Realiza scroll, aguarda elementos visíveis e clica via JavaScript no 'View Cart'.
        Ideal para lidar com sobreposições, delays e menus suspensos.
        """
        try:
            cart = self.wait.until(EC.presence_of_element_located(self.CART_ICON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", cart)
            ActionChains(self.driver).move_to_element(cart).perform()

            view_cart = self.wait.until(EC.element_to_be_clickable(self.VIEW_CART_BUTTON))
            self.driver.execute_script("arguments[0].click();", view_cart)
        except TimeoutException:
            raise Exception("Não foi possível abrir o carrinho — elemento invisível ou inacessível.")
    
    def click_checkout(self):
        """Clica no botão 'Checkout' presente na página do carrinho."""
        self.click(self.CHECKOUT_BUTTON)

     
    
