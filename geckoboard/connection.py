import api

class Connection():
  def __init__(self, api_key):
    self.api_key = api_key

  def get(self, path):
    return api.get(path, self.api_key)

  def delete(self, path):
    return api.delete(path, self.api_key)

  def post(self, path, body):
    return api.post(path, body, self.api_key)

  def put(self, path, body):
    return api.put(path, body, self.api_key)
