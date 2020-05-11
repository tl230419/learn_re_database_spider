from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Numeric
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:123456@localhost:3306/itmovie?charset=utf8", echo=True)
if engine:
    print("connect ok")
else:
    print("connect failed")

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Movie(Base):
    __tablename__ = "t_movie"

    id = Column(Integer, primary_key=True)
    img_url = Column(String(255))
    title = Column(String(100))
    download_url = Column(String(100))

    def __str__(self):
        return "User(id={},name={},icon={},url={})".format(self.id, self.img_url, self.title, self.download_url)