'''
GB 登录的相关操作
'''
from .base_action import BaseAction
from ..page.gb_login_page import GbLoginPage


class GbLoginAction(BaseAction):
    def __init__(self, selenium_driver):
        super().__init__()
        self.gb_login_pg = GbLoginPage(selenium_driver)

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        self.gb_login_pg.user_login(username, password)

    # 正常登录
    def do_login(self):
        username = self.demo_data.get_data_by_tag('username')
        password = self.demo_data.get_data_by_tag('password')
        self.user_login_verify(username, password)
