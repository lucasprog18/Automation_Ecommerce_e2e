import pytest
from src.utils.driver_manager import get_driver



@pytest.fixture
def driver():
    """
    Inicializa o WebDriver para uso nos testes e o finaliza após execução.

    Uso:
        Injetado automaticamente em qualquer função de teste que aceite 'driver' como argumento.
    """
    driver = get_driver()
    yield driver
    driver.quit()