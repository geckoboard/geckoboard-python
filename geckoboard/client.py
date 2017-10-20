from geckoboard.connection import Connection
from geckoboard.datasets_client import DatasetsClient


class Client():
    def __init__(self, api_key):
        connection = Connection(api_key)

        self.__connection = connection
        self.datasets = DatasetsClient(connection)

    def ping(self):
        self.__connection.get('/')

        return True
