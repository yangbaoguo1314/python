# mystr = 'xxxSPAMxxx'
# print(mystr.find('SPAM'))
# print('SPAM' in mystr)
# print('yang' in mystr)
# print(mystr.find("yang"))
# mystr = '\t yang\n'
# print(mystr.strip())
# print(mystr.rstrip())
# mystr = 'SHRUBBERY'
# print(mystr.lower())
# print(mystr.isalpha())
# print(mystr.isdigit())
# import string
# string.ascii_lowercase('abcdefghijklmnopqrstuvwxyz')
# string.whitespace('\t\n\r\x0b\x0c')
# mystr = 'xxaaxxaa'
# print(mystr.replace('aa','SPAM'))
# #print(mystr)
#

import string, random

length = 8
seedlower = string.lowercase
seeddigit = string.digits
seedupper = string.uppercase
pwd = pwdd = pwdl = pwdu = ''

countl = random.randrange(1, length - 1)
countu = random.randrange(1, length - countl)
countd = (length - countl - countu)

# 生成随机的字符
for l in random.sample(seedlower, countl):
    pwdl += l
for u in random.sample(seedupper, countu):
    pwdu += u
for d in random.sample(seeddigit, countd):
    pwdd += d

# 在随机位置出现随机的字符
seed = pwdl + pwdu + pwdd
shuffler = random.sample(seed, len(seed))
pwd = "".join(shuffler)
print(pwd)
