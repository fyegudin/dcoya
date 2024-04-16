import pytest

from playwright.sync_api import Page
from infra.page.home_page import HomePage
from infra.page.work_packages import LoginPage, BlogPage, EventPage, CreateNewEventPage
from infra.data_generator.string_generator import StringGenerator

from infra.constants import BASE_URL


@pytest.mark.webtests
class TestNewEvent:

    @pytest.mark.parametrize("user_name,password", [("stepik1", "sos123456")])
    def test_new_event_valid(self, page: Page, user_name, password):
        home_page = HomePage(page)
        login_page = LoginPage(page, user_name=user_name, password=password)
        blog_page = BlogPage(page)
        event_page = EventPage(page)
        create_new_event = CreateNewEventPage(page, title="Wedding", phone_number="0502346646",
                                              comments="Wellcome to wedding my dear!!!")
        home_page.goto_home()
        home_page.click_on_login_button()
        login_page.fill_login_all_fields_and_submit()
        assert page.url == BASE_URL+"/blog/"
        blog_page.click_event_button()
        assert page.url == BASE_URL + "/wedding/"
        event_page.click_create_new_event_button()
        assert page.url == BASE_URL + "/wedding/create"
        create_new_event.fill_all_fields_and_upload()






    @pytest.mark.parametrize("user_name,password", [("", ""), ("s", "ss"), ("sqqqqqqqqqqqqqqqqqq", "ssaaaaaaaaaaaaa")])
    def test_login_invalid(self, page: Page, user_name, password):
        home_page = HomePage(page)
        login_page = LoginPage(page, user_name=user_name, password=password)
        home_page.goto_home()
        home_page.click_on_login_button()
        login_page.fill_login_all_fields_and_submit()
        print(page.url)
        assert page.url != BASE_URL+"/blog/"

    def test_login_random_invalid(self, page: Page):
        random_user_name = StringGenerator(length=8).string_generate()
        random_password = StringGenerator(length=8).string_generate()
        home_page = HomePage(page)
        login_page = LoginPage(page, user_name=random_user_name, password=random_password)
        home_page.goto_home()
        home_page.click_on_login_button()
        login_page.fill_login_all_fields_and_submit()
        print(page.url)
        assert page.url != BASE_URL+"/blog/"



