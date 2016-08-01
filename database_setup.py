from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, PrimaryKeyConstraint, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('photo_id', Integer, ForeignKey('photo.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Person(Base):
    __tablename__ = 'person'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    gender = Column(String)
    nationality = Column(String)
    hometown = Column(String)
    hashed_password = Column(String)
    photos = relationship('Photo', backref='author')
    comments = relationship('Comment', backref='commenter')


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey('person.id'))
    url = Column(String)
    tags = relationship('Tag', secondary=association_table, back_populates='photos')
    comments =  relationship('Comment', backref='Photo')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer, ForeignKey('photo.id'))
    commenter_id =Column(Integer, ForeignKey('person.id'))
    comment_string = Column(String)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    photos = relationship('Photo', secondary=association_table, back_populates='tags')