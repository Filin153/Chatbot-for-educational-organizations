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
    text = sqlalchemy.Column(sqlalchemy.String, default='Нет текста')
    photos_name = sqlalchemy.Column(
        sqlalchemy.String, nullable=False, default='Нет фото'
    )
    documents_name = sqlalchemy.Column(
        sqlalchemy.String, nullable=False, default='Нет файлов'
    )
    teacher_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    made_date = sqlalchemy.Column(
        sqlalchemy.DATE, default=datetime.datetime.now()
    )
    edit_date = sqlalchemy.Column(
        sqlalchemy.DATE, default=datetime.datetime.now()
    )
