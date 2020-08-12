#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
#from sqlalchemy import Column, Integer, String, ForeignKey
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship


#Base = declarative_base()


class State(BaseModel):
    """ State class """
    name = ""
 #   __tablename__ = 'states'
 #   name = Column(String(128), nullable=False)
 #   cities = relationship("City", back_populates="state",
 #                         cascade="all, delete")
