from test_case.test_base import BaseCase
from src.gui.action.gb_login_action import GbLoginAction
from src.gui.action.recaptcha_action import RecaptchaAction
from src.gui.action.recaptcha2_action import Recaptcha2Action
import unittest
from src.util.decorator import *


class GbLoginCase(BaseCase):

    # 测试密码错误
    @testcase
    def test_login_err_action(self):
        try:
            login_action = GbLoginAction(self.driver)
            login_action.user_login_verify(username='caiwen@globalegrow.com', password='adminaaaa')
            self.assertTrue(login_action.login_success())
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise

    @testcase
    def test_recaptcha(self):
        try:
            action = RecaptchaAction(self.driver)
            action.do_click()
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise

    @testcase
    def test_recaptcha2(self):
        try:
            action = Recaptcha2Action(self.driver)
            action.do_click()
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise

if __name__ == "__main__":
    unittest.main()
