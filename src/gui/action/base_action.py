from src.util import data
import time
from src.util import screenshot
from src.util import log


class BaseAction(object):
        def __init__(self, selenium_driver):
            self.demo_data = data.Data('', 'demo.xml')
            self.driver = selenium_driver

        def delay_time(self, sec):
            time.sleep(sec)

        def get_cookies(self):
            return self.driver.get_cookies()

        def get_cookie_named(self, name):
            return self.driver.get_cookie(name)
