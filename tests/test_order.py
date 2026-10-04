import allure
import pytest

from pages.home_page import HomePage
from pages.order_page import OrderPage
from urls import BASE_URL
from data import ORDER_DATASET_1, ORDER_DATASET_2, EXPECTED_SUCCESS_MODAL_HEADER


class TestOrder:

    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий")
    @allure.title("Оформление заказа самоката")
    @pytest.mark.parametrize("dataset", [ORDER_DATASET_1, ORDER_DATASET_2], ids=["dataset_1", "dataset_2"])
    @pytest.mark.parametrize("entry_button", [HomePage.ORDER_BUTTON_TOP, HomePage.ORDER_BUTTON_BOTTOM], ids=["top_button", "bottom_button"])
    def test_order_scooter(self, driver, entry_button, dataset):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Нажимает кнопку "Заказать" (точка входа определяется параметром)
        home_page.click_order_button(entry_button)

        # Заполняет Шаг 1 и переходит на Шаг 2
        order_page = OrderPage(driver)
        order_page.fill_step_one(dataset)
        order_page.click_next()

        # Заполняет Шаг 2 и отправляет заказ
        order_page.fill_step_two(dataset)
        order_page.submit_order()

        # Проверяет текст финального модального окна
        modal_text = order_page.get_success_modal_text()
        assert EXPECTED_SUCCESS_MODAL_HEADER in modal_text

        # Переходит на страницу статуса заказа (там доступна шапка сайта без модального окна)
        order_page.click_view_status()

        # Проверяет переход на главную страницу по клику на логотип "Самоката"
        home_page.click_scooter_logo()
        assert home_page.get_current_url() == BASE_URL

        # Проверяет, что логотип Яндекса открывает в новом окне домен Яндекса (редирект)
        original_window = home_page.get_window_handle()
        home_page.click_yandex_logo()
        home_page.switch_to_new_window()
        assert "yandex" in home_page.get_current_url()

        # Закрывает окно Яндекса и возвращается в исходное окно
        home_page.close_current_window_and_switch_to(original_window)

        