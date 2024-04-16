import pytest

from playwright.sync_api import Page
from infra.page.home_page import HomePage
from infra.page.work_packages import LoginPage, BlogPage, CreateBlogPage
from infra.data_generator.values_generator import FakeGenerator

from infra.constants import BASE_URL


@pytest.mark.webtests
class TestBlog:

    @pytest.mark.parametrize("user_name,password", [("stepik", "sos12345")])
    def test_add_blog_valid(self, page: Page, user_name, password):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        login_page = LoginPage(page, user_name=user_name, password=password)
        blog_page = BlogPage(page)
        create_blog = CreateBlogPage(page, title=fake_generator.generate_title(),
                                     content=fake_generator.generate_text())
        home_page.goto_home()
        home_page.click_on_login_button()
        login_page.fill_login_all_fields_and_submit()
        assert page.url == BASE_URL+"/blog/"
        blog_page.create_blog()
        create_blog.add_post()
        assert '/'.join(page.url.split('/')[:-2])+"/" == BASE_URL + "/blog/post/"

    @pytest.mark.parametrize("user_name,password", [("stepik", "sos12345")])
    @pytest.mark.parametrize("title,content", [("אבא שבת", "שבת שלום לכולם!")])
    def test_add_blog_in_hebrew_valid(self, page: Page, user_name, password, title, content):
        home_page = HomePage(page)
        login_page = LoginPage(page, user_name=user_name, password=password)
        blog_page = BlogPage(page)
        create_blog = CreateBlogPage(page, title=title, content=content)
        home_page.goto_home()
        home_page.click_on_login_button()
        login_page.fill_login_all_fields_and_submit()
        assert page.url == BASE_URL+"/blog/"
        blog_page.create_blog()
        create_blog.add_post()
        assert '/'.join(page.url.split('/')[:-2])+"/" == BASE_URL + "/blog/post/"








