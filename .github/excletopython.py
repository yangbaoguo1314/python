'''import pandas as pd

s1 =pd.Series(['a','b','c','d'])
s2 =pd.Series([1,2,3,4],index=['a','b','c','d'])
s3 =pd.Series({'a':1,'b':2,'c':3,'d':4})
print(s1)
print(s2)
print(s3)
print(s1.index)
print(s2.index)
print(s1.values)
print(s2.values)
'''

import pandas as pd
df1 =pd.DataFrame({'a','b','c','d'})
print(df1)
df2 =pd.DataFrame([("a","A"),("b","B"),("c","C"),("d","D")])
print(df2)
df3 =pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]],columns=['小写','大写'])
print(df3)

df4 =pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]],columns=['小写','大写'],index=['一','二','三','四'])
print(df4)

data = {"小写":["a","b","c","d"],"大写":["A","B","C","D"]}
df5 =pd.DataFrame(data,index=['一','二','三','四'])
print(df5)

print(df5.columns)
print(df2.columns)
print(df2.index)
print(df5.index)
