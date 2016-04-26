#coding:utf8
#file is used to manu database
#time = 2016.04.24
#  #author = 'tanghan'

from sqlalchemy import String,Column,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''医学图片分类别有'''

#数据库基类
Base = declarative_base()

#定义数据库对象




#初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:tanghan@localhost:3306/Disease_Pics')
DBSession = sessionmaker(bind=engine)