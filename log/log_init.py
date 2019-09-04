import logging


def init(root_path: str):
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

    logger = logging.getLogger('db_logger')
    handle = logging.FileHandler('%s/log/db_log.log' % (root_path) )
    handle.setFormatter(formatter)
    logger.addHandler(handle)