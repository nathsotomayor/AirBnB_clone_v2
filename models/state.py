#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete')
    else:
        @property
        def cities(self):
            """Returns the list of City instances with 'state_id'
            equals to the current 'State.id'"""
            from models.city import City
            from models import storage
            list_cities = []
            all_cities = storage.all(City)
            for value in all_cities.values():
                if value.state_id == self.id:
                    list_cities.append(value)
            return list_cities
