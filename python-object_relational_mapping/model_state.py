#!/usr/bin/python3
"""SQLAlchemy model for the states table."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """State model mapped to the states table."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
