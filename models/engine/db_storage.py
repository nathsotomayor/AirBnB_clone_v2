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
        """Objects that depending of the class name"""
        all_obj_cls = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls is None:
            obj_query = self.__session.query(State, City, User,
                                             Place, Review, Amenity).all()

            for obj in obj_query:
                key_obj = ("{}.{}".format(obj.__class__.__name__, obj.id))
                all_obj_cls.update({key_obj: obj})
            return all_obj_cls
        else:
            if cls in classes:
                obj_query = self.__session.query(cls).all()
                for obj in obj_query:
                    key_obj = ("{}.{}".format(obj.__class__.__name__, obj.id))
                    all_obj_cls.update({key_obj: obj})
                return all_obj_cls
            else:
                return {}

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
