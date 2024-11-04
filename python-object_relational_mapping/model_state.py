#!/usr/bin/python3
"""
Defines a State class and an instance of Base using SQLAlchemy ORM.
"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Crear instancia de Base para declarar modelos
Base = declarative_base()

class State(Base):
    """
    State class linked to the 'states' table in the MySQL database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
