import unittest
from src.util import html_report
from src.util import driver
import approot

class RunAllTests(object):

    def __init__(self):
        self.test_case_path = "./test_case"
        self.title = "自动化测试报告"
        self.description = "测试报告"

    def run(self):
        test_suite = unittest.TestLoader().discover(self.test_case_path, "test_gb*.py")
        # 启动测试时创建文件夹并获取报告的名字
        daf = html_report.DirAndFiles()
        daf.create_dir(title=self.title)
        report_path = html_report.GlobalMsg.get_value("report_path")
        fp = open(report_path, "wb")
        runner = html_report.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester=input("请输入你的名字："))
        runner.run(test_suite)
        fp.close()
        # 用例测试完毕，打开测试报告
        driver_class = driver.Driver()
        my_driver = driver_class.get_driver('firefox')
        report_path = approot.get_root() + report_path
        my_driver.get("file://" + report_path)


if __name__ == "__main__":
    RunAllTests().run()
