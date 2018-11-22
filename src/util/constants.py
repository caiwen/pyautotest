def _init():
    global _global_dict
    _global_dict = {}


""" 设置一个全局变量 """


def set_value(key, value):
    _global_dict[key] = value


""" 获得一个全局变量,不存在则返回默认值 """


def get_value(key, def_value=None):
    try:
        return _global_dict[key]
    except KeyError:
        return def_value
