import logging


def init():

    add_logger('db_logger', 'db.log')
    add_logger('request_logger', 'request.log')


def add_logger(logger_name: str, log_name: str):
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logger = logging.getLogger(logger_name)
    handle = logging.FileHandler('log/%s' % (log_name))
    handle.setFormatter(formatter)
    logger.addHandler(handle)