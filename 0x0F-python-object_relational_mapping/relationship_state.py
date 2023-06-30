#!/usr/bin/python3
"""
Definition of the State class in relationship to City class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base



class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')