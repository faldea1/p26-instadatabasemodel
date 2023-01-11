import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

##class: Here we define columns for each table. Notice that each column is also a normal Python instance attribute.
## nullable = False significa que es campo obligatorio.



##TABLAS PREDETERMINADAS -> BOILERPLATE:


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



##TABLAS ADICIONALES:


##Personas que usan la App.
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False) 
    second_name = Column(String(150), nullable=True)
    last_name = Column(String(150), nullable=False)
    profile_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    signup_date = Column(String(150), nullable=False)


##Donde personas agregan fotos/videos a la App.
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date_time = Column(String(150), nullable=False)


##Tabla separada donde se guardan las fotos/videos en un post.
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey('post.id'))
    media_file = Column (String(200), nullable=False)
    position_file = Column (Integer, nullable=False)
    relation_post = relationship(Post)


##Tabla para capturar los "seguidos" de un usuario.
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    following_user_id = Column(Integer, ForeignKey('user.id'))
    followed_user_id = Column(Integer, ForeignKey('user.id'))
    relation_user = relationship(User)


##Tabla de notificación -> etiquetar usuario/s en post de foto
class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    media_id = Column(Integer, ForeignKey('media.id'))
    user_id = Column (Integer, ForeignKey('user.id'))
    relation_media = relationship(Media)
    relation_user = relationship(User)


##Tabla de comentarios -> opción de que otros users comenten post.
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    date_time = Column(String(150), nullable=False)
    comment_text = Column(String(300), nullable=True)
    relation_user = relationship(User)
    relation_post = relationship(Post)
    

##Tabla de likes -> booleano.
class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    relation_user = relationship(User)
    relation_post = relationship(Post)



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
