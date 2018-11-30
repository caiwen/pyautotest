from test_case.test_base import BaseCase
from src.gui.action.gb_login_action import GbLoginAction
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


if __name__ == "__main__":
    unittest.main()
