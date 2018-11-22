from src.util import data


class BaseAction(object):
        def __init__(self, selenium_driver):
            self.demo_data = data.Data('', 'demo.xml')
            self.driver = selenium_driver
