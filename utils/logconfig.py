import logging
from inspect import currentframe
from os.path import basename

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def logger(msg, level='info'):
    level = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warn': logging.WARN,
        'error': logging.ERROR
    }.get(level, level)

    func = currentframe().f_back.f_code
    msg_format = '[{module}][{func}:{line}] {msg}'
    logging.log(level, msg_format.format(module=basename(func.co_filename),
                                         func=func.co_name,
                                         line=func.co_firstlineno,
                                         msg=msg))
