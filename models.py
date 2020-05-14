import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    avatar = Column(String(250), nullable=True)
    password = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=False)
    video = Column(String(250), nullable=True)
    followers = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    likes = relationship('likes', secondary = 'Like_Post')

class Like_Post(Base):
    __tablename__ = 'likes_posts'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    post_id = Column(
        Integer, 
        ForeignKey('posts.id'), 
        primary_key = True)
    like_id = Column(
        Integer, 
        ForeignKey('likes.id'), 
        primary_key = True)


class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    posts = relationship('posts', secondary = 'Like_Post')

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    avatar = Column(String(250), nullable=True)
    posts = relationship('posts', secondary = 'Like_Post')

class Follower_Post(Base):
    __tablename__ = 'followers_posts'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    post_id = Column(
        Integer, 
        ForeignKey('posts.id'), 
        primary_key = True)
    follower_id = Column(
        Integer, 
        ForeignKey('followers.id'), 
        primary_key = True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')