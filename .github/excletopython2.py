import pandas as pd
df =pd.read_excel(r"C:\Users\Administrator\Desktop\text.xlsx")
df2 =pd.read_excel(r"C:\Users\Administrator\Desktop\text.xlsx",sheet_name= 1,index_col= 0,header= 0,usecols= [1,3])
#sheet_name制定sheet编号，从0开始，也可以用名字，index_col行索引，从0开始；
#header列索引，从0开始,usecols指定需要的数据列，从0开始,可以指定行号进行选择；

#print(df)
#print(df2)
#print(df2.head())
print(df2.info())