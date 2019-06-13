#-*-coding:utf-8-*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Text,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
engine = create_engine('mysql+mysqldb://root:zlp308@localhost:3306/blog')
print(engine)
Base = declarative_base()
#nullable表示列不为空，index=True表示在该列创建索引
#数据类型：String、Integer、Text、Boolean、SmallInteger、DateTime
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),nullable=False,index=True)
    pwd = Column(String(64),nullable=False)
    email = Column(String(64),nullable=False,index=True)
    articals = relationship('Artical')
    def __repr__(self):
        return "%s(%r)" %(self.__class__.__name__,self.name)

#一对多,用户可以写多篇文章
class Artical(Base):
    __tablename__ = "articals"
    id = Column(Integer,primary_key=True)
    title = Column(String(255),nullable=False,index=True)
    content = Column(Text)
    user_id = Column(Integer,ForeignKey('users.id'))
    auther = relationship('User')
    def __repr__(self):
       return "%s(%r)" %(self.__class__.__name__,self.title)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    user = User(name='zhangsan',pwd='zhangsan',email='zhangsan@163.com')
    session.add(user)
    session.commit()
