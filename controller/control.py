from service.tools import send_emil
from config.service_config import EMAIL_CONT, EMAIL_CONFESSION
from dao.email_send_db import EmailSend


def email_send_confession(email, name, sex, o_email, o_name):
    send_emil(o_email, EMAIL_CONT)
    email_send = EmailSend()
    email_send.add_email(email, o_email, EMAIL_CONT, EMAIL_CONFESSION)
    if email_send.if_sender_exist(email) is False:
        email_send.add_email_sender(email, name, sex, o_email, o_name)
    else:
        email_send.update_email_sender(email, name, sex, o_email, o_name)
    return True