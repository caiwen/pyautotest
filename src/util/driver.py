"""
工具类获取浏览器驱动
"""
from selenium import webdriver


class Driver:
    @staticmethod
    def get_driver(name):
        if name == 'chrome':
            return webdriver.Chrome()
        if name == 'firefox':
            return webdriver.Firefox()
        return webdriver.Chrome()
