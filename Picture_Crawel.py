#-*- coding: utf-8 -*-
#file is used to grap picture and their figure or paper from some specific websits
#author = tanghan
import random
import urllib

from bs4 import BeautifulSoup
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#图片抓取类,负责从特定的图片数据库中抓取图片及Paper
class Crawel:
    def __init__(self):
        print ('Start Grap')

root = 'http://emedicine.medscape.com'
class MedCrawel:
    def __init__(self, root, pre):
        if root[:4] != 'http':
            root += 'http://'
        self.__root = root
        self.__pre = pre
        self.driver = webdriver.PhantomJS('D:\phantomjs-1.9.7-windows\phantomjs.exe')
        self.artical_dic = {}
        self.__imgdir = './image/'

    def getImageUrl(self):
        self.driver.get(self.__root)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        target_div = soup.find(attrs={'id': 'subdiralphalist'})
        lis = target_div.find_all('li')
        for li in lis:
            artical_name = li.getText()
            __url = li.a['href']
            artical_url = self.__pre + __url
            self.artical_dic[artical_name] = artical_url

    def getImage(self):
        for key in self.artical_dic.keys():
            self.driver.get(self.artical_dic.get(key))
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            target_div = soup.find_all(attrs={'class': 'inlineImage'})
            for div in target_div:
                if div.img:
                    img_url = div.img['src']
                    start = img_url.rfind('/')
                    imgname = img_url[start+1:len(img_url)]
                    imgpath = self.__imgdir+imgname
                    rawdata = urllib.urlretrieve(img_url, imgpath)

    # def imageclassification(self,imgpath):

    def start(self):
        self.getImageUrl()
        self.getImage()

class

med = MedCrawel('http://reference.medscape.com/guide/anatomy', 'http://reference.medscape.com')
med.start()