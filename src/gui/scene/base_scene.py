from src.util import constants


class BaseScene(object):

    def __init__(self):
        self.driver = constants.get_value('my_driver')
