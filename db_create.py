#This file is used to create the database and the tables in the database

from sqlalchemy import create_engine
engine = create_engine('sqlite:///curricular.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from models import *
Base.metadata.create_all(engine)