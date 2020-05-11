# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, Float, ForeignKey, String, TIMESTAMP, Table, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Category(Base):
    __tablename__ = 'category'

    cid = Column(INTEGER(11), primary_key=True)
    cname = Column(String(20))
    cdesc = Column(String(50))


class User(Base):
    __tablename__ = 'user'

    uid = Column(INTEGER(11), primary_key=True)
    name = Column(String(10))
    password = Column(String(20))
    mobile = Column(String(11))



class Order(Base):
    __tablename__ = 'orders'

    oid = Column(INTEGER(11), primary_key=True)
    total = Column(Float(asdecimal=True))
    otime = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    uno = Column(ForeignKey('user.uid'), index=True)

    user = relationship('User')


class Product(Base):
    __tablename__ = 'product'

    pid = Column(INTEGER(11), primary_key=True)
    pname = Column(String(10))
    price = Column(Float(asdecimal=True))
    pdesc = Column(String(50))
    cno = Column(ForeignKey('category.cid'), index=True)

    category = relationship('Category')


t_orderitem = Table(
    'orderitem', metadata,
    Column('ono', ForeignKey('orders.oid'), index=True),
    Column('pno', ForeignKey('product.pid'), index=True),
    Column('num', INTEGER(11)),
    Column('subtotal', Float(asdecimal=True))
)

# engine = create_engine('sqlite:///foo.db')
# # Unix/Mac - 4 initial slashes in total
# engine = create_engine('sqlite:////absolute/path/to/foo.db')
#
# # Windows
# engine = create_engine('sqlite:///C:\\path\\to\\foo.db')
#
# # Windows alternative using raw string
# engine = create_engine(r'sqlite:///C:\path\to\foo.db')