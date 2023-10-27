import sqlalchemy

from loader import Base
import datetime


class TrainingDepartamentData(Base):
    __tablename__ = "training_departament_data"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    password = sqlalchemy.Column(sqlalchemy.String)
    made_date = sqlalchemy.Column(
        sqlalchemy.DATE, default=datetime.datetime.now()
    )
