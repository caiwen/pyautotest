from src.gui.page.base_page import BasePage
from selenium.webdriver.common.by import By
from src.util.decorator import *
from time import sleep

class Recaptcha2TestPage(BasePage):
    # 点击按钮的定位
    login_button_loc = (By.NAME, 'smit')
    recaptcha_button_loc = (By.ID, 'recaptcha-anchor')

    url = "http://homestead.test/static/recaptcha2.html"
    title = "reCAPTCHA demo: Simple page"

    def __init__(self,selenium_driver):
        BasePage.__init__(self, selenium_driver, self.url, self.title)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @teststep
    def do_click(self):
        sleep(10)
        self.find_element(*self.recaptcha_button_loc).click()
        sleep(1)
        self.find_element(*self.login_button_loc).click()
