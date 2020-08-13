#!/usr/bin/python3
"""This module defines a class to manage all in DBStorage engine to connect
and manipulate the databases"""

from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """Creating class for DBStorage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for DBStorage engine"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects of a class """
        obj_dict = {}
        if cls is None:
            type_obj = self.__session.query(User, State, City, Amenity,
                                            Place, Review).all()
            for obj in type_obj:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict.update({key: obj})
        else:
            objects = self.__session.query(cls).all()
            for all_obj in objects:
                key = "{}.{}".format(type(all_obj).__name__, all_obj.id)
                obj_dict.update({key: all_obj})
        return obj_dict

    def new(self, obj):
        """Add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and the
        current database session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
