from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import WAIT_TIMEOUT


class HomePage:

    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    COOKIE_CONFIRM_BUTTON = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        # Сохраняет драйвер, чтобы использовать его в методах страницы
        self.driver = driver

    def open(self, url):
        # Открывает главную страницу по переданному URL
        self.driver.get(url)
        # Закрывает баннер cookie, если он появился
        cookie_buttons = self.driver.find_elements(*self.COOKIE_CONFIRM_BUTTON)
        if len(cookie_buttons) > 0:
            cookie_buttons[0].click()

    def click_order_button(self, button_locator):
        # Нажимает кнопку "Заказать" — верхнюю или нижнюю, в зависимости от переданного локатора
        button = self.driver.find_element(*button_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()

    def click_yandex_logo(self):
        # Нажимает логотип Яндекса
        self.driver.find_element(*self.LOGO_YANDEX).click()

    def click_scooter_logo(self):
        # Нажимает логотип "Самоката"
        self.driver.find_element(*self.LOGO_SCOOTER).click()

    def faq_question_locator(self, index):
        # Локатор кнопки-вопроса в FAQ по индексу (0-7)
        return (By.ID, "accordion__heading-" + str(index))

    def faq_answer_locator(self, index):
        # Локатор текста ответа в FAQ по индексу (0-7)
        return (By.ID, "accordion__panel-" + str(index))

    def click_faq_question(self, index):
        # Раскрывает вопрос FAQ по индексу (клик через JS — обходит перекрытие анимированными элементами)
        question = self.driver.find_element(*self.faq_question_locator(index))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        self.driver.execute_script("arguments[0].click();", question)

    def get_faq_answer_text(self, index):
        # Дожидается появления ответа и возвращает его текст
        answer = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.faq_answer_locator(index))
        )
        return answer.text

    def get_current_url(self):
        # Возвращает текущий URL активного окна
        return self.driver.current_url

    def get_window_handle(self):
        # Возвращает идентификатор текущего окна
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        # Переключается на последнее открытое окно и дожидается завершения редиректа
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.url_contains("yandex"))

    def close_current_window_and_switch_to(self, window_handle):
        # Закрывает текущее окно и возвращает фокус на переданное окно
        self.driver.close()
        self.driver.switch_to.window(window_handle)

