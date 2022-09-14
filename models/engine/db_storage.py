#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        """linked to the MySQL database and user created"""
        MySQL_user = os.getenv('HBNB_MYSQL_USER')
        MySQL_password = os.getenv('HBNB_MYSQL_PWD')
        MySQL_host = os.getenv('HBNB_MYSQL_HOST')
        MySQL_database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            MySQL_user, MySQL_password, MySQL_host, MySQL_database),
            pool_pre_ping=True)

        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dict_clases = {"State": State, "City": City, "Place": Place,
                       "Amenity": Amenity, "Review": Review, "User": User}

        dict_all = {}

        if cls is not None:
            value = dict_clases[cls]
            objects = self.__session.query(value).all()
        else:
            for clas, name in dict_clases.items():
                objects.append(self.__session.query(name).all())

        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if '_sa_instance_state' in obj.__dict__:
                del obj.__dict__['_sa_instance_state']
            dict_all[key] = obj

        return dict_all

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        This method:
        - create all tables in the database
        - create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_make = sessionmaker(expire_on_commit=False, bind=self.__engine)
        Session = scoped_session(session_make)
        self.__session = Session()

    def close(self):
        """Close method """
        self.__session.close()
