from idk import db
from idk import add_post
from idk import Post
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base, relationship
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd

for m in session.query(model).all():
    print [getattr(m, x.__str__().split('.')[1]) for x in model.__table__.columns]
    # additional code


#add_post('test', 132, 0o317)

