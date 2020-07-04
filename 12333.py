import cx_Oracle
import os
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.WE8ISO8859P1'

conn = cx_Oracle.connect("dbusrgfc/future@192.168.2.216:1521/jdgfc", encoding="UTF-8",
                             nencoding="UTF-8")  # ,encoding='UTF-8',nencoding='UTF-8'
curs = conn.cursor()

sql = "select  OAGH ,fgetpassword(OAPWD) from operaccnt where OAISLOGIN='Y'"
curs.execute(sql)

num=0

for (oagh,oapwd) in curs:
    num +=1
    print(num,oagh,oapwd)

curs.close()
conn.close()