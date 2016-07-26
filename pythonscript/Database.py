# coding:utf8
# file is used to manu database
# time = 2016.04.24
#  #author = 'tanghan'
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, create_engine, Integer, Table, MetaData

'''医学图片分类别有'''

# 数据库基类
metadata = MetaData()
engine = create_engine('mysql+mysqldb://root:tanghan@localhost:3306/medicalpic')

#总表， 供hash值比对
picture = Table("picture", metadata,
                Column('id', Integer, autoincrement=True, primary_key=True),
                Column('pid', Integer, nullable=False),
                Column('sourcetableid', Integer, ForeignKey('sourcetables.id'), nullable=False),
                Column('hashstr', String(64), nullable=False)
                )

#记录图片存储表
sourcetables = Table("sourcetables", metadata,
                     Column('id', Integer, autoincrement=True, primary_key=True),
                     Column("tablename", String(255), nullable=False, unique=True)
                     )

#xctmr文章url存储表
xctmr_website = Table("xctmr_website", metadata,
                      Column('id', Integer, autoincrement=True),
                      Column('url', Integer, unique=True)
                      )

#xctmr图片存储表
xctmr_picture = Table("xctmr_picture", metadata,
                      Column('id', Integer, autoincrement=True, primary_key=True),
                      Column('localaddr', String(255), nullable=False, unique=True),
                      Column('urlid', String(255), nullable=True)
                      )

metadata.create_all(engine)
# 初始化数据库连接
conn = engine.connect()