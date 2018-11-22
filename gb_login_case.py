from base_case import BaseCase
from src.gui.action.gb_login_action import GbLoginAction
from src.gui.scene.gb_login_scene import GbLoginScene
import unittest


class GbLoginCase(BaseCase):

    # 测试正常登录动作
    def test_login1_action(self):
        GbLoginAction(self.driver).do_login()

    # 测试登录场景，一个场景里面会有多个动作，比如注册登录可以视为一个场景
    def test_login_scene(self):
        GbLoginScene(self.driver).test_login()


if __name__ == "__main__":
    unittest.main()
