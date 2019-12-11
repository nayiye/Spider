#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import requests
import re
from fontTools.ttLib import TTFont
from selenium import webdriver
from PIL import Image
import os
import pytesseract


class Number_parser:
    def __init__(self):
        '''初始化'''
        self.content = None
        self.url = None
        self.font = None
        self.names = None
        self.font_dict = None

    def get_headers(self):
        '''
        获取请求头
        :return:
        '''
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        return headers

    def down(self,url):
        '''下载制定页面'''
        response = requests.get(url, headers=self.get_headers())
        self.content = response.text
        self.url = response.url
        #print(self.content)

    def font_handle(self):
        '''下载字体文件'''
        pat = re.compile(r"\n           url\('(.*?.woff)'\).*?format\('woff'\)",re.M|re.S)
        font_url  = 'http:'+pat.search(self.content).group(1).strip()
        print('font_url:',font_url)
        ttf = requests.get(font_url,stream=True,headers=self.get_headers())
        with open('./data/maoyan.woff','wb') as pdf:
            for chunck in ttf.iter_content(chunk_size=1024):
                if chunck:
                    pdf.write(chunck)
        self.font = TTFont('./data/maoyan.woff')
        self.font.saveXML('./data/maoyan.xml')

    def gen_html(self):
        '''生成html页面,建立编码和字符之间的映射关系'''
        self.names = self.font.GetIDsOfNames()  # 获取字体文件中name信息
        print(self.names)
        chars = []
        tmps = []
        for name in self.names:
            if name.find('uni')>=0:
                char = name.replace('uni','&#x') + ';'
                chars.append(char)
                tmps.append(name)
        print(chars)
        self.names = tmps
        with open('./data/font_template.html','r',encoding='utf-8') as file:
            html = file.read()
        pat1 = re.compile(r"src: url\('.*?.woff'\)",re.M|re.S)
        pat2 = re.compile(r'<span class="stonefont">(.*?)</span>',re.M|re.S)
        html = pat1.sub("src: url('./maoyan.woff')",html)
        html = pat2.sub('<span class="stonefont">'+'&nbsp;'.join(chars)+'</span>',html)
        #print(html)
        with open('./data/font.html','w',encoding='utf-8') as file:
            file.write(html)

    def parse_font(self):
        '''解析字体文件中的字符'''
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=option) #
        browser.get('file:///'+os.path.abspath('./data/font.html'))
        browser.save_screenshot('./images/demo01.png')
        img = Image.open('./images/demo01.png')
        text = pytesseract.image_to_string(img)
        print(text)
        self.font_dict = {self.names[i]:text[i] for i in range(len(self.names))}
        print(self.font_dict)
        browser.quit()

    def parse_number(self,val):
        '''对数字解密'''
        pass

    def convert_number(self,val):
        '''对加密的数字格式转换'''
        pass

    def parse(self):
        '''网页源码解析'''
        pat1 = re.compile(r'<ul.*?class="ranking-wrapper ranking-box">(.*?)</ul>',re.M|re.S)
        content = pat1.search(self.content).group(1)
        pat2 = re.compile(r'<li.*?>(.*?)</li>',re.M|re.S)
        ls = pat2.findall(content)
        print('len:',len(ls))
        pat3 = re.compile(r'<span.*?class="ranking-movie-name">(.*?)</span>', re.M | re.S)
        pat4 = re.compile(r'<span.*?class="ranking-top-moive-name">(.*?)</span>', re.M | re.S)
        pat5 = re.compile(r'<span.*?class="stonefont">(.*?)</span>', re.M | re.S)

        for each in ls:
            title = pat3.search(each)
            if title != None:
                title = title.group(1)
            else:
                title = pat4.search(each).group(1)
            print('title:',title)
            nums = pat5.search(each).group(1)
            print('nums:',nums)
            print('='*200)


if __name__ == '__main__':
    parser = Number_parser()
    url = 'https://maoyan.com/'
    parser.down(url)
    parser.font_handle()
    parser.gen_html()
    parser.parse_font()
    parser.parse()
