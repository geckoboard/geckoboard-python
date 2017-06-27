from mock import Mock, patch
from nose.tools import assert_equal
import geckoboard

API_KEY = 'ABC'
ERROR_MESSAGE = 'Whoops!'
DATASET_ID = 'Sales.by_day'
FIELDS = {}
ITEMS = [{ 'amount' : 123 }]

@patch('geckoboard.api.put')
def test_makes_api_call(mock_api_put):
  mock_api_put.return_value = Mock(status_code=200)
  client = geckoboard.client(API_KEY)
  dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

  dataset.put(ITEMS)

  mock_api_put.assert_called_with(
    '/datasets/' + DATASET_ID + '/data',
    { 'data': ITEMS },
    API_KEY
  )

@patch('geckoboard.api.put')
def test_returns_true_on_success(mock_api_put):
  mock_api_put.return_value = Mock(status_code=200)
  client = geckoboard.client(API_KEY)
  dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

  response = dataset.put(ITEMS)

  assert_equal(response, True)

@patch('geckoboard.api.put')
@patch('geckoboard.response_handler.get_error_message')
def test_rethrows_api_error(mock_get_error_message, mock_api_put):
  # Make the initial put pass so we can create the dataset
  mock_api_put.return_value = Mock(status_code=200)
  client = geckoboard.client(API_KEY)
  dataset = client.datasets.find_or_create(DATASET_ID, FIELDS)

  # Now make it fail so we can test the error response
  mock_response = Mock(status_code=401)
  mock_api_put.return_value = mock_response
  mock_get_error_message.return_value = ERROR_MESSAGE

  try:
    dataset.put(ITEMS)
  except Exception as err:
    mock_get_error_message.assert_called_with(mock_response)
    assert_equal(err.message, ERROR_MESSAGE)
