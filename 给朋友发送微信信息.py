# -*- coding: utf-8 -*-
import requests
import os
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from wxpy import *


bot = Bot()  # 登陆网页微信，并保存登陆状态
def sendblogmsg(content):
    # 搜索自己的好友，注意中文字符前需要+u
    my_group = bot.friends().search(u'杨宝国')[0]
    my_group.send(content)  # 发送天气预报

def getHTMLText(url,headers):
    try:
        r=requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

def parsehtml(namelist,urllist,html):
    url='http://www.tom61.com/'
    soup=BeautifulSoup(html,'html.parser')
    t=soup.find('dl',attrs={'class':'txt_box'})
    i=t.find_all('a')
    for link in i:
        urllist.append(url+link.get('href'))
        namelist.append(link.get('title'))
    print(urllist)
    print(namelist)
    return urllist,namelist

def mylittlestory():
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
               }
    urllist=[]#定义存放故事URL的列表
    namelist=[]#定义存放故事名字的列表
    if not os.path.exists('myshortStories'):#将所有的故事放到一个目录下
        os.mkdir('myshortStories')
    for i in range(1,2):
        if i==1:#爬取故事的地址和故事名
            url='http://www.tom61.com/ertongwenxue/shuiqiangushi/index.html'
        else:
            url='http://www.tom61.com/ertongwenxue/shuiqiangushi/index_'+str(i)+'.html'
        print ("正在爬取第%s页的故事链接：" % (i))
        print (url+'\n')
        html=getHTMLText(url,headers)
        urls,storiesNames = parsehtml(namelist,urllist,html)
        littleStories = []
        m=0
        for url in urls:#通过URL在爬取具体的故事内容
            print('已经爬取了'+str(((i-1)*70+m))+'篇文章')
            littlestory = ''
            storyhtml = getHTMLText(url,headers)
            soup = BeautifulSoup(storyhtml, 'html.parser')
            t = soup.find('div', class_='t_news_txt')
            ptexts = t.find_all('p')
            for ptext in ptexts: #将一个故事作为数列的一个元素
                storytext = ptext.text
                littlestory = littlestory+storytext
            littleStories.append(littlestory.replace('\u3000\u3000',''))
            m=m+1
            time.sleep(1)
        myLittleStorySets = dict(zip(storiesNames,littleStories))#将故事名和故事内容拼接成字典的形式
        print("爬取链接完成")
        k=0
        for storyName, storyContent in myLittleStorySets.items():
            textName = 'myshortStories/'+'Day'+str(((i-1)*70+k))+'.txt'#为每个故事建立一个TXT文件
            with open(textName, 'a', encoding='utf-8') as f:
                f.write(storyName)
                f.write('\n')
                f.write(storyContent)
                k = k + 1
                print("正在写入Day"+str(((i-1)*70+k))+"故事")
                time.sleep(1)

def getZZWeatherAndSendMsg():
    # 要改为自己想要获取的城市的url，下面是青岛的url
    resp = urlopen('http://www.weather.com.cn/weather1d/101220106.shtml')
    soup = BeautifulSoup(resp, 'html.parser')
     # 获取温度数据
    tem = soup.find('p', class_="tem").find('span').string
    # 第一个包含class="tem"的p标签即为存放今天天气数据的标签
    # 获取天气状况
    weather = soup.find('p', class_="wea").string
    # 获取风力情况
    win = soup.find('p', class_="win").find('span').string
     # 获取日出时间
    sun = soup.find('p', class_="sun sunUp").find('span').string
     # 拼接要发送的消息格式
    weatherContent = '庐江今日：' + '\n' + '天气：' + weather + '\n' + '温度：' + tem + '℃' + '\n' + '风力：' + win + '\n' + sun + '\n' + '注意天气变化！！'
    i=0
    for i in range(100):
        fileName = './myshortStories/'+'Day'+str(i)+'.txt'
        storyContent = open(fileName,encoding='utf-8').read()
        sentContents = weatherContent+ '\n\n'+'每天给你讲一个小故事，今天的是：'+ '\n\n'+storyContent
        sendblogmsg(sentContents)
         # 设置每天发送一次v
        #t = Timer(24*60*60,job)
        #t.start()
        time.sleep(24 * 60 * 60)

if __name__=='__main__':
    mylittlestory()
    getZZWeatherAndSendMsg()
