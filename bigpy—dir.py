"""
#coding utf-8
import os,glob,sys

dirname =r'd:\python3\pythonbook' if len(sys.argv) ==1 else sys.argv[1] #被检索的目录

allsizes=[]
allpy = glob.glob(dirname+ os.sep+ '*.py')
for filename in allpy:
    filesize =os.path.getsize(filename)
    allsizes.append((filesize,filename))

allsizes.sort()  #排序
print(allsizes[:2])
print(allsizes[-2:])
"""

#coding utf-8
#bigpy_tree 查询目标树
"""
import sys,os,pprint
trace = False
if sys.platform.startswith('win'):
    dirname=r'd:\python3'#windows
else:
    dirname='/usr/lib/python' #unix\linux

allsize=[]
for (thisDir,subsHere,filehead) in os.walk(dirname):
    if trace:
        print(thisDir)
    for filename in filehead:
        if filename.endswith('.py'):
            if trace:print('...',filename)
            fullname=os.path.join(thisDir,filename)
            fullsize = os.path.getsize(fullname)
            allsize.append((fullsize,fullname))

allsize.sort()
pprint.pprint(allsize[:2])
pprint.pprint(allsize[-2:])
"""
"""
###检索模块搜索路径
import sys,os,pprint
import time
trace =0  #0 关闭，1为目录，2文件
start_time=time.clock()
visited ={}
allsizes =[]
for srcdir in sys.path:
    for (thisdir,subbsHere,filesHere) in os.walk(srcdir):
        if trace>0:
            print(thisdir)
        thisdir=os.path.normpath(thisdir)
        fixcase = os.path.normcase(thisdir)
        if fixcase in visited:
            continue
        else:
            visited[fixcase] = True
        for filename in filesHere:
            if filename.endswith('.py'):
                if trace>1:
                    print('......',filename)
                pypath = os.path.join(thisdir,filename)
                try:
                    pysize = os.path.getsize(pypath)
                except os.error as e:
                    print('skipping',pypath,sys.exc_info()[0],e)
                else:
                    pylines = len(open(pypath,'rb').readlines())
                    allsizes.append((pysize,pylines,pypath))

print('by size...')
allsizes.sort()
stop_time1=time.clock()
print(f'本次执行程序耗时：{round(stop_time1-start_time,6)}秒')
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])


stop_time2=time.clock()
print('by lines...')
allsizes.sort(key=lambda x:x[1])
print(f'本次执行程序耗时：{round(stop_time2-start_time,6)}秒')
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])
"""
#检索整个硬盘

import os, pprint
from sys import argv, exc_info

trace = 0  # 0=关闭, 1=目录, 2=+文件
dirname, extname = r'd:/', '.zip'  # default is .py files in cwd
if len(argv) > 1: dirname = argv[1]  # ex: C:\, C:\Python31\Lib
if len(argv) > 2: extname = argv[2]  # ex: .pyw, .txt
if len(argv) > 3: trace = int(argv[3])  # ex: ". .py 2"


def tryprint(arg):
    try:
        print(arg)  # unprintable filename?
    except UnicodeEncodeError:
        print(arg.encode())  # try raw byte string


visited = set()
allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: tryprint(thisDir)
    thisDir = os.path.normpath(thisDir)
    fixname = os.path.normcase(thisDir)
    if fixname in visited:
        if trace: tryprint('skipping ' + thisDir)
    else:
        visited.add(fixname)
        for filename in filesHere:
            if filename.endswith(extname):
                if trace > 1: tryprint('+++' + filename)
                fullname = os.path.join(thisDir, filename)
                try:
                    bytesize = os.path.getsize(fullname)
                    linesize = sum(+1 for line in open(fullname, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                else:
                    allsizes.append((bytesize, linesize, fullname))

for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    allsizes.sort(key=lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])