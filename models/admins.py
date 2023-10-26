import sqlalchemy

from loader import Base
import datetime


class Admin(Base):
    __tablename__ = "admins"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    full_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    tg_user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, nullable=False)
