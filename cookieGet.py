import requests
from bs4 import BeautifulSoup

class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/marketplace'
        self.session = requests.Session()
#先是以get方式模拟登陆页面获取对应的东西
    def token(self):
        response=self.session.get(self.login_url,headers=self.headers)
        soup=BeautifulSoup(response.text,'lxml')
        authenticity_token=soup.find_all('input')
        token=authenticity_token[1]['value']#获取对应标签的值的一个方法
        return token

#进行模拟登陆
    def login(self,user,password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': user,
            'password': password
        }
        response=self.session.post(self.post_url,data=post_data,headers=self.headers)
        if response.status_code==200:
            print("success")
        else:
            print('something else')

        response=self.session.get(self.logined_url,headers=self.headers)
        if response.status_code==200:
            soup1=BeautifulSoup(response.text,'lxml')
            print(soup1.find_all('div'))
        else:
            print('fail')

x=Login()
x.token()
x.login(user='scpyzl',password='258258scpyzl')
