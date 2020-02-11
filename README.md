# geckoboard-python

A Python client library for [Geckoboard datasets API](https://api-docs.geckoboard.com/).

## Installation

Install the package with pip

```
pip install geckoboard.py
```

## Usage

The latest documentation and user guide can be found on the [Geckoboard developer docs](https://developer.geckoboard.com/hc/en-us/articles/360018322692)

---

## Getting started

Install the python client from PIP

```
pip install geckoboard.py
```

Import the Geckoboard package and create an instance of the client using your API key:

```python
import geckoboard

client = geckoboard.client(API_KEY)
```

**Note:** You can find your API key by logging into the Geckoboard application and visiting the Account section.

## Authentication

Verify that your API key is valid and that you can reach the Geckoboard API with the `ping` method.

```python
client.ping()
```

### Example:

```python
client('good-api-key').ping() # => true
client('bad-api-key').ping() # => raises Exception
```

## Finding or creating a dataset

Find and verify an existing dataset or create a new dataset with the `find_or_create` method. `unique_by` is an optional list of one or more field names whose values will be unique across all your records.

```python
client.datasets.find_or_create(dataset_id, fields, unique_by)
```

### Params:
- `dataset_id` [required] <[str][str-type]>
- `fields` [required] <[dict][dict-type]>
   - `type` [required] <[str][str-type]></li>
   - `name` [required] <[str][str-type]></li>
   - `optional` <[boolean][boolean-type]></li>
- `unique_by` <[list][list-type]>

### Example:

```python
dataset = client.datasets.find_or_create('sales.by_night', {
  'amount': { 'type': 'number', 'name': 'Amount', 'optional': False },
  'timestamp': { 'type': 'datetime', 'name': 'Time' }
}, ['timestamp'])
```

The full list of available field types is described at the top of this page.

## Replacing all data in a dataset

Replace all data in the dataset by calling the `put` method.

```python
dataset.put(items)
```

### Params:

- `items` [required] <[list][list-type]>

### Example:

```python
dataset.put([
  { 'timestamp': '2016-01-01T12:00:00Z', 'amount': 819 },
  { 'timestamp': '2016-01-02T12:00:00Z', 'amount': 409 },
  { 'timestamp': '2016-01-03T12:00:00Z', 'amount': 164 }
])
```

## Appending data to a dataset

Append records to a dataset by calling the `post` method.

Should the number of records in your dataset exceed the limit following a post [old records will be discarded](#record-count-limit).

```python
dataset.post(items, delete_by)
```

### Params:
- `items` [required] <[list][list-type]>
- `delete_by` <[str][str-type]>

### Example:

```python
dataset.post([
  { 'timestamp': '2016-01-03T12:00:00Z', 'amount': 312 },
  { 'timestamp': '2016-01-04T12:00:00Z', 'amount': 665 },
  { 'timestamp': '2016-01-05T12:00:00Z', 'amount': 453 }
], 'timestamp')
```

## Deleting a dataset

Delete the dataset and all data with the given id.

```python
client.datasets.delete(dataset_id)
```

### Params:
- `dataset_id` [required] <[str][str-type]>

### Example:

```python
client.datasets.delete('sales.gross') # => true
```

You can also delete a dataset by calling the `delete` method on a dataset.

```python
dataset = client.datasets.find_or_create(...)
dataset.delete() # => true
```

[boolean-type]: https://docs.python.org/2/library/stdtypes.html#boolean-values
[str-type]: https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange
[dict-type]: https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
[list-type]: https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange

---

## Timeout
To enable timeouts for requests package
```python
import geckoboard

client = geckoboard.client(API_KEY, timeout=60)
# or as positional parameter
client = geckoboard.client(API_KEY, 60)
```

## Development

Clone this repo
```
git clone https://github.com/geckoboard/geckoboard-python && cd geckoboard-python
```

Install package dependencies
```
python setup.py develop
```

Run tests
```
nosetests
```


