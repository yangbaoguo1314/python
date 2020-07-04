# python版本3.7
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:35:17 2018
@author: Administrator
"""

# 系统 & 网络下载 & 解压缩
import os, sys
# 时间 & 网络下载 & 解压缩
import time
# 多线程
import threading
# 邮件相关
import smtplib
# 定时相关
import datetime
import time
import xlwt
import datetime as dt

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import pymysql
import pandas as pd
from email.mime.text import MIMEText


class mail():
    def __init__(self):
        self.me = 'yourpassword@163.com'
        self.user = 'youremail@163.com'
        self.password = 'yourpassword'
        # 注意163是授权码 QQ邮箱依据权限设置不同也可能需要授权码，不是输入邮箱密码
        self.mail_host = 'smtp.163.com'

    def send_mail(self, to_list, sub, excel):
        msg = MIMEMultipart()
        msg['From'] = self.me
        msg['To'] = ".".join(to_list)
        msg['Subject'] = '同步接口巡查'
        # 抄送
        msg['Cc'] = 'xxx@qq.com'
        # 邮件正文
        msg.attach(MIMEText('自动检查结果邮件', 'plain', 'utf-8'))
        print(to_list)
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(r'C:\test\test.xls', "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="auth_order.xlsx"')
        msg.attach(part)

        try:
            s = smtplib.SMTP()
            s.connect(self.mail_host)
            s.login(self.user, self.password)
            s.sendmail(self.me, to_list, msg.as_string())
            s.close()
            return True
        except Exception as e:
            print(str(e))
            return False


class monitor(threading.Thread):
    def __init__(self, mail_list):
        super(monitor, self).__init__()
        self.mail_list = mail_list

    def run(self):
        while True:
            now = datetime.datetime.now()
            print(now.hour, now.minute)
            # 设置每天几点几分发送，譬如每天16时18分则为下面的写法
            if now.hour == 12 and now.minute == 55:
                print('do my task once')
                ###################################################### （1）定时任务代码，此处替换成你的 定时任务代码
                # -*- coding: utf-8 -*-

                print('doing my task')
                conn = pymysql.connect(host='xxx', port=23310, user='op_root', password='xxxx',
                                       database='dw', charset='utf8')

                # cursor获得python执行Mysql命令的方法,也就是操作游标
                cur = conn.cursor()

                # v_sql = "select * from risk_task"
                v_sql = sql = "SELECT DATE(t3.app_date) AS app_date,COUNT(t3.order_no) AS order_num, \
                                                SUM(CASE WHEN t3.task_status =6 then 1 else 0 end)/COUNT(t3.order_no) AS order_rate, \
                                                sum(t4.FPD)/SUM(t4.FPD_amt) AS fpd_rate,SUM(t5.coin)/SUM(t5.coin_sum) AS coin_rate \
                                                FROM \
                                                (SELECT t1.app_date,t1.customer_id,t2.order_no,t2.task_status \
                                                FROM risk_task t1 \
                                                LEFT JOIN \
                                                (SELECT customer_id,order_no,task_status \
                                                FROM risk_task \
                                                WHERE loan_type = 4 and vip_flag not in ('VIP','0') \
                                                AND close_reason NOT LIKE '%测试%' \
                                                AND DATE(app_date)>='2018-01-01') t2 \
                                                ON t1.customer_id = t2.customer_id \
                                                WHERE t1.loan_type = 3 and t1.vip_flag not in ('VIP','0') \
                                                AND t1.close_reason NOT LIKE '%测试%' \
                                                AND DATE(t1.app_date)>='2018-01-01' \
                                                AND DATE(t1.app_date)<=date_sub(CURDATE(),interval 1 day)) t3 \
                                                LEFT JOIN \
                                                (SELECT order_id, \
                                                CASE WHEN TO_DAYS(CASE WHEN actl_date IS NULL THEN CURDATE() ELSE \
                                                actl_date END)-TO_DAYS(plan_date)>0 THEN loan_amount ELSE 0 END AS FPD, \
                                                loan_amount FPD_amt \
                                                FROM risk_repay_plan \
                                                WHERE period=1 and prod_line='商城分期订单' and vip_flag not in ('VIP','0') and state not in (5,127))t4 \
                                                ON t3.order_no=t4.order_id \
                                                LEFT JOIN \
                                                (SELECT order_id, \
                                                case when dpd>0 then loanbalanceb else 0 end AS coin, \
                                                loanbalanceb as coin_sum \
                                                FROM risk_overdue \
                                                WHERE prod_line ='商城' AND vip_flag NOT IN ('VIP','0') AND DATE(data_date)=date_sub(CURDATE(),interval 1 day))t5 \
                                                ON t3.order_no=t5.order_id \
                                                GROUP BY DATE(t3.app_date)"
                cur.execute(v_sql)

                # data = pd.read_sql(sql,db)
                # data.to_excel(r'C:\test\auth_order.xlsx')
                # fetchall()则是接收全部的返回结果行
                rows = cur.fetchall()
                v_cnt = len(rows)
                # print(data.head())
                # 生成excel文件
                book = xlwt.Workbook()

                # 如果对一个单元格重复操作，会引发
                # returns error:
                # Exception: Attempt to overwrite cell:
                # sheetname=u'sheet 1' rowx=0 colx=0
                # 所以在打开时加cell_overwrite_ok=True解决
                sheet1 = book.add_sheet('Sheet1', cell_overwrite_ok=True)

                # 设置样式
                styleBlueBkg = xlwt.easyxf(
                    'pattern: pattern solid, fore_colour ocean_blue; font: bold on;');  # 80% like
                # styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour sky_blue;');

                # blueBkgFontStyle = xlwt.XFStyle()
                # blueBkgFontStyle.Pattern = blueBackgroundPattern;
                # styleBlueBkg = blueBkgFontStyle;

                styleBold = xlwt.easyxf('font: bold on');

                # 日期格式转化
                dateFormat = xlwt.XFStyle()

                dateFormat.num_format_str = 'yyyy/mm/dd'

                # 居中
                style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式

                al = xlwt.Alignment()
                al.horz = 0x02  # 设置水平居中
                al.vert = 0x01  # 设置垂直居中
                style.alignment = al

                # sheet1.write(0, 0, dt.date.today(), dateFormat)

                # worksheet.write(0, 0, dt.date.today(), dateFormat)

                # 表头标题
                sheet1.write(0, 0, 'number', styleBlueBkg)
                sheet1.write(0, 1, 'app_date', styleBlueBkg)
                sheet1.write(0, 2, 'order_number', styleBlueBkg)
                sheet1.write(0, 3, 'order_rate', styleBlueBkg)
                sheet1.write(0, 4, 'fpd_rate', styleBlueBkg)
                sheet1.write(0, 5, 'coin_rate', styleBlueBkg)
                # sheet1.write(0, 6, '姓名')
                # sheet1.write(0, 7, '职位')
                # sheet1.write(0, 8, '案件来源')
                # sheet1.write(0, 9, '调查原因')
                # sheet1.write(0, 10, '涉及合同号')

                # first_col=sheet1.col(0)       #xlwt中是行和列都是从0开始计算的
                sec_col = sheet1.col(1)
                sec_col.width = 256 * 20
                # 每一列写入excel文件，不然数据会全在一个单元格中
                num = 1
                for i in range(len(rows)):
                    for j in range(6):
                        # print (rows[i][j])-
                        # print ("--------")
                        # i+1表示从Excel第2行开始写数据，第1行为表头
                        if j == 0:  # 写序号
                            sheet1.write(i + 1, 0, num)
                        elif j == 1:  # 写日期
                            sheet1.write(i + 1, 1, rows[i][j - 1], dateFormat)
                        else:  # 写其他数据
                            sheet1.write(i + 1, j, rows[i][j - 1])
                    num = num + 1
                # c:\\test\\my doc
                # r'E:\picture\quanPing.png'

                book.save(r'C:\test\test.xls')
                print('do my task success')
                ###################################################### 结束（1）

                ###################################################### （2）发送邮件
                mail_sub = 'auth_order'
                mail_content = r'C:\test\test.xls'
                m = mail()
                if m.send_mail(self.mail_list, mail_sub, mail_content):
                    print('send mail successed.')
                else:
                    print('send mail failed.')
                ###################################################### 结束（2）

            # 每隔60秒检测一次
            time.sleep(60)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        m = monitor(['381784599@qq.com'])
        m.start()
# m = monitor(['xxx@xxx.com','xxx@xxx.com'])
