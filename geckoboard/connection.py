"""
Private class: Connection

A utility wrapper for containing API details and exposing
simplified API access methods.
"""

from geckoboard import api
from geckoboard import response_handler


class Connection:
    def __init__(self, api_key, timeout=None):
        self.api_key = api_key
        self.timeout = timeout

    def get(self, path):
        response = api.get(path, self.api_key, self.timeout)
        return self.handle_response(response)

    def delete(self, path):
        response = api.delete(path, self.api_key, self.timeout)
        return self.handle_response(response)

    def post(self, path, body):
        response = api.post(path, body, self.api_key, self.timeout)
        return self.handle_response(response)

    def put(self, path, body):
        response = api.put(path, body, self.api_key, self.timeout)
        return self.handle_response(response)

    @staticmethod
    def handle_response(response):
        if response.status_code < 200 or response.status_code >= 300:
            raise Exception(response_handler.get_error_message(response))

        return response
