from functools import wraps
from src.util.my_log import MyLog
log = MyLog()


def teststep(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('\t--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('\t<-- %s, %s, %s', func.__qualname__, 'AssertionError', 'Error')
            raise
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('\t<-- %s, %s, %s', func.__qualname__, 'Exception', 'Error')
            raise
    return wrapper


def teststeps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('  --> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.i('  <-- %s, %s', func.__qualname__, 'Success')
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('  <-- %s, %s, %s', func.__qualname__, 'AssertionError', 'Error')
            raise
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('  <-- %s, %s, %s', func.__qualname__, 'Exception', 'Error')
            raise

    return wrapper


def _wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.i('<-- %s, %s\n', func.__qualname__, 'Success')
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('<-- %s, %s, %s\n', func.__qualname__, 'AssertionError', 'Fail')
            raise
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', 'Error')
            raise

    return wrapper


def testcase(func):
    return _wrapper(func)


def setup(func):
    return _wrapper(func)


def teardown(func):
    return _wrapper(func)


def setupclass(func):
    return _wrapper(func)


def teardownclass(func):
    return _wrapper(func)
