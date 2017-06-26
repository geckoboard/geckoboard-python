import requests

class Client():
  def __init__(self, api_key):
    self.api_key = api_key

  def ping(self):
    r = requests.get('https://api.geckoboard.com/', auth=(self.api_key, ''))

    if r.status_code < 200 or r.status_code >= 300:
      r.raise_for_status()

    return True
