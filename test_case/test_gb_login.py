from test_base import BaseCase
from src.gui.action.gb_login_action import GbLoginAction
from src.gui.scene.gb_login_scene import GbLoginScene
import unittest


class GbLoginCase(BaseCase):

    # 测试正常登录动作
    def test_login1_action(self):
        GbLoginAction(self.driver).do_login()

    # 测试密码错误
    def test_login2_action(self):
        GbLoginAction(self.driver).user_login_verify(username ='caiwen@globalegrow.com', password ='adminaaaa')

    # 测试密码没填
    def test_login3_action(self):
        GbLoginAction(self.driver).user_login_verify(username='caiwen@globalegrow.com')

    # 测试邮箱没填没填
    def test_login4_action(self):
        GbLoginAction(self.driver).user_login_verify(password='caiwen@globalegrow.com')

    # 测试邮箱和密码都没填
    def test_login5_action(self):
        GbLoginAction(self.driver).user_login_verify()

    # 测试登录场景，一个场景里面会有多个动作，比如注册登录可以视为一个场景
    def test_login_scene(self):
        GbLoginScene(self.driver).test_login()


if __name__ == "__main__":
    unittest.main()
