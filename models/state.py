#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.city import City

class State(BaseModel, Base if (os.getenv('HBNB_TYPE_STORAGE') == 'db') else object): 
    """ State class """
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities =  relationship("City", cascade='all, delete, delete-orphan', backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """" getter attribute cities that returns the list of City instances"""
            from models import storage
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
