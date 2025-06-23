import pytest
from src.utils.driver_manager import get_driver



@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()