from .base_action import BaseAction
from ..page.recaptcha2_page import Recaptcha2TestPage
from src.util.decorator import *


class Recaptcha2Action(BaseAction):
    @teststeps
    def do_click(self):
        page = Recaptcha2TestPage(self.driver)
        # 打开登录页面
        page.open()
        page.do_click()
        self.delay_time(2)
