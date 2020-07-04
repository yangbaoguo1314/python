# -*- coding: utf-8 -*-
import cx_Oracle
import os
os.environ['NLS_LANG']='AMERICAN_AMERICA.WE8ISO8859P1'

conn = cx_Oracle.connect("dbusrgfc/future@192.168.2.216:1521/jdgfc",encoding="UTF-8",nencoding="UTF-8")  #,encoding='UTF-8',nencoding='UTF-8'
curs = conn.cursor()

sql = "select  OAGH ,fgetpassword( OAPWD) from PAYMODE"
curs.execute(sql)

for result in curs:
    print(result[0]+'||'+result[1].encode('latin1').decode('gbk'))


curs.close()
conn.close()

"""
#代码不知道对不对？理论上是对的？
import cx_Oracle
import os
os.environ['NLS_LANG']='AMERICAN_AMERICA.WE8ISO8859P1'
def paymode_list():
  conn = cx_Oracle.connect("dbusrgfc/future@192.168.2.216:1521/jdgfc",encoding="UTF-8",nencoding="UTF-8")  #,encoding='UTF-8',nencoding='UTF-8'
  curs = conn.cursor()
  sql = "select PMCODE, PMNAME from PAYMODE where PMSTATUS='Y'"
  curs.execute(sql)
  for result in curs:
      #print(result[0]+'||'+result[1].encode('latin1').decode('gbk'))
      return result[0]+'||'+result[1].encode('latin1').decode('gbk')
  curs.close()
  conn.close()
"""