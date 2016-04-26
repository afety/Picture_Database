#coding:utf8
#file is used to grap picture and their figure or paper from some specific websits
#author = tanghan

#文本分析类，用于大致判断图片类别
class Text_Parser:
    def __init__(self,webtext):
        self.__text = webtext

#图片抓取类,负责从特定的图片数据库中抓取图片及Paper
class Crawel:
    def __init__(self):
        print ('Start Grap')

