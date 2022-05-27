import smtplib
from email.mime.text import MIMEText
from email.header import Header


class smtp_client:
    def send_email(self):
        sender_email_address = 'donaldshawn1199@163.com'
        sender_email_password = 'QQTYBRQTVIJMPPUZ'
        smtp_server_host = "smtp.163.com"
        smtp_server_port = 25
        receiver_email = 'shangwentao3@outlook.com'
        message_subject = 'Nemo Diablo'
        
        # 要发送的邮件内容 
        message_context = 'Hello World!'
        message = MIMEText(message_context, 'plain', 'utf-8')
        message["From"] = Header(sender_email_address)
        message["To"] = Header(receiver_email)
        message["Subject"] = Header(message_subject)
        email_client = smtplib.SMTP(smtp_server_host, smtp_server_port)
        try:
            email_client.login(sender_email_address, sender_email_password)
            print(
                f"向{receiver_email}发送邮件中")
        except:
            print(
                "请检查配置文件")
        else:
            email_client.sendmail(sender_email_address,
                                  receiver_email, message.as_string())
            print(f"发送完毕")
        finally:
            email_client.close()

