import allure
from playwright.sync_api import expect
from .locators import Locators


class LoginPage:

    def __init__(self, page):
        self.page = page

    @allure.step("Fill in login field: {email}")
    def fill_email_field(self, page, email):
        self.page.fill(Locators.EMAIL_FIELD, email)
        return LoginPage(page)

    @allure.step("Fill in login field: {password}")
    def fill_pass_field(self, page, password):
        self.page.fill(Locators.PASS_FIELD, password)
        return LoginPage(page)

    @allure.step("Click Log in button")
    def click_auth_button(self):
        self.page.click(Locators.LOG_IN_BUTTON)
        expect(self.page.locator(Locators.USER_DASHBOARD)).to_be_visible()
