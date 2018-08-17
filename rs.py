#爬取猫眼电影前一百的排名的电影的各种消息链接为  http://maoyan.com/board/4
import requests
#将文件写入csv(可用excel打开)当获取的是字典形式的写入
import csv
import time
import json
import lxml
from bs4 import BeautifulSoup
def get_one_page(url):
    #加入headers，模拟以浏览器身份爬虫否则提取不出来页面
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    re=requests.get(url,headers=headers)
    if re.status_code==200:
        return re.text
    return None
def main():
   for offset in range(10):
     url="http://maoyan.com/board/4?offset="+str(offset*10)
     html=get_one_page(url)
     parse_one_page(html)
     print("===================================================")
     time.sleep(1)
    # print(html)

def parse_one_page(html):
    soup=BeautifulSoup(html,'lxml')
    dd=soup.find_all(name='dd')
    dic={}
    fp=open(r'C:\Users\20441\Desktop\maoyan.csv','a+')
    #字典形式的写入csv文件中
    fieldnames=['name','data-src','star','release-data']
    writes=csv.DictWriter(fp,fieldnames=fieldnames)
    writes.writeheader()
    for img_movinfo in dd:
        #这里的img_movinfo是tag类型，他的一个兄弟节点是空白再下一个就是有实际内容了
        img_src=img_movinfo.img.next_sibling.next_sibling
        dic['name']=img_src['alt']
        dic['data-src']=img_src['data-src']
        movie_info=img_movinfo.p.next_sibling.next_sibling
        #注意这里获得的是一个生成器，需要对生成器里的内容进行取值，即可完成简单的代码
        for m in movie_info.stripped_strings:
            dic['star']=m
        movie_info1=movie_info.next_sibling.next_sibling
        for n in movie_info1.stripped_strings:
            dic['release-data']=n
        print(dic)
        try:
           writes.writerow(dic)
        except:
            print("none")
    fp.close()
main()

