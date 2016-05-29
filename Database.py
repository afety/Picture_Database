#coding:utf8
#file is used to manu database
#time = 2016.04.24
#  #author = 'tanghan'

from sqlalchemy import Column, String, create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''医学图片分类别有'''

#数据库基类
Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:tanghan@localhost:3306/medicalpic')
#定义数据库对象
class Brain(Base):
    #表明
    __tablename__ = 'Brain'


    id = Column(Integer,autoincrement=True,primary_key=True)
    local_addr = Column(String(128),nullable=False)
    net_addr = Column(String(128),nullable=False)

class Lung_CR(Base):
    # 表明
    __tablename__ = 'Lung_CR'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), nullable=False)
    net_addr = Column(String(255), nullable=False)


class Lung_CT(Base):
    # 表明
    __tablename__ = 'Lung_CT'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), nullable=False)
    net_addr = Column(String(255), nullable=False)


class Iris(Base):
    # 表明
    __tablename__ = 'Iris'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), nullable=False)
    net_addr = Column(String(255), nullable=False)

class Abdomen(Base):
    # 表明
    __tablename__ = 'Abdomen'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), nullable=False)
    net_addr = Column(String(255), nullable=False)



#初始化数据库连接
DBSession = sessionmaker(bind=engine)
