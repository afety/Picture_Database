#coding:utf8
#time : 2016.07.27
#file is used to get images from xctmr
import urllib2

import chardet
from bs4 import BeautifulSoup
from DBMan import DBMan

class xctmrcrawel():
    def __init__(self):
        # 类型链接
        self.typelinks = []
        self.rooturl = 'http://www.xctmr.com/bl/'
        self.homeurl = 'http://www.xctmr.com'
        self.imagesdir = '../images'
        self.dbman = DBMan()

    def __gettypelinks(self):
        res = urllib2.urlopen(self.rooturl)
        pagesource = res.read()
        soup = BeautifulSoup(pagesource, 'html.parser')
        target = soup.find(attrs={'bordercolor': '#CCCCCC'})
        links = target.find_all('a')
        for link in links:
            temp = link.text.encode('utf8)')
            if temp.find('病例') == -1:
                self.typelinks.append([link['href'], temp])
        self.__getarticallist()

    #获取病例类型网站 并获取文章列表
    def __getarticallist(self):
        for typeandlink in self.typelinks:
            type = typeandlink[1]
            typelink = typeandlink[0]
            #类型插入
            if not self.dbman.type_typenameexist(type):
                if not self.dbman.type_insert(type):
                    return
            typeid = self.dbman.type_getidbytypename(type)
            # 获取类型全部页面地址
            #先判断是否有分页
            articallist = []
            res = urllib2.urlopen(typelink)
            pagesource = res.read()
            soup = BeautifulSoup(pagesource)
            target_list = soup.find(attrs={'class': 'news_list'})
            links = target_list.find_all('a')
            trailerpageurl = ''
            #全部页面地址
            for link in links:
                if link.text.encode('utf8') == '尾页':
                    trailerpageurl += link['href']

            # 若trailerpageurl为''则只有一页, 否则有多页
            if trailerpageurl == '':
                for link in links:
                    if link.has_attr('href') and link.has_attr('title'):
                        if not self.dbman.xctmrwebsite_urlexist(link['href']):
                            if self.dbman.xctmrwebsite_insert(url=link['href'], typeid=typeid):
                                articallist.append(link['href'])
                            else:
                                return
            else:
                pagecount = int(trailerpageurl[trailerpageurl.rfind('_')+1:trailerpageurl.rfind('.')])
                pages = []
                prefix = trailerpageurl[:trailerpageurl.rfind('_')]
                for page in xrange(1, pagecount+1):
                    if page == 1:
                        pages.append(prefix + '.html')
                    else:
                        pages.append(prefix + '_' + str(page) + '.html')
                for pageurl in pages:
                    res = urllib2.urlopen(pageurl)
                    source = res.read()
                    sub_soup = BeautifulSoup(source, 'html.parser')
                    target_lists = sub_soup.find(attrs={'class': 'news_list'})
                    articalurls = target_list.find_all('a')
                    for link in articalurls:
                        if link.has_attr('href') and link.has_attr('title'):
                            if not self.dbman.xctmrwebsite_urlexist(link['href']):
                                if self.dbman.xctmrwebsite_insert(url=link['href'], typeid=typeid):
                                    articallist.append(link['href'])
                                else:
                                    return
            for articalurl in articalurls:
                self.getarticalimages(articalurl)

    # 文章图片抓取， 并判断分页情况
    def getarticalimages(self, articalurl):
        res = urllib2.urlopen(articalurl)
        pagesource = res.read()
        soup = BeautifulSoup(page_source, 'html.parser')
        target_td = soup.find(attrs={'id': 'text'})
        links = target_td.find_all('a')
        trailerpageurl = ''
        for link in links:
            if link.text.encode('utf8') == '尾页':
                trailerpageurl += link['href']

        # 图片地址
        imageurls = []
        # 多页和单页分析
        if trailerpageurl == '':
            imgs = target_td.find_all('img')
            for img in imgs:
                imageurls.append(self.homeurl + img['src'])
        else:
            pagecount = trailerpageurl[trailerpageurl.rfind('_')+1:trailerpageurl.rfind('.')]
            prefix = trailerpageurl[:trailerpageurl.rfind('_')]
            pages = []
            for page in xrange(1, pagecount+1):
                if page == 1:
                    pages.append(prefix + '.html')
                else:
                    pages.append(prefix + '_ ' + str(page) + '.html')
            for pageurl in pages:
                sub_source  = urllib2.urlopen(pageurl).read()
                sub_soup = BeautifulSoup(sub_source, 'html.parser')
                sub_target_td = sub_soup.find(attrs={'id': 'text'})
                imgs = sub_target_td.find_all('img')
                for img in imgs:
                    imageurls.append(self.homeurl + img['src'])
        # 图片存储
        for imageurl in imageurls:



if __name__ == "__main__":
    res = urllib2.urlopen('http://www.xctmr.com/thorax/lung/2010-05-20/4ab52af276e7722bec138939c6f789e3.html')
    page_source = res.read()
    char = chardet.detect(page_source)
    print char
    soup = BeautifulSoup(page_source, 'html.parser')
    target_td = soup.find(attrs={'id': 'text'})
    links = target_td.find_all('a')
    for link in links:
        print link