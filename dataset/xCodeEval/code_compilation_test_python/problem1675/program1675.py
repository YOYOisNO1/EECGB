    # -*- coding: utf-8 -*-
    # @Time : 2019/6/5 13:21
    # @Author : yuggu
    # @Site :
    # @File : test.py
    # @Software: PyCharm\
    
    # import pymysql
    # # 打开数据库连接，参数1：主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名称
    # db=pymysql.connect("localhost","root","root","school")
    # # 使用cursor()方法创建一个游标对象cursor
    # cursor=db.cursor()
    # # 使用execute()方法执行sql查询
    # cursor.execute("select version()")
    # # 使用fetchone()
    # data=cursor.fetchone()
    # print("Data version:%s " % data)
    # # 关闭数据库连接
    # db.close()
    
    # import sys
    # import pygame
    #
    # charlotte=pygame.image.load("1.jpg")                   # 加载图片
    # charlotterect=charlotte.get_rect()                     # 获取矩形区域
    # size=(int(charlotterect[2]/3),int(charlotterect[3]/3)) # 这里把图片给缩小为原来的1/3
    # charlotte=pygame.transform.scale(charlotte,size)       # 进行对原图片的缩小并返回一个缩小后图片的surface
    #
    # pygame.init()
    # screen=pygame.display.set_mode(size)
    # color=(0,0,0)
    # charlotte=pygame.transform.scale(charlotte,size)
    # charlotterect= (charlotte.get_rect())  # 获取矩形区域
    
    # pygame.init()
    # size=width,height=700,600
    # screen=pygame.display.set_mode(size)
    # color=(0,0,0)
    
    # while True:
    #     for event in pygame.event.get():
    #          if event.type == pygame.KEYDOWN:
    #              sys.exit()
    #     screen.fill(color)
    #     screen.blit(charlotte,charlotterect)
    #     pygame.display.flip()
    # pygame.quit()
    
    #
    # import urllib.request
    # import urllib.parse
    #
    # data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
    # response=urllib.request.urlopen("http://httpbin.org/post",data=data)
    # html=response.read()
    # print(html)
    
    # import requests
    # url='https://blog.csdn.net'
    # # 创建头部信息
    # headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    # response=requests.get(url,headers=headers)
    # print(response.content)
    
    # # 爬虫爬取网页框架
    # import requests
    #
# def getHTMLText(url):
    #     try:
    #         r=requests.get(url,timeout=30)
    #         r.raise_for_status() # 如果状态不是200，引发HTTPError异常,然后抛出捕获
    #         # ,内部进行判断
    #         r.encoding=r.apparent_encoding
    #         return r.text
    #     except:
    #         return "产生异常"
    #
    # if __name__ == "__main__":
    #     url="http://blog.csdn.net"
    #     print(getHTMLText(url))
    #
    #
    # # 浏览器headers模拟
    # import requests
    #
    # kv={'User-Agent':'Mozilla/5.0'}
    # response=requests.get('http://www.amazon.cn/',headers=kv)
    # response.encoding=response.apparent_encoding
    # print(response.request.headers)
    
    # # 网络图片爬取
    # import requests
    # path='D://abc.jpg'  # 保存在D盘下，以abc.jpg命名
    # url='https://wx4.sinaimg.cn/mw690/8d05b653ly1g4n0elm7axj20j60b475b.jpg'
    #
    # r=requests.get(url)
    # print(r.encoding)
    # with open(path,'wb') as f:
    #     f.write(r.content)
    
    # # 百度关键字提交接口
    # import requests
    # kv={'wd':'Python'}
    # r=requests.get('http://www.baidu.com/s',params=kv)
    # print(r.request.url)
    
    
    # from bs4 import BeautifulSoup
    # import urllib.request
    # html = urllib.request.urlopen("https://www.csdn.net/").read().decode('utf-8')
    # soup = BeautifulSoup(html,"html.parser")
    # titles=soup.select("h3[class='company_name'] a") # CSS 选择器
    # for title in titles:
    # print(title.get_text(),title.get('href'))# 标签体、标签属性
    
    
    # # 标签树向上遍历
    # import requests
    # from bs4 import BeautifulSoup
    #
    # url='https://python123.io/ws/demo.html'
    # demo=requests.get(url).text
    # soup=BeautifulSoup(demo,'html.parser')
    # for parent in soup.a.parents:
    # 	if parent is None:
    # 		print(parent)
    # 	else:
    # 		print(parent.name)
    
    
    # # 起点小说爬取
    # import requests
    # from bs4 import BeautifulSoup
    # import bs4
    #
    #
    # path="3.txt"
    # fw=open(path,'w',encoding='utf-8')
    #
    # url = "https://book.qidian.com/info/1015323848#Catalog"
    # r=requests.get(url,timeout=30)
    # r.raise_for_status()
    # r.encoding=r.apparent_encoding
    #
    # soup = BeautifulSoup(r.text, 'html.parser')
    # for li in soup.find_all('ul')[3]:
    #     if isinstance(li, bs4.element.Tag):
    #         chapter = li.a
    #         #print(chapter)
    #         chapter_url = 'https:%s' % chapter.get('href')
    #         #chapter_title=chapter.contents # ->['第一节 龙城']
    #         chapter_title=chapter.text      # ->第一节 龙城
    #         print(chapter_title)
    #         print(chapter_url)
    #         chapter_response=requests.get(chapter_url)
    #         chapter_response.encoding=chapter_response.apparent_encoding
    #         chapter_html=chapter_response.text
    #         chapter_soup=BeautifulSoup(chapter_html,'html.parser')
    #         chapter_tag=chapter_soup.find('div',class_='read-content j_readContent')
    #         fw.write(chapter_title)
    #         fw.write(chapter_tag.text)
    #
    # fw.close()
    #
    # import re
    # import requests
    #
    #
# def getHtmlText(url):
    #     try:
    #         r = requests.get(url)
    #         r.raise_for_status()
    #         r.encoding = r.apparent_encoding
    #         return r.text
    #     except:
    #         return ""
    #
    #
# def getInfor(html):
    #     print(html)
    #     print(re.findall(r'<tbody>.*?</tbody>', html))
    #
    #
# def main():
    #     url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.41.7fab2157JOw8dn&id=555305762446&ns=1&abbucket=10'
    #     html = getHtmlText(url)
    #     getInfor(html)
    #
    #
    # main()
    
    if __name__ == '__main__':
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(reverse = True)
        res = 0
        k = 100000000
        for i in range(n) :
            # print(i)
            k = max(min(k, a[i]),0)
            res += k
            k -= 1
    
        print(res)