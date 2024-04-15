import time
from retry import retry

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

from locators.locators import CustomBasePageLocators, LoginPageLocators

HOST = 'https://www.citilink.ru/'


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = HOST
        self.wait = WebDriverWait(driver, 3)
        self.action = ActionChains(driver)
        self.open_main_page()

    def close(self):
        self.driver.close()

    def open_by_url(self, url: str):
        """
        Открыть страницу по ссылке
        """
        self.driver.get(url)
        return self

    def open_main_page(self, url: str = None):
        """
        Метод открывает страницу
        """
        url = url or self.url
        self.driver.get(url)
        assert self.element_is_present(locator=CustomBasePageLocators.CATEGORY_CARD_BY_NAME.format("Телевизоры"))
        if self.element_is_present(locator=CustomBasePageLocators.COOKIE_CONFORME_BUTTON):
            self.move_to_element_and_click(locator=CustomBasePageLocators.COOKIE_CONFORME_BUTTON)
        return self

    def auth_person(self, person: dict, clean: bool=False):
        """
        Метод авторизации
        """
        self.set_value(locator=LoginPageLocators.LOGIN_INPUT, value=person["email"], clean=clean)
        self.set_value(locator=LoginPageLocators.PASSWORD_INPUT, value=person["password"], clean=clean)
        self.move_to_element_and_click(locator=LoginPageLocators.SUBMIT_BUTTON)
        return self

    @staticmethod
    def self_exception_case(err, locator=None):
        error = err.__class__.__name__

        match error:
            case 'InvalidSelectorException':
                raise Exception(f"Не валидный локатор {locator}")
            case "TimeoutException":
                raise Exception(f"Время ожидания вышло {locator}")
            case 'NoSuchElementException':
                raise Exception(f"Элемента нет на странице {locator}")
            case 'InvalidArgumentException':
                raise Exception(f"В метод передан не верный аргумент {locator}, возможно ожидали WebElement")
            case _:
                raise Exception("Неизвестная ошибка")

    @retry((TimeoutException, NoSuchElementException), tries=5, delay=2)
    def get_element_path(self, locator: str) -> WebElement:
        """
            Найти элемент по локатору
        """
        try:
            return self.driver.find_element(By.XPATH, value=locator)
        except (TimeoutException, NoSuchElementException) as err:
            self.self_exception_case(err, locator)
        except BaseException as err:
            self.self_exception_case(err, locator)

    def get_elements_path(self, locator):
        """
            Найти элементы по локатору
        """
        try:
            self.wait.until(EC.presence_of_all_elements_located(locator=(By.XPATH, locator)))
            return self.driver.find_elements(By.XPATH, value=locator)
        except BaseException as err:
            self.self_exception_case(err, locator)

    def element_is_present(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def move_to_element_and_click(self, locator: str):
        for _ in range(3):
            try:
                element = self.get_element_path(locator=locator)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
                self.action.move_to_element(to_element=element).click(element).perform()
                time.sleep(2)
                break
            except self.self_exception_case(err='Не удалось навести курсор на элемент и нажать', locator=locator):
                continue
        else:
            raise StaleElementReferenceException("Элемент стал устаревшим (StaleElementReferenceException)")
        return self

    @retry((TimeoutException, NoSuchElementException), tries=5, delay=2)
    def get_text(self, locator) -> str:
        element = self.get_element_path(locator)
        text = element.text
        assert bool(text), "Текст пуст"
        return text

    def get_text_element(self, element: WebElement) -> str:
        """
        Получить текст элемента
        """
        return element.text

    def set_value(self, locator, value, clean=False):
        if clean:
            self.get_element_path(locator=locator).clear()
        element = self.get_element_path(locator)
        element.send_keys(value)
        return self

    def clear_text_input(self, locator):
        """
        Очистить поле
        """
        for i in range(0, int(len(self.get_attribute_from_value(locator=locator, attribute_name='value'))) + 1):
            self.set_value(locator=locator, value=Keys.BACKSPACE)
            self.set_value(locator=locator, value=Keys.DELETE)
        return self

    def get_attribute_from_value(self, locator: str, attribute_name: str):
        """
        Получить атребуты по локатору
        """
        element = self.get_element_path(locator)
        return element.get_attribute(attribute_name)

