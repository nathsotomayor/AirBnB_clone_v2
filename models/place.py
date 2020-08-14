#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True)
                     )


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
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)

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

        @property
        def amenities(self):
            """Returns the list of Amenity instances with 'amenity_ids'
            linked to the Place"""
            from models.amenity import Amenity
            from models import storage
            list_amenities = []
            all_amenities = storage.all(Amenity)
            for value in all_amenities.values():
                if value.place_id == self.id:
                    list_amenities.append(value)
            return list_amenities

        @amenities.setter
        def amenities(self, value):
            """Adds amenity ids to the 'amenity_ids' class attribute"""
            from models import storage
            if type(value) == 'Amenity':
                self.amenity_ids.append(value.id)
