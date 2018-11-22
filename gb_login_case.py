from base_case import BaseCase
from src.gui.action.gb_login_action import GbLoginAction
import unittest


class GbLoginCase(BaseCase):

    # 测试正常登录
    def test_login1(self):
        GbLoginAction(self.driver).do_login()


if __name__ == "__main__":
    unittest.main()
