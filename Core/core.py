from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session

class TeachersBase(DeclarativeBase):
    pass

class GroupsBase(DeclarativeBase):
    pass

class ParentsBase(DeclarativeBase):
    pass

class SkipsBase(DeclarativeBase):
    pass

class Teachers(TeachersBase):
    __tablename__ = 'teachers'
    t_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(34))
    nickname: Mapped[Optional[str]] = mapped_column(String(34))
    p_id: Mapped[str] = mapped_column(String(34))
    tg_id: Mapped[int] = mapped_column(String(34))

class Groups(GroupsBase):
    __tablename__ = 'groups'
    g_id: Mapped[int] = mapped_column(primary_key=True)
    age: Mapped[str] = mapped_column(String(34))
    name: Mapped[str] = mapped_column(String(34))
    tag: Mapped[str] = mapped_column(String(34))
    users: Mapped[str] = mapped_column(String(34))

class Parents(ParentsBase):
    __tablename__ = 'parents'
    p_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(34))
    tg_id: Mapped[int] = mapped_column(String(34))

class Skips(SkipsBase):
    __tablename__ = 'skips'
    s_id: Mapped[int] = mapped_column(primary_key=True)
    t_id: Mapped[int] = mapped_column(String(34))
    backoffice: Mapped[bool] = mapped_column(String(34))
    date: Mapped[Optional[str]] = mapped_column(String(34))
    warning: Mapped[bool] = mapped_column(String(34))

engine = create_engine('sqlite:///bot_DB.db')

TeachersBase.metadata.create_all(engine)
GroupsBase.metadata.create_all(engine)
ParentsBase.metadata.create_all(engine)
SkipsBase.metadata.create_all(engine)