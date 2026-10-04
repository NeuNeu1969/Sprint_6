import allure

from pages.home_page import HomePage
from urls import BASE_URL
from data import FAQ_ANSWERS


class TestFAQ:

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса 0 в FAQ")
    def test_faq_question_0(self, driver):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Раскрывает вопрос 0 и проверяет текст ответа
        home_page.click_faq_question(0)
        answer_text = home_page.get_faq_answer_text(0)

        assert answer_text == FAQ_ANSWERS[0]

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса 1 в FAQ")
    def test_faq_question_1(self, driver):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Раскрывает вопрос 1 и проверяет текст ответа
        home_page.click_faq_question(1)
        answer_text = home_page.get_faq_answer_text(1)

        assert answer_text == FAQ_ANSWERS[1]

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса 2 в FAQ")
    def test_faq_question_2(self, driver):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Раскрывает вопрос 2 и проверяет текст ответа
        home_page.click_faq_question(2)
        answer_text = home_page.get_faq_answer_text(2)

        assert answer_text == FAQ_ANSWERS[2]

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса 3 в FAQ")
    def test_faq_question_3(self, driver):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Раскрывает вопрос 3 и проверяет текст ответа
        home_page.click_faq_question(3)
        answer_text = home_page.get_faq_answer_text(3)

        assert answer_text == FAQ_ANSWERS[3]

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса 4 в FAQ")
    def test_faq_question_4(self, driver):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Раскрывает вопрос 4 и проверяет текст ответа
        home_page.click_faq_question(4)
        answer_text = home_page.get_faq_answer_text(4)

        assert answer_text == FAQ_ANSWERS[4]

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса 5 в FAQ")
    def test_faq_question_5(self, driver):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Раскрывает вопрос 5 и проверяет текст ответа
        home_page.click_faq_question(5)
        answer_text = home_page.get_faq_answer_text(5)

        assert answer_text == FAQ_ANSWERS[5]

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса 6 в FAQ")
    def test_faq_question_6(self, driver):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Раскрывает вопрос 6 и проверяет текст ответа
        home_page.click_faq_question(6)
        answer_text = home_page.get_faq_answer_text(6)

        assert answer_text == FAQ_ANSWERS[6]

    @allure.feature("Главная страница")
    @allure.story("FAQ")
    @allure.title("Раскрытие вопроса 7 в FAQ")
    def test_faq_question_7(self, driver):
        # Открывает главную страницу
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

        # Раскрывает вопрос 7 и проверяет текст ответа
        home_page.click_faq_question(7)
        answer_text = home_page.get_faq_answer_text(7)

        assert answer_text == FAQ_ANSWERS[7]

        