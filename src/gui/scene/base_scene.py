from src.util import constants


class BaseScene(object):

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
