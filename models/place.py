#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import os
from sqlalchemy import metadata, Table

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          "places.id"), nullable=False, primary_key=True),
                      Column('amenity_id', String(60), ForeignKey(
                          "amenities.id"), nullable=False, primary_key=True),
                      )

class Place(BaseModel, Base if (os.getenv('HBNB_TYPE_STORAGE') == 'db') else object):
    """ A place to stay """
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship(
            "Review", cascade='all, delete, delete-orphan', backref="place")
        amenities = relationship(
            "Amenity", secondary=place_amenity, backref="place", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """" getter attribute cities that returns the list of City instances"""
            from models import storage
            review_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.Place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """" getter attribute cities that returns the list of City instances"""
            from models import storage
            amenities_list = []
            all_amenities = storage.all(Amenity)
            for ameniti in all_amenities.values():
                if ameniti.amenity_ids == self.id:
                    amenities_list.append(ameniti)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute"""
            str_obj = obj.__class__.__name__
            if str_obj == "Amenity":
                self.amenity_ids.append(str(obj.id))
