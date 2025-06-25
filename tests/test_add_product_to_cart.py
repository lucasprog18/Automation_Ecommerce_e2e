from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

def test_add_product_to_cart(driver):
    """
    Teste de fluxo E2E: busca por produto, adição ao carrinho e verificação da notificação de sucesso.

    Passos:
        1. Abre a página inicial
        2. Busca pelo produto "iPod Nano"
        3. Clica no primeiro resultado da busca
        4. Adiciona o produto ao carrinho
        5. Verifica se a notificação confirma a adição com sucesso
    """
    home_page = HomePage(driver)
    search_page = SearchResultsPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    home_page.open_home()
    home_page.search_product("iPod Nano")
    search_page.click_first_product()
    product_page.add_to_cart()

    assert cart_page.is_product_added()
