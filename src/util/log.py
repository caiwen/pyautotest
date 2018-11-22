#!/usr/bin/env python3 
# -*- coding: UTF-8 -*-

'''
日志输出配置文件
by lina
'''
import logging
import os
from src.util import constants

class Log:
	
	def __init__(self):
		#初始化日志写入的文件
		self.folder = constants.get_value('log_folder')
		self.file = constants.get_value('log_file')

		#查询文件夹是否存在，不存在则创建文件
		if not os.path.exists(self.folder):
			os.makedirs(self.folder)

		#配置日志输出参数
		logging.basicConfig(
			level = logging.INFO,
			format = '%(asctime)s %(levelname)s %(message)s',
			datefmt = '%Y-%m-%d %A %H:%M:%S',
			filename= self.folder+'/'+self.file+'.txt',
			filemode='a'
		)

	"""
	写入日志
	func:运行的方法 des:中文描述
	by lina
	"""
	def add_log(self,page,func,des):
		out_str = page+' : '+func+' : '+des
		logging.info(out_str)



		



