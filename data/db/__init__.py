"""
    Initialize the database engine + base model
"""
# pylint: disable=too-few-public-methods
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine("sqlite://db.sqlite3")
class Base(DeclarativeBase):
    pass
