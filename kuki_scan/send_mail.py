import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 配置SMTP服务器
smtp_server = 'smtp.qq.com'  # 替换为您的SMTP服务器
smtp_port = 587  # 替换为您的SMTP服务器端口
smtp_user = ''  # 替换为您的邮箱地址
smtp_password = ''  # 替换为您的SMTP授权码

# 接收邮件的邮箱
to_email = ''  # 替换为接收通知的邮箱地址

# 文件路径
file_path = 'scan_result'
last_position = 0

while True:
    try:
        with open(file_path, 'r') as file:
            # 移动到上次读取位置
            file.seek(last_position)
            new_content = file.read()

            if new_content:
                # 更新最后读取位置
                last_position = file.tell()

                # 发送邮件
                msg = MIMEMultipart()
                msg['From'] = smtp_user
                msg['To'] = to_email
                msg['Subject'] = Header('New Content in scan_result.txt', 'utf-8')
                msg.attach(MIMEText(new_content, 'plain', 'utf-8'))

                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_user, smtp_password)
                    server.sendmail(smtp_user, to_email, msg.as_string())
                print(f"New content sent to {to_email}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # 每小时检查一次
    time.sleep(3600)