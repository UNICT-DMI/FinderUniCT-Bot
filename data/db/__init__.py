"""
    Initialize the database engine + base model
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db.sqlite3")
engine = create_engine("sqlite:///" + db_path)
Session = sessionmaker(engine)

# pylint: disable=too-few-public-methods
class Base(DeclarativeBase):
    pass

# pylint: disable=wrong-import-position,cyclic-import
from .models import User

Base.metadata.create_all(engine)
