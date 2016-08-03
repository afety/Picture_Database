#coding:utf8
from sqlalchemy import text
from sqlalchemy.orm import Mapper

from Database import *
from sqlalchemy.sql import select

class DBMan:
    '''xctmr_website 表操作'''
    # 插入
    def xctmrwebsite_insert(self, url, typeid):
        try:
            session = DBSession()
            website = xctmr_Website(url=url, typeid=typeid)
            session.add(website)
            session.commit()
            session.close()
        except Exception, e:
            print 'Error in insert xctmr_website:', e
            return False
        return True
    #查询
    #url存在
    def xctmrwebsite_urlexist(self, url):
        try:
            print url
            session = DBSession()
            result = session.query(xctmr_Website.id).filter(xctmr_Website.url == url).one()
            print result
            session.close()
            return not result[0] == None
        except Exception, e:
            print 'Error in judge whether url exist:', e
            return False
    #id存在
    def xctmrwebsite_idexist(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.id).filter(xctmr_Website.id == id).one()
            return not result[0] == None
        except Exception,e:
            print 'Error in judge id exist in xctmr_website:', e
            return False
    # typeid存在
    def xctmrwebsite_typeidexist(self, typeid):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.id).filter(xctmr_Website.typeid == typeid).one()
            return not result[0] == None
        except Exception, e:
            print 'Error in judge typeid exist in xctmr_website:', e
            return False


    # id获取url
    def xctmrwebsite_getidbyurl(self, url):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.id).filter(xctmr_Website.url == url).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error in get id by url on xctmr_website:', e
            return None
    # id获取信息
    def xctmrwebsite_getwebsiteinfobyid(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.id, xctmr_Website.url, xctmr_Website.typeid).filter(xctmr_Website.url == id).one()
            session.close()
            return [result[0], result[1]]
        except Exception, e:
            print 'Error in get id by url on xctmr_website:', e
            return []
    # url获取id
    def xctmrwebsite_geturlbyid(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.url).filter(xctmr_Website.id == id).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error in get url by id on xctmr_website:', e
            return None

    '''xctmr_picture表操作'''
    #插入
    def xctmrpicture_insert(self, localaddr, urlid, sid):
        try:
            session = DBSession()
            xctmrpicture = xctmr_picture(localaddr=localaddr, urlid=urlid, sourcetableid=sid)
            session.add(xctmrpicture)
            session.commit()
            session.close()
        except Exception, e:
            print 'Error in insert into xctmr_picture:', e
            return False
        return True

    # 查询
    # id exist
    def xctmrpicture_idexist(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.id).filter(xctmr_picture.id == id).one()
            session.close()
            return not result[0] == None
        except Exception, e:
            print 'Error on xctmr_picture id exist:', e
            return False

    # localaddr exist
    def xctmrpicture_localaddrexist(self, localaddr):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.id).filter(xctmr_picture.localaddr == localaddr).one()
            session.close()
            return not result[0] == None
        except Exception, e:
            print 'Error on xctmr_picture localaddr exist:', e
            return False

    # 查询
    def xctmrpicture_getidbylocaladdr(self, localaddr):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.id).filter(xctmr_picture.localaddr == localaddr).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error on xctmrpicture_getidbylocaladdr:', e
            return None

    def xctmrpicture_getlocaladdrbyid(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.localaddr).filter(xctmr_picture.id == id).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error on xctmrpicture_getlocaladdrbyid:', e
            return None

    def xctmrpicture_getwtablenamebyid(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.sourcetableid).filter(xctmr_picture.id == id).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error on xctmrpicture_getwtablenamebyid:', e
            return None

    def xctmrpicture_getwtablenamebylocaladdr(self, localaddr):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.sourcetableid).filter(xctmr_picture.localaddr == localaddr).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error on xctmrpicture_getwtablenamebylocaladdr:', e
            return None


    '''sourcetables表操作'''
    def sourcetables_insert(self, tablename):
        try:
            session = DBSession()
            t = sourcetables(tablename=tablename)
            session.add(t)
            session.commit()
            session.close()
        except Exception, e:
            print 'sourcetables insert error:', e
            return False
        return True
    #查询
    # id exist
    def sourcetables_idexist(self, id):
        try:
            session = DBSession()
            result = session.query(sourcetables.id).filter(sourcetables.id == id).one()
            session.close()
            return not result[0] == None
        except Exception, e:
            print 'Error in sourcetables_idexist:', e
            return False

    # tablename exist
    def sourcetables_tablenameexist(self, tablename):
        try:
            session = DBSession()
            result = session.query(sourcetables.id).filter(sourcetables.tablename == tablename).one()
            session.close()
            return not result[0] == None
        except Exception, e:
            print 'Error in sourcetables_tablenameexist:', e
            return False

    # get id by tablename
    def sourcetabls_getidbytablename(self, tablename):
        try:
            session = DBSession()
            result = session.query(sourcetables.id).filter(sourcetables.tablename == tablename).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error in getidbytablename:', e
            return None

    # get tablename by id
    def sourcetable_gettablenamebyid(self, id):
        try:
            session = DBSession()
            result = session.query(sourcetables.tablename).filter(sourcetables.id == id).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error in gettablenamebyid:', e
            return None


    '''picture表操作'''
    #插入
    #表数据插入
    def picture_insert(self, pid, sourcetableid, hashstr):
        try:
            session = DBSession()
            pic = picture(pid=pid, sourcetableid=sourcetableid, hashstr=hashstr)
            session.add(pic)
            session.commit()
            session.close()
        except Exception, e:
            print 'Error in insert picture:', e
            return False
        return True

    #查询
    # id exist
    def picture_idexist(self, id):
        try:
            session = DBSession()
            result = session.query(picture.id).filter(picture.id == id).one()
            return not result[0] == None
        except Exception, e:
            print 'Error in picture_idexist:', e
            return False

    # pid exist
    def picture_pidexist(self, pid):
        try:
            session = DBSession()
            result = session.query(picture.id).filter(picture.pid == pid).one()
            return not result[0] == None
        except Exception, e:
            print 'Error in picture_pidexist:', e
            return False

    # sourcetableid exist
    def picture_sourcetableidexist(self, sourcetableid):
        try:
            session = DBSession()
            result = session.query(picture.id).filter(picture.sourcetableid == sourcetableid).one()
            return not result[0] == None
        except Exception, e:
            print 'Error in picture_sourcetableidexist:', e
            return False

    # hashstr exist
    def picture_hashstrexist(self, hashstr):
        try:
            session = DBSession()
            result = session.query(picture.id).filter(picture.hashstr == hashstr).one()
            return not result[0] == None
        except Exception, e:
            print 'Error in picture_hashstrexist:', e
            return False


    # get info by hashstr
    def picture_getinfobyhashstr(self, hashstr):
        try:
            session = DBSession()
            result = session.query(picture.id, picture.pid, picture.sourcetableid, picture.hashstr).filter(picture.hashstr == hashstr).all()
            session.close()
            temp = []
            for row in result:
                temp.append([row[0], row[1], row[2], row[3]])
            return temp
        except Exception, e:
            print 'Error in picture_getinfobyhashstr:', e
            return []

    # get info by id
    def picture_getinfobyid(self, id):
        try:
            session = DBSession()
            result = session.query(picture.id, picture.pid, picture.sourcetableid, picture.hashstr).filter(picture.id == id).all()
            session.close()
            temp = []
            for row in result:
                temp.append([row[0], row[1], row[2], row[3]])
            return temp

        except Exception, e:
            print 'Error in picture_getinfobyhashstr:', e
            return []

    '''type表操作'''
    def type_insert(self, typename):
        try:
            session = DBSession()
            t = typetable(typename=typename)
            session.add(t)
            session.commit()
            session.close()
        except Exception, e:
            print 'Error in type_insert:', e
            return False
        return True

    # typename存在
    def type_typenameexist(self, typename):
        try:
            print 'typename:', typename
            session = DBSession()
            result = session.query(typetable.id).filter(typetable.typename == typename).one()
            return not result[0] == None
        except Exception, e:
            print 'Error in type_typenameexist:', e
            return False

    # id获取typename
    def type_getidbytypename(self, typename):
        try:
            session = DBSession()
            result = session.query(typetable.id).filter(typetable.typename == typename).one()
            return result[0]
        except Exception, e:
            print 'Error in type_getidbytypename:', e
            return None

    # typename 获取 id
    def type_gettypenamebyid(self, id):
        try:
            session = DBSession()
            result = session.query(typetable.typename).filter(typetable.id == id).one()
            return result[0]
        except Exception, e:
            print 'Error in type_typenameexist:', e
            return None

    # 传递表名和ID值获取图片信息
    def getinfobytablenameandid(self, tablename, id):
        try:
            session = DBSession()
            getinfotext = text("select * from " + tablename + " where id=:id")
            result = session.execute(getinfotext, {'id': id})
            info = []
            for row in result:
                for x in row:
                    info.append(x)
            session.close()
            return info
        except Exception, e:
            print 'Error in getinfobytablenameandid:', e
            return []

    '''yxtk_website 表操作'''

    # 插入
    def yxtkwebsite_insert(self, url, typeid):
        try:
            session = DBSession()
            website = yxtk_website(url=url, typeid=typeid)
            session.add(website)
            session.commit()
            session.close()
        except Exception, e:
            print 'Error in insert yxtk_website:', e
            return False
        return True

    # 查询
    # url存在
    def yxtkwebsite_urlexist(self, url):
        try:
            print url
            session = DBSession()
            result = session.query(yxtk_website.id).filter(yxtk_website.url == url).one()
            print result
            session.close()
            return not result[0] == None
        except Exception, e:
            print 'Error in yxtk_website whether url exist:', e
            return False

    # id存在
    def yxtkwebsite_idexist(self, id):
        try:
            session = DBSession()
            result = session.query(yxtk_website.id).filter(yxtk_website.id == id).one()
            return not result[0] == None
        except Exception, e:
            print 'Error in judge id exist in yxtk_website:', e
            return False

    # typeid存在
    def yxtkwebsite_typeidexist(self, typeid):
        try:
            session = DBSession()
            result = session.query(yxtk_website.id).filter(yxtk_website.typeid == typeid).one()
            return not result[0] == None
        except Exception, e:
            print 'Error in judge typeid exist in yxtk_website:', e
            return False

    # id获取url
    def yxtkwebsite_getidbyurl(self, url):
        try:
            session = DBSession()
            result = session.query(yxtk_website.id).filter(yxtk_website.url == url).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error in get id by url on yxtk_website:', e
            return None

    # id获取信息
    def yxtkwebsite_getwebsiteinfobyid(self, id):
        try:
            session = DBSession()
            result = session.query(yxtk_website.id, yxtk_website.url, yxtk_website.typeid).filter(
                xctmr_Website.url == id).one()
            session.close()
            return [result[0], result[1]]
        except Exception, e:
            print 'Error in get id by url on yxtk_website:', e
            return []

    # url获取id
    def yxtkwebsite_geturlbyid(self, id):
        try:
            session = DBSession()
            result = session.query(yxtk_website.url).filter(yxtk_website.id == id).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error in get url by id on yxtk_website:', e
            return None

    '''yxtk_picture表操作'''

    # 插入
    def yxtkpicture_insert(self, localaddr, urlid, sid):
        try:
            session = DBSession()
            picture = yxtk_picture(localaddr=localaddr, urlid=urlid, sourcetableid=sid)
            session.add(picture)
            session.commit()
            session.close()
        except Exception, e:
            print 'Error in insert into yxtk_picture:', e
            return False
        return True

    # 查询
    # id exist
    def yxtkpicture_idexist(self, id):
        try:
            session = DBSession()
            result = session.query(yxtk_picture.id).filter(yxtk_picture.id == id).one()
            session.close()
            return not result[0] == None
        except Exception, e:
            print 'Error on yxtk_picture id exist:', e
            return False

    # localaddr exist
    def yxtkpicture_localaddrexist(self, localaddr):
        try:
            session = DBSession()
            result = session.query(yxtk_picture.id).filter(yxtk_picture.localaddr == localaddr).one()
            session.close()
            return not result[0] == None
        except Exception, e:
            print 'Error on yxtk_picture localaddr exist:', e
            return False

    # 查询
    def yxtkpicture_getidbylocaladdr(self, localaddr):
        try:
            session = DBSession()
            result = session.query(yxtk_picture.id).filter(yxtk_picture.localaddr == localaddr).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error on yxtkpicture_getidbylocaladdr:', e
            return None

    def yxtkpicture_getlocaladdrbyid(self, id):
        try:
            session = DBSession()
            result = session.query(yxtk_picture.localaddr).filter(yxtk_picture.id == id).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error on yxtkrpicture_getlocaladdrbyid:', e
            return None

    def yxtkpicture_getwtablenamebyid(self, id):
        try:
            session = DBSession()
            result = session.query(yxtk_picture.sourcetableid).filter(yxtk_picture.id == id).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error on yxtkpicture_getwtablenamebyid:', e
            return None

    def yxtkpicture_getwtablenamebylocaladdr(self, localaddr):
        try:
            session = DBSession()
            result = session.query(yxtk_picture.sourcetableid).filter(yxtk_picture.localaddr == localaddr).one()
            session.close()
            return result[0]
        except Exception, e:
            print 'Error on yxtkpicture_getwtablenamebylocaladdr:', e
            return None

if __name__ == "__main__":
    session = DBSession()
    tablename = "xctmr_website"
    sqlstr = text("select * from " + tablename + " where id =:id")
    result = session.execute(sqlstr, params={'id': 1535})
    for row in result:
        print [x for x in row]
