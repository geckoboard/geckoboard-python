from mock import Mock, patch
from nose.tools import assert_equal
import geckoboard

API_KEY = 'ABC'
ERROR_MESSAGE = 'Whoops!'
DATASET_ID = 'Sales.by_day'


@patch('geckoboard.api.delete')
def test_makes_api_call(mock_api_delete):
    mock_api_delete.return_value = Mock(status_code=200)
    client = geckoboard.client(API_KEY)

    client.datasets.delete(DATASET_ID)

    mock_api_delete.assert_called_with('/datasets/' + DATASET_ID, API_KEY)


@patch('geckoboard.api.delete')
def test_returns_true_on_success(mock_api_delete):
    mock_api_delete.return_value = Mock(status_code=200)
    client = geckoboard.client(API_KEY)

    response = client.datasets.delete(DATASET_ID)

    assert_equal(response, True)


@patch('geckoboard.api.delete')
@patch('geckoboard.response_handler.get_error_message')
def test_rethrows_api_error(mock_get_error_message, mock_api_delete):
    mock_response = Mock(status_code=401)
    mock_api_delete.return_value = mock_response
    mock_get_error_message.return_value = ERROR_MESSAGE
    client = geckoboard.client(API_KEY)

    try:
        client.datasets.delete(DATASET_ID)
    except Exception as err:
        mock_get_error_message.assert_called_with(mock_response)
        assert_equal(err.message, ERROR_MESSAGE)
