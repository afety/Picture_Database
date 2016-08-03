#coding:utf-8
#file is used to crawel pictures from yxtk
import os
import urllib2

from bs4 import BeautifulSoup
from DBMan import DBMan
from pythonscript.DCTTransf import gethashstr
from pythonscript.randonname import randomname


class yxtk_crawel:
    def __init__(self):
        self.rooturl = 'http://www.yxyxtk.com/'
        self.starturl = 'http://www.yxyxtk.com/tuku.php'
        self.dbman = DBMan()
        self.images = '../images/yxtk'

    # 获取bingli网址
    def getbingliurl(self):
        res = urllib2.urlopen(self.starturl)
        soup = BeautifulSoup(res.read(), 'html.parser')
        target_bingli = soup.find_all('ul', attrs={'class': 'left'})
        for bingli in target_bingli:
            for a in bingli.find_all('a'):
                print 'link:',a.text, ' ', self.rooturl + a['href']
                self.gettypeurl(self.rooturl + a['href'])

    # 获取type url
    def gettypeurl(self, entry):
        target_bingli = []
        try:
            res = urllib2.urlopen(entry)
            soup = BeautifulSoup(res.read(), 'html.parser')
            target_bingli = soup.find_all(attrs={'class': 'a1'})
        except Exception, e:
            print 'Error in yxtk gettypeurl:', e
        for div in target_bingli:
            a = div.a
            link = self.rooturl + a['href']
            print 'typelink:', a.text,' ', link
            # type存储并获取类型id
            type = (div.text).encode('utf8')
            if not self.dbman.type_typenameexist(type):
                self.dbman.type_insert(type)
            typeid = self.dbman.type_getidbytypename(type)

            # yxtk_website 存储
            if not self.dbman.yxtkwebsite_urlexist(link):
                self.dbman.yxtkwebsite_insert(url=link, typeid=typeid)
                print 'insert website success'

            #生成图片存储目录
            imgdir = self.images + '/' + randomname(6)
            while os.path.exists(imgdir):
                imgdir = self.images + '/' + randomname(6)
            os.mkdir(imgdir)
            self.getimage(link.encode('utf8'), imgdir)
    # 图片存储
    def getimage(self, articalurl, dirpath):
        target_images = []
        print 'articalurl:', articalurl
        try:
            res = urllib2.urlopen(articalurl)
            soup = BeautifulSoup(res.read(), 'html.parser')
            target = soup.find_all('ul', attrs={'class': 'xuan_p baguetteBoxOne gallery'})
            for t in target:
                if not t.has_attr('style'):
                    target = t
                    break
            target_images = target.find_all('img')
        except Exception, e:
            print 'Error in yxtk_crawel getimage:', e
        for img in target_images:
            imgsrc = img['src']
            print 'imgsrc', imgsrc
            imgname = imgsrc[imgsrc.rfind('/'):]
            imgpath = dirpath + '/' + imgname
            if not os.path.exists(imgpath):
                try:
                    resp = urllib2.urlopen(self.rooturl + imgsrc)
                    with open(imgpath, 'wb') as imgf:
                        imgf.write(resp.read())
                    urlid = self.dbman.yxtkwebsite_getidbyurl(articalurl)
                    sid = self.dbman.sourcetabls_getidbytablename('yxtk_website')
                    self.dbman.yxtkpicture_insert(urlid=urlid, localaddr=imgpath, sid=sid)

                    # picture表存储
                    hashstr = gethashstr(imgpath)
                    if not self.dbman.picture_hashstrexist(hashstr):
                        pid = self.dbman.yxtkpicture_getidbylocaladdr(imgpath)
                        sourcetableid = self.dbman.sourcetabls_getidbytablename(tablename='yxtk_picture')

                        self.dbman.picture_insert(pid=pid, sourcetableid=sourcetableid, hashstr=hashstr)
                except Exception, e:
                    print 'Error in yxtk_crawel get image:', e

    def start(self):
        self.getbingliurl()

if __name__ == "__main__":
    yx = yxtk_crawel()
    yx.start()