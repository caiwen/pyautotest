
from time import sleep
import unittest, random
from .models import myunit, function
from .page_obj.loginPage import Login


class LoginTest(myunit.MyTest):

    # 测试用户登录
    def user_login_verify(self, username ="", password =""):
        Login(self.driver).user_login(username, password)

    def test_login1(self):
        # 用户名、密码为空登录
        self.user_login_verify()
        po = Login(self.driver)
        self.assertEqual(po.login_error_hint(), '用户名或密码不能为空')
        function.insert_img(self.driver, "user_pawd_empty.jpg")

    def test_login2(self):
        # 用户名正确，密码为空登录验证
        self.user_login_verify(username="ces")
        po = Login(self.driver)
        self.assertEqual(po.login_error_hint(), "用户名或密码不能为空")
        function.insert_img(self.driver,"pawd_empty.jpg")

    def test_login3(self):
        # 用户名为空，密码正确
        self.user_login_verify(password="12334ddf")
        po = Login(self.driver)
        self.assertEqual(po.login_error_hint(),"用户名或密码不能为空")
        function.insert_img(self.driver, "user_empty.jpg")

    def test_login4(self):
        # 用户名和密码不匹配
        character = random.choice('abcdefghijklmnopqrstuvwxyz')
        username = "sdw" + character
        self.user_login_verify(username=username, password="2sdfd")
        po = Login(self.driver)
        self.assertEqual(po.login_error_hint(), "用户名或密码错误")
        function.insert_img(self.driver, "user_pass_error.jpg")

    def test_login5(self):
        # 用户名、密码正确
        self.user_login_verify(username="caiwen@globalegrow.com" , password="admin123")
        sleep(3)
        po = Login(self.driver)
        self.assertEqual(po.login_user_success(), u'adtest')
        function.insert_img(self.driver, "user_pwd_true.jpg")


if __name__ == '__main__':
    unittest.main()
