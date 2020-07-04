# !/usr/bin/python
# -*- coding:utf-8 -*-

import pymysql
import time, datetime
from openpyxl import Workbook

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

query_sql = """ SELECT d.project_id,d.project_name,
 d.end_time,
 u.username,d.target_user,
 u.real_name,
 u.email,
 u.phone,
 u.company
 FROM t_data_push_record_table d
 LEFT JOIN t_user u
 ON d.target_user = u.id
 WHERE d.target_user NOT IN('8a828b81612cff980161415a9957000c','8a817f674d663d1e014d7aec4a2b52f2') AND d.push_state='success' AND d.target_path IS NOT NULL AND d.start_time BETWEEN %s AND %s AND d.app_type IS NOT NULL AND d.type='project' ORDER BY d.start_time DESC;"""
table_head = ["project_id", "project_name", "推送时间", "username", "target_user", "姓名", "邮箱", "电话", "单位"]
sender_config = ["457455@163.com", "smtp.263.net", "123456"]
receivers = ['email1', 'email2']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
export_file_path = "/opt/push_project_data.xls"
'''
  获取数据库链接，查询相关数据
'''


def get_sql_connection(start_time, end_time):
    try:
        db = pymysql.connect("localhost", "dev_cloud", "dev_cloud.123", "dev_cloud", charset='utf8')
        cursor = db.cursor()
        sql = "\n" + query_sql % (start_time, end_time)
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except:
        print( '''Error: query sql is fail''')
    return None


def write_result_to_content(results):
    if results is None:
        return
    print( '''create workbook excel file''')
    wb = Workbook()
    sheet = wb.create_sheet('data', index=1)
    sheet.append(table_head)
    print( len(results))
    for result in results:
        sheet.append(result)
    wb.save(export_file_path)


def deal_time(days):
    now_time = datetime.datetime.now()
    delta_time = datetime.timedelta(days=days)
    start_time = now_time + delta_time
    return "'" + start_time.strftime("%y-%m-%d") + "'"


def email_config():
    message = MIMEMultipart()
    message['From'] = Header("biocloud", "utf-8")
    message['to'] = Header("biocloud", "utf-8")
    subject = '本周项目推送情况统计'
    message['subject'] = Header(subject, 'utf-8')

    message.attach(MIMEText('附件为本周项目推送情况统计，请查看！', 'plain', 'utf-8'))

    att = MIMEText(open(export_file_path, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="项目推送统计.xls"'
    message.attach(att)
    return message


def send_email(message):
    try:
        smtpObj = smtplib.SMTP(sender_config[1])
        smtpObj.login(sender_config[0], sender_config[2])
        smtpObj.sendmail(sender_config[0], receivers, message.as_string())
        print( '''邮件发送成功''')
        return True
    except smtplib.SMTPException:
        print( '''Error: 无法发送邮件''')
        return False


if __name__ == '__main__':
    if time.strftime("%w", time.localtime()) == "2":
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        results = get_sql_connection(deal_time(-20), "'" + now_time + "'")
        write_result_to_content(results)
        message = email_config()
        if send_email(message) is False:
            time.sleep(5)
            send_email(message)
