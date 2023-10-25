import sqlalchemy

from loader import Base
import datetime


class User(Base):
    __tablename__ = "users"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    tg_user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    user_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    group = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    is_study = sqlalchemy.Column(sqlalchemy.BOOLEAN, default=1)
    made_date = sqlalchemy.Column(sqlalchemy.DATE, default=datetime.datetime.now())
