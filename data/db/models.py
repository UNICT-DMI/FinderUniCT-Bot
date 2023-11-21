"""
    Definition of database tables
"""
import hashlib

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base

# pylint: disable=too-few-public-methods
class User(Base):
    """
        User table, maps the following fields:
        - id (int): primary key, autoincrement
        - email (str): hexdigest of salted user's email hashed with sha256
        - chat_id (int): id of the chat the user is in
    """
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(64), unique=True)
    chat_id: Mapped[int] = mapped_column(unique=True)

    def __init__(self, email: str, chat_id: int):
        self.email = hashlib.sha256(email.encode()).hexdigest()
        self.chat_id = chat_id
