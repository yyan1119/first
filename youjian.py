#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : admin
# @DATETIME : 2019/1/28 18:12
# @SOFTWARE : PyCharm

# from email.mime.text import MIMEText
# # 纯文本邮件
# # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# # html邮件
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
#
# # 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')
# # 输入收件人地址:
# to_addr = input('To: ')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')

# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

# 纯文本邮件
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# html邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()