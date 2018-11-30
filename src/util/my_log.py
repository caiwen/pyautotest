import logging
from src.util import constants
import datetime


class MyLog:
    def __init__(self):
        # 初始化日志写入的文件
        now_time = datetime.datetime.now()
        # 设置当次测试日志输出的文件夹与文件
        log_path = './log/'
        log_folder = log_path + now_time.strftime('%Y-%m-%d')
        log_file = now_time.strftime('%H%M%S')
        self.folder = constants.get_value('log_folder')
        self.file = constants.get_value('log_file')
        filename = log_folder + '/' + log_file + '_debug.txt'
        self.set_logger(self.file, filename)

    @classmethod
    def set_logger(cls, udid, file):
        logger = logging.getLogger('PYAUTOTEST')
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler(file)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s'
                                      + ' - %s' % udid
                                      + ' - %(levelname)s'
                                      + ' - %(message)s')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        cls.logger = logger

    def d(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def i(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def w(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def c(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)


