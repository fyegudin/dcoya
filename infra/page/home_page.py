from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.page.abstract_page import AbsPage
from infra.page.work_packages import AboutPage, EventPage, BlogPage, LoginPage, SignupPage
from infra.constants import BASE_URL


class HomePage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._logo_button: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[1]')
        self._about_button: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[1]/a')
        self._event_button: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[1]')
        self._blog_button: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[2]')
        self._login_button: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[3]')
        self._register_button: Locator = page.locator('xpath=//*[@id="navbarToggle"]/div[2]/a[4]')

    def goto(self) -> HomePage:
        raise NotImplemented()

    def goto_home(self) -> HomePage:
        self._page.goto(BASE_URL)
        return HomePage(self._page)

    def click_on_logo_button(self) -> HomePage:
        self._logo_button.click()
        return HomePage(self._page)

    def click_on_about_button(self) -> AboutPage:
        self._about_button.click()
        return AboutPage(self._page)

    def click_on_event_button(self) -> EventPage:
        self._event_button.click()
        return EventPage(self._page)

    def click_on_blog_button(self) -> BlogPage:
        self._blog_button.click()
        return BlogPage(self._page)

    def click_on_login_button(self) -> LoginPage:
        self._login_button.click()
        return LoginPage(self._page)

    def click_on_signin_button(self) -> SignupPage:
        self._register_button.click()
        return SignupPage(self._page)
