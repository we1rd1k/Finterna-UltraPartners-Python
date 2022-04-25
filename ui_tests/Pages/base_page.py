import allure

from .inputs import Urls
from .locators import Locators
from .login_page import LoginPage


class BasePage:
    def __init__(self, page):
        self.page = page

    @allure.step(f"Open main page {Urls.BASE_DEV_URL}")
    def open_main_page(self, page):
        self.page.goto(Urls.BASE_DEV_URL)
        return BasePage(page)

    @allure.step("Click login button and go to login page")
    def go_to_login_page(self, page):
        self.page.click(Locators.LOGIN_BUTTON)
        return LoginPage(page)
