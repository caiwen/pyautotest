"""
GB 登录的相关操作
"""
from .base_action import BaseAction
from ..page.gb_login_page import GbLoginPage
from src.util.decorator import *


class GbLoginAction(BaseAction):
    # 测试用户登录
    @teststeps
    def user_login_verify(self, username="", password=""):
        login_page = GbLoginPage(self.driver)
        # 打开登录页面
        login_page.open()
        # 输入用户名
        login_page.login_username(username)
        # 输入密码
        login_page.login_password(password)
        # 点击登陆按钮
        login_page.login_button()
        self.delay_time(2)

    # 正常登录
    def do_login(self):
        username = self.demo_data.get_data_by_tag('username')
        password = self.demo_data.get_data_by_tag('password')
        self.user_login_verify(username, password)
        self.delay_time(3)

    def login_success(self):
        if self.get_cookie_named('gb_userinfo') is None:
            return False
        return True

    def asset_response_result(self, msg):
        login_page = GbLoginPage(self.driver)
        return login_page.login_response_err_hint() == msg
