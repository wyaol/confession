import datetime
from service.tools import send_emil, get_code
from config.service_config import EMAIL_CONT, EMAIL_CONFESSION, EMAIL_CONT_CONGRATULATE, EMAIL_CONGRATULATE, BLOCK_TIME
from dao.email_send_db import EmailSend
from exceptions.custom_exception import CodeVerifyFailException, BlockTimeException

CODE_VERIFY_FAIL = '验证码校验失败'


def email_send_confession(email, name, sex, o_email, o_name, code):
    check_sender_info(email)

    email_send = EmailSend()

    if verify_code(email, code) is False:
        raise CodeVerifyFailException(CODE_VERIFY_FAIL)
    else:
        email_send.del_code(email)

    if email_send.if_exist_pair(email, o_email):
        email_send_congratulate(email, o_email)
        return True

    send_emil(o_email, EMAIL_CONT)
    email_send.add_email(email, o_email, EMAIL_CONT, EMAIL_CONFESSION)
    if email_send.if_exist_sender(email) is False:
        email_send.add_email_sender(email, name, sex, o_email, o_name)
    else:
        email_send.update_email_sender(email, name, sex, o_email, o_name)

    return True


def check_sender_info(email):
    rest_time = get_rest_block_time(email, BLOCK_TIME)
    if rest_time != 0:
        raise BlockTimeException(rest_time, '您当前处于冻结时间')


def email_send_congratulate(email, o_email):
    send_emil(email, EMAIL_CONT_CONGRATULATE)
    send_emil(o_email, EMAIL_CONT_CONGRATULATE)
    email_send = EmailSend()
    email_send.add_email(email, o_email, EMAIL_CONT_CONGRATULATE, EMAIL_CONGRATULATE)
    email_send.add_email(o_email, email, EMAIL_CONT_CONGRATULATE, EMAIL_CONGRATULATE)


def email_send_code(email):
    email_send = EmailSend()
    if email_send.if_exist_code(email) is False:
        code = get_code()
        email_send.add_code(email, code)
    else:
        code = email_send.get_code(email)
    send_emil(email, code, title=code)


def verify_code(email, code):
    email_send = EmailSend()
    db_code = email_send.get_code(email)
    return code == db_code and code != ''


def get_rest_block_time(email, block_time) -> int:
    """
    获取剩余的冻结时间 s
    :param email: 这次发送的邮件
    :param block_time: 设定的冻结时间
    :return: 秒
    """
    email_send = EmailSend()
    time_last = email_send.get_current_send_timestamp(email)
    if time_last == 0: return 0
    time_current = datetime.datetime.now()
    time_long = time_current - time_last
    if block_time <= time_long.total_seconds(): return 0
    res = datetime.timedelta(seconds=block_time) - time_long
    return int(res.total_seconds())