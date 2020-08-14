#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """Class to create table Places"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',
                               backref='place',
                               cascade='all, delete')

    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with 'place_id'
            equals to the current 'Place.id'"""
            from models.review import Review
            from models import storage
            list_reviews = []
            all_reviews = storage.all(Review)
            for value in all_reviews.values():
                if value.place_id == self.id:
                    list_reviews.append(value)
            return list_reviews
