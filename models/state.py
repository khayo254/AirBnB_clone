#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
from models.base_model import BaseModel
import mysql.connector

class State(BaseModel):
    """ State class """
    name = ""

    @staticmethod
    def get_initial_state_count():
        """Method to get the initial count of records in the 'states' table"""
        # Establish database connection
        connection = mysql.connector.connect(
            host="hostname",
            user="username",
            password="password",
            database="database_name"
        )

        # Create cursor
        cursor = connection.cursor()

        try:
            # Execute SQL query to get count of records
            cursor.execute("SELECT COUNT(*) FROM states")

            # Fetch initial count
            initial_count = cursor.fetchone()[0]

            return initial_count

        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()


# Example usage:
if __name__ == "__main__":
    initial_count = State.get_initial_state_count()
    print("Initial count of records in 'states' table:", initial_count)
=======
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
>>>>>>> origin
