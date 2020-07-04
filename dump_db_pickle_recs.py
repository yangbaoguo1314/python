import pickle,glob

for filename in glob.glob('*.pkl'): ##选择所有的.pkl文件
    recfile = open(filename,'rb')#rd模式打开上述限定的文件
    record = pickle.load(recfile)#将打开的文件转换
    print(filename,'=>\n',record)#输出转换好的数据

suefile = open('sue.pkl','rb')
print(pickle.load(suefile)['name'])