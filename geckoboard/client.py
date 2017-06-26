from connection import Connection

class Client():
  def __init__(self, api_key):
    self.connection = Connection(api_key)

  def ping(self):
    request = self.connection.get('/')

    if request.status_code < 200 or request.status_code >= 300:
      request.raise_for_status()

    return True
