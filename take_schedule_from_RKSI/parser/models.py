from dataclasses import dataclass
from datetime import date, datetime, time

from beanie import Document
from pydantic import BaseModel, Field


class ThemeSource:
    pass


class SourcesReference(BaseModel):
    """SourcesReference model

    Contains accepted contacts

    """

    data: str


class SubjectEntry(BaseModel):
    """SubjectEntry model

    SubjectEntry

    """

    startsat: datetime
    endsat: datetime
    name: str

    removedat: datetime


class Group(Document):
    name: str
    schedule: list[SubjectEntry]
    lastupdate: datetime = Field(default_factory=datetime.now)
    removedat: datetime = None


@dataclass
class RawSubjectEntry:
    starts_at: time = None
    ends_at: time = None
    teacher: str = None
    audience: str = None
    name: str = None
    date: date = None
