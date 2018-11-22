"""
GB 登录的相关操作
"""
from .base_action import BaseAction
from ..page.gb_login_page import GbLoginPage


class GbLoginAction(BaseAction):
    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        # 获取用户名和页面登录
        login_page = GbLoginPage(self.driver)
        login_page.open()
        # 登录页面截屏
        self.mscreenshot.add_screenshot(self.driver, 'gb_login_page(1)')
        login_page.login_username(username)
        login_page.login_password(password)
        # 输入之后截屏
        self.mscreenshot.add_screenshot(self.driver, 'gb_login_input(2)')
        login_page.login_button()
        # 点击登陆之后截屏
        self.delay_time(2)
        self.mscreenshot.add_screenshot(self.driver, 'gb_login_click(3)')

    # 正常登录
    def do_login(self):
        username = self.demo_data.get_data_by_tag('username')
        password = self.demo_data.get_data_by_tag('password')
        self.user_login_verify(username, password)
        self.delay_time(3)
        self.mscreenshot.add_screenshot(self.driver, 'gb_login_success(4)')
