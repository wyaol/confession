import logging
from db_tool import SQL


if __name__ == '__main__':
    logger = logging.getLogger('db_logger')
    logger.setLevel(logging.DEBUG)
    handle = logging.FileHandler('../log/create_db.log')
    formatter = logging.Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    handle.setFormatter(formatter)
    logger.addHandler(handle)

    sql_client = SQL()
    sql_client.execute_scripts_from_file('create_db.sql')