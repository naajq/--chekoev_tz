
class NavigateLocator:
    NAV_ITEMS = "//nav//li[@class='item_PYQt8']/a"
    NAV_ITEMS_BY_NAME = "//nav//li[@class='item_PYQt8']/a[text()='{}']"
    PAGE_TITLE = "//h1[text()]"


class CustomBasePageLocators:
    CATEGORY_CARD_ALL = "//div[@data-meta-name='CategoryTilesLayout__category-tiles']//div[2]//span[text()]"
    CATEGORY_CARD_BY_NAME = "//div[@data-meta-name='CategoryTilesLayout__category-tiles']//div[2]//span[text() = '{}']"
    COOKIE_CONFORME_BUTTON = "//span[text() = 'Я согласен']"
    LOG_IN_BUTTON = "//div[@data-meta-name='UserButtonContainer']"
    HEADER_NAV = "//header/div[3]/div/div/div[2]/div[2]/a/span"
    CHANGE_CITY_BUTTON = "//button[@data-meta-name='CityChangeButton']"
    CART_BUTTON = "//div/div[2]/div/div/div[2]/div[2]/a[2]/div/div"


class ProductListingPage:
    LISTING_TITLE = "//div[1]/div[1]/div[2]/h1"


class LoginPageLocators:
    LOGIN_INPUT = "//input[@name='login']"
    PASSWORD_INPUT = "//input[@name='pass']"
    SUBMIT_BUTTON = "//div/div[2]/div/div/div/form/div/button"
    ERRORE_TITLE = "//div[@class='LoginPageLayout__error-message']"


class ChangeCityPageLocators:
    SEARCH_INPUT = "//input[@name='search-city']"
    CLEAR_TEXT = "//div/div/div/div/div/div/div[2]/div[2]/div/label/div/button[1]"


class CartPageLocators:
    CART_TITLE = "//main/div[1]/div[1]/div/div/span[text()='Корзина']"


class ProfileDropdownLocators:
    PROFILE_DROPDOWN_ALL_BUTTONS = "//div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/a"
    PROFILE_DROPDOWN_BY_NAME = "//div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/a[text()='{}']"


class ProfilePageLocators:
    PROFILE_PAGE_TITLE = "//section/div[2]/section/div[1]/section/span/h2[text()='Профиль']"