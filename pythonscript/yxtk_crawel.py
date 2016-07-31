#coding:utf-8
#file is used to crawel pictures from yxtk
import urllib2

from bs4 import BeautifulSoup

from pythonscript import DBMan


class yxtk_crawel:
    def __init__(self):
        self.rooturl = 'http://www.yxyxtk.com/'
        self.starturl = 'http://www.yxyxtk.com/tuku.php'
        self.dbman = DBMan()

    # 获取bingli网址
    def getbingliurl(self):
        res = urllib2.urlopen(self.starturl)
        soup = BeautifulSoup(res.read(), 'html.parser')
        target_bingli = soup.find_all('ul', attrs={'class': 'left'})
        lis = []
        for bingli in target_bingli:
            for a in bingli.find_all('a'):
                lis.append(a)
                self.gettypeurl(self.rooturl + a['href'])

    # 获取type url
    def gettypeurl(self, entry):
        try:
            res = urllib2.urlopen(entry)
            soup = BeautifulSoup(res.read(), 'html.parser')
            target_bingli = soup.find(attrs={'class': 'a1'})
            for div in target_bingli:
                link = self.rooturl + div['href']
                type = div.text
                if not self.dbman.type_typenameexist(type):
                    self.dbman.type_insert(type)


if __name__ == "__main__":
    yx = yxtk_crawel()
    yx.getbingliurl()