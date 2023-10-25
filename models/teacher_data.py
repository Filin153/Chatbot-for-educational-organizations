import sqlalchemy

from loader import Base
import datetime


class TeacherData(Base):
    __tablename__ = "teachers_data"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    password = sqlalchemy.Column(sqlalchemy.String, unique=True)
    full_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    made_date = sqlalchemy.Column(
        sqlalchemy.DATE, default=datetime.datetime.now()
    )
