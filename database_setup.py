from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import flask.ext.login as flask_login

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    name = Column(String)
    email = Column(String, primary_key=True)
    gender = Column(String)
    nationality = Column(String)
    hometown = Column(String)
    hashed_password = Column(String)
