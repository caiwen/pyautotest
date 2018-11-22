"""
场景基类，一个场景会有多个动作
"""


class BaseScene(object):

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
