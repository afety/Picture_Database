#-*- coding: utf-8 -*-
#file is used to grap picture and their figure or paper from some specific websits
#author = tanghan
import os
import random
import threading
import urllib

from bs4 import BeautifulSoup
from selenium import webdriver
import sys
from DBMan import insertPicture

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
        print 'start'
        for li in lis:
            artical_name = li.getText()
            __url = li.a['href']
            artical_url = self.__pre + __url
            self.artical_dic[artical_name] = artical_url
        print self.artical_dic

    def getImage(self):
        for key in self.artical_dic.keys():
            self.driver.get(self.artical_dic.get(key))
            artical_url = self.artical_dic.get(key)
            artical_name = key.strip()
            artical_name = artical_name.replace(' ', '_')
            imagedir = "./image/"+artical_name+'/'
            if not os.path.exists(imagedir):
                os.mkdir(imagedir)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            target_div = soup.find_all(attrs={'class': 'inlineImage'})
            for div in target_div:
                t = threading.Thread(target=self.__insertimage, args=(div, imagedir, artical_url,))
                t.start()

    def __insertimage(self, div, imagedir, artical_url):
        if div.img:
            print 'imgurl:', div.img['src']
            img_url = div.img['src']
            start = img_url.rfind('/')
            imgname = img_url[start+1:len(img_url)]
            imgpath = imagedir+imgname
            if not os.path.exists(imgpath):
                rawdata = urllib.urlretrieve(img_url, imgpath)
                print 'save image:', rawdata

            local_addr = imgpath
            net_addr = img_url
            print 'local_addr:', local_addr
            print 'net_addr:', net_addr
            print 'artical_url:', artical_url
            self.insertpicture(local_addr, img_url, artical_url)

    def insertpicture(self, local_addr, net_addr, artical_url):
        print 'insert picture'
        insertPicture(local_addr, net_addr, artical_url)

    # def imageclassification(self,imgpath):

    def start(self):
        self.getImageUrl()
        self.getImage()



med = MedCrawel('http://reference.medscape.com/guide/anatomy', 'http://reference.medscape.com')
med.start()