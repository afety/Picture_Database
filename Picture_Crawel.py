#coding:utf8
#file is used to grap picture and their figure or paper from some specific websits
#author = tanghan
import random

import bs4
from selenium import webdriver
from DBMan import *

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

        self.driver.get(self.__root)

        soup = bs4.BeautifulSoup(self.driver.page_source,'html.parser')

        target_div = soup.find(attrs={'id': 'subdiralphalist'})

        links = target_div.find_all('a');

        for link in links:
            # self.record.append(root+link['href'])
            print link['href']
            choose = random.randint(0, 4)
            num = random.randint(0, 10)
            heading_localaddr = 'Pictures/Heading/'
            pupil_localaddr = 'Pictures/Pupil/'
            abdomen_localaddr = 'Pictures/Abdomen/'
            lung_localaddr = 'Pictures/Lung/'
            if(choose == 0):
                for i in xrange(num):
                    name = str(random.randint(0, 100000))+'.jpg'
                    insertHeading(heading_localaddr+name, root+link['href'])
            elif(choose == 1):
                for i in xrange(num):
                    name = str(random.randint(0, 100000)) + '.jpg'
                    insertLung(lung_localaddr+name, root + link['href'])
            elif (choose == 2):
                for i in xrange(num):
                    name = str(random.randint(0, 100000)) + '.jpg'
                    insertPupil(pupil_localaddr+name, root + link['href'])
            elif (choose == 3):
                for i in xrange(num):
                    name = str(random.randint(0, 100000)) + '.jpg'
                    insertAbdomen(abdomen_localaddr+name, root + link['href'])
test = MedCrawel()
test.start()