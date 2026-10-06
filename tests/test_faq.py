import allure
import pytest

from pages.home_page import HomePage
from urls import BASE_URL
from data import FAQ_ANSWERS


class TestFAQ:

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса FAQ")
    @pytest.mark.parametrize("question_index", range(len(FAQ_ANSWERS)))
    def test_faq_question(self, driver, question_index):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open_home_page(BASE_URL)

        # Раскрывает вопрос и проверяет текст ответа
        home_page.click_faq_question(question_index)
        answer_text = home_page.get_faq_answer_text(question_index)

        assert answer_text == FAQ_ANSWERS[question_index]

        