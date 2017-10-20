from mock import Mock, patch
from nose.tools import assert_equal
from geckoboard.api import get, put, post, delete

API_HOST = 'https://api.geckoboard.com'
PATH = '/bar'
API_KEY = 'ABC'
BODY = {'foo': 'bar'}
MOCK_RESPONSE = Mock(status_code=200)


@patch('requests.get')
def test_get_makes_network_request(mock_requests_get):
    mock_requests_get.return_value = MOCK_RESPONSE
    response = get(PATH, API_KEY)

    mock_requests_get.assert_called_with(API_HOST + PATH, auth=(API_KEY, ''))
    assert_equal(response, MOCK_RESPONSE)


@patch('requests.put')
def test_put_makes_network_request(mock_requests_put):
    mock_requests_put.return_value = MOCK_RESPONSE
    response = put(PATH, BODY, API_KEY)

    mock_requests_put.assert_called_with(
        API_HOST + PATH, json=BODY, auth=(API_KEY, ''))
    assert_equal(response, MOCK_RESPONSE)


@patch('requests.post')
def test_post_makes_network_request(mock_requests_post):
    mock_requests_post.return_value = MOCK_RESPONSE
    response = post(PATH, BODY, API_KEY)

    mock_requests_post.assert_called_with(
        API_HOST + PATH, json=BODY, auth=(API_KEY, ''))
    assert_equal(response, MOCK_RESPONSE)


@patch('requests.delete')
def test_delete_makes_network_request(mock_requests_delete):
    mock_requests_delete.return_value = MOCK_RESPONSE
    response = delete(PATH, API_KEY)

    mock_requests_delete.assert_called_with(
        API_HOST + PATH, auth=(API_KEY, ''))
    assert_equal(response, MOCK_RESPONSE)
