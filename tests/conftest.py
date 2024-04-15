import pytest
from driver import SetupDriver

from page_and_helpers.base_page import BasePage
from page_and_helpers.helper_user_generator import PersonDataGenerate


@pytest.fixture(scope="function")
def base_page():
    return BasePage(SetupDriver.setup_driver())


@pytest.fixture(scope="function")
def test_data():
    return PersonDataGenerate()
