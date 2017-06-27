from mock import Mock, patch
from nose.tools import assert_equal, assert_true
import geckoboard
from geckoboard.dataset import Dataset

API_KEY = 'ABC'
ERROR_MESSAGE = 'Whoops!'
DATASET_ID = 'Sales.by_day'
UNIQUE_BY = 'timestamp'
FIELDS = { 
  'amount': { 'foo': 'bar' },
  'timestamp': { 'foo': 'bar' },
}

@patch('geckoboard.api.put')
def test_makes_api_call(mock_api_put):
  mock_api_put.return_value = Mock(status_code=200)
  client = geckoboard.client(API_KEY)

  client.datasets.find_or_create(DATASET_ID, FIELDS)

  mock_api_put.assert_called_with(
    '/datasets/' + DATASET_ID, 
    { 'fields': FIELDS }, 
    API_KEY
  )

@patch('geckoboard.api.put')
def test_handles_unique_by(mock_api_put):
  mock_api_put.return_value = Mock(status_code=200)
  client = geckoboard.client(API_KEY)

  client.datasets.find_or_create(DATASET_ID, FIELDS, UNIQUE_BY)

  mock_api_put.assert_called_with(
    '/datasets/' + DATASET_ID, 
    { 'fields': FIELDS, 'unique_by': UNIQUE_BY }, 
    API_KEY
  )

@patch('geckoboard.api.put')
def test_returns_dataset(mock_api_put):
  mock_api_put.return_value = Mock(status_code=200)
  client = geckoboard.client(API_KEY)

  dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

  assert_true(isinstance(dataset, Dataset))

@patch('geckoboard.api.put')
@patch('geckoboard.response_handler.get_error_message')
def test_rethrows_api_error(mock_get_error_message, mock_api_put):
  mock_response = Mock(status_code=401)
  mock_api_put.return_value = mock_response
  mock_get_error_message.return_value = ERROR_MESSAGE
  client = geckoboard.client(API_KEY)

  try:
    client.datasets.find_or_create(DATASET_ID, FIELDS)
  except Exception as err:
    mock_get_error_message.assert_called_with(mock_response)
    assert_equal(err.message, ERROR_MESSAGE)