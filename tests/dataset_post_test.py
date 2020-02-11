from mock import Mock, patch
from nose.tools import assert_equal
import geckoboard

API_KEY = 'ABC'
ERROR_MESSAGE = 'Whoops!'
DATASET_ID = 'Sales.by_day'
DELETE_BY = 'amount'
UNIQUE_BY = 'timestamp'
ITEMS = [{'amount': 123}]
FIELDS = {
    'amount': {'foo': 'bar'},
    'timestamp': {'foo': 'bar'},
}
TIMEOUT = 50


@patch('geckoboard.api.put')
@patch('geckoboard.api.post')
def test_makes_api_call(mock_api_post, mock_api_put):
    mock_api_put.return_value = Mock(status_code=200)
    mock_api_post.return_value = Mock(status_code=200)
    client = geckoboard.client(API_KEY, timeout=TIMEOUT)
    dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

    dataset.post(ITEMS)

    mock_api_post.assert_called_with(
        '/datasets/' + DATASET_ID + '/data',
        {'data': ITEMS},
        API_KEY,
        TIMEOUT
    )


@patch('geckoboard.api.put')
@patch('geckoboard.api.post')
def test_handles_delete_by(mock_api_post, mock_api_put):
    mock_api_put.return_value = Mock(status_code=200)
    mock_api_post.return_value = Mock(status_code=200)
    client = geckoboard.client(API_KEY, timeout=TIMEOUT)
    dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

    dataset.post(ITEMS, DELETE_BY)

    mock_api_post.assert_called_with(
        '/datasets/' + DATASET_ID + '/data',
        {'data': ITEMS, 'delete_by': DELETE_BY},
        API_KEY,
        TIMEOUT
    )


@patch('geckoboard.api.put')
@patch('geckoboard.api.post')
def test_returns_true_on_success(mock_api_post, mock_api_put):
    mock_api_put.return_value = Mock(status_code=200)
    mock_api_post.return_value = Mock(status_code=200)
    client = geckoboard.client(API_KEY)
    dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

    response = dataset.post(ITEMS)

    assert_equal(response, True)


@patch('geckoboard.api.put')
@patch('geckoboard.api.post')
@patch('geckoboard.response_handler.get_error_message')
def test_rethrows_api_error(mock_get_error_message, mock_api_post, mock_api_put):
    mock_response = Mock(status_code=401)
    mock_api_put.return_value = Mock(status_code=200)
    mock_api_post.return_value = mock_response
    mock_get_error_message.return_value = ERROR_MESSAGE
    client = geckoboard.client(API_KEY)
    dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

    try:
        dataset.post(ITEMS)
    except Exception as err:
        mock_get_error_message.assert_called_with(mock_response)
        assert_equal(err.message, ERROR_MESSAGE)
