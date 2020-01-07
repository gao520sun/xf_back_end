
from sqlalchemy import Column, String, create_engine, Integer
from xfApp.xfMysql.createEngine import Base

# 定义User对象:
class Website(Base):
    # 表的名字:
    __tablename__ = 'website'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    url = Column(String(20))




