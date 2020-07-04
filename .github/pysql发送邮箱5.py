import pymysql
import time
import pexpect
import subprocess
import os
import socket
import urllib3
import sys

mintor_url = 'http://**************************&msg='  # 短息接口
News_Result_ = 'News_Result_'
tempdir = 'datas/'
tmpexedir = 'exedatas/'
reasultdir = 'redatas/'

##########oline###########
pubid = int(14219)
dbip = '********'

global ipath
ipath = os.getcwd() + '/'


def telme(info):
    global mintor_url
    tmp_url = mintor_url + info
    socket.setdefaulttimeout(10)
    response = urllib2.urlopen(tmp_url)
    html = response.read()
    print
    html
    response.close()


def getlogname(hour):
    return News_Result_ + str(time.strftime('%Y%m%d%H', time.localtime(time.time() - hour * 60 * 60))) + ".log"


def dbexe(filename):
    ida = str(time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60)))
    db = DB()
    data_list = db.getpubnews(pubid, ida)
    newsower = db.getnewsowerinfo(ida)
    print
    'open result file:', filename
    file = open(filename)
    k = 200
    dbresult = [];
    while 1:
        print
        'k:', k
        if k <= 0:
            break
        lines = file.readlines(200)
        if not lines:
            break
        for line in lines:
            try:
                if k <= 0:
                    break
                line = line.strip()
                lists = line.split('|')
                if (lists[0].isdigit() and lists[1].isdigit() and newsower.count(int(lists[0])) <= 0):
                    datainfo = []
                    datainfo.append(int(lists[0]))
                    datainfo.append(int(k))
                    dbresult.append(datainfo)
                    k -= 1
            except Exception as ex:
                print
                ex
    dbresult.reverse()
    if k > 100:
        print
        'data is to small,so return:', filename
        return
    if db.addpubnews(pubid, dbresult):
        if data_list[0] is not None:
            db.delpubnews(pubid, int(data_list[0]), int(data_list[1]))
    file.close()
    db.destory()


def checkexistsyn(name, num):
    if os.path.exists(name) == False:
        syndata(num)


def awkexe():
    log1 = ipath + tempdir + getlogname(2)

    log2 = ipath + tempdir + getlogname(3)
    log3 = ipath + tempdir + getlogname(4)
    checkexistsyn(log1, 2)
    checkexistsyn(log2, 3)
    checkexistsyn(log3, 4)

    reultname = ipath + reasultdir + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + '.log'
    cmd = ' cat ' + log1 + ' ' + log2 + ' ' + log3 + ' | awk \'$1 !~/^NULL/\'  | awk -F "|"  \'{a[$1]+=$2}END{for(x in a)print x"|"a[x]}\'  | sort -n  -r -k 2 -t "|" >> ' + reultname
    print
    'cmd:', cmd
    re = subprocess.call([cmd], shell=True)
    if re == 0:
        print
        'success'
        dbexe(reultname)
    else:
        telme('awk-exe-fail-oa')


def syndata(hour):
    logn = getlogname(hour)
    command = 'rsync -v user@**.**.***:*************t/' + logn + "  " + ipath + tempdir
    print
    'command:', command
    path = ipath + tempdir + logn
    foo = pexpect.spawn(command)
    index = foo.expect(["(?i)yes/no", "(?i)password", pexpect.EOF, pexpect.TIMEOUT])

    if (index == 0):
        print
        ' need---------------yes'
        foo.sendline('yes')
        foo.expect("(?i)password")
        foo.sendline('*******')
        foo.expect(pexpect.EOF)
        foo.close()
        print
        'syndata w success'
    elif (index == 1):
        print
        ' need---------------pass'
        foo.sendline('*******')
        foo.expect(pexpect.EOF)
        foo.close()

        print
        'syndata q success'
    else:
        print
        'has error'

    return os.path.exists(path)


def gethour():
    d4 = time.localtime(time.time())
    return int(d4.tm_hour)


def checkDate():
    hour = gethour()
    # if hour==9 or hour==12 or hour==17 or hour==20  or hour==0:
    #    return True

    return True


def startjob():
    k = 0
    while k < 10:
        k += 1
        if (syndata(2)):
            if checkDate():
                awkexe()
                return
            else:
                return
        else:
            time.sleep(60 * 5)

    telme('-ryn-data-error-oa-' + str(k))


def teststartjob():
    pass

    k = 0
    while k < 1:
        k += 1
        if (syndata(2)) and (syndata(3)) and syndata(4):
            #  if checkDate():
            awkexe()
            return
        else:
            time.sleep(60 * 5)

    telme('-ryn-data-error-oa')


class DB(object):

    def destory(self):
        if self.cur != None:
            print
            ('close db cur')
            self.cur.close()
        if self.conn != None:
            print
            ('close db conn')
            self.conn.close()
        print
        ('close db ')

    def __init__(self):

        self.conn = pymysql.connect(host=dbip, user='***', passwd='*****', db='****', port=3306, charset='utf8')
        self.cur = self.conn.cursor()

    def getnewsowerinfo(self, startTime):

        sql = "select oaid from DBUSRHQ.OPERACCNT"
        print(sql)
        list = (startTime)
        self.cur.execute(sql % list)
        data_list = []
        data_list.extend(self.cur.fetchall())
        result = []
        for data in data_list:
            try:
                result.append(int(data[0]))
            except Exception as eo:
                print("a date has error:", eo)
        return result

    def addpubnews(self, ipubid, datas):

        idate = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        sql = "insert into DBUSRGFC.OPERACCNT (oaid) values('%s')"
        for data in datas:
            list = (ipubid, data[0], data[1], idate, idate, idate, 'lixuan')
            # print "add sql:",sql%list
            self.cur.execute(sql % list)
        # self.cur.executemany(sql,relist)
        self.conn.commit()

        return True

    def delpubnews(self, ipubid, maxid, minid):

        print
        ('start dele data , maxid:%d,pubid:%d' % (maxid, ipubid))
        sql = 'delete from DBUSRGFC.OPERACCNT where oaid = %d '
        list = (maxid, minid, ipubid)
        self.cur.execute(sql % list)
        self.conn.commit()

    def getpubnews(self, ipubid, idate):
        # and createtime < '%s'
        sql = "select * from DBUSRGFC.OPERACCNT  where oaid =%d  "
        list = (ipubid)
        self.cur.execute(sql % list)
        data_list = []
        data_list.extend(self.cur.fetchall())
        return data_list[0];


if __name__ == '__main__':
    # global ipath
    if len(sys.argv) > 1:
        ipath = sys.argv[1]

    idate = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print
    ('start service...,', idate)
    # teststartjob()
    startjob()