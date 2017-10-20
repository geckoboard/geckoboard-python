"""
Private: requests response utility methods
"""


def get_error_message(response):
    return response.json()['error']['message']
