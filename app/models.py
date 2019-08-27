
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app import db


engine = create_engine('sqlite:///flaskapp.db', echo = True)
Base = declarative_base()


class PersonData(db.Model):
    __tablename__ = 'PersonData'

    id = Column(Integer, primary_key = True)

    username = Column(String(20))
    password = Column(String(20))
    name = Column(String(20))
    email = Column(String(50))
Base.metadata.create_all(engine)