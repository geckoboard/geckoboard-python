from connection import Connection
from datasets_client import DatasetsClient

class Client():
  def __init__(self, api_key):
    connection = Connection(api_key)

    self.__connection = connection
    self.datasets = DatasetsClient(connection)

  def ping(self):
    request = self.__connection.get('/')

    return True
