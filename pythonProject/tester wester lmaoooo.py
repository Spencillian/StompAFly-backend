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



#add_post('test', 133332, 0o317)

import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)

