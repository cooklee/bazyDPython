import psycopg2
from connection_settings import data


def connect(connection_data = None):
    if connection_data is None:
        connection_data = data
    connection = psycopg2.connect(**connection_data)
    connection.autocommit = True
    return connection
