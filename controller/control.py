from service.tools import send_emil, get_code
from config.service_config import EMAIL_CONT, EMAIL_CONFESSION, EMAIL_CONT_CONGRATULATE, EMAIL_CONGRATULATE
from dao.email_send_db import EmailSend
from exceptions.custom_exception import CodeVerifyFailException


CODE_VERIFY_FAIL = '验证码校验失败'


def email_send_confession(email, name, sex, o_email, o_name, code):
    email_send = EmailSend()

    if verify_code(email, code) is False:
        raise CodeVerifyFailException(CODE_VERIFY_FAIL)
    else:
        email_send.del_code(email)

    send_emil(o_email, EMAIL_CONT)
    email_send.add_email(email, o_email, EMAIL_CONT, EMAIL_CONFESSION)
    if email_send.if_exist_sender(email) is False:
        email_send.add_email_sender(email, name, sex, o_email, o_name)
    else:
        email_send.update_email_sender(email, name, sex, o_email, o_name)

    if email_send.if_exist_pair(email, o_email):
        email_send_congratulate(email, o_email)
    return True


def check_sender_info(email):
    pass


def email_send_congratulate(email, o_email):
    send_emil(email, EMAIL_CONT_CONGRATULATE)
    email_send = EmailSend()
    email_send.add_email(email, o_email, EMAIL_CONT_CONGRATULATE, EMAIL_CONGRATULATE)


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
    return code == db_code