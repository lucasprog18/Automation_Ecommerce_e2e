from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.login_page import LoginPage

def test_checkout_success(driver):
    home = HomePage(driver)
    search = SearchResultsPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    login = LoginPage(driver)

    # 1. Acessa a home
    home.open_home()

    # 2. Busca o produto e adiciona ao carrinho
    home.search_product("iPod Nano")
    search.click_first_product()
    product.add_to_cart()

    # 3. Vai para o carrinho e clica em “Checkout”
    cart.go_to_cart()
    cart.click_checkout()
    checkout.select_login_option()


    # 4. Faz login com usuário existente
    login.login_from_checkout("lucasprog1810@gmail.com", "Prog#864920")

    # 5. Preenche os campos Billing Address (obrigatórios)
    checkout.fill_billing_address()

    
    # 6. Continua o checkout já autenticado
    checkout.accept_terms_and_continue()
    checkout.confirm_order()

    # 7. Valida sucesso
    checkout.assert_order_success()

