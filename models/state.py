#!/usr/bin/python3
""" Contains state class to represent a State """

from models.base_model import BaseModel, Base
import models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class: class to represent states of cities"""
    if storage_type == 'db':
    __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """cities list
            """
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id):
                    related_cities.append(city)
            return related_cities
