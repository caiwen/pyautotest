from .base_action import BaseAction
from ..page.recaptcha_page import RecaptchaTestPage
from src.util.decorator import *


class RecaptchaAction(BaseAction):
    @teststeps
    def do_click(self):
        page = RecaptchaTestPage(self.driver)
        # 打开登录页面
        page.open()
        count = 0
        while (count < 50):
            page.do_click()
            count = count + 1

        self.delay_time(2)
