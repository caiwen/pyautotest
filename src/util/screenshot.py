"""
截图
"""
import os
from src.util import constants


class Screenshot:

    def __init__(self):
        # 初始化截图保存的文件
        self.folder = constants.get_value('screenshot_folder')

        # 查询文件夹是否存在，不存在则创建文件
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    """
    保存截图
    diver:驱动 img_name:截图的名称
    """
    def add_screenshot(self, driver, img_name):
        driver.get_screenshot_as_file(self.folder + '/' + img_name + ".png")
