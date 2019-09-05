import smtplib
import random
from email.mime.text import MIMEText   # 导入模块
from config import service_config


def send_emil(recv: str, content: str,
               title=service_config.EMAIL_TITLE, username=service_config.EMAIL_USERNAME, passwd=service_config.EMAIL_PASSWORD,
               mail_host=service_config.EMAIL_HOST, port=service_config.EMAIL_PORT):
    """
    :param recv: 收件者邮箱地址 例如123456@qq.com
    :param content: 邮件文本内容
    :param title: 邮件标题
    :param username: 邮箱用户名
    :param passwd: 邮箱密码
    :param mail_host:
    :param port:
    :return:
    """
    msg = MIMEText(content)  # 邮件内容
    msg['Subject'] = title
    msg['From'] = username
    msg['To'] = recv
    smtp = smtplib.SMTP_SSL(mail_host, port=port)  # 定义邮箱服务类型
    smtp.login(username, passwd)  # 登录邮箱
    smtp.sendmail(username, recv, msg.as_string())  # 发送邮件
    smtp.quit()
    return True


def get_code(len: int=6) -> str:
    res = ''
    for i in range(len):
        res += str(random.randint(0, 9))
    return res