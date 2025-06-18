import os
LOG_FILE = os.path.join(os.path.dirname(__file__), 'log.txt')

# 金价提醒阈值
TARGET = 720.0

# 邮件设置（请用户在使用前修改为自己的信息）
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = xxx
SENDER = 'your_email@example.com'
AUTH_CODE = 'your_app_password_here'
RECEIVER = ['receiver1@example.com', 'receiver2@example.com']