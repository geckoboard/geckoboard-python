geckoboard-python
=================

A Python client library for `Geckoboard datasets
API <https://developer.geckoboard.com/api-reference/>`__.

*Note: This library is still in Beta and the API has potential to change
before the release of V1.*

Installation
------------

Install the package with pip

::

    pip install geckoboard

Usage
-----

The latest documentation and user guide can be found on the `Geckoboard
developer
docs <https://developer.geckoboard.com/api-reference/python/>`__

--------------

Getting started
---------------

Install the python client from PIP

::

    pip install geckoboard

Import the Geckoboard package and create an instance of the client using
your API key:

.. code:: python

    import geckoboard

    client = geckbooard.client(API_KEY)

**Note:** You can find your API key by logging into the Geckoboard
application and visiting the Account section.

Authentication
--------------

Verify that your API key is valid and that you can reach the Geckoboard
API with the ``ping`` method.

.. code:: python

    client.ping()

Example:
~~~~~~~~

.. code:: python

    client('good-api-key').ping() # => true
    client('bad-api-key').ping() # => raises Exception

Finding or creating a dataset
-----------------------------

Find and verify an existing dataset or create a new dataset with the
``find_or_create`` method. ``unique_by`` is an optional list of one or
more field names whose values will be unique across all your records.

.. code:: python

    client.datasets.find_or_create(dataset_id, fields, unique_by)

Params:
~~~~~~~

-  ``dataset_id`` [required] <`str <https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange>`__>
-  ``fields`` [required] <`dict <https://docs.python.org/2/library/stdtypes.html#mapping-types-dict>`__>
    - ``type`` [required] <`str <https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange>`__>
    - ``name`` [required] <`str <https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange>`__>
    - ``optional`` <`boolean <https://docs.python.org/2/library/stdtypes.html#boolean-values>`__>
-  ``unique_by``
   <`list <https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange>`__>

Example:
~~~~~~~~

.. code:: python

    dataset = client.datasets.find_or_create('sales.by_night', {
      'amount': { 'type': 'number', 'name': 'Amount', 'optional': False },
      'timestamp': { 'type': 'datetime', 'name': 'Time' }
    }, ['timestamp'])

The full list of available field types is described at the top of this
page.

Replacing all data in a dataset
-------------------------------

Replace all data in the dataset by calling the ``put`` method.

.. code:: python

    dataset.put(items)

Params:
~~~~~~~

-  ``items`` [required]
   <`list <https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange>`__>

Example:
~~~~~~~~

.. code:: python

    dataset.put([
      { 'timestamp': '2016-01-01T12:00:00Z', 'amount': 819 },
      { 'timestamp': '2016-01-02T12:00:00Z', 'amount': 409 },
      { 'timestamp': '2016-01-03T12:00:00Z', 'amount': 164 }
    ])

Appending data to a dataset
---------------------------

Append records to a dataset by calling the ``post`` method.

Should the number of records in your dataset exceed the limit following
a post `old records will be discarded <#record-count-limit>`__.

.. code:: python

    dataset.post(items, delete_by)

Params:
~~~~~~~

-  ``items`` [required]
   <`list <https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange>`__>
-  ``delete_by``
   <`str <https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange>`__>

Example:
~~~~~~~~

.. code:: python

    dataset.post([
      { 'timestamp': '2016-01-03T12:00:00Z', 'amount': 312 },
      { 'timestamp': '2016-01-04T12:00:00Z', 'amount': 665 },
      { 'timestamp': '2016-01-05T12:00:00Z', 'amount': 453 }
    ], 'timestamp')

Deleting a dataset
------------------

Delete the dataset and all data with the given id.

.. code:: python

    client.datasets.delete(dataset_id)

Params:
~~~~~~~

-  ``dataset_id`` [required]
   <`str <https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange>`__>

Example:
~~~~~~~~

.. code:: python

    client.datasets.delete('sales.gross') # => true

You can also delete a dataset by calling the ``delete`` method on a
dataset.

.. code:: python

    dataset = client.datasets.find_or_create(...)
    dataset.delete() # => true

--------------

Development
-----------

Clone this repo

::

    git clone https://github.com/geckoboard/geckoboard-python && cd geckoboard-python

Install package dependencies

::

    python setup.py develop

Run tests

::

    nosetests
