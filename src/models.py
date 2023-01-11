import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

##class: Here we define columns for each table. Notice that each column is also a normal Python instance attribute


##tablas predeterminadas -> boilerplate:

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


##tablas adicionales:

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)


class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)


class Follower(User):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)


class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)


class Publicity(Base):
    __tablename__ = 'publicity'
    id = Column(Integer, primary_key=True)


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)









## Qué es lo que sigue abajo del boilerplate ¿? preguntar.


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
