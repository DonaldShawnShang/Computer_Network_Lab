from imap_client import imap_client
from smtp_client import smtp_client
receiver = imap_client()
sender = smtp_client()
print('🖥️  客户端初始化...')
connection = receiver.login()
receiver.hello(connection)
print('🖥️  客户端初始化完毕')
while True:
    op = input("🖥️  输入S发送邮件，输入C接受邮件，输入E退出\n")
    if(op == 'E' or op == 'e'):
        receiver.logout(connection)
        print("🖥️  客户端已退出")
        break
    elif(op == 'C' or op == 'c'):
        receiver.get_content(connection)
    elif(op == 'S' or op == 's'):
        sender.send_email()
    else:
        print("🖥️  请输入正确的操作符")
print("macbook''spro")
