import api
import json

class Connection():
  def __init__(self, api_key):
    self.api_key = api_key

  def get(self, path):
    response = api.get(path, self.api_key)
    return self.handle_response(response)

  def delete(self, path):
    response = api.delete(path, self.api_key)
    return self.handle_response(response)

  def post(self, path, body):
    response = api.post(path, body, self.api_key)
    return self.handle_response(response)

  def put(self, path, body):
    response = api.put(path, body, self.api_key)
    return self.handle_response(response)

  def handle_response(self, response):
    if response.status_code < 200 or response.status_code >= 300:
      error_message = response.json()['error']['message']

      raise Exception(error_message)

    return response
