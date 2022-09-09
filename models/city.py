#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
import os

class City(BaseModel, Base if (os.getenv('HBNB_TYPE_STORAGE') == 'db') else object):
    """ The city class, contains state ID and name """

    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        from models.base_model import Base
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(128), ForeignKey("states.id"), nullable=False)
    else:
        state_id = ""
        name = ""
