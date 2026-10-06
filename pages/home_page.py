from selenium.webdriver.common.by import By

import allure

from pages.base_page import BasePage


class HomePage(BasePage):

    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    COOKIE_CONFIRM_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_QUESTION_ID_PREFIX = "accordion__heading-"
    FAQ_ANSWER_ID_PREFIX = "accordion__panel-"

    @allure.step("Открыть главную страницу")
    def open_home_page(self, url):
        # Открывает главную страницу и закрывает баннер cookie, если он появился
        self.open(url)
        cookie_buttons = self.find_all(self.COOKIE_CONFIRM_BUTTON)
        if len(cookie_buttons) > 0:
            cookie_buttons[0].click()

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self, button_locator):
        # Нажимает кнопку "Заказать" — верхнюю или нижнюю, в зависимости от переданного локатора
        self.click(button_locator)

    @allure.step("Кликнуть по логотипу 'Самоката'")
    def click_scooter_logo(self):
        # Нажимает логотип "Самоката"
        self.click(self.LOGO_SCOOTER)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        # Нажимает логотип Яндекса (открывается в новом окне)
        self.click_js(self.LOGO_YANDEX)

    @allure.step("Раскрыть вопрос FAQ")
    def click_faq_question(self, index):
        # Раскрывает вопрос FAQ по индексу
        locator = (By.ID, self.FAQ_QUESTION_ID_PREFIX + str(index))
        self.click_js(locator)

    @allure.step("Получить текст ответа FAQ")
    def get_faq_answer_text(self, index):
        # Возвращает текст раскрытого ответа FAQ по индексу
        locator = (By.ID, self.FAQ_ANSWER_ID_PREFIX + str(index))
        return self.get_text(locator)

    