from datetime import datetime
from sqlalchemy.orm import Mapped
from .. import Base


class User(Base):
    __tablename__ = "users"

    date: Mapped[datetime]
    username: Mapped[str]
    password: Mapped[str]
    fav_word: Mapped[str]