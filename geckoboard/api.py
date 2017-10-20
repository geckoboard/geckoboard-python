"""
Private: api access methods
"""

import requests

API_HOST = 'https://api.geckoboard.com'


def get(path, api_key):
    return requests.get(API_HOST + path, auth=(api_key, ''))


def delete(path, api_key):
    return requests.delete(API_HOST + path, auth=(api_key, ''))


def post(path, body, api_key):
    return requests.post(API_HOST + path, json=body, auth=(api_key, ''))


def put(path, body, api_key):
    return requests.put(API_HOST + path, json=body, auth=(api_key, ''))
