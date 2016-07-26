#coding:utf8
from Database import *
from sqlalchemy.sql import select

'''picture表操作'''
#插入
#表数据插入
def picture_insert(pid, sourcetableid, hashstr):
    try:
        picture_table=Table("picture", metadata, autoload=True)
        insert = picture_table.insert()
        dict = {'pid': pid, 'sourcetableid': sourcetableid, 'hashstr': hashstr}
        conn.execute(insert, **dict)
    except Exception, e:
        print 'picture insert error:', e
        return False
#表数据查询
def picture_getinfo(hashstr):
    try:
        sel = select([picture]).where([picture.hashstr == hashstr])
        print sel
    except Exception, e:
        print 'Select error in picture: ', e
        return False


if __name__ == "__main__":
    picture_getinfo('1234123412341234123412341234123412341234123412341234123412341234')
