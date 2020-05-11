'''
*****************
Date: 2020-05-11
Author: Allen
*****************
'''

from sqlalchemy import create_engine

engine = create_engine("mysql://root:123456@localhost:3306/test?charset=utf8", echo=True)
if engine:
    print("connect ok")
else:
    print("connect failed")


#============
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Numeric

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, default=18)
    high = Column(Numeric(5, 2), default=18)

    def __str__(self):
        return "User(id={},name={},age={},high={})".format(self.id,self.name,self.age,self.high)

user = User(name="张三", age=18, high=170.2)
if user:
    print("create table user OK")
else:
    print("create table user failed")

Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()
user = User(name="张三", age=18, high=170.2)
session.add(user)
session.commit()

users = [
    User(name="张三",age=23,high=181.3),
    User(name="李四",age=24,high=191.3),
    User(name="王五",age=25,high=171.3),
]
session.add_all(users)
session.commit()

# update
session = Session()
user = session.query(User).filter(User.name=="张三").first()
user.name = "阿桑"

session.commit()
#session.close()

# delete
#session.query(User).filter(User.id > 2).delete()
#session.delete(user)
#session.commit()

# query
# ==
session.query(User).filter(User.id==1)
# !=
session.query(User).filter(User.id!=1)
# like
session.query(User).filter(User.name.like("%张%"))
# in
session.query(User).filter(User.id.in_([1,2,3]))
# not in
session.query(User).filter(~User.id.in_([1,2,3]))
# is null
session.query(User).filter(User.age == None)
# is not null
session.query(User).filter(User.age != None)
# and
from sqlalchemy import and_
session.query(User).filter(and_(User.id==1,User.name=='张三'))
# or
from sqlalchemy import or_
session.query(User).filter(or_(User.id==1,User.name=='张三'))
# limit
session.query(User).offset(2).limit(3).all()

# =========
from sqlalchemy import func
def test_func():
    session = Session()

    result = session.query(func.count(User.id)).scalar()
    print("count:", result)
    result = session.query(func.max(User.id)).scalar()
    print(result)
    result = session.query(func.min(User.id)).scalar()
    print(result)
    result = session.query(func.sum(User.id)).scalar()
    print(result)
    result = session.query(func.avg(User.id)).scalar()
    print(result)

    session.close()

test_func()