# !/usr/bin/python

# -*- coding: UTF-8 -*-


import pymysql

import smtplib

from email.mime.text import MIMEText

from email.header import Header

import time

date = time.strftime('%Y-%m-%d')

# 打开数据库连接

conn = pymysql.connect(

    host='localhost',

    port=3306,

    user='root',

    passwd='root',

    db='test',

    charset="utf8",

)

# 使用cursor()方法获取操作游标

cur = conn.cursor()

# 使用execute方法执行SQL语句

data = cur.execute("select id,phone,num,name from test.user_info;")

# print data

info = cur.fetchmany(data)

cur.close()

conn.commit()

conn.close()


def dd(info):
    s = ""

    for i in info:
        # print i[0]

        # print i[1]

        # print i[2]

        # print i[3].decode('utf-8')

        # 汉字需要 decode 成utf-8

        s += '%s;%s;%s;%s#' % (i[0], i[1], i[2], i[3].decode('utf-8'))

        # print s

    return s


# print(dd(info))

# print(date)


# 发送邮件

msg_from = '123456@QQ.com'  # 发送方邮箱

passwd = 'XXXXXX'  # 填入发送方邮箱的授权码

msg_to = '789@qq.com'  # 收件人邮箱

subject = "python邮件测试 + date "  # 主题

content = str(dd(info))  # 正文

msg = MIMEText(content)

msg['Subject'] = subject

msg['From'] = msg_from

msg['To'] = msg_to

try:

    s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 邮件服务器及端口号

    s.login(msg_from, passwd)

    s.sendmail(msg_from, msg_to, msg.as_string())

    print
    ("发送成功")

except s.SMTPException.e:

    print("发送失败")

finally:

    s.quit()