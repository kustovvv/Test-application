import pytest

from framework.sidebar_page import SideBarPage
from framework.login_page import LoginPage


@pytest.fixture(scope="session")
def sidebar_fixture(driver):
    sidebar = SideBarPage(driver)
    yield sidebar