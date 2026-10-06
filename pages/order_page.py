from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

import allure

from pages.base_page import BasePage


class OrderPage(BasePage):

    # Шаг 1 — "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION_XPATH_TEMPLATE = "//div[@class='Order_Text__2broi' and text()='{}']"
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2 — "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    NEXT_MONTH_BUTTON = (By.CLASS_NAME, "react-datepicker__navigation--next")
    DAY_XPATH_TEMPLATE = "//div[contains(@class,'react-datepicker__day') and not(contains(@class,'outside-month')) and text()='{}']"
    RENT_DURATION_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_DURATION_OPTION_XPATH_TEMPLATE = "//div[@class='Dropdown-option' and text()='{}']"
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Да']")
    SUCCESS_MODAL_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    @allure.step("Заполнить Шаг 1 формы заказа")
    def fill_step_one(self, data):
        # Заполняет имя, фамилию, адрес, станцию метро, телефон
        self.send_keys(self.NAME_INPUT, data["name"])
        self.send_keys(self.SURNAME_INPUT, data["surname"])
        self.send_keys(self.ADDRESS_INPUT, data["address"])

        self.send_keys(self.METRO_INPUT, data["metro_search"])
        metro_locator = (By.XPATH, self.METRO_OPTION_XPATH_TEMPLATE.format(data["metro_station"]))
        self.click(metro_locator)

        self.send_keys(self.PHONE_INPUT, data["phone"])

    @allure.step("Перейти на Шаг 2")
    def click_next(self):
        # Нажимает кнопку "Далее"
        self.click(self.NEXT_BUTTON)

    @allure.step("Выбрать дату доставки")
    def select_delivery_date(self, days_ahead):
        # Открывает календарь и выбирает дату через заданное количество дней от сегодня
        self.click(self.DATE_INPUT)

        today = datetime.now()
        target_date = today + timedelta(days=days_ahead)
        months_diff = (target_date.year - today.year) * 12 + (target_date.month - today.month)

        month_step = 0
        while month_step < months_diff:
            self.click(self.NEXT_MONTH_BUTTON)
            month_step = month_step + 1

        day_locator = (By.XPATH, self.DAY_XPATH_TEMPLATE.format(target_date.day))
        self.click(day_locator)

    @allure.step("Выбрать срок аренды")
    def select_rent_duration(self, duration_text):
        # Открывает Dropdown "Срок аренды" и выбирает нужный вариант
        self.click(self.RENT_DURATION_DROPDOWN)
        option_locator = (By.XPATH, self.RENT_DURATION_OPTION_XPATH_TEMPLATE.format(duration_text))
        self.click(option_locator)

    @allure.step("Выбрать цвет самоката")
    def select_color(self, color_id):
        # Отмечает чекбокс цвета самоката по id ("black" или "grey")
        self.click_js((By.ID, color_id))

    @allure.step("Заполнить комментарий для курьера")
    def fill_comment(self, comment_text):
        # Заполняет поле комментария
        self.send_keys(self.COMMENT_INPUT, comment_text)

    @allure.step("Заполнить Шаг 2 формы заказа")
    def fill_step_two(self, data):
        # Заполняет дату, срок аренды, цвет, комментарий
        self.select_delivery_date(data["delivery_days_ahead"])
        self.select_rent_duration(data["rent_duration"])
        self.select_color(data["color_id"])
        self.fill_comment(data["comment"])

    @allure.step("Отправить заказ и подтвердить")
    def submit_order(self):
        # Нажимает "Заказать", затем подтверждает "Да" во всплывшем окне
        self.click(self.ORDER_SUBMIT_BUTTON)
        self.click(self.CONFIRM_YES_BUTTON)

    @allure.step("Получить текст финального модального окна")
    def get_success_modal_text(self):
        # Возвращает текст финального модального окна с подтверждением заказа
        return self.get_text(self.SUCCESS_MODAL_HEADER)

    @allure.step("Перейти к статусу заказа")
    def click_view_status(self):
        # Нажимает "Посмотреть статус" в финальном модальном окне
        self.click(self.VIEW_STATUS_BUTTON)

    