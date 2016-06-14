#coding:utf8
#file is used to manu database
#time = 2016.04.24
#  #author = 'tanghan'
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
'''医学图片分类别有'''

#数据库基类
Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:tanghan940428@localhost:3306/medicalpic')
#定义数据库对象
class Picture(Base):
    #表名
    __tablename__ = 'Picture'

    local_addr = Column(String(255), nullable=False, primary_key=True)
    net_addr = Column(String(255), nullable=False)
    artical_url = Column(String(255), nullable = False)

    def __init__(self, local_addr, net_addr, artical_url):
        self.local_addr = local_addr
        self.net_addr = net_addr
        self.artical_url = artical_url

class Brain(Base):
    #表明
    __tablename__ = 'Brain'


    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(128), ForeignKey(Picture.local_addr))
    net_addr = Column(String(128), nullable=False)

    def __init__(self, local_addr, net_addr):
        self.local_addr = local_addr
        self.net_addr = net_addr

class Lung_CR(Base):
    # 表明
    __tablename__ = 'Lung_CR'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), ForeignKey(Picture.local_addr))
    net_addr = Column(String(255), nullable=False)

    def __init__(self, local_addr, net_addr):
        self.local_addr = local_addr
        self.net_addr = net_addr

class Lung_CT(Base):
    # 表明
    __tablename__ = 'Lung_CT'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), ForeignKey(Picture.local_addr))
    net_addr = Column(String(255), nullable=False)

    def __init__(self, local_addr, net_addr):
        self.local_addr = local_addr
        self.net_addr = net_addr

class Iris(Base):
    # 表明
    __tablename__ = 'Iris'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), ForeignKey(Picture.local_addr))
    net_addr = Column(String(255), nullable=False)

    def __init__(self, local_addr, net_addr):
        self.local_addr = local_addr
        self.net_addr = net_addr

class Abdomen(Base):
    # 表明
    __tablename__ = 'Abdomen'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), ForeignKey(Picture.local_addr))
    net_addr = Column(String(255), nullable=False)

    def __init__(self, local_addr, net_addr):
        self.local_addr = local_addr
        self.net_addr = net_addr

#初始化数据库连接
DBSession = sessionmaker(bind=engine)
