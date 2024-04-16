import pytest
from playwright.sync_api import Page
from infra.constants import BASE_URL


@pytest.mark.webtests
class TestHome:

    def test_about_button(self, page: Page):
        page.goto(BASE_URL)
        page.locator('xpath=//*[@id="navbarToggle"]/div[1]/a').click()
        assert page.url == f"{BASE_URL}/blog/about/"

    def test_navigate_from_home(self, page: Page):
        page.goto(BASE_URL)
        list_navigation = ["wedding", "blog", "login", "register"]
        for item in range(1, 4):
            page.locator(f'xpath=//*[@id="navbarToggle"]/div[2]/a[{item}]').click()
            assert page.url == f"{BASE_URL}/{list_navigation[item - 1]}/"
            page.go_back()
