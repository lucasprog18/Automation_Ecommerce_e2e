from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage

def test_search_product(driver):
    """
    Teste de busca por produto: realiza pesquisa e verifica se há resultados visíveis.

    Passos:
        1. Abre a home do site
        2. Realiza a busca por "Macbook"
        3. Verifica se a lista de produtos foi retornada com sucesso
    """
    home_page = HomePage(driver)
    results_page = SearchResultsPage(driver)

    home_page.open_home()
    home_page.search_product("Macbook")

    assert results_page.has_results()
