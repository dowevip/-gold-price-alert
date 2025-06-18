# notifier.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from log import log
from config_local import SMTP_SERVER, SMTP_PORT, SENDER, AUTH_CODE, RECEIVER

def send_email(price, body=None):
    subject = f"金价提醒：{price} 元/克"
    if body is None:
        body = f"当前金价为 {price} 元/克，已低于你设定的阈值。"

    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header("金价提醒", 'utf-8')
    message['To'] = Header("你", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER, AUTH_CODE)
            server.sendmail(SENDER, RECEIVER, message.as_string())
        log("邮件已成功发送", "SUCCESS")
    except Exception as e:
        log(f"邮件发送失败：{e}", "ERROR")