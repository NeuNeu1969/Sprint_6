from datetime import datetime, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import WAIT_TIMEOUT


class OrderPage:

    # Шаг 1 — "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2 — "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    NEXT_MONTH_BUTTON = (By.CLASS_NAME, "react-datepicker__navigation--next")
    RENT_DURATION_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Да']")
    SUCCESS_MODAL_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    def __init__(self, driver):
        # Сохраняет драйвер, чтобы использовать его в методах страницы
        self.driver = driver

    def metro_option_locator(self, station_name):
        # Локатор пункта станции метро в выпадающем списке по полному названию
        locator = "//div[@class='Order_Text__2broi' and text()='" + station_name + "']"
        return (By.XPATH, locator)

    def day_locator(self, day):
        # Локатор дня в календаре (исключает дни соседних месяцев)
        locator = "//div[contains(@class,'react-datepicker__day') and not(contains(@class,'outside-month')) and text()='" + str(day) + "']"
        return (By.XPATH, locator)

    def rent_duration_option_locator(self, duration_text):
        # Локатор пункта срока аренды в открытом Dropdown
        locator = "//div[@class='Dropdown-option' and text()='" + duration_text + "']"
        return (By.XPATH, locator)

    def color_checkbox_locator(self, color_id):
        # Локатор чекбокса цвета по id ("black" или "grey")
        return (By.ID, color_id)

    def fill_step_one(self, data):
        # Заполняет Шаг 1 формы заказа: имя, фамилия, адрес, станция метро, телефон
        self.driver.find_element(*self.NAME_INPUT).send_keys(data["name"])
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(data["surname"])
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(data["address"])

        metro_input = self.driver.find_element(*self.METRO_INPUT)
        metro_input.send_keys(data["metro_search"])
        metro_option = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.metro_option_locator(data["metro_station"]))
        )
        metro_option.click()

        self.driver.find_element(*self.PHONE_INPUT).send_keys(data["phone"])

    def click_next(self):
        # Нажимает кнопку "Далее", переходя на Шаг 2
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def select_delivery_date(self, days_ahead):
        # Открывает календарь и выбирает дату через заданное количество дней от сегодня
        self.driver.find_element(*self.DATE_INPUT).click()

        today = datetime.now()
        target_date = today + timedelta(days=days_ahead)
        months_diff = (target_date.year - today.year) * 12 + (target_date.month - today.month)

        month_step = 0
        while month_step < months_diff:
            self.driver.find_element(*self.NEXT_MONTH_BUTTON).click()
            month_step = month_step + 1

        day_element = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.day_locator(target_date.day))
        )
        day_element.click()

    def select_rent_duration(self, duration_text):
        # Открывает Dropdown "Срок аренды" и выбирает нужный вариант
        self.driver.find_element(*self.RENT_DURATION_DROPDOWN).click()
        option = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.rent_duration_option_locator(duration_text))
        )
        option.click()

    def select_color(self, color_id):
        # Отмечает чекбокс цвета самоката по id
        checkbox = self.driver.find_element(*self.color_checkbox_locator(color_id))
        self.driver.execute_script("arguments[0].click();", checkbox)

    def fill_comment(self, comment_text):
        # Заполняет поле комментария для курьера
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment_text)

    def fill_step_two(self, data):
        # Заполняет Шаг 2 целиком: дата, срок аренды, цвет, комментарий
        self.select_delivery_date(data["delivery_days_ahead"])
        self.select_rent_duration(data["rent_duration"])
        self.select_color(data["color_id"])
        self.fill_comment(data["comment"])

    def submit_order(self):
        # Нажимает "Заказать", затем подтверждает "Да" во всплывшем модальном окне
        self.driver.find_element(*self.ORDER_SUBMIT_BUTTON).click()
        confirm_button = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.CONFIRM_YES_BUTTON)
        )
        confirm_button.click()

    def get_success_modal_text(self):
        # Дожидается финального модального окна и возвращает его текст
        modal = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.SUCCESS_MODAL_HEADER)
        )
        return modal.text

    def click_view_status(self):
        # Нажимает "Посмотреть статус" в финальном модальном окне
        self.driver.find_element(*self.VIEW_STATUS_BUTTON).click()

    