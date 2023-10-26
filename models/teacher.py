import sqlalchemy

from loader import Base
import datetime


class Teacher(Base):
    __tablename__ = "teachers"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    tg_user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    user_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    full_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    made_date = sqlalchemy.Column(
        sqlalchemy.DATE, default=datetime.datetime.now()
    )
