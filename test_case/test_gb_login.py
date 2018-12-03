from test_case.test_base import BaseCase
from src.gui.action.gb_login_action import GbLoginAction
from src.gui.scene.gb_login_scene import GbLoginScene
import unittest
from src.util.decorator import *


class GbLoginCase(BaseCase):

    # 测试正常登录动作
    @testcase
    def test_login_success_action(self):
        try:
            login_action = GbLoginAction(self.driver)
            login_action.do_login()
            self.assertTrue(login_action.login_success())
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise

    # 测试密码错误
    @testcase
    def test_login_pwd_err_action(self):
        try:
            login_action = GbLoginAction(self.driver)
            login_action.user_login_verify(username='caiwen@globalegrow.com', password='adminaaaa')
            self.driver.switch_to_alert()
            self.assertTrue(login_action.asset_response_result('Your email/password is incorrect. Please try again'))
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise

    # 测试密码没填
    @testcase
    def test_login3_action(self):
        try:
            GbLoginAction(self.driver).user_login_verify(username='caiwen@globalegrow.com')
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise

    # 测试邮箱没填没填
    @testcase
    def test_login4_action(self):
        try:
            GbLoginAction(self.driver).user_login_verify(password='caiwen@globalegrow.com')
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise

    # 测试邮箱和密码都没填
    @testcase
    def test_login5_action(self):
        try:
            GbLoginAction(self.driver).user_login_verify()
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise

    # 测试登录场景，一个场景里面会有多个动作，比如注册登录可以视为一个场景
    @testcase
    def test_login_scene(self):
        try:
            GbLoginScene(self.driver).test_login()
        except Exception:
            self.daf.get_screenshot(self.driver)
            raise


if __name__ == "__main__":
    unittest.main()
