from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from src.pages.base_page import BasePage
import time

class CheckoutPage(BasePage):
    """Checkout ultrarresiliente que clica no botão de termos e 'Continuar' custe o que custar."""

    TERMS_CHECKBOX = (By.NAME, "agree")
    CONFIRM_BUTTON = (By.ID, "button-confirm")
    CONFIRMATION_HEADER = (By.CSS_SELECTOR, "#content h1")
    LOGIN_RADIO_LABEL = (By.CSS_SELECTOR, "label[for='input-account-login']")
    BILLING_FIRST = (By.ID, "input-payment-firstname")
    BILLING_LAST = (By.ID, "input-payment-lastname")
    BILLING_ADDRESS1 = (By.ID, "input-payment-address-1")
    BILLING_CITY = (By.ID, "input-payment-city")
    BILLING_POSTCODE = (By.ID, "input-payment-postcode")
    BILLING_COUNTRY = (By.ID, "input-payment-country")
    BILLING_REGION = (By.ID, "input-payment-zone")
    ORDER_SUCCESS_TITLE = (By.CSS_SELECTOR, "#content h1")

    def accept_terms_and_continue(self):
        self.fill(self.BILLING_FIRST, "Lucas")
        self.fill(self.BILLING_LAST, "QA")
        self.fill(self.BILLING_ADDRESS1, "Rua Teste 123")
        self.fill(self.BILLING_CITY, "São Paulo")
        self.fill(self.BILLING_POSTCODE, "01000-000")
        self.select_by_visible_text(self.BILLING_COUNTRY, "Brazil")

        def region_loaded(driver):
            try:
                el = driver.find_element(*self.BILLING_REGION)
                return any(opt.text.strip() == "São Paulo" for opt in Select(el).options)
            except StaleElementReferenceException:
                return False

        self.wait.until(region_loaded)
        Select(self.driver.find_element(*self.BILLING_REGION)).select_by_visible_text("São Paulo")
        self.driver.execute_script("arguments[0].blur();",
            self.driver.find_element(*self.BILLING_POSTCODE)
        )

        checkbox = self.driver.find_element(*self.TERMS_CHECKBOX)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
        try:
            self.wait.until(EC.element_to_be_clickable(self.TERMS_CHECKBOX))
            checkbox.click()
        except:
            self.driver.execute_script("arguments[0].click();", checkbox)

        continue_btn = self.driver.find_element(By.ID, "button-save")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_btn)
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, "button-save")))
            continue_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", continue_btn)

    def confirm_order(self):
        print("💥 Forçando clique no botão de aceite e botão continuar da etapa de pagamento...")

        try:
            checkbox = self.driver.find_element(By.ID, "input-agree")
            self.driver.execute_script("""
                arguments[0].checked = true;
                arguments[0].dispatchEvent(new Event('input'));
                arguments[0].dispatchEvent(new Event('change'));
                arguments[0].dispatchEvent(new Event('click'));
            """, checkbox)
            print("✅ Checkbox 'input-agree' marcado à força.")
        except Exception as e:
            print(f"⚠️ Falha ao marcar checkbox 'input-agree': {e}")

        try:
            label = self.driver.find_element(By.CSS_SELECTOR, "label[for='input-agree']")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
            self.driver.execute_script("arguments[0].click();", label)
            print("✅ Clique no label de aceite executado.")
        except Exception as e:
            print(f"⚠️ Falha ao clicar no label: {e}")

        time.sleep(1)  # Aguarda backend processar aceite
        try:
            button = self.driver.find_element(By.ID, "button-payment-method")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            self.driver.execute_script("arguments[0].click();", button)
            print("✅ Botão 'Continuar' clicado à força.")
        except Exception as e:
            print(f"❌ Erro ao clicar no botão 'Continuar': {e}")

        try:
            self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
            self.scroll_into_view(self.CONFIRM_BUTTON)
            self.click(self.CONFIRM_BUTTON)
            print("✅ Pedido confirmado com sucesso.")
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            print(f"🚨 Alerta inesperado: {alert.text}")
            alert.accept()
            raise Exception("❌ Confirmação falhou por alerta.")
        except Exception as e:
            print(f"❌ Falha na confirmação do pedido: {e}")

    def select_login_option(self):
        self.click(self.LOGIN_RADIO_LABEL)

    def assert_order_success(self):
        self.wait.until(lambda driver: "success" in driver.current_url)
        success_text = self.get_text(self.ORDER_SUCCESS_TITLE)
        assert "Your order has been placed!" in success_text, \
            f"⚠️ Mensagem inesperada: {success_text}"
        
    def fill_billing_address(self, first="Lucas", last="QA", address="Rua Teste 123",
                         city="São Paulo", postcode="01000-000", country="Brazil", region="São Paulo"):
        """
        Preenche os campos de endereço de cobrança no checkout.
        Pode ser usado como método auxiliar reutilizável.
        """

        print("🧾 Preenchendo endereço de cobrança...")
        self.fill(self.BILLING_FIRST, first)
        self.fill(self.BILLING_LAST, last)
        self.fill(self.BILLING_ADDRESS1, address)
        self.fill(self.BILLING_CITY, city)
        self.fill(self.BILLING_POSTCODE, postcode)

        self.select_by_visible_text(self.BILLING_COUNTRY, country)

        def region_ready(driver):
            try:
                el = driver.find_element(*self.BILLING_REGION)
                return any(opt.text.strip() == region for opt in Select(el).options)
            except StaleElementReferenceException:
                return False

        self.wait.until(region_ready)
        Select(self.driver.find_element(*self.BILLING_REGION)).select_by_visible_text(region)

        self.driver.execute_script(
            "arguments[0].blur();",
            self.driver.find_element(*self.BILLING_POSTCODE)
        )

        print("✅ Endereço de cobrança preenchido.")


