# !/python3/codeinsql
'''
import pymysql
import pandas as pd

eng = pymysql.connect(host ='localhost',
                      user='root',
                      password = 'root',
                      #prot ='3306',
                      db ='hrs',
                      charset='utf8')
args ='%B%'
#sql = "select guid,account,name,level,honorRankPoints," \
#      "taxi_path from characters where name like '%s' " %args
#sql2 = "select guid,account,name,level,honorRankPoints," \
#      "taxi_path from characters where name like '%s' " %args
sql = "select eno,ename,job,mgr,sal,comm,dno from tb_emp "
df = pd.read_sql(sql,eng)'''

#print(df.head(10)) #显示前10行
#print(df.head(-18)) #从倒数第18行开始显示
#print(df.shape) #统计数据条数、列数
#print(df.info())  #查询数据列的数据类型
#print(df.describe())  #对数值型数据进行统计
#print(df.isnull())    #对数据是否为空进行判断
#print(df.dropna())    #去除null值，print(df.dropna(how= "all"))表示仅删除全部都是空值的数据行
#print(df.fillna({"honorRankPoints":"10000000","taxi_path":"1000"}))  #对空值数据进行填充
#print(df.drop_duplicates(subset=['honorRankPoints','account','level'],keep= "last"))
#对关键字进行去重处理,单个关键字可以直接使用df.drop_duplicates('')，
# 多个关键字是属于或关系不是且关系；keep="leat" :保留最后一个重复结果，keep = False 表示不保留任何重复数据；
#print(df.drop_duplicates(subset=['honorRankPoints','account','level'],keep= False))
'''感觉我的理解有问题！！！'''
#print(df['name'].dtype)  #查看数据类型，跟info()差不多
#(df['level'].dtype)
'''
数据类型共分为：int(整数)、float（浮点数）、object（python对象类型）、string（字符串类型,常常用S表示S10表示字符串长度为10）
unicode（固定长度的unicode类型，跟string基本差不多）、datetime64[ns] （时间格式）
'''
#df.columns =["序号","账户","名","等级","荣誉","位置"]  ##修改行号的名称即修改行索引

#print(df)
#df.set_index("guid")  #excle中修改列索引



#print(df.rename(columns={"guid":"新序号","account":"账户名"},index={0:"一",1:"二",2:"三"}).head(5))  #修改列、行索引名称，并显示前5行数据

#print(df)
#df.reset_index(level=None,drop=False,inplace=False)  #重置索引，分别是将第几级转化为columns，将所有索引删除等

#print(df.iloc[:,[3,2,4]].head(5))  #使用iloc参数显示部分数据
#print(df.iloc[:,2:4].head(5))   #显示连续的数据
#print(df.loc[2])   #显示第几行数据
#print(df.loc[0:2])

#print(df[df["level"]>=1])  ##条件显示数据

#print(df.iloc[[0,1],[3,2]])  #iloc传输进入行列位置信息，不知道怎么回事我电脑上面的loc参数无法使用

#print(df[df["level"]>30]["level","name"]) ##无法使用普通索引？原因是？

#print(df[df["level"]>30].ix[0:999,['level','name']])   #切片索引+普通索引检索数据,并进行条件筛选


#df["level"].replace(16,60,inplace=True) #对level中为16的数据进行替换修改16=>60
#print(df)


#df["level"].replace([60,16,1],62,inplace=True) #对多个数据进行替换
#print(df)

#df["level"].replace({60:61,16:62},inplace=True)
#print(df)

#df.sort_values(by=["name",'account'])
#print(df)

#df.sort_values(by=["name",'account'],ascending=False)  #True升序排列，False降序排列
#print(df)

#df.sort_values(by=["name"],na_position="first")  #缺失值显示在前
#print(df)


#df.sort_values(by=["name",'account'],ascending=[False,True])  #True升序排列，False降序排列,本次为name降序，account升序排列
#print(df)

#print(df[df["level"].rank(method="average")])   #平均数

#print(df["level"].rank(method="first"))

#print(df["level"].rank(method="min"))

#print(df["level"].rank(method="max"))


#print(df.drop(["guid","account","taxi_path"],axis=1)) #axis=1表示删除列

#print(df.drop(df.columns[[3,4,5]],axis=1))  #也可以用df.columns的格式删除列部分数据

#print(df.drop(colunmns=["account","taxi_path"]))  #使用columns=列名的形式的时候可以不需要axis=1

#print(df)
#print(df.drop([3,4,5],axis=0))  #删除序号为3、4、5的行数据
#print(df.drop(df.index[[0,5]],axis=0))

#print(df.drop(index=[1,3,5,7,8,11])) #删除1,3,5,7,8,11的数据
#print(df[df["level"]>30].drop(index=[0,1,2,3,8,9,10,15,20,18])) #过滤level小于30的数值并去除0,1,2,3,8,9,10,15,20,18数据
#print(df["account"].value_counts(normalize=True))  #统计数字并计算成占比
#print(df["account"].value_counts())    #统计数字
#print(df)
#print(df["name"].isin(["Bunny","亡者"]))  #精确查找包含数值的数据并以True，False显示出来
#print(df)
#print(df.isin(["Bunny",60]))  #python中暂时没学习到是否有模糊查询的语句，但是暂时先这样吧
#print(pd.cut(df["level"],bins=[0,15,30,45,60]))  #简单的数据切分
#print(pd.cut(df['level'],3)) #将数据简单的切分成三等分
#print(df)
####df["name":"巨馍蘸酱"].insert(2,"level",[60])  #代码报错，后期在看看原因
####df['level' <=30]["level"]=[60]   #insert 的事后面再说！！！！！
#print(df.T)  #行列互换
#print(df.T.T) #行列互换之后在互换
#print(df.insert(2,"times",["1","3","2","5","3","2","1","7","8","9","11","12","15","14","17","16","10","18","19","20","22","21"]))

#print(df.stack())  #索引重塑
#print(df.stack().unstack()) #索引重塑再重塑

#print(df)
"""宽表修改成长表stack方法"""
#print(df.set_index(["job","dno"]))
#print(df.set_index(["job","dno"]).stack())
#print(df.set_index(["job","dno"]).stack().reset_index())
"""melt()方法"""
#print(df)
#print(df.drop(df.columns[[4,5,6]],axis=1).melt(id_vars=["job"]),var_name="工号",value_name="姓名")
#print(df.melt(id_vars=["eno","job","dno"]))
"""
pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)

 

frame: 要处理的数据集。

id_vars: 可选项，不需要被转换的列名。

value_vars: 可选项，需要转换的列，如果剩下的列全部都要转换，就不用写了。

var_name和value_name： 自定义设置对应的列名。

col_level :如果列是MultiIndex，则使用此级别。

 

function：Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

功能：将数据从从宽数据转换为长数据，有选择的保留标识列。

df.pivot() 将长数据集转换成宽数据集，df.melt() 则是将宽数据集变成长数据集

"""


#print(df["dno"]).apply(lambda x:x+1) #对dno进行全数量+1操作
#print(df.applymap(lambda x:x+1)) #对全数据进行+1处理，提示必须要是int模型，不能是文本

#print(df)
#print(df["eno"]+df["dno"])  #数组内数据加减乘除运算
#print(df["eno"]*1.10)   #数组内部分数据加减乘除运算
#print(df["eno"]>df["dno"])  #True比较运算
#print(df["eno"]!=df["dno"])
#print(df["eno"]<df["dno"])
#print(df["eno"] == df["dno"])

"""count求汇总"""
#print(df.count(axis=1))  #count()求汇总数，count(axis=0)将数字。。。。count(axis=1)
#print(df["ename"].count())  #列汇总

"""sum求和"""
#print(df.sum())   #按照。。求和

#print(df.sum(axis=1)) #对每一列进行求和

#print(df["dno"].sum())
"""mean求平均值"""
#print(df.mean())  # 求每一列的平均值

#print(df.mean(axis=1)) #每一行的平均值

#print(df["dno"].mean()) #某一列的平均值
"""max求最大值"""

#print(df.max())   #最大值

#print(df.max(axis= 1)) #每一行的最大值

#print(df["dno"].max(axis= 1)) #每一行的最大值


"""min求最小值"""

#print(df.min())   #整个表的最小值

#print(df.min(axis= 1)) #每一列的最大值

#print(df["dno"].min()) #某一行的最小值

"""median求中位数"""
#print(df.median())
#print(df.median(axis =1))
#print(df["dno"].median())
"""mode求众数"""

#print(df.mode())
#print(df.median(axis =1))
#print(df["dno"].median())

"""var求方差"""

#print(df.var())
#print(df.var(axis =1))
#print(df["dno"].var())

"""std求标准差(是平方差的平方根)"""

#print(df.std())
#print(df.std(axis =1))
#print(df["dno"].std())

"""quantile求分位数"""

#print(df.quantile(0.25))   #求数的四分之一分位数
#print(df.quantile(0.25,axis =1))
#print(df["dno"].quantile(0.25))


"""corr求相关系数"""

#print(df["dno"].corr(df["eno"]))

#print(df.corr())
"""时间参数显示时间情况"""
from datetime import datetime

#print(datetime.now().year)  #显示当前年份
#print(datetime.now().month) #显示当前月份
#print(datetime.now().day)   #显示当前日期
#print(datetime.now().weekday()+1) #显示当前是周几
#print(datetime.now().isocalendar()) #显示当前年份及第几周第几天
#print(datetime.now().isocalendar()[1]) #拆分前年份及第几周第几天数据【0-2】

#print(datetime.now().date()) #当前时间
#print(datetime.now().time()) #详细时间

#print(datetime.now().strftime('%Y-%m-%d')) #时间显示

#print(datetime.now().strftime('%Y-%m-%d %H:%M:%S' )) #时间显示
"""时间格式转换成字符串格式"""
#now = datetime.now()
#print(now)
#print(type(now))
#print(type(str(now)))
#print(str(now))

"""将字符串格式转换成时间格式"""

#str_time = "2020-04-17"
#from dateutil.parser import parse
#time = parse(str_time)
#print(time)
#print(type(str_time))
#print(type(time))

"""时间索引"""
#我的numpy貌似有问题
'''
import pandas as pd
import numpy as np
index = pd.DatetimeIndex(['2018-01-01','2018-01-02','2018-01-03','2018-01-04',
                          '2018-01-05','2018-01-06','2018-01-07','2018-01-08'
                          '2018-01-09','2018-01-10'])
date =pd.DataFrame(np.arange(1,11),columns=["num"],index=index)
print(date)
print(date['2018'])
print(date['2018-01'])
print(date['2018-01-01':'2018-01-05'])
'''
"""
import pymysql
import pandas as pd

eng = pymysql.connect(host ='localhost',
                      user='root',
                      password = 'root',
                      #prot ='3306',
                      db ='school',
                      charset='utf8')

sql = "select scid,a.stuid,c.stuname,a.couid,b.couname,scdate,scmark from tb_score a,tb_course b,tb_student c where a.couid=b.couid and a.stuid=c.stuid"
df = pd.read_sql(sql,eng)"""
#print(df)
#print(df[df["scdate"] == datetime(2017,9,1)])
#print(df[df["scdate"] > datetime(2017,9,1)])
#print(df[df["scdate"] < datetime(2017,9,30)])
#print(df[(df["scdate"] > datetime(2017,9,1))&(df["scdate"] <datetime(2017,9,6))]) #时间段内的数据集合
"""时间差计算"""
'''cha = datetime(2018,5,21,19,50)-datetime(2018,4,10,20,15)
print(cha)
print(cha.days)
print(cha.seconds)
print(cha.seconds/3600)'''

"""时间偏移"""
"""
from datetime import timedelta

date = datetime(2018,5,18,20,32)
date1 = date+timedelta(seconds=60)
print(date1)
date1 = date - timedelta(days= 1)
print(date1)
date1 = date + timedelta(minutes= 3600)
print(date1)

from pandas.tseries.offsets import Day,Hour,Minute

date = datetime(2018,5,18,20,32)

date1 = date +Day(1)
print(date1)
date1 = date + Hour(60)
print(date1)
date1 = date +Minute(30)
print(date1)
"""
"""分组函数"""
#print(df)
"""分组键是列名"""
#print(df.groupby("couid").count()) #数据分组
#print(df.groupby("couid").sum())
#print(df.groupby(["couid","scdate"]).count())
#print(df.groupby(["couid","scdate"]).sum())
#print(df.groupby("couid")["scdate"].count())
"""分组键是Series"""
#print(df["couid"])
#print(df.groupby(df["couid"]).count())
#print(df.groupby([df["couid"],df["scdate"]]).sum())
#print(df.groupby([df["couid"],df["scdate"]]).count())
#print(df.groupby(df["couid"])["scdate"].count())

"""aggregate函数"""
#print(df.groupby("couid").aggregate(["count","sum"]))


#print(df.groupby("couid").aggregate({"scdate":"count","scid":"sum","scmark":"sum"}))
"""数据分组处理后重置索引"""
#print(df.groupby("stuid").sum())

#print(df.groupby("stuid").sum().reset_index())  #数据分组处理后重置索引
"""数据透视表"""
#print(df)
"""格式"""
#pd.pivot_table(df,values=None,index=None,columns=None,aggfunc="mean",fill_value=None,margins=False,dropna=True,margins_name="all")
#print(pd.pivot_table(df,values="scid",columns="couname",index="scmark",aggfunc="count"))
#print(pd.pivot_table(df,values="scid",columns="couname",index="scmark",aggfunc="count",margins=True))
#print(pd.pivot_table(df,values="scid",columns="couname",index="stuid",aggfunc="count",margins=True,margins_name="合计").fillna(0)) #

#print(pd.pivot_table(df,values="scid",columns="couname",index="stuid",aggfunc="count",margins=True,margins_name="合计").fillna(0).reset_index())


# import pymysql
# import pandas as pd
#
# eng = pymysql.connect(host ='localhost',
#                       user='root',
#                       password = 'root',
#                       #prot ='3306',
#                       db ='school',
#                       charset='utf8')
#
# sql1 = "select scid,stuid ,couid,scdate from tb_score "
# sql2 ='select stuid,stuname,stubirth,stuaddr,collid from tb_student'
# df1 = pd.read_sql(sql1,eng)
# df2 = pd.read_sql(sql2,eng)

#print(df1)
#print(df2)
#print(pd.merge(df1,df2))
#print(pd.merge(df1,df2,on= "stuid"))
#print(df3)

#print(pd.merge(df1,df2,on=["stuid","stuname"]))

#print(pd.merge(df1,df2,left_on="bianhao",right_on="stuid"))

#print(pd.merge(df1,df2,left_index= True,right_index= True))
#print(pd.merge(df1,df2,left_index= True,right_on= "stuid"))
#print(pd.merge(df1,df2,on="stuid",how="inner")) #内连接查询
#print(pd.merge(df1,df2,on="stuid",how="left")) #左连接
#print(pd.merge(df1,df2,on="stuid",how="right")) #右连接
#print(pd.merge(df1,df2,on="stuid",how="outer")) #外连接
"""重复数据处理"""
#print(pd.merge(df1,df2,on='stuid',how='inner',suffixes=["_L","_R"])) #给重复的列名加上_L,_R标题
"""表的纵向拼接"""
"""数据合并"""
#print(pd.concat([df1,df2]))


############2020-04-19###############

"""原始数据"""
# import pymysql
# import pandas as pd
#
# eng = pymysql.connect(host ='localhost',
#                       user='root',
#                       password = 'root',
#                       #prot ='3306',
#                       db ='school',
#                       charset='utf8')
#
# sql1 = "select scid,stuid ,couid,scdate from tb_score "
# sql2 ='select stuid,stuname,stubirth,stuaddr,collid from tb_student'
# df1 = pd.read_sql(sql1,eng)
# df2 = pd.read_sql(sql2,eng)
#

"""索引设置"""
#print(df1)
#print(df2)
#print(pd.concat([df1,df2],ignore_index=True))  #从新建立索引
#print(pd.concat([df1,df2],ignore_index=False))  #不从新建立索引
#print(pd.concat([df1,df2],ignore_index=True).drop_duplicates()) #对新建索引的数据进行删除重复值操作

"""数据导出成xlsx格式"""
#df1.to_excel(excel_writer= r"C:\Users\Administrator\Desktop\测试文档.xlsx",sheet_name="ceshi",index=False,columns=["scid","stuid","couid","scdate"]  )
#不导出自动生成的索引
#df1.to_excel(excel_writer= r"C:\Users\Administrator\Desktop\测试文档.xlsx",sheet_name="ceshi",index=True,index_label="ID",columns=["scid","stuid","couid","scdate"])
#sheet_name为sheet的名字，index为最前一列一般为序号，index_label：索引名称，coulumns导出的数据列
"""导出数据编码设置"""
#df1.to_excel(excel_writer= r"C:\Users\Administrator\Desktop\测试文档.xlsx",sheet_name="ceshi",index=True,index_label="ID",columns=["scid","stuid","couid","scdate"],encoding="utf-8")
#设置导出的数据编码格式
"""缺失数值处理"""
#df1.to_excel(excel_writer= r"C:\Users\Administrator\Desktop\测试文档.xlsx",sheet_name="ceshi",index=True,index_label="ID",columns=["scid","stuid","couid","scdate"],na_rep= 0)
#将空值或者说缺失数值填充为0
"对NaN(空值)=0,inf(无穷值）=0进行处理"
#df1.to_excel(excel_writer= r"C:\Users\Administrator\Desktop\测试文档.xlsx",sheet_name="ceshi",index=True,index_label="ID",columns=["scid","stuid","couid","scdate"],encoding="utf=8",na_rep= 0,inf_rep= 0)

"""导出数据为CSV"""


#df2.to_csv(path_or_buf= r"C:\Users\Administrator\Desktop\测试文档.csv",
#           index=False,
#           columns=["stuid","stuname","stubirth","stuaddr"],
#           sep=",",
#           encoding="utf-8-sig",
#           na_rep=0
#           )

#sep为分隔符号
"""将文件导出到多个sheet"""
#excelpath = r"C:\Users\Administrator\Desktop\测试文档.xlsx"
#writer = pd.ExcelWriter(excelpath,engine='xlsxwriter')
#df3 =pd.concat([df1,df2])
#df1.to_excel(writer,sheet_name="表1",na_rep=0,inf_rep=0,encoding="utf-8")
#df2.to_excel(writer,sheet_name="表2",na_rep=0,inf_rep=0,encoding="utf-8")
#df3.to_excel(writer,sheet_name="表3",na_rep=0,inf_rep=0,encoding="utf-8")
#writer.save()



#####2020.4.20#####


# """数据可视化"""
# """简单的数据可视化初始化过程以下代码运行于jupyter Notebook"""
# import matplotlib.pyplot as plt               #引入matplotlib.pyplot函数
# #% matplotlib inline                           #使图表在jupyter Notebook中展示
# plt.rcParams["font.sans-serif"] = 'SimHei'    #解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False    #解决负号无法显示的问题
# #% config InlineBackend.figuer_format = 'svg'
# fig = plt.figure()
# plt.figure(figsize=(8,6))
# fig = plt.figure()
# ax1  = fig.add_subplot(1,1,1)
# print(fig)
#
# fig  = plt.figure()
# ax1  =fig.add_subplot(2,2,1) #设置区域位置
# ax2  =fig.add_subplot(2,2,2)
# ax3  =fig.add_subplot(2,2,3)
# ax4  =fig.add_subplot(2,2,4)
#
#
# plt.subplot2grid((2,2),(0,0))
#
#
# import numpy as np
# x = np.arange(6)
# y = np.arange(6)
# #将图表的整个区域分成2行2列，且在（0，0）位置做折线图
# plt.subplot2grid((3,3),(0,0))
# plt.plot(x,y)  #plot 线形？
#
# #将图表的整个区域分成2行2列，且在（0，0）位置做柱形图
# plt.subplot2grid((3,3),(0,1))
# plt.bar(x,y)   #bar  柱形？
#
#
# #plt.subplot设置坐标系
# import numpy as np
# x = np.arange(6)
# y= np.arange(6)
# plt.subplot(2,2,1)
# plt.plot(x,y)
# plt.subplot(2,2,4)
# plt.bar(x,y)
#
# import numpy as np
# fig,axes = plt.subplots(2,2)
# x = np.arange(6)
# y = np.arange(6)
#
# axes[0,0].plot(x,y)  #在0，0区域绘制线形图
#
# axes[1,1].bar(x,y)  #在1，1区域绘制柱形图
#
# plt.xlabel("月份")   #设置X的名称
# plt.ylabel("注册量")  #设置Y的名臣
#
# plt.xlabel("月份",fontsize='xx-large',color='#40AD47',fontweight='bold',labelpad = 10)  #设置大小及颜色，字体等
# plt.ylabel("注册量",labelpad=10)
#
# ##### 设置刻度
# plt.xticks(np.arange(9)['1月份','2月份','3月份','4月份','5月份','6月份','7月份','8月份','9月份'])
# plt.yticks(np.arange(1000,7000,1000),["1000人","2000人","3000人","4000人","5000人","6000人"])
#
# plt.xticks([])  #传空值进入系统，防止被人看见X、y名称
# plt.yticks([])
#
# #plt.tick_params(axis,reset,which,direction,length,width,color,pad,labelsize,labelcolor,bottom,top,left,right,labelbottom,laveltop,lavelleft,labelright) #轴刻度线设置可选参数
# """
# axis:对那个轴进行刻度线设置，X,Y,both可选
# reset:是否重置所有设置True/False
# which：对那种刻度线进行设置：major(主刻度线)、minor（次刻度线）、both三种可选
# direction:刻度线的朝向，in 朝里、 out 朝外、inout 内外均设置三种
# length:刻度线长度
# width：刻度线宽度
# color：刻度线颜色
# pad:刻度线和刻度标签的距离
# labelsize:刻度标签大小
# labelcolor：刻度标签颜色
# top,left,right：控制上下左右刻度是否显示，控制参数：True/False
# labelbottom,laveltop,lavelleft,labelright：控制上下左右刻度标签是否显示，控制参数：True/False
# """
# x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# y = np.arange([866,2335,5710,6482,6120,1605,3813,4428,4631])
# plt.subplot(2,1,1)
# plt.plot(x,y)
# plt.xlabel("月份")
# plt.ylabel("注册人数")
# plt.tick_params(axis="both",which ="both",direction = "inout",bottom= "False")
#
# plt.subplot(2,1,2)
# plt.plot(x,y)
# plt.xlabel("月份")
# plt.ylabel("注册人数")
# plt.tick_params(axis="both",which ="both",direction = "inout",bottom= "False")
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# #% config InlineBackend.figuer_format = 'svg'
# plt.title(label="1-9月份注册人数分析表", loc="left")
# # 可选择的设置项目：fontsize  字号大小；prop 关于文本的相关设置，以字典形式传给参数prop，facecolor 背景颜色
# # title 标题；title_fontsize 标题的大小；shadow  是否添加阴影，只有Treu和False
# # loc还可以设置显示位置共有：right靠右；left 靠左；center 居中三种
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([866, 2335, 5710, 6482, 6120, 1605, 3813, 4428, 4631])
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y)
# plt.xlabel("月份")
# plt.ylabel("注册人数")
# plt.tick_params(axis="both", which="both", direction="inout", bottom="False")
#
# plt.plot(x, y, label="折线图")
# plt.bar(x, y, label="柱形图")
# plt.legend(loc="lower center")
# plt.legend(loc=2)
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# % config
# InlineBackend.figuer_format = 'svg'
# # plt.title(label = "1-9月份注册人数分析表",loc= "left")
# # 可选择的设置项目：fontsize  字号大小；prop 关于文本的相关设置，以字典形式传给参数prop，facecolor 背景颜色
# # title 标题；title_fontsize 标题的大小；shadow  是否添加阴影，只有Treu和False
# # loc还可以设置显示位置共有：right靠右；left 靠左；center 居中三种
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([866, 2335, 5710, 6482, 6120, 1605, 3813, 4428, 4631])
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y)
# plt.xlabel("月份")
# plt.ylabel("注册人数")
# plt.tick_params(axis="both", which="both", direction="inout", bottom="False")
#
# plt.plot(x, y, label="折线图")
# plt.bar(x, y, label="柱形图")
# plt.legend(loc="lower center")
# plt.legend(loc=2)

"""设置数据标签"""
"""
plt.text(x,y,str,ha,va,fontsize)  
参数x,y 分别表示在哪里显示数值
str  需要显示的具体数据
horizontalalignment:简称ha,表示str在水平方向的位置有：center,left,right
verticalalignment:简称va,表示str在垂直方向的位置有center,top,bottom
fontsize:str字体大小
'''设置图标注释'''
plt.annotate(s,xy,xytext,arrowprops)
s：文本中注释的内容
xy：需要注释的位置
xytext：注释文本显示的位置
arrowprops：注释箭头参数颜色，箭类型等等
# """
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# % config
# InlineBackend.figuer_format = 'svg'
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([866, 2335, 5710, 6482, 6120, 1605, 3813, 4428, 4631])
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y)
# plt.xlabel("月份")
# plt.ylabel("注册人数")
# plt.tick_params(axis="both", which="both", direction="inout", bottom="False")
#
# for a, b in zip(x, y):
#     plt.text(a, b, b, ha="center", va="bottom", fontsize=11)  # 在峰值上面显示具体数值
#
# plt.annotate("下雨天，无人购物", xy=(6, 1605), xytext=(6, 5600), arrowprops=dict(facecolor='black', arrowstyle='->'))
#
# plt.plot(x, y, label="折线图")
# plt.bar(x, y, label="柱形图")
# plt.legend(loc="lower center")
# plt.legend(loc=2)

"""数据表"""
"""
table(celltext=None,cellColours=None,cellLoc='right',colWidths=None,rowLabels = None,rowColours = None,rowLoc='left',
      colLaberls = None,colColours = None, colLoc='center',loc='bottom')
celltext=None 数据表内的数值
cellColours=None 数据表的颜色
cellLoc='right' 数据表中数值的位置：left,right,center三种可选择
colWidths=None  列宽
rowLabels = None 行标签
rowColours = None 行标签颜色
rowLoc='left'  行标签位置
colLaberls = None 列标签
colColours = None 列标签颜色
colLoc='center'列标签的位置
loc='bottom' 整个数据表的位置，可选坐标系的上下左右
# """
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# % config
# InlineBackend.figuer_format = 'svg'
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([866, 2335, 5710, 6482, 6120, 1605, 3813, 4428, 4631])
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y)
# plt.xlabel("月份")
# plt.ylabel("注册人数")
# plt.tick_params(axis="both", which="both", direction="inout", bottom="False")
#
# for a, b in zip(x, y):
#     plt.text(a, b, b, ha="center", va="bottom", fontsize=11)  # 在峰值上面显示具体数值
#
# plt.annotate("下雨天，无人购物", xy=(6, 1605), xytext=(6, 5600), arrowprops=dict(facecolor='black', arrowstyle='->'))
#
# cellText = [[8566, 5335, 7310, 6482], [4283, 2667, 3655, 3241]]
# rows = ['任务量', '完成量']
# columns = ['东区', '南区', '西区', '北区']
# plt.table(cellText=cellText,
#           cellLoc='center',
#           rowLabel=rows,
#           rowColours=['red', 'yellow'],
#           rowLoc='center',
#           colLabels=columns,
#           colColours=['red', 'yellow', 'red', 'yellow'],
#           colLoc='left',
#           loc='bottom')
# plt.plot(x, y, label="折线图")
# plt.bar(x, y, label="柱形图")
# plt.legend(loc="lower center")
# plt.legend(loc=2)
#



"""plot参数"""
"""
plt.plot(x,y,color,linestyle,linewidth,marker,markeredgecolor,markeredgwidth,markerfacecolor,markersize,label)
x,y:x、y轴的数据
color: 颜色代码有：b 蓝色，g 绿色,r 红色,c 青色,m 品红,y 黄色,k 黑色,w 白色；颜色还可以用标准颜色名称、十六进制颜色值、RGB元组方式表示，
    例如：黑色：颜色缩写代码 k 标准颜色名称 black  十六进制颜色值  #000000，RGB元组  0，0，0
linestyle:线条风格，参数如下：solid 实线  dashed  短线   dashdot 线点相接  dotted 虚点线
linewidth：线的宽度，传入一个浮点数即可
marker：
折线图中每点的标记物形状
.点标记
o圆圈标记
v 下三角形标记
^上三角形标记
<> 左右三角形标记
s 正方形标记
p 五边形标记
* 五角星标记
h 六边形标记
+ +号标记
x x标记
D 大菱形标记
d 小菱形标记
_ 横线标记
其参数为：
markeredgecolor 标记外边的颜色
markeredgwidth  标记外边的线宽
markerfacecolor 标记实心颜色
markersize      标记大小
lavel           标记图例的名称即上述形状
# """
# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams["font.sans-serif"] = 'SimHei'    #解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False    #解决负号无法显示的问题
# #% config InlineBackend.figuer_format = 'svg'
# plt.subplot(1,1,1) #建立坐标系
# x = np.array([1,2,3,4,5,6,7,8,9]) #X数值
# y = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])  #Y数值
#
# plt.plot(x,y,color = 'k',linestyle="dashdot",linewidth=1,marker="o",markersize=5,label = "注册用户数")
#
# #设置标题
# plt.title("安德利1-9月份注册用户量",loc = "center")
#
# #添加数据标签
# for a,b in zip(x,y):
#     plt.text(a,b,b,ha='center',va= "bottom",fontsize=10)
#
#
# #设置网格线
#
# plt.grid(True)
#
# plt.legend() #设置图例，调用plot中的label
#
# plt.savefig(r"C:\Users\Administrator\Desktop\plot.jpg") #结果保存到

"""绘制柱形图"""
"""
plt.bar(x,height,width=0.8,bottom= None,align='center',color,edgecolor)
x: 在何处显示柱形图
height  每柱体高度
wigth   每柱体宽度，可以一样也可以不一样
bottom  柱体底部位置，可以一样也可以不一样
align   柱子的位置跟X的关系，有center 柱子位于X数值的中心位置,edge 柱子位于X数值的边缘位置
color   柱体颜色
edgecolor 柱体边缘的颜色
# """
# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams["font.sans-serif"] = 'SimHei'    #解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False    #解决负号无法显示的问题
# #% config InlineBackend.figuer_format = 'svg'
# plt.subplot(1,1,1) #建立坐标系
# x = np.array(["东","西","南","北"]) #X数值
# y = np.array([8566,6482,5335,7310])  #Y数值
# #绘图
# plt.bar(x,y,width=0.5,align= "center",label ="任务情况")
# #设置标题
# plt.title("全国各区任务量",loc = "center")
#
# #添加数据标签
# for a,b in zip(x,y):
#     plt.text(a,b,b,ha='center',va="bottom",fontsize=12)
#
# #设置X、y轴的名称
# plt.xlabel("分区")
# plt.ylabel("任务量")
#
# plt.legend() #显示图例
#
# plt.savefig(r"C:\Users\Administrator\Desktop\bar1.jpg")
#
# # 绘制簇装柱形图
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1, 1, 1)  # 建立坐标系
# x = np.array([1, 2, 3, 4])  # X数值
# y1 = np.array([8566, 5335, 7310, 6482])  # Y数值
# y2 = np.array([4283, 2667, 3655, 3241])
# # 绘图
# plt.bar(x, y1, width=0.3, label="任务量")
# plt.bar(x + 0.3, y2, width=0.3, label="完成量")  # x+0.3相当于将完成量的每个柱子向右移动0.3
# # 设置标题
# plt.title("全国各区任务量并完成情况", loc="center")
#
# # 添加数据标签
# for a, b in zip(x, y1):
#     plt.text(a, b, b, ha='center', va="bottom", fontsize=12)
# for a, b in zip(x + 0.3, y2):
#     plt.text(a, b, b, ha='center', va="bottom", fontsize=12)
#
# # 设置X、y轴的名称
# plt.xlabel("区域")
# plt.ylabel("任务情况")
#
# plt.xticks(x + 0.15, ["东", "南", "西", "北"])  # 设置X轴的刻度
#
# plt.grid(False)
#
# plt.legend()  # 显示图例
#
# plt.savefig(r"C:\Users\Administrator\Desktop\bar2.jpg")
#
#
#
# ##堆积柱形图
#
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1, 1, 1)  # 建立坐标系
# x = np.array(["东", "南", "西", "北"])  # X数值
# y1 = np.array([8566, 5335, 7310, 6482])  # Y数值
# y2 = np.array([4283, 2667, 3655, 3241])
# # 绘图
# plt.bar(x, y1, width=0.3, label="任务量")
# plt.bar(x, y2, width=0.3, label="完成量")  # x+0.3相当于将完成量的每个柱子向右移动0.3
# # 设置标题
# plt.title("全国各区任务量并完成情况", loc="center")
#
# # 添加数据标签
# for a, b in zip(x, y1):
#     plt.text(a, b, b, ha='center', va="bottom", fontsize=12)
# for a, b in zip(x, y2):
#     plt.text(a, b, b, ha='center', va="bottom", fontsize=12)
#
# # 设置X、y轴的名称
# plt.xlabel("区域")
# plt.ylabel("任务情况")
#
#
# plt.grid(False)
#
# plt.legend(loc="upper center",ncol= 2)  # 显示图例
#
# plt.savefig(r"C:\Users\Administrator\Desktop\bar3.jpg")
#
#
# #绘制条形图
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1, 1, 1)  # 建立坐标系
# x = np.array(["东", "南", "西", "北"])  # X数值
# y = np.array([8566, 5335, 7310, 6482])  # Y数值
# # 绘图
# plt.barh(x,height=0.5, width=y, align="center")
#
# # 设置标题
# plt.title("全国各区任务并完成情况", loc="center")
#
# # 添加数据标签
# for a, b in zip(x, y):
#     plt.text(b, a, b, ha='center', va="center", fontsize=12)
#
#
# # 设置X、y轴的名称
# plt.ylabel("区域")
# plt.xlabel("任务情况")
#
#
# plt.grid(False)
#
# plt.legend() # 显示图例
#
# plt.savefig(r"C:\Users\Administrator\Desktop\bar4.jpg")
#
#
# """
# 绘制散点图
# scatter
# plt.scatter(x,y,s,c,marker,linewidths,edgecolors)
# x,y  散点的位置
# s    散点的面积 可以设置相同也可以不相同
# c    散点的颜色，可以多色彩
# marker  点标记
# linewidths 散点的线宽
# edgecolors 散点轮廓颜色
# """
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1, 1, 1)  # 建立坐标系
# x = [5.5,6.6,8.1,15.8,19.5,22.4,28.3,28.9]  # X数值
# y = [2.38,3.85,4.41,5.67,5.44,6.03,8.15,6.87]  # Y数值
# # 绘图
# plt.scatter(x,y,marker = "o",s = 100)
#
# # 设置标题
# plt.title("全国各区任务关系图", loc="center")
#
#
# # 设置X、y轴的名称
# plt.ylabel("气温")
# plt.xlabel("任务情况")
#
#
# plt.grid(False)
#
# plt.legend() # 显示图例
#
# plt.savefig(r"C:\Users\Administrator\Desktop\scatter.jpg")
#

#
#
# #绘制条形图
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1, 1, 1)  # 建立坐标系
# x = np.array([5.5,6.6,8.1,15.8,19.5,22.4,28.3,28.9])  # X数值
# y = np.array([2.38,3.85,4.41,5.67,5.44,6.03,8.15,6.87])  # Y数值
# # 绘图
# colors =y *10  #根据Y生成不同颜色
# area   = y*100 #根据Y生成不同形状
#
# plt.scatter(x,y,c = colors,marker ="o",s = area)
#
# # 设置标题
# plt.title("全国各区任务关系图", loc="center")
#
# # 添加数据标签
# for a, b in zip(x, y):
#     plt.text(a, b, b, ha='center', va="center", fontsize=10,color="white")
#
#
# # 设置X、y轴的名称
# plt.ylabel("区域")
# plt.xlabel("任务情况")
#
#
# plt.grid(False)
#
# plt.legend() # 显示图例
#
# plt.savefig(r"C:\Users\Administrator\Desktop\scatter1.jpg")
#
#
# #绘制面积图
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1, 1, 1)  # 建立坐标系
# x = np.array([1,2,3,4,5,6,7,8,9])  # X数值
# y1 = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])  # Y数值
# y2 = np.array([433,1167,2855,3241,3060,802,1906,214,2315])
# # 绘图
# labels =["注册人数","激活人数"]
#
# plt.stackplot(x,y1,y2,labels=labels)
#
# # 设置标题
# plt.title("全国各区注册激活情况分析表", loc="center")
#
# # 设置X、y轴的名称
# plt.ylabel("时间")
# plt.xlabel("注册与激活人数")
#
#
# plt.grid(False)
#
# plt.legend() # 显示图例
#
# plt.savefig(r"C:\Users\Administrator\Desktop\stackplot.jpg")

"""树形图"""
"""
squarify.plot(sizes,label,color,value,edgecolor,linewidth)
size :待绘图数据
label  ：不同类别的图例标签
color  ：不同类别的颜色
value  ：不同类别的数据标签
edgecolor：不同类别之间边框的颜色
linewidth: 边框线宽
# """
# import squarify
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# #设置图块大小
# size =np.array([3.4,0.693,0.585,0.570,0.562,0.531,0.530,0.524,0.501,0.478,0.468,0.436,0.30])
# #设置图块文字标签
# xingzou =np.array(["未知","摩羯座","天秤座","双鱼座","天蝎座","金牛座","处女座","双子座","射手座","狮子座","水瓶座","白羊座","巨蟹座"])
# #设置图块数值标签
# rate   =np.array(["34%","6.93%","5.85%","5.70%","5.62%","5.31%","5.30%","5.24%","5.01%","4.78%","4.68%","4.36","1.39%"])
# #设置图块颜色
# colors = ['steelblue','#9999ff','red','indianred','green','yellow','orange']
# #绘图
# plot = squarify.plot(sizes=size,
#                      label=xingzou,
#                      color=colors,
#                      value= rate,
#                      edgecolor = 'white',
#                      linewidth=3
#                      )
# #标题
# plt.title('星座分析情况图',loc='center',fontdict={'fontsize':12})
# #去除坐标轴
# plt.axis('off')
# #去除上边框和右边框的刻度
# plt.tick_params(top = 'off',right ='off')
# #显示
# plt.legend()
# #保存
# plt.savefig(r"C:\Users\Administrator\Desktop\squarify.jpg")


###2020.4.22#####
"""
雷达图
plt.polar(theta,r,color,marker,linewidth)

theta   每一点在极坐标系中的角度.
r       每一点在极坐标系的半径
color   连接各点之间线的颜色
marker  每点的标记物
linewidth  连接线的宽度
# """
# import squarify
# import numpy as np
# import matplotlib.pyplot as plt
# #
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(111,polar = True) #polor = True表示建立一个极坐标系
# dateLenth = 6
# #np.linspace 表示在指定的间隔内返回均匀间隔的数值
# angles = np.linspace(0,2*np.pi,dateLenth,endpoint=False)
# labels = ["积极性","主动性","屈从性","盲目性","自信心","傻逼性"]
# data   = [2,3.5,4,4.5,5,9]
#
# data   = np.concatenate((data,[data[0]]))  #闭合
# angles = np.concatenate((angles,[angles[0]])) #闭合
# #绘图
# plt.polar(angles,data,color ="r",marker = "o")
#
# plt.xticks(angles,labels)
#
# plt.title(label='一个傻逼的自我修养',loc='center')
#
# plt.legend()
#
# plt.savefig(r"C:\Users\Administrator\Desktop\polar.jpg")
#
#
# """
# 箱形图
# plt.boxplot(x,vert,widths,label)
# x 待绘图数据
# vert 图方向True表示纵向，False 表示横向，默认纵向
# widths 图的宽度
# label  图标签
# """
#
# import numpy as np
# import matplotlib.pyplot as plt
# #
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1,1,1)
# #X数值
# y1 = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])
# y2 = np.array([433,167,2855,3241,3060,802,1906,2214,2315])
# x = [y1,y2]
# #绘图
# labels = ["注册人数","付费人数"]
# plt.boxplot(x,labels=labels,vert=True,widths= [0.2,0.5])
#
# plt.title("公司注册激活付费人数一览表",loc="center")
#
# plt.grid(False)
#
# plt.legend()
#
# plt.savefig(r"C:\Users\Administrator\Desktop\boxplot.jpg")
#
#
# """
# 饼图
# plt.pie(x,ecplode,labels,colors,autopct,pctdistance,shadow,laberldistance,startangle,radius,coimterclock
# ,wedgeprops,textprops,centern,frame)
# 绘图数据，每一快离圆心的距离，块标签，块颜色，百分比格式，标签距离中心距离，是否有阴影，索引距离中心距离，初始角度，半径，是否逆时针显示，内外边界属性，文本相关属性
# 中心位置，背后的图框
# """
# import numpy as np
# import matplotlib.pyplot as plt
# #
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1,1,1)
# x = np.array([8566,5335,7310,6482])
#
# labels =["东","南","西","北"]
# explode = [0.05,0,0,0]
# labeldistance=1.1
# plt.pie(x,labels=labels,autopct='%.0f%%',shadow=True,explode=explode,radius=1.0,labeldistance=labeldistance)
#
# plt.title("任务占比",loc="center")
# plt.legend()
# plt.savefig(r"C:\Users\Administrator\Desktop\pie.jpg")
#
# """圆环图"""
#
# import numpy as np
# import matplotlib.pyplot as plt
# #
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1,1,1)
# x1 = np.array([8566,5335,7310,6482])
# x2 = np.array([4283,2667,3655,3241])
# #绘图
# labels =["东","南","西","北"]
#
# plt.pie(x1,labels=labels,shadow=True,radius=1.0,wedgeprops=dict(width=0.3,edgecolor='w'))
# plt.pie(x2,radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'))
# #添加注释
# plt.annotate("完成量",xy=(0.35,0.35),xytext=(0.7,0.45),arrowprops = dict(facecolor='black',arrowstyle='->'))
# plt.annotate("任务量",xy=(0.75,0.25),xytext=(1.1,0.2),arrowprops = dict(facecolor='black',arrowstyle='->'))
#
# plt.title("任务及完成量占比",loc="center")
# plt.legend()
# plt.savefig(r"C:\Users\Administrator\Desktop\pie1.jpg")
#
#
# """
# 热力图
# plt.imshow(x,cmap) cmap 配色方案
# """
# import itertools
# import numpy as np
# import matplotlib.pyplot as plt
# #
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# cm = np.array([[1,0.082,0.031,-0.0086],
#               [0.082,1,-0.09,0.062],
#               [0.031,-0.09,1,0.026],
#               [-0.0086,0.062,0.026,1]]
#               )
# cmap =plt.cm.cool
# plt.imshow(cm,cmap=cmap)
# plt.colorbar()
#
# classes=["负债率","信贷数量","年龄","家属"]
# tick_maker = np.arange(len(classes))
# plt.xticks(tick_maker,classes)
# plt.yticks(tick_maker,classes)
#
# for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):plt.text(j,i,cm[i,j],horizontalalignment='center')
#
# plt.grid(False)
#
# plt.legend()
# plt.savefig(r"C:\Users\Administrator\Desktop\imshow1.jpg")
#
# """多位置划线"""
# import matplotlib.pyplot as plt
# plt.subplot(1,2,1)
# plt.axhline(y=2,xmin=0.2,xmax=0.6)
# plt.subplot(1,2,2)
# plt.axvline(x=2,ymin=0.2,ymax=0.6)

# """绘制组合图"""
# import numpy as np
# import matplotlib.pyplot as plt
# #
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
# # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1,1,1)
#
# x = np.array([1,2,3,4,5,6,7,8,9])
# y1 =np.array([866,2335,5710,6482,120,1605,3813,4428,4631])
# y2 =np.array([433,1167,2855,3241,3060,802,1906,2214,2315])
#
# plt.plot(x,y1,color = "k",linestyle="solid",linewidth=1,marker="o",markersize=3,label="注册人数")
# plt.plot(x,y2,color = "k",linestyle="dashdot",linewidth=1,marker="o",markersize=3,label="激活人数")
#
# plt.title("注册和激活人数",loc="center")
#
# for a,b in zip(x,y1):
#     plt.text(a,b,b,ha="center",va="bottom",fontsize=11)
#
# for a,b in zip(x,y2):
#     plt.text(a,b,b,ha="center",va="bottom",fontsize=11)
#
# plt.xlabel("时间")
# plt.ylabel("人数")
#
# plt.xticks(np.arange(1,10,1),["1月","2月份","3月份","4月份","5月份","6月份","7月份","8月份","9月份"])
# plt.yticks(np.arange(1000,7000,1000),["1000人","2000人","3000人","4000人","5000人","6000人"])
#
# plt.legend()
# plt.savefig(r"C:\Users\Administrator\Desktop\plot10.jpg")


"""折线图+柱形图"""
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
#  # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1,1,1)
# x = np.array([1,2,3,4,5,6,7,8,9])
# y1 =np.array([866,2335,5710,6482,120,1605,3813,4428,4631])
# y2 =np.array([433,1167,2855,3241,3060,802,1906,2214,2315])
#
#
#
# plt.plot(x,y1,color = "k",linestyle="solid",linewidth=1,
#          marker="o",markersize=3,label="注册人数")
# plt.bar(x,y2,color = "k",label="激活人数")
#
# plt.title("注册和激活人数",loc="center")
#
# for a,b in zip(x,y1):
#     plt.text(a,b,b,ha="center",va="bottom",fontsize=11)
#
# for a,b in zip(x,y2):
#     plt.text(a,b,b,ha="center",va="bottom",fontsize=11)
#
# plt.xlabel("时间")
# plt.ylabel("人数")
#
# plt.xticks(np.arange(1,10,1),["1月","2月份","3月份","4月份","5月份","6月份","7月份","8月份","9月份"])
# plt.yticks(np.arange(1000,7000,1000),["1000人","2000人","3000人","4000人","5000人","6000人"])
#
# plt.legend()
# plt.savefig(r"C:\Users\Administrator\Desktop\bar10.jpg")


#
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题
#  # % config InlineBackend.figuer_format = 'svg'
# plt.subplot(1,1,1)
# x = np.array([1,2,3,4,5,6,7,8,9])
# y1 =np.array([866,2335,5710,6482,120,1605,3813,4428,4631])
# y2 =np.array([0.54459448,0.32392354,0.39002751,
#               0.41121879,0.32063077,0.33152276,
#               0.92226226,0.02950071,0.15716906])
#
#
#
#
# plt.plot(x,y1,color = "k",linestyle="solid",linewidth=1,
#          marker="o",markersize=3,label="注册人数")
#
# plt.xlabel("时间")
# plt.ylabel("人数")
#
# plt.legend(loc ="upper left")
#
# plt.twinx()
# plt.plot(x,y2,color = "k",linestyle="dashdot",linewidth=1,
#          marker="o",markersize=3,label="激活率")
# plt.xlabel("月份")
# plt.ylabel("激活率")
#
# plt.legend()
#
# plt.title("注册和激活人数",loc="center")
#
# plt.legend()
# plt.savefig(r"C:\Users\Administrator\Desktop\bar10.jpg")
# ####数据简单的合并和邮件发送
# import  pandas as pd
# from datetime import datetime
# import pymysql
#
#
# eng = pymysql.connect(host ='localhost',
#                       user='root',
#                       password = 'root',
#                       #prot ='3306',
#                       db ='school',
#                       charset='utf8')
#
# sql1 = "select scid,stuid ,couid,scdate from tb_score "
# sql2 ='select stuid,stuname,stubirth,stuaddr,collid from tb_student'
# df1 = pd.read_sql(sql1,eng)
# df2 = pd.read_sql(sql2,eng)
# ###本月销售情况
# this_month=df1[(df1["成交时间"]>=datetime(2018,2,1))&(df1["scdate"]>=datetime(2018,2,28))]
# #客流量计算
# sales_1 =(this_month["销量"]*this_month["单价"]).sum()
# traffic_1 = this_month["订单ID"].drop_duplicates().count()
# s_t_1 =sales_1/traffic_1  #客单价
# print("本月销售额为:{:.2f},客流量为：{}，"
#       "客单价为:{:.2f}".format(sales_1,traffic_1,s_t_1))
# #上月销售情况
# last_month=df1[(df1["成交时间"]>=datetime(2018,1,1))&(df1["scdate"]>=datetime(2018,1,31))]
# #客流量计算
# sales_2 =(last_month["销量"]*last_month["单价"]).sum()
# traffic_2 = last_month["订单ID"].drop_duplicates().count()
# s_t_2 =sales_2/traffic_2  #客单价
# print("本月销售额为:{:.2f},客流量为：{}，"
#       "客单价为:{:.2f}".format(sales_2,traffic_2,s_t_2))
#
# #去年同期
# same_month=df1[(df1["成交时间"]>=datetime(2017,2,1))&(df1["scdate"]>=datetime(2017,2,28))]
# #客流量计算
# sales_3 =(same_month["销量"]*same_month["单价"]).sum()
# traffic_3 = same_month["订单ID"].drop_duplicates().count()
# s_t_3 =sales_3/traffic_3  #客单价
# print("本月销售额为:{:.2f},客流量为：{}，"
#       "客单价为:{:.2f}".format(sales_3,traffic_3,s_t_3))
#
# def get_month_data(df1):
#     sale=((df1["单价"]*df1["销量"]).sum())
#     traffic =df1["订单"].drop_duplcates().count()
#     s_t     =sale/traffic
#     return (sale,traffic,s_t)
# #计算本月指标
# sales_1,traffic_1,s_t_1 =get_month_data(this_month)
# #计算上月指标
# sales_2,traffic_2,s_t_2 =get_month_data(last_month)
# #计算去年同期指标
# sales_3,traffic_3,s_t_3 =get_month_data(same_month)
# #对数据进行汇总
# report = pd.DataFrame([[sales_1,sales_2,sales_3],
#                       [traffic_1,traffic_2,traffic_3],
#                       [s_t_1,s_t_2,s_t_3]],
#                       columns=["本月累计","上月同期","去年同期"],
#                       index  =["销售额","客流量","客单价"])
# print(report)
# #给数据添加同比、环比字段
# report["环比"]=report["本月累计"]/report["上月同期"] -1
# report["同比"]=report["本月累计"]/report["去年同期"] -1
# print(report)
# #将数据导出为CSV
# report.to_csv(r"C:\Users\Administrator\Desktop\order.CSV",encoding="utf-8")

# #发送短信
# import smtplib
# from email import encoders
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.utils import parseaddr,formataddr
# from email.mime.application import MIMEApplication
#
# asender = "115787463@sina.com"
# areceiver = "381784599@qq.com"
# acc="1173230589@qq.com"
#
# asubject = "测试"
#
# from_addr = "115787463@sina.com"
# password = "84005b78031cc3a5"
# #右键设置
# msg = MIMEMultipart()
# msg['Subject'] =asubject
# msg['to'] = areceiver
# msg['Cc'] = acc
# msg['from'] = "杨宝国"
# #正文
# body = "你好，邮件状态测试！"
#
# msg.attach(MIMEText(body,'plain','utf-8'))
#
# #添加附件
#
# xlsxpart =MIMEApplication(open(r"C:\Users\Administrator\Desktop\新生活卡.xlsx",'rb').read())
# xlsxpart.add_header('Content-Disposotion',
#                     'attachment',
#                     filename='新生活卡.xlsx')
# msg.attach(xlsxpart)
#
#
# smtp_server ="pop.sina.com"
# server = smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.ehlo()
# server.starttls()
# server.login(from_addr,password)
#
# server.sendmail(from_addr,areceiver.split(',')+acc.split(','),
#                 msg.as_string())
# server.quit()











# -*- coding: utf-8 -*-

#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import numpy as np

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
os.environ['NLS_LANG']='AMERICAN_AMERICA.WE8ISO8859P1'

conn = cx_Oracle.connect("dbusrgfc/future@192.168.2.216:1521/jdgfc",encoding="UTF-8",nencoding="UTF-8")  #,encoding='UTF-8',nencoding='UTF-8'
curs = conn.cursor()

sql = "select to_char(OEDATE,'yyyymmdd') ,OEKEY from OPERERRORS where OPERERRORS.OEDATE>=trunc(sysdate)-15"
curs.execute(sql)

for result in curs:
    #result[0] + result[1].encode('latin1').decode('gbk')
    #print(result[0]+','+result[1].encode('latin1').decode('gbk'))
    mail_body = result[0] +'     '+ result[1].encode('latin1').decode('gbk')
    print(mail_body)

curs.close()
conn.close()


mail_body = np.array[mail_body] #忘记怎么将查询结果全部发送了，有时间在修改
#创建一个实例
message = MIMEText( mail_body, 'plain', 'utf-8' )   #邮件正文
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

