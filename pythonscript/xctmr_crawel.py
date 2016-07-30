#coding:utf8
#time : 2016.07.27
#file is used to get images from xctmr
import os
import urllib2

import chardet
from bs4 import BeautifulSoup
from DBMan import DBMan
from pythonscript.DCTTransf import gethashstr
from pythonscript.randonname import randomname


class xctmrcrawel():
    def __init__(self):
        # 类型链接
        self.typelinks = []
        self.rooturl = 'http://www.xctmr.com/bl/'
        self.homeurl = 'http://www.xctmr.com'
        self.imagesdir = str('../images')
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
            type = typeandlink[1].decode('utf-8').encode('utf8')
            typelink = typeandlink[0]
            #类型插入
            if not self.dbman.type_typenameexist(type):
                if not self.dbman.type_insert(type):
                    return
            typeid = self.dbman.type_getidbytypename(type)
            print 'typeid:', typeid
            # 获取类型全部页面地址
            #先判断是否有分页
            articallist = []
            res = urllib2.urlopen(typelink)
            pagesource = res.read()
            soup = BeautifulSoup(pagesource, 'html.parser')
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
                    articalurls = target_lists.find_all('a')
                    for link in articalurls:
                        if link.has_attr('href') and link.has_attr('title'):
                            if not self.dbman.xctmrwebsite_urlexist(link['href']):
                                if self.dbman.xctmrwebsite_insert(url=link['href'], typeid=typeid):
                                    articallist.append(link['href'])
                                else:
                                    return
            for articalurl in articallist:
                dirname = randomname(6)
                while os.path.exists(self.imagesdir + '/' + str(dirname)):
                    dirname = randomname(6)
                dirpath = str(self.imagesdir) + '/' + str(dirname)
                # try:
                print dirpath
                os.mkdir(dirpath)
                self.getarticalimages(articalurl, dirpath)
                # except Exception, e:
                #     print 'Except occurred in mkdir image dir:', e
                #     return
    # 文章图片抓取， 并判断分页情况
    def getarticalimages(self, articalurl, dirpath):
        if articalurl[:4] != 'http':
            articalurl = self.homeurl + articalurl
        res = urllib2.urlopen(articalurl)
        pagesource = res.read()
        soup = BeautifulSoup(pagesource, 'html.parser')
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
                imageurls.append(str(img['src']))
        else:
            pagecount = trailerpageurl[trailerpageurl.rfind('_')+1:trailerpageurl.rfind('.')]
            prefix = trailerpageurl[:trailerpageurl.rfind('_')]
            pages = []
            for page in xrange(1, int(pagecount)+1):
                url = ''
                if page == 1:
                    url += prefix + '.html'
                else:
                    url += prefix + '_ ' + str(page) + '.html'
                if url != '' and url[:4] != 'http':
                    url = self.homeurl + url
                pages.append(url.replace(' ', ''))
            for pageurl in pages:
                error = []
                try:
                    sub_source  = urllib2.urlopen(pageurl).read()
                    sub_soup = BeautifulSoup(sub_source, 'html.parser')
                    sub_target_td = sub_soup.find(attrs={'id': 'text'})
                    imgs = sub_target_td.find_all('img')
                    error = imgs
                    for img in imgs:
                        imageurls.append(img['src'])
                except Exception, e:
                    print 'Connect Error in getarticalimage in get imageurls:', e
                    with open('getimageurlerror.log', 'w') as logfile:
                        for img in error:
                            logfile.write(img['src'] + '\n')
        # 图片存储
        # 获取网站ID
        urlid = self.dbman.xctmrwebsite_getidbyurl(articalurl)
        IMGNAMELENGTH = 8
        for imageurl in imageurls:
            imgname = randomname(IMGNAMELENGTH)
            suffix = imageurl[imageurl.rfind('.'):]
            while os.path.exists(dirpath + '/' + imgname + suffix):
                imgname = randomname(IMGNAMELENGTH)
            imgpath = dirpath + '/' + imgname + suffix
            print 'imageurl:', imageurl
            if imageurl[0:4] != 'http':
                imageurl = self.homeurl + imageurl
            try:
                resp = urllib2.urlopen(imageurl)
                with open(imgpath, 'wb') as imgfile:
                    imgfile.write(resp.read())

                # 图片插入
                websitesourcetableid = self.dbman.sourcetabls_getidbytablename("xctmr_website")
                if not self.dbman.xctmrpicture_localaddrexist(localaddr=imgpath):
                    self.dbman.xctmrpicture_insert(localaddr=imgpath, urlid=urlid, sid=websitesourcetableid)
                pid = self.dbman.xctmrpicture_getidbylocaladdr(localaddr=imgpath)
                sourcetableid = self.dbman.sourcetabls_getidbytablename("xctmr_picture")
                # hashstr计算
                hashstr = gethashstr(imgpath)
                print 'hashstr:', hashstr
                if not self.dbman.picture_hashstrexist(hashstr) and hashstr != None:
                    self.dbman.picture_insert(pid=pid, sourcetableid=sourcetableid, hashstr=hashstr)
            except Exception, e:
                print 'Get IMage error:', e
    def start(self):
        self.__gettypelinks()
if __name__ == "__main__":
    crawel = xctmrcrawel()
    crawel.start()