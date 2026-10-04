import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Создаёт браузер и передаёт его в тест
    driver = webdriver.Firefox()
    # Разворачивает окно браузера на весь экран
    driver.maximize_window()
    yield driver
    # Закрывает браузер после завершения теста
    driver.quit()

    