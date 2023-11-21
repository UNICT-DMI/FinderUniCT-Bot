"""
    Initialize the database engine + base model
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#: Base has to be imported from models to create tables, otherwise no tables
#: will be created since the models don't exist at the time of creation (line 16)
from .models import Base

db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db.sqlite3")
engine = create_engine("sqlite:///" + db_path)
Session = sessionmaker(engine)

Base.metadata.create_all(engine)
