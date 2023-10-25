import sqlalchemy

from loader import Base
import datetime


class Homework(Base):
    __tablename__ = "homeworks"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    group = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name_lesson = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    files_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    teacher_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    next_lesson = sqlalchemy.Column(sqlalchemy.String)
    made_date = sqlalchemy.Column(
        sqlalchemy.DATE, default=datetime.datetime.now()
    )
    edit_date = sqlalchemy.Column(
        sqlalchemy.DATE, default=datetime.datetime.now()
    )
