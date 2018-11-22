"""
gear best 网站的登录场景
"""
from src.gui.scene.base_scene import BaseScene
from src.gui.action import gb_login_action


class GbLoginScene(BaseScene):

    def test_login(self):
        gb_login_action.GbLoginAction(self.driver).do_login()
