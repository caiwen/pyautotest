'''
GB 登录的相关操作
'''
from .base_action import BaseAction
from ..page.gb_login_page import GbLoginPage


class GbLoginAction(BaseAction):

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        GbLoginPage(self.driver).user_login(username, password)

    # 正常登录
    def do_login(self):
        username = self.demo_data.get_data_by_tag('username')
        password = self.demo_data.get_data_by_tag('password')
        self.user_login_verify(username, password)
