1. Установить на машину питон 
2. Создать venv, python3 -m venv venv, активировать
3. Установить в виртуальное окружение зависимости pip install -r requirements.txt
4. Запустить тесты из корня репозитория командой, pytest tests/test_base.py --alluredir=allure
5. Дальше, если сервер с отчетом не поднялся сам, можно сделать самому allure serve allure/
6. Просмотреть отчет о прогоне



Описание тестов:

Авторизация:

1. test_authorization_failed - Тест на проверку негативной авторизации

2. test_authorization_passed - Тест на проверку позитивной авторизации

3. test_profile_dropdown_elements - Проверка дропдаун меню профиля

4. test_profile_open - Тест на переход в профиль с главной страницы

Главная страница:

1. test_main_page_popular_category_card - Проверка карточек популярных категорий на главной странице

2. test_main_page_popular_category_card_click - Проверка переходов по карточкам

3. test_header_nav_object_check - Проверка верхней шапки главной страницы

4. test_change_city_check - Проверка смены города

5. test_cart_page - Проверка перехода в корзину