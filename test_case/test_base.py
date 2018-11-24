"""
测试用例的基类
"""
import unittest
from bootstrap.bootstrap import Bootstrap
from src.util import constants
from src.util.html_report import DirAndFiles


class BaseCase(unittest.TestCase):
        def setUp(self):
            Bootstrap()
            self.driver = constants.get_value('my_driver')
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.daf = DirAndFiles()

        def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
        unittest.main()
