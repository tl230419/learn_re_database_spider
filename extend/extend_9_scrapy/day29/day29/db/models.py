from sqlalchemy import Column, String, create_engine
from sqlalchemy.dialects.mssql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata

class Movie(Base):
    __tablename__ = 'movie'

    id = Column(INTEGER, primary_key=True)
    name = Column(String(100))
    icon = Column(String(100))
    url = Column(String(100))

engine = create_engine("mysql://root:123456@localhost:3306/test?charset=utf8", echo=True)

Session = sessionmaker(bind=engine)