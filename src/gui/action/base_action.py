from src.util import data


class BaseAction(object):
        def __init__(self):
            self.demo_data = data.Data('', 'demo.xml')
