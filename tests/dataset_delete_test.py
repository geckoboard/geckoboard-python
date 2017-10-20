from mock import Mock, patch
from nose.tools import assert_equal
import geckoboard

API_KEY = 'ABC'
ERROR_MESSAGE = 'Whoops!'
DATASET_ID = 'Sales.by_day'
FIELDS = {}


@patch('geckoboard.api.put')
@patch('geckoboard.api.delete')
def test_makes_api_call(mock_api_delete, mock_api_put):
    mock_api_put.return_value = Mock(status_code=200)
    mock_api_delete.return_value = Mock(status_code=200)
    client = geckoboard.client(API_KEY)
    dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

    dataset.delete()

    mock_api_delete.assert_called_with('/datasets/' + DATASET_ID, API_KEY)


@patch('geckoboard.api.put')
@patch('geckoboard.api.delete')
def test_returns_true_on_success(mock_api_delete, mock_api_put):
    mock_api_put.return_value = Mock(status_code=200)
    mock_api_delete.return_value = Mock(status_code=200)
    client = geckoboard.client(API_KEY)
    dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

    response = dataset.delete()

    assert_equal(response, True)


@patch('geckoboard.api.put')
@patch('geckoboard.api.delete')
@patch('geckoboard.response_handler.get_error_message')
def test_rethrows_api_error(mock_get_error_message, mock_api_delete, mock_api_put):
    mock_response = Mock(status_code=401)
    mock_api_put.return_value = Mock(status_code=200)
    mock_api_delete.return_value = mock_response
    mock_get_error_message.return_value = ERROR_MESSAGE
    client = geckoboard.client(API_KEY)
    dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

    try:
        dataset.delete()
    except Exception as err:
        mock_get_error_message.assert_called_with(mock_response)
        assert_equal(err.message, ERROR_MESSAGE)
