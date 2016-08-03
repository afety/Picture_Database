# coding:utf8
# file is used to manu database
# time = 2016.04.24
#  #author = 'tanghan'
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''医学图片分类别有'''

# 数据库基类
engine = create_engine('mysql+mysqldb://root:tanghan@localhost:3306/medicalpic')
Base = declarative_base(bind=engine)
#总表， 供hash值比对
class picture(Base):
    __tablename__ = 'picture'

    id = Column(Integer, autoincrement=True, primary_key=True)
    pid = Column(Integer, nullable=False)
    sourcetableid = Column(Integer, ForeignKey('sourcetables.id'), nullable=False)
    hashstr = Column(String(64), nullable=False)

    def __init__(self, pid, sourcetableid, hashstr):
        self.pid = pid
        self.sourcetableid = sourcetableid
        self.hashstr = hashstr

#记录图片存储表
class sourcetables(Base):
    __tablename__ = 'sourcetables'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tablename = Column(String(255), nullable=False, unique=True)

    def __init__(self, tablename):
        self.tablename = tablename


#xctmr文章url存储表
class xctmr_Website(Base):
    __tablename__ = "xctmr_website"

    id = Column(Integer, autoincrement=True, primary_key=True)
    url = Column(String(255), unique=True)
    typeid = Column(Integer, ForeignKey('type.id'))

    def __init__(self, url, typeid):
        self.url = url
        self.typeid = typeid

#xctmr图片存储表
class xctmr_picture(Base):
    __tablename__ = "xctmr_picture"

    id = Column(Integer, autoincrement=True, primary_key=True)
    localaddr = Column(String(255), nullable=False, unique=True)
    urlid = Column(String(255), nullable=True)
    sourcetableid = Column(String(255), nullable=True)


    def __init__(self, localaddr, urlid, sourcetableid):
        self.localaddr = localaddr
        self.urlid = urlid
        self.sourcetableid = sourcetableid

'''类型表'''
class typetable(Base):
    __tablename__ = "type"

    id = Column(Integer, autoincrement=True, primary_key=True)
    typename = Column(String(255), nullable=False, unique=True)

    def __init__(self, typename):
        self.typename = typename

'''yxtk_website 表'''
class yxtk_website(Base):
    __tablename__ = 'yxtk_website'

    id = Column(Integer, autoincrement=True, primary_key=True)
    url = Column(String(255), unique=True)
    typeid = Column(Integer, ForeignKey('type.id'))

    def __init__(self, url, typeid):
        self.url = url
        self.typeid = typeid

'''yxtk_picture 表'''
class yxtk_picture(Base):
    __tablename__ = "yxtk_picture"

    id = Column(Integer, autoincrement=True, primary_key=True)
    localaddr = Column(String(255), nullable=False, unique=True)
    urlid = Column(String(255), nullable=True)
    sourcetableid = Column(String(255), nullable=True)

    def __init__(self, localaddr, urlid, sourcetableid):
        self.localaddr = localaddr
        self.urlid = urlid
        self.sourcetableid = sourcetableid

DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
