from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

metadata_obj = MetaData()
engine = create_engine('sqlite:///poster.db')

metadata_obj = MetaData()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Post(db.Model):
    #every post is going to have a image, a title - aka location, time, isverfied boolean
    title_tag = db.Column(db.String(60), nullable = False) #max title length 60 char
    useID = db.Column(db.Integer, primary_key = True)
    time = db.Column(db.Integer, nullable = False)
    #what type do images save as??
    #imgsave = Column(, nullable = False)
    isver = db.Column(db.Integer, nullable = False)
    upvote = db.Column(db.Integer, nullable = False)
    downvote = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name

metadata_obj.create_all(engine)