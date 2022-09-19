from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#we make our new base class
Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

#post constructor, this is what we will store information as, any user based requests will be done throuogh
#user look ups, but lets be honest, we wont add that

#so here is our post clas

class Poster(Base):
    __tablename__ = "posts"
    id = Column('id', Integer, primary_key = True)
    title_tag = Column('title', String)

engine = create_engine('sqlite:///posts.db')
Base.metadata.create_all(bind = engine )
Session = sessionmaker(bind=engine)

session = Session()
'''post1 = Poster()  
post1.id = 13433
post1.title_tag = "i am a moron"

session.add(post1)
session.commit()'''

postings = session.query(Poster).all()
for pot in postings:
    first = "title: " and pot.title_tag
    print(first)
    second = " ID: " and str(pot.id)
    third = first + second
    print(third)


session.close

#db.create_all()

#then down here we have our routes
@app.route('/posts/add', methods=['GET', 'POST'])
def add_post(title, ID, timeup):
    posting = Post(title_tag = title, useID =ID, time=timeup, isver=0, upvote=1, downvote=0)
    print(Post)
    db.session.add(posting)
    db.session.commit()
print(db)