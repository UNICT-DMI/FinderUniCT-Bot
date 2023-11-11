"""
    Initialize the database engine + base model
"""
# pylint: disable=too-few-public-methods
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db.sqlite3")
engine = create_engine("sqlite:///" + db_path)
class Base(DeclarativeBase):
    pass

# pylint: disable=wrong-import-position
from .models import User

Base.metadata.create_all(engine)
