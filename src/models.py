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

    children10 = relationship('Address', back_populates='address_relation_person')


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

    address_relation_person = relationship('Person', back_populates='children10') 



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

    children1 = relationship('Like', back_populates='like_relation_user')
    children3 = relationship('Comment', back_populates='comment_relation_user')
    children6 = relationship('Tag', back_populates='tag_relation_user')
    children7 = relationship('Follower', back_populates='follower_relation_user')
    children9 = relationship('Post', back_populates='post_relation_user')

##Donde personas agregan fotos/videos a la App.
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date_time = Column(String(150), nullable=False)

    children2 = relationship('Like', back_populates='like_relation_post')
    children4 = relationship('Comment', back_populates='comment_relation_post')
    children8 = relationship('Media', back_populates='media_relation_post')

    post_relation_user = relationship('User', back_populates='children9')


##Tabla separada donde se guardan las fotos/videos en un post.
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey('post.id'))
    media_file = Column (String(200), nullable=False)
    position_file = Column (Integer, nullable=False)

    children5 = relationship('Tag', back_populates='tag_relation_media')

    media_relation_post = relationship('Post', back_populates='children8')


##Tabla para capturar los "seguidos" de un usuario.
class Follower(Base):
    __tablename__ = 'follower'
    following_user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    followed_user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

    follower_relation_user = relationship('User', back_populates='children7')


##Tabla de notificación -> etiquetar usuario/s en post de foto
class Tag(Base):
    __tablename__ = 'tag'
    media_id = Column(Integer, ForeignKey('media.id'), primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'), primary_key=True)

    tag_relation_media = relationship('Media', back_populates='children5')
    tag_relation_user = relationship('User', back_populates='children6')


##Tabla de comentarios -> opción de que otros users comenten post.
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    date_time = Column(String(150), nullable=False)
    comment_text = Column(String(300), nullable=True)

    comment_relation_user = relationship('User', back_populates='children3')
    comment_relation_post = relationship('Post', back_populates='children4')

    
##Tabla de likes -> booleano.
class Like(Base):
    __tablename__ = 'like'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)

    like_relation_user = relationship('User', back_populates='children1')
    like_relation_post = relationship('Post', back_populates='children2')



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
