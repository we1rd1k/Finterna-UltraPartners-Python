class Locators:
    LOGIN_BUTTON = "//div[@class = 'container-fluid']//button[@type = 'submit' and .='LOGIN']"
    LOG_IN_BUTTON = "//button[@type = 'submit' and .='LOG IN']"
    EMAIL_FIELD = "id=email-log"
    PASS_FIELD = "id=pass"

    AFFILIATE_ADMIN_PAGE = "//div[@id='page-name']//span[text()='Affiliates']"
    USER_DASHBOARD = "//nav[contains(@class, 'sidebar-left')]//span[text()='Dashboard']"

    LOGOUT_BUTTON = "//div[contains(@class, 'dropdown-content')]//p//a[text()='Logout']"
    AFFILIATE_PROFILE_BUTTON = "//div[contains(@class, 'menu-top-switch')]//div"
    DROPDOWN_MENU = "//section[contains(@class, 'greeting')]//div//p[contains(text(), 'Affiliate')]"
