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
engine = create_engine('mysql+mysqldb://root:tanghan@localhost:3306/Disease_Pictures')
#定义数据库对象
class Heading(Base):
    #表明
    __tablename__ = 'Heading'


    id = Column(Integer,autoincrement=True,primary_key=True)
    local_addr = Column(String(255),nullable=False)
    net_addr = Column(String(255),nullable=False)

class Lung(Base):
    # 表明
    __tablename__ = 'Lung'

    id = Column(Integer, autoincrement=True, primary_key=True)
    local_addr = Column(String(255), nullable=False)
    net_addr = Column(String(255), nullable=False)

class Pupil(Base):
    # 表明
    __tablename__ = 'Pupil'

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
