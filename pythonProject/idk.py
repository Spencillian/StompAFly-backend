from flask import Flask

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

#we make our new base class
Base = declarative_base()

class Post(Base):
    #every post is going to have a image, a title - aka location, time, isverfied boolean
    __tablename__ = "storage"
    title_tag = Column(String, nullable = False)
    useID = Column(Integer, primary_key = True, nullable = False)
    time = Column(Integer, nullable = False)
    #what type do images save as??
    #imgsave = Column(, nullable = False)
    isver = Column(Integer, nullable = False)
    upvote = Column(Integer, nullable = False)
    downvote = Column(Integer, nullable = False)




