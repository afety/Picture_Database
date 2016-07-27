#coding:utf8
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
            session = DBSession()
            result = session.query(xctmr_Website.id).filter(xctmr_Website.url == url).fetchone()
            session.close()
            return not result == None
        except Exception, e:
            print 'Error in judge whether url exist:', e
            return False
    #id存在
    def xctmrwebsite_idexist(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.id).filter(xctmr_Website.id == id).fetchone()
            return not result == None
        except Exception,e:
            print 'Error in judge id exist in xctmr_website:', e
            return False
    # typeid存在
    def xctmrwebsite_typeidexist(self, typeid):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.id).filter(xctmr_Website.typeid == typeid).fetchone()
            return not result == None
        except Exception, e:
            print 'Error in judge typeid exist in xctmr_website:', e
            return False


    # id获取url
    def xctmrwebsite_getidbyurl(self, url):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.id).filter(xctmr_Website.url == url).fetchone()
            session.close()
            return result
        except Exception, e:
            print 'Error in get id by url on xctmr_website:', e
            return None
    # id获取信息
    def xctmrwebsite_getwebsiteinfobyid(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.id, xctmr_Website.url, xctmr_Website.typeid).filter(xctmr_Website.url == url).fetchone()
            session.close()
            return result
        except Exception, e:
            print 'Error in get id by url on xctmr_website:', e
            return []
    # url获取id
    def xctmrwebsite_geturlbyid(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_Website.url).filter(xctmr_Website.id == id).fetchone()
            session.close()
            return result
        except Exception, e:
            print 'Error in get url by id on xctmr_website:', e
            return None

    '''xctmr_picture表操作'''
    #插入
    def xctmrpicture_insert(self, localaddr, urlid):
        try:
            session = DBSession()
            xctmrpicture = xctmr_picture(localaddr=localaddr, urlid=urlid)
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
            result = session.query(xctmr_picture.id).filter(xctmr_picture.id == id).fetchone()
            session.close()
            return not result == None
        except Exception, e:
            print 'Error on xctmr_picture id exist:', e
            return False

    # localaddr exist
    def xctmrpicture_localaddrexist(self, localaddr):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.id).filter(xctmr_picture.localaddr == localaddr).fetchone()
            session.close()
            return not result == None
        except Exception, e:
            print 'Error on xctmr_picture localaddr exist:', e
            return False

    # 查询
    def xctmrpicture_getidbylocaladdr(self, localaddr):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.id).filter(xctmr_picture.localaddr == localaddr).fetchone()
            session.close()
            return result
        except Exception, e:
            print 'Error on xctmr_picture localaddr exist:', e
            return None

    def xctmrpicture_getlocaladdrbyid(self, id):
        try:
            session = DBSession()
            result = session.query(xctmr_picture.localaddr).filter(xctmr_picture.id == id).fetchone()
            session.close()
            return result
        except Exception, e:
            print 'Error on xctmr_picture localaddr exist:', e
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
            result = session.query(sourcetables.id).filter(sourcetables.id == id).fetchone()
            session.close()
            return not result == None
        except Exception, e:
            print 'Error in sourcetables_idexist:', e
            return False

    # tablename exist
    def sourcetables_tablenameexist(self, tablename):
        try:
            session = DBSession()
            result = session.query(sourcetables.id).filter(sourcetables.tablename == tablename).fetchone()
            session.close()
            return not result == None
        except Exception, e:
            print 'Error in sourcetables_tablenameexist:', e
            return False

    # get id by tablename
    def sourcetabls_getidbytablename(self, tablename):
        try:
            session = DBSession()
            result = session.query(sourcetables.id).filter(sourcetables.tablename == tablename).fetchone()
            session.close()
            return result
        except Exception, e:
            print 'Error in getidbytablename:', e
            return None

    # get tablename by id
    def sourcetable_gettablenamebyid(self, id):
        try:
            session = DBSession()
            result = session.query(sourcetables.tablename).filter(sourcetables.id == id).fetchone()
            session.close()
            return result
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
            result = session.query(picture.id).filter(picture.id == id).fetchone()
            return not result == None
        except Exception, e:
            print 'Error in picture_idexist:', e
            return False

    # pid exist
    def picture_pidexist(self, pid):
        try:
            session = DBSession()
            result = session.query(picture.id).filter(picture.pid == pid).fetchone()
            return not result == None
        except Exception, e:
            print 'Error in picture_pidexist:', e
            return False

    # sourcetableid exist
    def picture_sourcetableidexist(self, sourcetableid):
        try:
            session = DBSession()
            result = session.query(picture.id).filter(picture.sourcetableid == sourcetableid).fetchone()
            return not result == None
        except Exception, e:
            print 'Error in picture_sourcetableidexist:', e
            return False

    # hashstr exist
    def picture_hashstrexist(self, hashstr):
        try:
            session = DBSession()
            result = session.query(picture.id).filter(picture.hashstr == hashstr).fetchone()
            return not result == None
        except Exception, e:
            print 'Error in picture_hashstrexist:', e
            return False


    # get info by hashstr
    def picture_getinfobyhashstr(self, hashstr):
        try:
            session = DBSession()
            result = session.query(picture.id, picture.pid, picture.sourcetableid, picture.hashstr).filter(picture.hashstr == hashstr).fetchall()
            session.close()
            return result
        except Exception, e:
            print 'Error in picture_getinfobyhashstr:', e
            return []

    # get info by id
    def picture_getinfobyid(self, id):
        try:
            session = DBSession()
            result = session.query(picture.id, picture.pid, picture.sourcetableid, picture.hashstr).filter(picture.id == id).fetchall()
            session.close()
            return result
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
            session = DBSession()
            result = session.query(typetable.id).filter(typetable.typename == typename).fetchone()
            return not result == None
        except Exception, e:
            print 'Error in type_typenameexist:', e
            return False

    # id获取typename
    def type_getidbytypename(self, typename):
        try:
            session = DBSession()
            result = session.query(typetable.id).filter(typetable.typename == typename).fetchone()
            return result
        except Exception, e:
            print 'Error in type_getidbytypename:', e
            return None

    # typename 获取 id
    def type_gettypenamebyid(self, id):
        try:
            session = DBSession()
            result = session.query(typetable.typename).filter(typetable.id == id).fetchone()
            return result
        except Exception, e:
            print 'Error in type_typenameexist:', e
            return None

if __name__ == "__main__":
    dbman = DBMan()
    dbman.xctmrwebsite_insert('123')
