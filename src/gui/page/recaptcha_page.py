from src.gui.page.base_page import BasePage
from selenium.webdriver.common.by import By
from src.util.decorator import *


class RecaptchaTestPage(BasePage):
    # 点击按钮的定位
    login_button_loc = (By.NAME, 'clik')
    url = "http://homestead.test/static/recaptcha3.html"
    title = "reCAPTCHA demo: Simple page"

    def __init__(self,selenium_driver):
        BasePage.__init__(self, selenium_driver, self.url, self.title)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @teststep
    def do_click(self):
        self.find_element(*self.login_button_loc).click()
