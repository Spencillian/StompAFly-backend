from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

#we make our new base class
Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

#post constructor, this is what we will store information as, any user based requests will be done throuogh
#user look ups, but lets be honest, we wont add that

#so here is our post class
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



#db.create_all()

#then down here we have our routes
@app.route('/posts/add', methods=['GET', 'POST'])
def add_post(title, ID, timeup):
    posting = Post(title_tag = title, useID =ID, time=timeup, isver=0, upvote=1, downvote=0)
    print(Post)
    db.session.add(posting)
    db.session.commit()
