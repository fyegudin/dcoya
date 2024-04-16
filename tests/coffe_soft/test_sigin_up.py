import pytest
from playwright.sync_api import Page
from infra.page.home_page import HomePage
from infra.page.work_packages import SignupPage
from infra.data_generator.values_generator import FakeGenerator
from infra.data_generator.string_generator import StringGenerator

from infra.constants import BASE_URL


@pytest.mark.webtests
class TestSigInUp:

    def test_sig_in_up_valid(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_first_name(),
                                     email=fake_generator.generate_email(),
                                     password=StringGenerator(length=8).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/login/"

    def test_sig_in_up_valid_long_username(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_string_with_length(150),
                                     email=fake_generator.generate_email(),
                                     password=StringGenerator(length=8).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/login/"

    @pytest.mark.xfail
    def test_sig_in_up_invalid_long_username(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_string_with_length(200),
                                     email=fake_generator.generate_email(),
                                     password=StringGenerator(length=8).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_username(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name="!!!",
                                     email=fake_generator.generate_email(),
                                     password=StringGenerator(length=8).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_empty_username(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name="",
                                     email=fake_generator.generate_email(),
                                     password=StringGenerator(length=8).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_email(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_first_name(),
                                     email="stam",
                                     password=StringGenerator(length=8).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_empty_email(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_first_name(),
                                     email="",
                                     password=StringGenerator(length=8).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_empty_password(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_first_name(),
                                     email=fake_generator.generate_email(),
                                     password="")
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_empty_all_fields(self, page: Page):
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name="",
                                     email="",
                                     password="")
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_short_password(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_first_name(),
                                     email=fake_generator.generate_email(),
                                     password=StringGenerator(length=7).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_number_password(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_first_name(),
                                     email=fake_generator.generate_email(),
                                     password=StringGenerator(length=8).number_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_username_password(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        username = fake_generator.generate_first_name()
        sign_in_up_page = SignupPage(page, user_name=username,
                                     email=fake_generator.generate_email(),
                                     password=username)
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_contain_username_password(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        username = fake_generator.generate_first_name()
        sign_in_up_page = SignupPage(page, user_name=username,
                                     email=fake_generator.generate_email(),
                                     password=username+"123")
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"

    def test_sig_in_up_invalid_password_confirmation(self, page: Page):
        fake_generator = FakeGenerator()
        home_page = HomePage(page)
        sign_in_up_page = SignupPage(page, user_name=fake_generator.generate_first_name(),
                                     email=fake_generator.generate_email(),
                                     password=StringGenerator(length=8).string_generate(),
                                     password_confirm=StringGenerator(length=8).string_generate())
        home_page.goto_home()
        home_page.click_on_signin_button()
        sign_in_up_page.fill_sign_up_all_fields_and_submit()
        print(page.url)
        assert page.url == BASE_URL+"/register/"





