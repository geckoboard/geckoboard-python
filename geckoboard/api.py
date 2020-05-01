"""
Private: api access methods
"""

import requests

API_HOST = 'https://api.geckoboard.com'


def get(path, api_key, timeout=None):
    return requests.get(API_HOST + path, auth=(api_key, ''), timeout=timeout)


def delete(path, api_key, timeout=None):
    return requests.delete(API_HOST + path, auth=(api_key, ''), timeout=timeout)


def post(path, body, api_key, timeout=None):
    return requests.post(API_HOST + path, json=body, auth=(api_key, ''), timeout=timeout)


def put(path, body, api_key, timeout=None):
    return requests.put(API_HOST + path, json=body, auth=(api_key, ''), timeout=timeout)
