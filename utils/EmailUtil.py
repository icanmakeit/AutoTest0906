from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.Conf import ConfigYaml
from utils.LogUtil import my_log
import smtplib


class SendEmail:
    def __init__(self, smtp_addr, username, password, recv, title, content=None, file=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.log = my_log("EmailUtil")

    def send_mail(self):
        msg = MIMEMultipart()
        msg.attach(MIMEMultipart(self.content, _charset="utf-8"))
        msg["Subject"] = self.title
        msg["From"] = self.username
        msg["To"] = self.recv

        # 邮件附件，判断是否附件
        if self.file:
            # MIMEText读取文件
            att = MIMEText(open(self.file).read())
            att["Content-type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment;filename="%s"' % self.file
            msg.attach(att)

        self.smtp = smtplib.SMTP(self.smtp_addr, port=25)
        self.smtp.login(self.username, self.password)
        self.smtp.sendmail(self.username, self.recv, msg.as_string())
        self.log.info("发送邮件成功")


if __name__ == '__main__':
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(smtp_addr, username, password, recv, "测试")
    email.send_mail()

