#!/usr/bin/python3
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
