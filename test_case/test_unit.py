from test_case.test_base import BaseCase
from src.gui.action.gb_login_action import GbLoginAction
import unittest


class GbLoginCase(BaseCase):

    # 测试正常登录动作
    def test_login_success_action(self):
        login_action = GbLoginAction(self.driver)
        login_action.do_login()
        self.assertTrue(login_action.login_success())


if __name__ == "__main__":
    unittest.main()
