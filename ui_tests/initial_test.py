import allure
import pytest

from .Pages.affiliate_page import AffiliatePage
from .Pages.inputs import Credentials
from .Pages.base_page import BasePage


@allure.feature("Login test")
@allure.description("Login test")
@pytest.mark.smoke
def test_affiliate_login(page):
    main_page = BasePage(page)
    main_page \
        .open_main_page(page) \
        .go_to_login_page(page) \
        .fill_email_field(page, Credentials.LOGIN_AFFILIATE) \
        .fill_pass_field(page, Credentials.PASSWORD) \
        .click_auth_button()


@allure.feature("Logout test")
@allure.description("Logout test")
@pytest.mark.smoke
def test_affiliate_logout(page):
    BasePage(page) \
        .open_main_page(page) \
        .go_to_login_page(page) \
        .fill_email_field(page, Credentials.LOGIN_AFFILIATE) \
        .fill_pass_field(page, Credentials.PASSWORD) \
        .click_auth_button()
    AffiliatePage(page) \
        .open_affiliate_profile_dropdown_list(page) \
        .logout(page)
