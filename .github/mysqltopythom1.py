#2020.4.24


# """绘制简单的波峰图"""
# import matplotlib.pyplot as plt
# import numpy as np
# t = np.arange(0.,1.0,0.01)
# s = np.sin(2*np.pi*t)
#
# plt.rcParams['lines.color'] = 'r'
# plt.plot(t,s)
#
# c= np.cos(2*np.pi*t)
#
# plt.rcParams['lines.linewidth'] ='3'
# plt.plot(t,c)
# #plt.show()
# plt.legend()
# plt.savefig(r"C:\Users\Administrator\Desktop\plot1.jpg")

# """.csv处理复习"""
# import csv,sys
#
# filename = r'D:\python3\bao\python data visualization cookbook\PythonDataVisualizationCookbookSE_Code\Chapter 02\ch02-data.csv'
#
# data = []
# try:
#     with open(filename) as f:
#         reader=csv.reader(f)
#         header = next(reader)   #python2代码是 reader.next(),python3中reader无next
#         data =[row for row in reader]
# except csv.Error as e:
#     print(f"Error reading csv file at line {reader.line_num,e}")
#     sys.exit(-1)
# if header:
#     print(f"{header}")
#     print("===============")
#
# for datarow in data:
#     print(f"{datarow}")

#
# import csv,sys,openpyxl
# #
# file = r'D:\python3\bao\python data visualization cookbook\PythonDataVisualizationCookbookSE_Code\Chapter 02\ch02-xlsxdata.xlsx'
# wb =openpyxl.open(filename=file)
# ws = wb.get_sheet_by_name('sheet1')
#
# data = []
# for r in range(ws.nrows):
#     col =[]
#     for c in range(ws.ncols):
#         col.append(ws.cell(r,c).value)
#         data.append(col)
# from pprint import pprint
# pprint(data)
#
# import string
# import struct
#
# datafilr = r'D:\python3\bao\python data visualization cookbook\PythonDataVisualizationCookbookSE_Code\Chapter 02\ch02-fixed-width-1M.data'
# mask ='9s14s5s'
#
# with open(datafilr,'r') as f:
#     for line in f:
#         fields = struct.Struct(mask).unpack_from(line)
#         print(fields)
#
#
# import os
# import sys
# import argparse
#
# try:
#     import io as StringIO
# except:
#     import StringIO
#
# import struct
# import json
# import csv
#
# def impirt_data(import_file):
#     mask = '9s14s5s'
#     data = []
#     with open(import_file,'r') as f:
#         for line in f:
#             fields = struct.Struct(mask).unpack_from(line)
#             data.append(list([f.strip() for f in fields]))
#     return  data
#
# def write_data(data,export_format):
#     if export_format =="csv":
#         return write_csv(data)
#     elif export_format =="json":
#         return write_json(data)
#     elif export_format=="xlsx":
#         return  write_xlsx(data)
#     else:
#         raise Exception('Illegal format defined')
#
# def write_csv(data):
#     f = StringIO.StringIO()
#     writer = csv.writer(f)
#     for row in data:
#         writer.writerow(row)
#     return f.getvalue()
# def write_json(data):
#     j = json.dumps(data)
#     return j
#
# def write_xlsx(data):
#     from xlwt import Workbook
#     book = Workbook()
#     sheet1 = book.add_sheet("sheet1")
#     row = 0
#     for line in data:
#         col = 0
#         for datum in line:
#             print(datum)
#             sheet1.write(row,col,datum)
#             col +=1
#         row +=1
#         if row>65535:
#             print(f"{sys.stderr},数据过大，无法保存了！")
#             break
#         f = StringIO.StringIO()
#         book.save(f)
#         return f.getvalue()
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("import_file",help="path to a fixed-width data file.")
#     parser.add_argument("export_format",help="Export format:json,csv,xlsx")
#     args =parser.parse_args()
#     if args.import_file is None:
#         print(f"{sys.stderr},you must specify path to import from.")
#         sys.exit(1)
#     if args.export_format not in ('csv','json','xlsx'):
#         print(f"{sys.stderr},你输入的文件格式不对",{args.import_file})
#         sys.exit(1)
#
#     data = impirt_data(args.import_file)
#     print(write_data(data,args.export_format))

# #xlsx文件转csv文件"""
# import xlrd
#
# import csv
#
# def xlsx_to_csv():
#     workbook = xlrd.open_workbook('1.xlsx')
#     table = workbook.sheet_by_index(0)
#     with codecs.open('1.csv', 'w', encoding='utf-8') as f:
#         write = csv.writer(f)
#         for row_num in range(table.nrows):
#             row_value = table.row_values(row_num)
#             write.writerow(row_value)
#
# if __name__ == '__main__':
#     xlsx_to_csv()
#
# """使用第三方库pandas将xlsx文件转csv文件"""
# import pandas as pd
#
# def xlsx_to_csv_pd():
#    data_xls = pd.read_excel('1.xlsx', index_col=0)
#    data_xls.to_csv('1.csv', encoding='utf-8')
#
# if __name__ == '__main__':
#     xlsx_to_csv_pd()
#
# """csv文件转换成xlsx文件"""
"""
import csv
import xlwt
def csv_to_xlsx():
    with open('1.csv', 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data') # 创建一个sheet表格
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i) # 一个一个将单元格数据写入
                r = r + 1
        l = l + 1
    workbook.save('1.xlsx') # 保存Excel
#
#
if __name__ == '__main__':
    csv_to_xlsx()
"""
#
# """使用pandas将csv文件转成xlsx文件"""
"""
import pandas as pd
#
def csv_to_xlsx_pd():
    csv = pd.read_csv('1.csv', encoding='utf-8')
    csv.to_excel('1.xlsx', sheet_name='data')
#
#
if __name__ == '__main__':
    csv_to_xlsx_pd()
"""
# """xlsx文件转json文件"""
"""
from collections import OrderedDict
import json
import codecs
wb = xlrd.open_workbook('positive_previous.xlsx')
convert_list = []
sh = wb.sheet_by_index(0)
title = sh.row_values(0)
for rownum in range(1, sh.nrows):
    rowvalue = sh.row_values(rownum)
    single = OrderedDict()
    for colnum in range(0, len(rowvalue)):
        print(title[colnum], rowvalue[colnum])
        single[title[colnum]] = rowvalue[colnum]
    convert_list.append(single)
j = json.dumps(convert_list)
#
with codecs.open('positive_previous.json', "w", "utf-8") as f:
    f.write(j)
"""
# """csv文件转化为json文件"""
"""
import sys, json

# 获取输入数据
input_file = sys.argv[1]
lines = open(input_file, "r", encoding="utf_8_sig").readlines()
lines = [line.strip() for line in lines]
# # 获取键值
keys = lines[0].split(',')
line_num = 1
total_lines = len(lines)
parsed_datas = []
while line_num < total_lines:
    values = lines[line_num].split(",")
    parsed_datas.append(dict(zip(keys, values)))
    line_num = line_num + 1
#
json_str = json.dumps(parsed_datas, ensure_ascii=False, indent=4)
output_file = input_file.replace("csv", "json")
# # write to the file
f = open(output_file, "w", encoding="utf-8")
f.write(json_str)
f.close()
print("解析结束！")
"""

"""简单的打开sqlite数据库"""
# #ch02-sqlite-import
"""
import sqlite3
import sys
if len(sys.argv)<2:
    print("Error:you must supply at least sql script！")
    print("usage:%s table.db ./sql-dump.sql" %(sys.argv[0]))
    sys.exit(1)
script_path = sys.argv[1]
if len(sys.argv)==3:
    db=sys.argv[2]
else:
    db=":memory:"
#
try:
    con=sqlite3.connect(db)
    with con:
        cur =con.cursor()
        with open(script_path,'rb') as f:
            cur.executescript(f.read())
except sqlite3.Error as err:
    print(f"ERROR:{err}")
"""
# ###python ch02-sqlite-import.py world.sql world.db
# #ch02-sqlite-read.py
"""
import sqlite3
import sys
#
if len(sys.argv) !=2:
    print("please specify database file!")
    sys.exit(1)
#
db=sys.argv[1]
#
try:
    con = sqlite3.connect(db)
    with con:
        cur=con.cursor()
        qyery ="select id,name,population from city order by population desc LIMIT 1000;"
        con.text_factory=str
        cur.execute(qyery)
#
        resultset=cur.fetchall()
        col_names =[cn[0] for cn in cur.description]
        print("10s %30s %10s" %tuple(col_names))
        print("="*(10+1+30+1+10))
        for row in resultset:
            print("%10s %30s %10s" %row)
#
except sqlite3.Error as err:
    print(f"ERROR:{err}")
"""
# #python ch02-sqlite-read.py world.db
"""异常数据清理"""
#1柱形图
"""
import numpy as np
import matplotlib.pyplot as plt
#
def is_outlier(points,thershold=3.5):
    if len(points.shape)==1:
        points =points[:,None]
    median = np.median(points,axis=0)
#
    diff=np.sum((points-median)**2,axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation =np.median(diff)
    modified_z_score=0.6745 * diff/med_abs_deviation
#
    return modified_z_score>thershold
x=np.random.random(100)
buckets = 50
x = np.r_[x,-49,95,100,-100]
filtered = x[~is_outlier(x)]
plt.figure()
plt.subplot(211)
plt.hist(x,buckets)
plt.xlabel('Raw')
plt.subplot(212)
plt.hist(filtered,buckets)
plt.xlabel('Cleaned')
#
plt.show()
"""
# #2散点图
"""
from pylab import  *
sparead=rand(50)*100
center = ones(25)*50
#
filer_high = rand(10)*100+100
filer_low  = rand(10)*-100
data = concatenate((sparead,center,filer_high,filer_low),0)
#
subplot(311)
boxplot(data,0,'gx')
subplot(312)
sparead_1 =concatenate((sparead,filer_high,filer_low),0)
center_1 = ones(70)*25
scatter(center_1,sparead_1)
xlim([0,50])
#
subplot(313)
center_2 =rand(70) *50
scatter(center_2,sparead_1)
xlim([0,50])
show()
"""
#读取数据,顺序读取
"""
import sys
#
filename=sys.argv[1]
#
with open(filename,'rb') as hugefile:
    chunksize = 1000
    readable = ''
    while hugefile:
        start =hugefile.tell()
        print("starting as : %s" %start)
        file_block=''
        for _ in range(start,start+chunksize):
            line = hugefile.__next__()
            file_block=file_block+line
            print(f"file_block{type(file_block)}{file_block}")
        readable = readable +file_block
        stop = hugefile.tell()
        print(f'readable{type(readable)}{readable}')
        print(f'reading bytes from {start} to {stop}')
        print(f'read bytes total:{len(readable)}')
"""


##循环读取数据源
"""
import time
import os
import sys

if len(sys.argv) !=2:
    print(f"{sys.stderr},please sepecify filename to read!")
filename = sys.argv[1]
#
if not os.path.isfile(filename):
    print(f'{sys.stderr},given file:{filename}  is not a file')
with open(filename,'r') as f:
    filesize = os.stat(filename)[6]
    f.seek(filename)
    while True:
        where =f.tell()
        line =f.readline()
        if not line:
            time.sleep(1)
            f.seek(where)
        else:
            print(line)
"""
##简单的图片处理
"""
import scipy.misc
import matplotlib.pyplot as plt
lena=scipy.misc.face() #scipy.misc.ascent()
plt.gray()
plt.imshow(lena)
plt.colorbar()
plt.show()
"""

"""读取图片"""
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

bug = Image.open(r"D:\小米资料\截屏\Screenshot_2016-07-14-18-42-41_com.mllj.forum.png")
arr = np.array(bug.getdata(),np.uint8).reshape(bug.size[1],bug.size[0],3)

plt.gray()
plt.imshow(arr)
plt.colorbar()
plt.show()
"""
"""图片的简单处理"""
"""
import matplotlib.pyplot as plt
import scipy,imageio
import numpy as np

bug = imageio.imread(r"D:\小米资料\截屏\Screenshot_2016-07-14-18-42-41_com.mllj.forum.png")
bug1 = np.memmap(r"D:\小米资料\截屏\Screenshot_2016-07-14-18-42-41_com.mllj.forum.png",dtype=np.uint8,shape=(375,500)) #大图片numpy 处理较为快捷
bug=bug[:,:,0]

plt.figure()
plt.gray()
plt.subplot(121)
plt.imshow(bug)
zbug = bug[100:500,140:550]  #放大显示区域
plt.subplot(122)
plt.imshow(zbug)
plt.show()
"""
"""随机数生成后制作成表格"""
"""
import pylab
import random

SAMPLE_SIZE = 100
random.seed()
real_rand_vars = []
real_rand_vars=[random.random() for val in range(SAMPLE_SIZE)] #random.uniform(min.max) for val in range(SAMPLE_SIZE) 可以生成浮点数
pylab.hist(real_rand_vars,10)
pylab.xlabel("Number range")
pylab.ylabel("Count")

pylab.show()
"""

"""虚拟价格增长数据时序图"""
"""
import pylab
import random

duration = 100
mean_inc = 0.2
std_dev_inc = 1.2

x = range(duration)
y= []
price_today= 0

for i in x:
    next_delta = random.normalvariate(mean_inc,std_dev_inc)
    price_today += next_delta
    y.append(price_today)

pylab.plot(x,y)
pylab.xlabel("Time")
pylab.ylabel("Value")
pylab.show()
"""


#coding:utf-8
"""
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
SAMPLE_SIZE = 1000
buckets =100
plt.figure()
mpl.rcParams.update({'font.size':7})

plt.subplot(621)
plt.xlabel("random.random")
res =[random.random() for _ in range(1,SAMPLE_SIZE)]
plt.hist(res,buckets)

plt.subplot(622)
plt.xlabel("random.uniform")
a =1
b=SAMPLE_SIZE
res = [random.uniform(a,b) for _ in range(1,SAMPLE_SIZE)]
plt.hist(res,buckets)

plt.subplot(623)
plt.xlabel("random.triangular")
low = 1
hight = SAMPLE_SIZE
res = [random.triangular(low,hight) for _ in range(1,SAMPLE_SIZE)]
plt.hist(res,buckets)

plt.subplot(624)
plt.xlabel("random.betavariate")
alpha = 1
beta = 10
res = [random.betavariate(alpha,beta) for _ in range(1,SAMPLE_SIZE)]
plt.hist(res,buckets)

plt.subplot(625)
plt.xlabel("random.expovariate")
lambd = 1.0/((SAMPLE_SIZE+1)/2.)
res = [random.expovariate(lambd) for _ in range(1,SAMPLE_SIZE)]
plt.hist(res,buckets)

plt.subplot(626)
plt.xlabel("random.gammavariate")
alpha =1
beta = 10
res = [random.gammavariate(alpha,beta) for _ in range(1,SAMPLE_SIZE)]
plt.hist(res,buckets)

plt.subplot(627)
plt.xlabel("random.lognormvariate")
nu = 1
sigma = 0.5
res = [random.lognormvariate(nu,sigma) for _ in range(1, SAMPLE_SIZE)]
plt.hist(res, buckets)


plt.subplot(628)
plt.xlabel("random.normalvariate")
nu = 1
sigma = 0.5
res = [random.normalvariate(nu,sigma) for _ in range(1, SAMPLE_SIZE)]
plt.hist(res, buckets)

plt.subplot(629)
plt.xlabel("random.paretovariate")
alpha =1
res = [random.paretovariate(alpha) for _ in range(1,SAMPLE_SIZE)]
plt.hist(res,buckets)

plt.tight_layout()
plt.show()
#random生成随机数random.SystemRandom 可以生成不重复的随机数，这种情况下seed() 和setstate()就不在有差别
"""

"""生成简单的随机单词"""
"""
import random
for i in range(11):
    for j in range(5):
        ij = random.randint(65,90)+random.randint(0,1) *32
        print(chr(ij),end='')
    print()
 """
"""生成随机中文名字"""
"""
import random

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

def first_name():  #   随机取姓氏字典
    first_name_list = [
        "赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨",
        "朱","秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜",
        "戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","葛","奚","范","彭","郎",
        "鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐",
        "费","廉","岑","薛","雷","贺","倪","汤","滕","殷","罗","毕","郝","邬","安","常",
        "乐","于","时","傅","皮","卞","齐","康","伍","余","元","卜","顾","孟","平","黄",
        "和","穆","萧","尹","姚","邵","湛","汪","祁","毛","禹","狄","米","贝","明","臧",
        "计","伏","成","戴","谈","宋","茅","庞","熊","纪","舒","屈","项","祝","董","梁",
        "杜","阮","蓝","闵","席","季","麻","强","贾","路","娄","危","江","童","颜","郭",
        "梅","盛","林","刁","钟","徐","邱","骆","高","夏","蔡","田","樊","胡","凌","霍",
        "虞","万","支","柯","昝","管","卢","莫","经","房","裘","缪","干","解","应","宗",
        "丁","宣","贲","邓","郁","单","杭","洪","包","诸","左","石","崔","吉","钮","龚",
        "程","嵇","邢","滑","裴","陆","荣","翁","荀","羊","於","惠","甄","曲","家","封",
        "芮","羿","储","靳","汲","邴","糜","松","井","段","富","巫","乌","焦","巴","弓",
        "牧","隗","山","谷","车","侯","宓","蓬","全","郗","班","仰","秋","仲","伊","宫",
        "宁","仇","栾","暴","甘","钭","厉","戎","祖","武","符","刘","景","詹","束","龙",
        "叶","幸","司","韶","郜","黎","蓟","薄","印","宿","白","怀","蒲","邰","从","鄂",
        "索","咸","籍","赖","卓","蔺","屠","蒙","池","乔","阴","鬱","胥","能","苍","双",
        "闻","莘","党","翟","谭","贡","劳","逄","姬","申","扶","堵","冉","宰","郦","雍",
        "卻","璩","桑","桂","濮","牛","寿","通","边","扈","燕","冀","郏","浦","尚","农",
        "温","别","庄","晏","柴","瞿","阎","充","慕","连","茹","习","宦","艾","鱼","容",
        "向","古","易","慎","戈","廖","庾","终","暨","居","衡","步","都","耿","满","弘",
        "匡","国","文","寇","广","禄","阙","东","欧","殳"",沃","利","蔚","越","夔","隆",
        "师","巩","厍","聂","晁","勾","敖","融","冷","訾","辛","阚","那","简","饶","空",
        "曾","毋","沙","乜","养","鞠","须","丰","巢","关","蒯","相","查","后","荆","红",
        "游","竺","权","逯","盖","益","桓","公","万俟","司马","上官","欧阳","夏侯","诸葛",
        "闻人","东方","赫连","皇甫","尉迟","公羊","澹台","公冶","宗政","濮阳","淳于","单于",
        "太叔","申屠","公孙","仲孙","轩辕","令狐","钟离","宇文","长孙","慕容","鲜于","闾丘",
        "司徒","司空","丌官","司寇","仉督","子车","颛孙","端木","巫马","公西","漆雕","乐正",
        "壤驷","公良","拓跋","夹谷","宰父","谷梁","晋楚","闫法","汝鄢","涂钦","段干","百里",
        "东郭","南门","呼延","归海","羊舌","微生","岳帅","缑亢","况郈","有琴","梁丘","左丘",
        "东门","西门","商牟","佘佴","伯赏","南宫","墨哈","谯笪","年爱","阳佟","第五","言福"]
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name

def second_name():
    # 随机取数组中字符，取到空字符则没有second_name
    second_name_list = [GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name

def last_name():
    return GBK2312()

def last_name():
    return GBK2312()

def create_name():
    name = first_name() + second_name() + last_name()
    return name

print(create_name())
"""
"""
import random
xing = [ '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
        '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
        '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
        '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
        '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
 
ming = [ '的', '一', '是', '了', '我', '不', '人', '在', '他', '有','这', '个', '上', '们', '来', '到', '时', '大', '地',
        '为', '子', '中', '你', '说', '生', '国', '年', '着', '就', '那','和', '要', '她', '出', '也', '得', '里', '后', '自',
        '以', '会', '家', '可', '下', '而', '过', '天', '去', '能', '对','小', '多', '然', '于', '心', '学', '么', '之', '都',
        '好', '看', '起', '发', '当', '没', '成', '只', '如', '事', '把','还', '用', '第', '样', '道', '想', '作', '种', '开',
        '美', '总', '从', '无', '情', '己', '面', '最', '女', '但', '现','前', '些', '所', '同', '日', '手', '又', '行', '意',
        '动', '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分','爱', '老', '因', '很', '给', '名', '法', '间', '斯',
        '知', '世', '什', '两', '次', '使', '身', '者', '被', '高', '已','亲', '其', '进', '此', '话', '常', '与', '活', '正',
        '感', '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定','本', '公', '特', '做', '外', '孩', '相', '西', '果',
        '走', '将', '月', '十', '实', '向', '声', '车', '全', '信', '重','三', '机', '工', '物', '气', '每', '并', '别', '真',
        '打', '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水','像', '眼', '等', '体', '却', '加', '电', '主', '界',
        '门', '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性',
        '马', '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让',
        '母', '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英',
        '军', '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快',
        '原', '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条',
        '呢', '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片',
        '罗', '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合',
        '反', '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运',
        '及', '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司',
        '巴', '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形',
        '影', '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈',
        '容', '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计',
        '您', '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻',
        '统', '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示',
        '愿', '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社',
        '算', '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息',
        '功', '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图',
        '具', '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引',
        '食', '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试',
        '怀', '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除',
        '跑', '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳',
        '验', '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿',
        '睡', '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店',
        '否', '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河',
        '续', '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪',
        '索', '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族',
        '低', '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅',
        '街', '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀',
        '律', '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职',
        '属', '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉',
        '遗', '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳',
        '差', '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府',
        '压', '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童',
        '顶', '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯',
        '巨', '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层',
        '付', '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀',
        '营', '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊',
        '降', '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙',
        '杰', '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡',
        '预', '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误', '乾', '坤']
 
for i in range(1):
    x = random.randint(0,len(xing))
    m1 = random.randint(0,len(ming))
    m2 = random.randint(0,len(ming))
    name = (''+xing[x]+ming[m1]+ming[m2])
    print(name)

"""

"""生成手机号"""

# -*- coding: utf-8 -*-
"""
import random

def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位数字
    third = {3: random.randint(0, 9),
             4: [5, 7, 9][random.randint(0, 2)],
             5: [i for i in range(10) if i != 4][random.randint(0, 8)],
             7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
             8: random.randint(0, 9), }[second]
    # 最后八位数字
    suffix = random.randint(9999999, 100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)
    # 生成手机号


phone = create_phone()
print(phone)
"""
"""生成身份证号码"""
"""
from datetime import date
from datetime import timedelta
import random


def getdistrictcode():
    codelist = []
    file = open('districtcode.txt')
    lines = file.readlines()  # 逐行读取
    for line in lines:
        if line.lstrip().rstrip().strip() != '' and (line.lstrip().rstrip().strip())[:6][
                                                    -2:] != '00':  # 如果每行中去重后不为空，并且6位数字中最后两位不为00，则添加到列表里。（最后两位为00时为省份或地级市代码）
            codelist.append(line[:6])
            # print(line[:6])
            # print(codelist)
    return codelist


def gennerator():
    codelist = getdistrictcode()
    id = codelist[random.randint(0, len(codelist))]  # 地区项
    id = id + str(random.randint(1950, 1998))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
    id = id + checkcode[str(count % 11)]  # 算出校验码
    return id


if __name__ == '__main__':
    print(gennerator())
"""

"""简单的数据除燥处理"""
"""
from pylab import *
from numpy import *
import matplotlib.pyplot as plt

def moving_average(interval,window_size):
    window =ones(int(window_size))/float(window_size)
    return convolve(interval,window,'same')

t = linspace(-4,4,100)
y = sin(t)+randn(len(t))*0.1

plot(t,y,"k.")
for a,b in zip(t,y):
    plt.text(a,b,b,ha="center",va="bottom",fontsize=3)  #将T,Y数值显示在plot上方
y_av = moving_average(y,10)   
#for a,b in zip(t,y_av):plt.text(a,b,b,ha="center",va="bottom",fontsize=7)
plot(t,y_av,"r")

xlabel("time")
ylabel("Value")
grid(True)
show()
"""
"""
import numpy as np
from numpy import *
from pylab import *
from matplotlib.pyplot import  *

windows = ['flat','hanning','hamming','bartlett','blackman']
def smooth(x,window_len=11,window ='hanning'):
    if x.ndim !=1:
        raise(ValueError,"smooth only accepts 1 dimension arrays.")
    if x.size<window_len:
        raise (ValueError,"input vector needs to be bigger than window size.")
    if window_len<3:
        return x

    if not window in windows:
        raise ValueError("windows is one of 'flat','hanning','hamming','bartlett','blackman'")
    s = np.r_[x[window_len-1:0:-1],x,x[-1:window_len:1]]
    if window == 'flat':
        w = np.ones(window_len,'d')
    else:
        w = eval('np.'+window+'(window_len)')

    y =np.convolve(w/w.sum(),s,mode='valid')
    return y

t =linspace(-4,4,100)
x = sin(t)
xn =x + randn(len(t))*0.1
y = smooth(x)
ws =31
plot(ones(ws))
matplotlib.pyplot.hold(True)  #python3之后hold
for w in windows[1:]:
    eval('plot('+w+'(ws))')
axis([0,30,0,1.1])
legend(windows)
title("smoothing windows")

subplot(212)
plot(x)

plot(xn)

for n in windows:
    plot(smooth(xn,10,w))
l =['original signal','signal with noise']
l.extend(windows)
legend(1)

title("smoothed signal")

show()
"""
###中值滤波####
"""
import numpy as np
import pylab as p
import scipy.signal as signal
x = np.linspace(0,1,101)

x[3::10] = 1.5

p.plot(x)
p.plot(signal.medfilt(x,3))
p.plot(signal.medfilt(x,5))
p.legend(['original signal','length 3','length 5'])

p.show()

"""
"""
#matplotlib.pyplot绘制简单的图形
from matplotlib.pyplot import *

x = [1,2,3,4]
y = [5,4,3,2]
figure()
subplot(2,3,1)
plot(x,y) #线

subplot(2,3,2)
bar(x,y)  #柱形

subplot(2,3,3)
barh(x,y)  #矩形

subplot(2,3,4)
bar(x,y,color = 'r')
y1 = [7,8,5,3]
bar(x,y1,bottom=y,color = 'k')  #叠加

subplot(2,3,5)
boxplot(x)  #箱


subplot(2,3,6)
scatter(x,y)  #散点

show()
"""
"""
import pymysql
import  pandas as pd

eng = pymysql.connect(host ='localhost',
                      user='root',
                      password = 'root',
                      #prot ='3306',
                      db ='school',
                      charset='utf8')

sql1 = "select DISTINCT teaid,couid from tb_course "

df1 = pd.read_sql(sql1,eng)
"""
"""
dataset=[]
dataset=df1
from pylab import *

subplot(1,2,1)

boxplot(dataset,vert=False)

subplot(1,2,2)
hist(dataset)

show()
"""
"""正弦余弦"""
"""
import matplotlib.pyplot as plt
import  numpy as np
from pylab import *

x = np.linspace(-np.pi,np.pi,256,endpoint=True)

y = np.cos(x)
y1 = np.sin(x)
plt.plot(x,y)
plt.plot(x,y1)
title("Functions $\sin$ and $\cos$")
xlim(-3.0,3.0)
ylim(-1.0,1.0)
xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
yticks([-1,0,+1],[r'$-1$',r'$0$',r'$+1$'])
plt.show()
"""
"""时间格式转换"""
"""
from datetime import datetime
1.获取当前日期
now = datetime.now() # 格式为 datetime.datetime
now_date = datetime.now().strftime('%Y-%m-%d')    # 格式为str
now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    # 格式为 str
2.从数据库中获取存入的日期 ，格式为 datetime.date
3.时间数据格式之间的相互转换：
from datetime import datetime
（1）datetime.datetime 转str:
 b = datetime.now().strftime('%Y-%m-%d')
（2）str 转datetime.datetime
 d = datetime.strptime(b, '%Y-%m-%d')  # strptime()内参数必须为string格式
 （3）str 转 datetime.date
  先将str转datetime,再转datetime.date
  e = datetime.date(d) # date()内参数需要datetime.datetime型
  （4）datetime.date转str
   h = str(e)
"""
"""
from pylab import *
import matplotlib as mpl
import datetime

fig = figure()

ax =gca()
"""
"""
nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
time_split = nowtime.split('-') #通过str.split的函数将原始时间数据根据‘-’进行切分
#输出结果为['2019','08','01']
#注意，此时的切分后的数据仍为str格式组成的一个列表
#此时可以使用使用map函数来进行转换
time_int = list(map(int, time_split))
#或者
time_int = [int(i) for i in time_split]
#这样处理后数据结果应为[2019,8,1]
start1=datetime.date(*time_int) #将str转换成datetime
start =datetime.datetime.now()
stop=(datetime.datetime.now()+datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
"""
"""
start =datetime.datetime(2013,1,1)
stop  =datetime.datetime(2013,12,31)
delta = datetime.timedelta(days=1)

dates = mpl.dates.drange(start,stop,delta)
values = np.random,rand(len(dates))

ax = gca()

ax.plot_date(dates.values,linestyle='-',marker=' ')

date_format = mpl.dates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
show()
"""

