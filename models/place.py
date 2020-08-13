#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    place_amenity = Table(
            'place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey(
                'places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey(
                'amenities.id'), primary_key=True, nullable=False))

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 backref='places', viewonly=False)
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
            """Return reviews instance list"""
            from models import storage
            from models.review import Review
            objList = []
            for key, value in storage.all(Review).items():
                objList.append(value)
            return objList

        @property
        def amenities(self):
            """Return amenities instance list"""
            from models import storage
            from models.review import Amenity
            objList = []
            for amenity in storage.all(Amenity):
                if amenity.id in self.amenity_ids:
                    objList.append(value)
            return objList

        @property.setter
        def amenities(self, obj):
            """Return reviews instance list"""
            from models import storage
            from models.review import Amenity
            if type(obj) == Amenity:
                self.amenity_ids.apped(obj.id)
