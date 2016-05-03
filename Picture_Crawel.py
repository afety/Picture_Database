#coding:utf8
#file is used to grap picture and their figure or paper from some specific websits
#author = tanghan

import bs4
from selenium import webdriver


#文本分析类，用于大致判断图片类别
class Text_Parser:
    def __init__(self,webtext):
        self.__text = webtext

#图片抓取类,负责从特定的图片数据库中抓取图片及Paper
class Crawel:
    def __init__(self):
        print ('Start Grap')

root = 'http://emedicine.medscape.com'
class MedCrawel:
    def __init__(self):
        self.__root = 'http://reference.medscape.com/guide/anatomy'
        self.driver = webdriver.PhantomJS()
        self.record = []

    def start(self):
        print 1
        self.driver.get(self.__root)
        print 2
        soup = bs4.BeautifulSoup(self.driver.page_source,'html.parser')
        print 3
        target_div = soup.find(attrs={'id': 'subdiralphalist'})
        print 4
        links = target_div.find_all('a');
        print 5
        for link in links:
            # self.record.append(root+link['href'])
            print link['href']
test = MedCrawel()
test.start()