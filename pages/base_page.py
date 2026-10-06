import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import WAIT_TIMEOUT


class BasePage:

    def __init__(self, driver):
        # Сохраняет драйвер, чтобы использовать его во всех методах взаимодействия
        self.driver = driver

    @allure.step("Открыть страницу")
    def open(self, url):
        # Открывает страницу по переданному URL
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find(self, locator):
        # Дожидается видимости элемента и возвращает его
        return WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти все элементы без ожидания")
    def find_all(self, locator):
        # Возвращает список всех найденных элементов (без явного ожидания)
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        # Дожидается элемента, прокручивает к центру экрана и кликает по нему
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step("Кликнуть по элементу через JavaScript")
    def click_js(self, locator):
        # Кликает через JS — обходит визуальное перекрытие другими элементами
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле")
    def send_keys(self, locator, text):
        # Дожидается поля и вводит в него текст
        element = self.find(locator)
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        # Дожидается элемента и возвращает его текст
        return self.find(locator).text

    @allure.step("Дождаться исчезновения элемента")
    def wait_invisible(self, locator):
        # Дожидается, пока элемент перестанет быть видимым
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Дождаться URL, содержащего текст")
    def wait_url_contains(self, text):
        # Дожидается, пока текущий URL не будет содержать переданный текст
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.url_contains(text))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        # Возвращает текущий URL активного окна
        return self.driver.current_url

    @allure.step("Получить идентификатор текущего окна")
    def get_window_handle(self):
        # Возвращает идентификатор текущего окна
        return self.driver.current_window_handle

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        # Переключается на последнее открытое окно
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Закрыть текущее окно и вернуться к исходному")
    def close_current_window_and_switch_to(self, window_handle):
        # Закрывает текущее окно и возвращает фокус на переданное окно
        self.driver.close()
        self.driver.switch_to.window(window_handle)

        