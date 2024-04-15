import allure

from locators.locators import CustomBasePageLocators, LoginPageLocators, ProfileDropdownLocators, ProfilePageLocators


class TestAuthorizationPage:

    @allure.title("Авторизация - 001")
    @allure.description("Авторизация с неверными данными")
    def test_authorization_failed(self, base_page, test_data):

        with allure.step("Негатив - Вход с фейк данными, проверка появления ошибки"):
            person_random = test_data.get_random_person()
            base_page.move_to_element_and_click(locator=CustomBasePageLocators.LOG_IN_BUTTON)
            base_page.auth_person(person_random)
            assert base_page.element_is_present(
                locator=LoginPageLocators.ERRORE_TITLE), "Ошибка данных авторизации не отобразилась"

    @allure.title("Авторизация - 002")
    @allure.description("Авторизация с верными данными")
    def test_authorization_passed(self, base_page, test_data):
        with allure.step("Позитив - Вход с верными, проверка отсутствия ошибки и переход в профиль"):
            person_random = test_data.get_admin()
            base_page.move_to_element_and_click(locator=CustomBasePageLocators.LOG_IN_BUTTON)
            base_page.auth_person(person_random)
            assert not base_page.element_is_present(
                locator=LoginPageLocators.ERRORE_TITLE), "Ошибка данных авторизации отобразилась"

            assert base_page.element_is_present(
                locator=f"//div[2]/div[2]/div[1]/div/div/div/span[text()='{person_random['username']}']")

    @allure.title("Авторизация - 003")
    @allure.description("Проверка дропдауна профиля")
    def test_profile_dropdown_elements(self, base_page, test_data):
        with allure.step("Позитивная авторизация в профиль"):
            person_random = test_data.get_admin()
            base_page.move_to_element_and_click(locator=CustomBasePageLocators.LOG_IN_BUTTON)
            base_page.auth_person(person_random)
            assert not base_page.element_is_present(
                locator=LoginPageLocators.ERRORE_TITLE), "Ошибка данных авторизации отобразилась"

        with allure.step("Проверка дропдауна профиля"):
            assert base_page.element_is_present(
                locator=f"//div[2]/div[2]/div[1]/div/div/div/span[text()='{person_random['username']}']")

            base_page.move_to_element_and_click(
                locator=f"//div[2]/div[2]/div[1]/div/div/div/span[text()='{person_random['username']}']")

            assert len(base_page.get_elements_path(
                locator=ProfileDropdownLocators.PROFILE_DROPDOWN_ALL_BUTTONS)) == 5, "Не хватает всех элементов дропдауна"

    @allure.title("Авторизация - 004")
    @allure.description("Переход в профиль")
    def test_profile_open(self, base_page, test_data):
        with allure.step("Позитивная авторизация в профиль"):
            person_random = test_data.get_admin()
            base_page.move_to_element_and_click(locator=CustomBasePageLocators.LOG_IN_BUTTON)
            base_page.auth_person(person_random)
            assert not base_page.element_is_present(
                locator=LoginPageLocators.ERRORE_TITLE), "Ошибка данных авторизации отобразилась"

        with allure.step("Проверка дропдауна профиля"):
            base_page.move_to_element_and_click(
                locator=f"//div[2]/div[2]/div[1]/div/div/div/span[text()='{person_random['username']}']")

            base_page.move_to_element_and_click(locator=ProfileDropdownLocators.PROFILE_DROPDOWN_BY_NAME.format("Мой профиль"))

            assert base_page.element_is_present(locator=ProfilePageLocators.PROFILE_PAGE_TITLE), "Заголовок профиля не отобразился"
