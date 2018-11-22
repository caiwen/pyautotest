
'''
gb 登录场景
by caiwen
'''
from src.gui.scene.base_scene import BaseScene
from src.gui.action import gb_login_action


class GbLoginScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.gb_login_action = gb_login_action.GbLoginAction()

    def test_login(self):
        self.gb_login_action.do_login()
