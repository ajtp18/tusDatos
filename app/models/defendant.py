from __future__ import annotations
from sqlalchemy import Column, String, Integer
from database.base import Base

class Defendant(Base):
    __tablename__ = "defendant"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    date = Column(String)
    process_number = Column(String)
    action_infraction = Column(String)
    detail = Column(String)