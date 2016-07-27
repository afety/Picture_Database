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
    url = Column(Integer, unique=True)

    def __init__(self, url):
        self.url = url

#xctmr图片存储表
class xctmr_picture(Base):
    __tablename__ = "xctmr_picture"

    id = Column(Integer, autoincrement=True, primary_key=True)
    localaddr = Column(String(255), nullable=False, unique=True)
    urlid = Column(String(255), nullable=True)

    def __init__(self, localaddr, urlid):
        self.localaddr = localaddr
        self.urlid = urlid

DBSession = sessionmaker()
Base.metadata.create_all(engine)