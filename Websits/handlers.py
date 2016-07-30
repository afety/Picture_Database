#coding:utf8
#time:2016.05.07
#file is used to established a website to get imgs
import StringIO
import imghdr
import os

import shutil
import threading
import urllib2

from PIL import Image

from tornado import web, ioloop, escape

from pythonscript.DBMan import DBMan
from pythonscript.DCTTransf import gethashstr
from pythonscript.randonname import randomname
Image_Format = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'bmp', 'png']


class UploadFileHandler(web.RequestHandler):
    def get(self):
        self.render('TinEyeReverseImageSearch.html')

    def post(self):
        self.dbman = DBMan()
        userurl = None
        try:
            userurl = self.get_argument('url')
        except:
            pass
        file_metas = []
        if userurl == None:
            file_metas = self.request.files['image']
        else:
            try:
                res = urllib2.urlopen(userurl)
                file_metas.append({'body': res.read(), 'filename': randomname(5) + 'png'})
            except Exception, e:
                file_metas.append({'body': '', 'filename': randomname(5) + 'png'})
        items = []
        for meta in file_metas:
            print meta
            name = meta['filename']
            print 'userimage:', name
            suffix = name[name.rfind('.'):]
            filename = randomname(5) + suffix
            userimagepath = "./static/userimages"
            if not os.path.exists(userimagepath):
                os.mkdir(userimagepath)
            # 储存用户上传的图片
            while os.path.exists(userimagepath + '/' + filename):
                filename = randomname(5) + suffix
            with open(userimagepath + '/' + filename, 'wb') as ifile:
                ifile.write(meta['body'])


            userimgpath = userimagepath + '/' + filename

            abspath =  os.path.abspath(userimgpath)
            if imghdr.what(abspath) in Image_Format:
                uimg = Image.open(abspath)
                items.append([userimgpath, imghdr.what(userimgpath), str(uimg.size[0]) + '*' + str(uimg.size[1]), str(os.path.getsize(userimgpath)/1000) + 'kb'])
                # hashstr计算
                userimage_hashstr = gethashstr(userimgpath)

                # 获取相同hashstr的图片信息
                infos =self.dbman.picture_getinfobyhashstr(hashstr=userimage_hashstr)
                for info in infos:
                    pid = info[1]
                    sourcetableid = info[2]
                    sourcetablename = self.dbman.sourcetable_gettablenamebyid(sourcetableid)
                    pictureinfo = self.dbman.getinfobytablenameandid(sourcetablename, pid)
                    print 'pictureinfo:', pictureinfo

                    # 定位图像locaaddr与url
                    localaddr = pictureinfo[1]
                    # 获取图片属性
                    img = Image.open(localaddr)
                    pictype = imghdr.what(localaddr)
                    picsize = str(img.size[0]) + "*" + str(img.size[1])
                    picsto = str(os.path.getsize(localaddr)/1000) + ' kb'


                    # 移动图片进入static目录
                    staticname = randomname(6) + localaddr[localaddr.rfind('.'):]
                    shutil.copy(localaddr, 'static/userimages/' + staticname)
                    # 静态文件路径
                    staticpath = 'userimages/' + staticname

                    urlid = pictureinfo[2]
                    wid = pictureinfo[3]
                    wtablename = self.dbman.sourcetable_gettablenamebyid(wid)
                    winfo = self.dbman.getinfobytablenameandid(wtablename, urlid)

                    # 获取网址
                    netaddr = winfo[1]

                    typeid = winfo[2]

                    # 类型
                    type = self.dbman.type_gettypenamebyid(typeid)

                    items.append(['./static/'+staticpath, pictype, picsize, picsto, netaddr, type])
        self.render('Result.html', items=items)