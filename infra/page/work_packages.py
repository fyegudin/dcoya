from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.page.abstract_page import AbsPage


class AboutPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._latest_post: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[1]')
        self._contact_me: Locator = page.locator('xpath=/html/body/main/div[2]/div/div/a[2]')

    def goto(self):
        raise NotImplemented()


class EventPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._contact_me: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a')
        self._create_new_event: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[2]')
        self._download_excel_file: Locator = page.locator(
            'xpath=/html/body/main/div[1]/div[1]/div[3]/div[1]/div/div/a/button')
        self._download_txt_file: Locator = page.locator(
            'xpath=/html/body/main/div[1]/div[1]/div[3]/div[2]/div/div/a/button')

    def goto(self):
        raise NotImplemented()

    def click_create_new_event_button(self):
        self._create_new_event.click()
        return CreateBlogPage(self._page)


class CreateNewEventPage(AbsPage):

    def __init__(self, page: Page, title=None, phone_number=None, comments=None):
        super().__init__(page)
        self.title = title
        self.phone_number = phone_number
        self.comments = comments
        self._contact_me: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a')
        self._event_title: Locator = page.locator('xpath=//*[@id="id_Event_Title"]')
        self._phone_number: Locator = page.locator('xpath=//*[@id="id_Your_Phone_Number"]')
        self._comments: Locator = page.locator('xpath=//*[@id="id_comments"]')
        self._choose_file: Locator = page.locator('xpath=//*[@id="id_file"]')
        self._event_checkbox: Locator = page.locator('xpath=//*[@id="id_eventType"]')
        self._check_no_robot: Locator = page.locator('xpath=//*[@id="recaptcha-anchor-label"]')
        self._upload: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/form/div[2]/button')

    def goto(self):
        raise NotImplemented()

    def fill_all_fields_and_upload(self):
        self._event_title.fill(self.title)
        self._phone_number.fill(self.phone_number)
        self._comments.fill(self.comments)
        self._event_checkbox.select_option("פרסום")
        with self._page.expect_file_chooser() as fc_info:
            self._choose_file.click()
        file_chooser = fc_info.value
        file_chooser.set_files("wedd.xlsx")
        self._upload.click()
        return EventPage(self._page)


class BlogPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._contact_me: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[2]')
        self._latest_post: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[1]')
        self._create_post: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[1]')
        self._event_app: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[2]')

    def goto(self):
        raise NotImplemented()

    def create_blog(self):
        self._create_post.click()
        return CreateBlogPage(self._page)

    def click_event_button(self):
        self._event_app.click()
        return EventPage(self._page)


class CreateBlogPage(AbsPage):

    def __init__(self, page: Page, title=None, content=None):
        super().__init__(page)
        self.title = title
        self.content = content
        self._contact_me: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[2]')
        self._latest_post: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[1]')
        self._title_field: Locator = page.locator('xpath=//*[@id="id_title"]')
        self._content_field: Locator = page.locator('xpath=//*[@id="id_content"]')
        self._post_button: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/form/div/button')

    def goto(self):
        raise NotImplemented()

    def add_post(self):
        self._title_field.fill(self.title)
        self._content_field.fill(self.content)
        self._post_button.click()
        return CreateBlogPage(self._page)


class LoginPage(AbsPage):

    def __init__(self, page: Page, user_name=None, password=None):
        super().__init__(page)
        self.user_name = user_name
        self.password = password
        self._contact_me: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[2]')
        self._latest_post: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[1]')
        self._username: Locator = page.locator('xpath=//*[@id="id_username"]')
        self._password: Locator = page.locator('xpath=//*[@id="id_password"]')
        self._submit_button: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/form/div/button')
        self._forgot_password: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/div/h6/a')
        self._signup: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/div/small/a')

    def goto(self):
        raise NotImplemented()

    def fill_login_all_fields_and_submit(self) -> InsidePage:
        self._username.fill(self.user_name)
        self._password.fill(self.password)
        self._submit_button.click()
        return InsidePage(self._page)


class SignupPage(AbsPage):

    def __init__(self, page: Page, user_name=None, email=None, password=None, password_confirm=None):
        super().__init__(page)
        self.user_name = user_name
        self.email = email
        self.password = password
        self.password_confirm = password_confirm
        self._contact_me: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[2]')
        self._latest_post: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[1]')
        self._username: Locator = page.locator('xpath=//*[@id="id_username"]')
        self._email: Locator = page.locator('xpath=//*[@id="id_email"]')
        self._password_initial: Locator = page.locator('xpath=//*[@id="id_password1"]')
        self._password_confirm: Locator = page.locator('xpath=//*[@id="id_password2"]')
        self._signup_button: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/form/div/button')
        self._signin: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/div/small/a')

    def goto(self):
        raise NotImplemented()

    def fill_sign_up_all_fields_and_submit(self) -> LoginPage:
        self._username.fill(self.user_name)
        self._email.fill(self.email)
        self._password_initial.fill(self.password)
        if self.password_confirm:
            self._password_confirm.fill(self.password_confirm)
        else:
            self._password_confirm.fill(self.password)
        self._signup_button.click()
        return LoginPage(self._page)


class InsidePage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._contact_me: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[2]')
        self._latest_post: Locator = page.locator('xpath=/html/body/main/div[1]/div[2]/div/div/a[1]')
        self._home_button: Locator = page.locator('xpath=//html/body/header/nav/div/a/img')
        self._blog_home_button: Locator = page.locator('xpath=///*[@id="navbarToggle"]/div[1]/a[1]')
        self._about_button: Locator = page.locator('xpath=///*[@id="navbarToggle"]/div[1]/a[2]')
        self._event_app: Locator = page.locator('xpath=///*[@id="navbarToggle"]/div[2]/a[2]')
        self._add_blog: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[1]')
        self._view_profile: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[3]')
        self._logout: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[4]')
        self._next_button: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/a[4]')
        self._last_button: Locator = page.locator('xpath=/html/body/main/div[1]/div[1]/div/a[5]')

    def goto(self):
        raise NotImplemented()





