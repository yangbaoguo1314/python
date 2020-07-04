bob = {'name':'Bob Smith','age':40,'pay':30000,'job':'dev'}
sue = {'name':'Sue Jones','age':45,'pay':430000,'job':'hdw'}
tom = {'name':'Tom Smith','age':50,'pay':0,'job':None}

db={}
db['bob']=bob
db['sue']=sue
db['tom']=tom

if __name__=='__main__':
    for key in db:
        print(key,'==>\n',db[key])