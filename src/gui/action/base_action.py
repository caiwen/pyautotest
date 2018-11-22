from src.util import data
import time
from src.util import screenshot


class BaseAction(object):
        def __init__(self, selenium_driver):
            self.demo_data = data.Data('', 'demo.xml')
            self.driver = selenium_driver
            self.mscreenshot = screenshot.Screenshot()

        def delay_time(self, sec):
            time.sleep(sec)
