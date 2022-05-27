import email
import email.header
import imaplib
ROOT_DIR = "resourses/"


class imap_client:
    def __init__(self):

        
        self.user_id = 'donaldshawn1199@163.com'
        self.password = 'QQTYBRQTVIJMPPUZ'
        self.imap_server = 'imap.163.com'

    def login(self):
        try:
            serv = imaplib.IMAP4(self.imap_server, 143)
            print('imap----服务器连接成功')
        except Exception as e:
            print('imap----服务器连接失败:', e)
            return

        try:
            serv.login(self.user_id, self.password)
            print('imap----登录成功')
            return serv
        except Exception as e:
            print('imap----登录失败：', e)
            return

    def logout(self, conn):
        conn.close
        conn.logout()

    def get_content(self, conn):
        conn.select()
        op = input("默认显示未读邮件，输入A读取所有邮件")
        if op == 'A':
            ret, data = conn.search(None, 'ALL')
        else:
            ret, data = conn.search(None, 'UNSEEN')
        # 邮件列表
        email_list = data[0].split()
        emailnum = len(email_list)
        if (emailnum == 0):
            print('收件箱为空，已退出')
            return
        print("查询到", emailnum, "封邮件")
        while True:
            try:
                num = int(input("请输入需要获取的邮件序号"))
                break
            except ValueError:
                print("请输入一个合法数字")
        item = email_list[len(email_list) - num]
        ret, data = conn.fetch(item, '(RFC822)')
        msg = email.message_from_string(data[0][1].decode())
        sub = msg.get('subject')
        email_from = msg.get('from')
        email_to = msg.get('to')
        sub_text = email.header.decode_header(sub)
        email_from_text = email.header.decode_header(email_from)
        email_to_text = email.header.decode_header(email_to)
        # 如果是特殊字符，元组的第二位会给出编码格式，需要转码
        if sub_text[0]:
            sub_detail = self.__tuple2str(sub_text[0])
        email_from_detail = ''
        for i in range(len(email_from_text)):
            email_from_detail = email_from_detail + \
                self.__tuple2str(email_from_text[i])
        email_to_detail = ''
        for i in range(len(email_to_text)):
            email_to_detail = email_to_detail + \
                self.__tuple2str(email_to_text[i])

        print('主题：', sub_detail)
        print('发件人：', email_from_detail)
        print('收件人：', email_to_detail)
        # 通过walk可以遍历出所有的内容
        for part in msg.walk():
            # 这里要判断是否是multipart，如果是，数据没用丢弃
            if not part.is_multipart():
                content_type = part.get_content_type()
                name = part.get_filename()
                if name:
                    trans_name = email.header.decode_header(name)
                    if trans_name[0][1]:
                        file_name = trans_name[0][0].decode(trans_name[0][1])
                    else:
                        file_name = trans_name[0][0]
                    print('开始下载附件:', file_name)
                    attach_data = part.get_payload(
                        decode=True)  # 解码存储数据
                    try:
                        f = open(ROOT_DIR + file_name, 'wb')
                    except Exception as e:
                        print(e)
                        f = open(ROOT_DIR + 'tmp', 'wb')
                        # 遇到错误缓存文件
                    f.write(attach_data)
                    f.close()
                    print('附件下载成功:', file_name)
                else:
                    # 文本内容
                    txt = part.get_payload(decode=True)
                    if content_type == 'text/html':
                        print("文件格式为html，请使用浏览器查看文件")
                        htmlfile = open("resourses/html_content.html", 'w')
                        try:
                            txt = txt.decode()
                        except UnicodeDecodeError:
                            txt = txt.decode('gbk')
                        htmlfile.write(txt)
                        htmlfile.close()
                    elif content_type == 'text/plain':
                        print('邮件正文：')
                        # 尝试解码
                        try:
                            txt = txt.decode()
                        except UnicodeDecodeError:
                            txt = txt.decode('gbk')

                        print(txt)

    def hello(self, conn):
        imaplib.Commands['ID'] = 'AUTH'
        args = ("name", "lisi", "contact", "null",
                "version", "0.0", "vendor", "myclient")
        typ, dat = conn._simple_command('ID', '("' + '" "'.join(args) + '")')

    def __tuple2str(self, tuple_):

        if tuple_[1]:
            out_str = tuple_[0].decode(tuple_[1])
        else:
            if isinstance(tuple_[0], bytes):
                out_str = tuple_[0].decode('gbk')
            else:
                out_str = tuple_[0]
        return out_str
