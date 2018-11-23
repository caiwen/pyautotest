from src.util import config
from src.util import constants
from src.util import driver
import datetime
import os


class Bootstrap:
    def __init__(self):
        # 初始化配置类
        conf = config.Config()
        constants._init()
        now_time = datetime.datetime.now()

        # 设置当次测试日志输出的文件夹与文件
        log_path = conf.get_config('system', 'log_path')
        log_folder = log_path + now_time.strftime('%Y-%m-%d')
        log_file = now_time.strftime('%H%M%S')

        constants.set_value('log_folder', log_folder)
        constants.set_value('log_file', log_file)

        # 设置当次测试截图输出的文件夹
        screenshot_path = conf.get_config('system', 'screenshot_path')
        screenshot_folder = screenshot_path + now_time.strftime('%Y-%m-%d_%H%M%S')
        constants.set_value('screenshot_folder', screenshot_folder)

        # 设置当次测试excel报告输出的文件
        excel_report_path = conf.get_config('system', 'excel_report_path')
        excel_report_folder = excel_report_path + now_time.strftime('%Y-%m-%d')
        excel_report_file = now_time.strftime('%H%M%S')
        constants.set_value('excel_report_folder', excel_report_folder)
        constants.set_value('excel_report_file', excel_report_file)

        # html文件存放路径
        html_report_path = conf.get_config('system', 'html_report_path')
        constants.set_value('html_report_path', html_report_path)

        # 创建导出excel报告的文件夹
        if not os.path.exists(excel_report_folder):
            os.makedirs(excel_report_folder)

        # 设置驱动
        driver_class = driver.Driver()
        my_driver = driver_class.get_driver(conf.get_config('driver', 'default'))
        constants.set_value('my_driver', my_driver)


if __name__ == "__main__":
    ind = Bootstrap()
