import pytest

from playwright.sync_api import Page
from infra.page.home_page import HomePage
from infra.page.work_packages import LoginPage
from infra.data_generator.string_generator import StringGenerator

from infra.constants import BASE_URL


@pytest.mark.webtests
class TestLogin:

    @pytest.mark.parametrize("user_name,password", [("stepik", "sos12345"), ("stepik1", "sos123456")])
    def test_login_valid(self, page: Page, user_name, password):
        home_page = HomePage(page)
        login_page = LoginPage(page, user_name=user_name, password=password)
        home_page.goto_home()
        home_page.click_on_login_button()
        login_page.fill_login_all_fields_and_submit()
        assert page.url == BASE_URL+"/blog/"

    @pytest.mark.parametrize("user_name,password", [("", ""), ("s", "ss"), ("sqqqqqqqqqqqqqqqqqq", "ssaaaaaaaaaaaaa")])
    def test_login_invalid(self, page: Page, user_name, password):
        home_page = HomePage(page)
        login_page = LoginPage(page, user_name=user_name, password=password)
        home_page.goto_home()
        home_page.click_on_login_button()
        login_page.fill_login_all_fields_and_submit()
        assert page.url != BASE_URL+"/blog/"

    def test_login_random_invalid(self, page: Page):
        random_user_name = StringGenerator(length=8).string_generate()
        random_password = StringGenerator(length=8).string_generate()
        home_page = HomePage(page)
        login_page = LoginPage(page, user_name=random_user_name, password=random_password)
        home_page.goto_home()
        home_page.click_on_login_button()
        login_page.fill_login_all_fields_and_submit()
        assert page.url != BASE_URL+"/blog/"



