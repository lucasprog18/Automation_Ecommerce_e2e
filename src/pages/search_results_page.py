from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SearchResultsPage(BasePage):
    """Página de resultados de busca — lida com listagem e interação com os produtos retornados."""
    RESULT_TITLES = (By.CSS_SELECTOR, ".product-thumb h4 a")

    def get_result_titles(self):
        """
        Retorna uma lista com os nomes de todos os produtos listados na busca.

        Returns:
            list[str]: Lista com os títulos/texto dos resultados encontrados.
        """
        return [el.text for el in self.find_all(self.RESULT_TITLES)]

    def has_results(self):
        """
        Verifica se a busca retornou ao menos um produto.

        Returns:
            bool: True se houver ao menos um item listado, False caso contrário.
        """
        return len(self.get_result_titles()) > 0
    
    def click_first_product(self):
        """
        Aguarda o carregamento dos resultados e clica no primeiro produto da lista.

        Raises:
            Exception: Se nenhum produto for carregado ou o primeiro item não estiver clicável.
        """
        try:
            # Aguarda todos os títulos de produtos estarem presentes no DOM
            self.wait.until(EC.presence_of_all_elements_located(self.RESULT_TITLES))
            
            # Aguarda que o primeiro produto esteja clicável e executa o clique
            first_result = self.wait.until(
                EC.element_to_be_clickable(self.RESULT_TITLES)
            )
            first_result.click()
        except TimeoutException:
            raise Exception("Primeiro produto não clicável ou resultados não carregados.")

