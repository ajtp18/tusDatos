from __future__ import annotations
from sqlalchemy import Column, String, Integer
from database.base import Base


class Detail(Base):
    __tablename__ = "details"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    date = Column(String)
    actors = Column(String)
    defendants = Column(String)
    judicial_process = Column(String)
