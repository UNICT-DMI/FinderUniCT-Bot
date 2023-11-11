"""
    Definition of database tables
"""
# pylint: disable=too-few-public-methods
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from . import Base

class User(Base):
    """
        User table, maps the following fields:
        - id (int): primary key, autoincrement
        - email (str): hexdigest of salted user's email hashed with sha256
        - salt (str): random string used to salt the user's email (8 bytes)
        - chat_id (int): id of the chat the user is in
    """
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(80))
    salt: Mapped[str] = mapped_column(String(16))
    chat_id: Mapped[int]
