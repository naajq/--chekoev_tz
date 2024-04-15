import allure

from constants import main_page_category_card, header_nav_button_name
from locators.locators import CustomBasePageLocators, ProductListingPage, ChangeCityPageLocators, CartPageLocators


class TestCustomBasePage:

    @allure.title("Главная страница - 001")
    @allure.description("Проверка на отображение всех карточек популярных категорий на главной странице")
    def test_main_page_popular_category_card(self, base_page):
        nav_items = main_page_category_card

        with allure.step("Проверка на наличие всех карточек популярных категорий"):
            elements = base_page.get_elements_path(locator=CustomBasePageLocators.CATEGORY_CARD_ALL)
            assert len(elements) == len(nav_items), "Нет всех карточек на странице"
            assert all(base_page.get_text_element(element=i) in nav_items for i in elements)

    @allure.title("Главная страница - 002")
    @allure.description("Проверка преходов по всем карточкам категорий и проверка соответствия заголовка после перехода")
    def test_main_page_popular_category_card_click(self, base_page):
        nav_items = main_page_category_card

        with allure.step("Проверка на наличие всех карточек популярных категорий"):
            elements = base_page.get_elements_path(locator=CustomBasePageLocators.CATEGORY_CARD_ALL)
            assert len(elements) == len(nav_items), "Нет всех карточек на странице"
            assert all(base_page.get_text_element(element=i) in nav_items for i in elements)

        with allure.step("Проверка переходов по карточкам, сверяем заголовок открывшейся страницы с названием карточки"):
            # Цикл с перебором всек полученных карточек
            for card_name in nav_items:
                # Нажатия по карточкам
                base_page.move_to_element_and_click(locator=CustomBasePageLocators.CATEGORY_CARD_BY_NAME.
                                                    format(card_name))
                base_page.element_is_present(locator=ProductListingPage.LISTING_TITLE)

                # Проверка на соответствие
                assert base_page.get_text(locator=ProductListingPage.LISTING_TITLE) == card_name
                # Переход обратно на главнуюж страницу в конце цикла
                base_page.open_main_page()

    @allure.title("Главная страница - 003")
    @allure.description("Проверка наличия всх кнопок в шапке страницы")
    def test_header_nav_object_check(self, base_page):
        with allure.step("Проверка на наличие нужных элементов навигации на странице"):
            nav = header_nav_button_name
            elements = base_page.get_elements_path(locator=CustomBasePageLocators.HEADER_NAV)
            assert len(elements) == 7, "Не отображается главная навигация по сайту"
            assert all(base_page.get_text_element(element=i) in nav for i in elements)

    @allure.title("Главная страница - 004")
    @allure.description("Проверка меню смены города")
    def test_change_city_check(self, base_page):
        city_list = ["Пермь", "Краснодар", "Казань"]
        with allure.step("Проверка на отображение кнопки смены города в шапке и клик по ней"):
            assert base_page.element_is_present(
                locator=CustomBasePageLocators.CHANGE_CITY_BUTTON), "Кнопка сменить город не отобразилась на странице"

            base_page.move_to_element_and_click(locator=CustomBasePageLocators.CHANGE_CITY_BUTTON)
            assert base_page.element_is_present(
                locator=ChangeCityPageLocators.SEARCH_INPUT), "Поле для ввода города не появилось"

        with allure.step("Проверка поиска городов"):
            for city in city_list:
                base_page.set_value(locator=ChangeCityPageLocators.SEARCH_INPUT, value=city)
                assert base_page.element_is_present(locator=f"//a[@rel='nofollow']/span[text()='{city}']")
                assert not base_page.element_is_present(locator="//a[@rel='nofollow']/span[text()='Москва']")
                base_page.move_to_element_and_click(locator=ChangeCityPageLocators.CLEAR_TEXT)

    @allure.title("Главная страница - 005")
    @allure.description("Проверка карзины")
    def test_cart_page(self, base_page):
        with allure.step("Проверка кнопки 'Корзина' на главной старнице и переход по ней"):
            assert base_page.element_is_present(locator=CustomBasePageLocators.CART_BUTTON)
            base_page.move_to_element_and_click(locator=CustomBasePageLocators.CART_BUTTON)
            assert base_page.element_is_present(locator=CartPageLocators.CART_TITLE)
