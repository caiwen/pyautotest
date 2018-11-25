"""
工具类，获取配置信息
"""
import configparser
import approot


class Config:

    def __init__(self):
        # 配置文件目录
        self.file = '/config/config.ini'

    # 获取配置
    def get_config(self, section, name):
        conf = configparser.ConfigParser()
        config_path = approot.get_root() + self.file
        conf.read(config_path)
        name = conf.get(section, name)
        return name
