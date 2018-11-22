#!/usr/bin/env python3 
# -*- coding: UTF-8 -*-

'''
测试报告输出
by lina
'''
import xlrd
import os
import time
import datetime
from xlutils.copy import copy
from xlwt import Style
from src.util import constants
from src.util import report


class Report:

    def __init__(self):
        # 初始化报告保存的文件
        self.output_file = constants.get_value('excel_report_folder') + '/' + constants.get_value(
            'excel_report_file') + '.xls'

    """
    保存截图
    story:用户故事 action:操作 des:描述
    by lina
    """

    def add_excel_report(self, story, action, des):
        now_time = datetime.datetime.now()
        rexcel = xlrd.open_workbook(self.output_file, formatting_info=True)
        row = rexcel.sheets()[0].nrows
        addexcel = copy(rexcel)
        addsheet = addexcel.get_sheet(0)
        addsheet.write(row, 0, story)
        addsheet.write(row, 1, action)
        addsheet.write(row, 2, des)
        addsheet.write(row, 3, now_time.strftime('%Y-%m-%d %H:%M:%S'))
        addexcel.save(self.output_file)
