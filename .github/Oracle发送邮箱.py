"""
import psutil
import os
from jinja2 import Environment,FileSystemLoader
import webbrowser
import cx_Oracle

#Monitor Memory
def monMem():

    memInfo = psutil.virtual_memory()
    totalMem = str(round(memInfo.total/1024/1024,2)) + 'M'
    freeMem = str(round(memInfo.free/1024/1024,2)) + 'M'
    avaMem = str(round(memInfo.available/1024/1024,2)) + 'M'

    mInfo = {}
    mInfo['totalMem'] = totalMem
    mInfo['freeMem'] = freeMem
    mInfo['avaMem'] = avaMem
'''
#这里区分下不同平台的情况
    if os.name == 'posix':
        bufMem = memInfo.buffers
        cachedMem = memInfo.cached

        mInfo['bufMem'] = bufMem
        mInfo['cachedMem'] = cachedMem

    return mInfo
'''
#Monitor CPU
def monCpu():
    physical_cpu_count = psutil.cpu_count(logical=False)
    logical_cpu_count = psutil.cpu_count()
    use_cpu_percent = psutil.cpu_percent(interval=1)

    cpuInfo = {}

    cpuInfo['physical_cpu_count'] = physical_cpu_count
    cpuInfo['logical_cpu_count'] = logical_cpu_count
    cpuInfo['use_cpu_percent'] = use_cpu_percent

    return cpuInfo


#Monitor Disk
def monDisk():
    # select partiton of disk
    diskInfo = psutil.disk_partitions()

    mountPoint = []
    for disk in diskInfo:
        mountPoint.append(disk.mountpoint)
    # print(mountPoint)

    dInfo = {}
    for mp in mountPoint:
        print(mp + "'s usage info is: ")
        print("\t Total: \t" + str(psutil.disk_usage(mp).total))
        print("\t Used: \t\t" + str(psutil.disk_usage(mp).used))
        print("\t Free: \t\t" + str(psutil.disk_usage(mp).free))
        print("\t Percent: \t" + str(psutil.disk_usage(mp).percent) + "%")

        dInfo[mp] = {
            'total' : str(round(psutil.disk_usage(mp).total/1024/1024,2)) + 'M',
            'used' : str(round(psutil.disk_usage(mp).used/1024/1024,2)) + 'M',
            'free' : str(round(psutil.disk_usage(mp).free/1024/1024,2)) + 'M',
            'percent' : str(psutil.disk_usage(mp).percent) + '%'
        }

    return dInfo
"""
#select data from oracle
"""
def getResults():
    conn = cx_Oracle.connect('dbusrgfc/future@192.168.2.216/jdgfc')
    cursor = conn.cursor()

    selectSql = '''select  a.tablespace_name,
        a.file_id,
        round(a.free/1024/1024,2) || 'M' as "free_size",
        b.total/1024/1024 || 'M' as "total_size",
        round(b.maxbytes/1024/1024,2) || 'M' as "can_max_auto_allocated_size",
        round(((b.total-a.free)/total)*100,2) || '%' as "used_percent",
        round(((b.maxbytes-b.total)/b.maxbytes)*100,2) || '%' as "can_auto_allocated_percent"
from
(select tablespace_name,file_id,sum(bytes) as free
        from dba_free_space group by tablespace_name,file_id) a,
(select tablespace_name,file_id,sum(bytes) as total,maxbytes
        from dba_data_files
        group by tablespace_name,file_id,maxbytes) b
where a.file_id = b.file_id
order by file_id'''
    cursor.execute(selectSql)
    results = []
    emp_title_list = []

    for desc in cursor.description:
        emp_title_list.append(desc[0])
    results.append(emp_title_list)

    result = cursor.fetchall()
    results.append(result)

    cursor.close()
    conn.close()

    return results

#获取网页内容函数
def render(tplPath,**kwargs):
    path,fileName = os.path.split(tplPath)
    template = Environment(loader=FileSystemLoader(path)).get_template(fileName)
    content = template.render(**kwargs)

    return content

def getContent():
    emp_title_list = getResults()[0]
    emp = 'emp'
    results = getResults()[1]
    mInfo = monMem()
    cpuInfo = monCpu()
    dInfo = monDisk()

    return render('Test.html',**locals())

#show web immediate
def showWeb():
    html = 'testJinja2.html'

    with open(html,'w') as fObj:
        fObj.write(getContent())
        fObj.close()

    webbrowser.open(html,new=1)

if __name__ == '__main__':
   # print(monMem())
   # print(monCpu())
   # print(monDisk())
	showWeb()

"""

"""下方代码可以执行"""
# -*- coding: utf-8 -*-

#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#收件人和发件人
receiver = '115787463@sina.com'
sender = '381784599@qq.com'

#发件人邮箱的SMTP服务器（即sender的SMTP服务器）
smtpserver = 'smtp.qq.com'

#发件人邮箱的用户名和授权码（不是登陆邮箱的密码）
username = '381784599@qq.com'
password = 'lnmmppcutjbnbgcc'       #（83xxxx202@qq.com邮箱的授权码）

mail_title = '系统有故障产生！'

import cx_Oracle
import os
import numpy as np
os.environ['NLS_LANG']='AMERICAN_AMERICA.WE8ISO8859P1'

conn = cx_Oracle.connect("dbusrgfc/future@192.168.2.216:1521/jdgfc",encoding="UTF-8",nencoding="UTF-8")  #,encoding='UTF-8',nencoding='UTF-8'
curs = conn.cursor()

sql = "select to_char(OEDATE,'yyyymmdd') ,OEKEY from OPERERRORS where OPERERRORS.OEDATE>=trunc(sysdate)-15"
curs.execute(sql)

for result in curs:
    #result[0] + result[1].encode('latin1').decode('gbk')
    #print(result[0]+','+result[1].encode('latin1').decode('gbk'))
    #mail_body=[]
    mail_body = result[0] +'     '+ result[1].encode('latin1').decode('gbk')
    print(type(mail_body))

curs.close()
conn.close()



#创建一个实例
mail_body = np.array[mail_body]
message = MIMEText(mail_body, 'plain', 'utf-8' )   #邮件正文
# (plain表示mail_body的内容直接显示，也可以用text，则mail_body的内容在正文中以文本的形式显示，需要下载）
message ['From'] = sender                                               #邮件上显示的发件人
message['To'] = receiver                                                   #邮件上显示的收件人
message['Subject'] = Header( mail_title, 'utf-8' )   #邮件主题


smtp = smtplib.SMTP()                                                     #创建一个连接
smtp.connect( smtpserver )                                            #连接发送邮件的服务器
smtp.ehlo()
smtp.starttls()
smtp.login( username, password )                                #登录服务器
smtp.sendmail( sender, receiver, message.as_string() )      #填入邮件的相关信息并发送
smtp.quit()
"""
#!/usr/bin/python
#coding: utf-8
import sys
import xlwt
import MySQLdb
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os.path
 
host = 'localhost'
user = 'user'
pwd = 'Passwd'
port = 3306
db = 'database'
sheet_name = 'report' + time.strftime("%Y-%m-%d")
filename = 'report_' + time.strftime("%Y-%m-%d") + '.xls'
out_path = '/data/monitor/temp/report_'+ time.strftime("%Y-%m-%d") + '.xls'
print(out_path)
sql = 'Select * from sys_user;'
def export():
    conn = MySQLdb.connect(host,user,pwd,db,charset='utf8')
    cursor = conn.cursor()
    count = cursor.execute(sql)
    print("查询出" + str(count) + "条记录")
    if count>0:
        #来重置游标的位置
        cursor.scroll(0,mode='absolute')
        #搜取所有结果
        results = cursor.fetchall()
        # 获取MYSQL里面的数据字段名称
        fields = cursor.description
        workbook = xlwt.Workbook(encoding = 'utf-8') # workbook是sheet赖以生存的载体。
        sheet = workbook.add_sheet(sheet_name,cell_overwrite_ok=True)
        # 写上字段信息
        for field in range(0,len(fields)):
            sheet.write(0,field,fields[field][0])
        # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1,len(results)+1):
            for col in range(0,len(fields)):
                sheet.write(row,col,u'%s'%results[row-1][col])
        workbook.save(out_path)
    else:
        print("无数据")
 
_user = "XXXX@qq.com"
_pwd = "passwd"
areceiver = "xxxxx@139.com"
acc = "xxxxx@139.com"
 
#如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] =u'【数据统计_' + time.strftime("%Y-%m-%d") + u'】'
msg["From"] = _user
msg["To"] = areceiver
msg["Cc"] = acc
 
def send_email():
    conn = MySQLdb.connect(host,user,pwd,db,charset='utf8')
    cursor = conn.cursor()
    count = cursor.execute(sql)
    #---这是文字部分---
    content = '''Deal all,\n附件是系统每日统计情况，请查收！
    总计结果数为：'''+str(count)
 
    part = MIMEText(content,'plain','utf-8')
    msg.attach(part)
    if count>0:
        #---这是附件部分---
        #xls类型附件
        file_name = '/data/monitor/temp/' + filename
        part = MIMEText(open(file_name,'rb').read(), 'base64', 'gb2312')
        part["Content-Type"] = 'application/octet-stream'
        basename = os.path.basename(file_name)
        part["Content-Disposition"] = 'attachment; filename=%s' % basename.encode('gb2312')
        msg.attach(part)
        s = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25
        s.login(_user, _pwd)#登陆服务器
        s.sendmail(_user, areceiver.split(',') + acc.split(','), msg.as_string())#发送邮件
        print("Email send successfully")
        s.close()
    else:
        print("nothing to send!")
#调用函数
if __name__=="__main__":
    export()
    send_email()

"""

"""
import os
import smtplib
import zipfile
from datetime import datetime, timedelta
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
import mysql.connector
import xlwt
 
mysql_host = ''  # TODO 请设置数据库地址
mysql_port = 3306  # TODO 请设置数据库端口
mysql_user = ''  # TODO 请设置数据库用户名
mysql_password = ''  # TODO 请设置数据库密码
 
 
class SQL(object):
    def __init__(self, name, params=None, formula=None):
        self._name = name
        self._params = params
        self.formula = formula
        with open(os.path.join('sql', name + '.sql'), 'r', encoding='utf-8') as f:
            self._sql = f.read()
 
    @property
    def filename(self):
        return self._name
 
    @property
    def sql(self):
        return self._sql
 
    @property
    def params(self):
        return self._params
 
 
class SQL1(SQL):
    @property
    def filename(self):
        today = datetime.now().strftime('%Y-%m-%d')
        return today + self._name + '.xls'
 
 
class SQL2(SQL):
    @property
    def filename(self):
        today = datetime.now().strftime('%Y-%m-%d')
        return today + self._name + '.xls'
 
    @property
    def sql(self):
        today = datetime.now()
        return self._sql % tuple([(today - timedelta(days=i)).strftime('%Y%m%d') for i in range(0, 7)])
 
 
def export(SQL, d='.'):
    conn = mysql.connector.connect(host=mysql_host, port=mysql_port, database='wifi', user=mysql_user,
                                   password=mysql_password)
    cursor = conn.cursor()
    cursor.execute(SQL.sql, SQL.params)
 
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')
 
    for i, val in enumerate(cursor.column_names):
        sheet.write(0, i, val)
 
    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        r = sheet.row(i + 1)
        for j, v in enumerate(row):
            r.write(j, v)
    if SQL.formula:
        sheet.write(len(rows) + 1, len(cursor.column_names), xlwt.Formula(SQL.formula))
    book.save(os.path.join(d, SQL.filename))
 
 
def export_all(sqls, dir='.'):
    if not sqls or len(sqls) < 1:
        return
    for item in sqls:
        try:
            export(item, dir)
        except Exception as e:
            print(e)
 
 
def do_export(d='.'):
    export_all([
        SQL1('SQL文件1'),
        SQL2('SQL文件2', formula='SUM($C$2:$C$100)'),
    ], d)
 
 
def zip_dir(d):
    f = zipfile.ZipFile(d + '.zip', 'w', zipfile.ZIP_DEFLATED)
    for *_, filenames in os.walk(d):
        for filename in filenames:
            f.write(os.path.join(d, filename))
    f.close()
 
 
def send_email(sender, sender_pass, receiver, filename):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(filename, 'utf-8').encode()
 
    # 邮件正文是MIMEText:
    msg.attach(MIMEText('统计数据 %s,请查看附件' % filename, 'plain', 'utf-8'))
 
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(filename, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('application', 'octet-stream', filename=filename)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=filename)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    smtp_server = 'smtp.qiye.163.com'
 
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.login(sender, sender_pass)
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()
 
 
def export_and_send():
    sender = ''  # TODO 请输入发送者邮箱,例如 mawei@ssgm.net
    sender_password = ''  # TODO 请输入发送者邮箱密码
    receiver = ''  # TODO 请输入接收者邮箱,例如 ssgmlihong@ssgm.net
    d = datetime.now().strftime('%Y-%m-%d') + ' 统计数据'
    if not os.path.exists(d):
        os.mkdir(d)
    do_export(d)
    zip_dir(d)
    send_email(sender, sender_password, receiver, d + '.zip')
 
 
if __name__ == '__main__':
    export_and_send()

"""