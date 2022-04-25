import allure

from .base_page import BasePage
from .locators import Locators


class AffiliatePage:

    def __init__(self, page):
        self.page = page

    @allure.step("Open account menu")
    def open_affiliate_profile_dropdown_list(self, page):
        self.page.click(Locators.AFFILIATE_PROFILE_BUTTON)
        return AffiliatePage(page)

    @allure.step("Logout from affiliate")
    def logout(self, page):
        self.page.click(Locators.LOGOUT_BUTTON)
        return BasePage(page)
