"""
Public class: Dataset
"""


class Dataset():
    """
    Update or delete an individual dataset.

    Parameters
    ----------
    dataset_id : str
        The name of the dataset
    """

    def __init__(self, dataset_id, connection):
        self.__id = dataset_id
        self.__connection = connection

    def put(self, items):
        """
        Replace all data entries in the Dataset

        Parameters
        ----------
        items : list
            A list of the entries to replace the current ones

        Returns
        -------
        bool
            True if the dataset was successfully updated

        Raises
        ------
        Exception
            If the items do not match the dataset schema

        ConnectionError
            If you could not connect to the Geckoboard API
        """
        body = {
            'data': items,
        }

        self.__connection.put('/datasets/' + self.__id + '/data', body)

        return True

    def post(self, items, delete_by=None):
        """
        Append new data entries to the Dataset

        Parameters
        ----------
        items : list
            A list of the entries to append to the current ones

        Returns
        -------
        bool
            True if the dataset was successfully updated

        Raises
        ------
        Exception
            If the items do not match the dataset schema

        ConnectionError
            If you could not connect to the Geckoboard API
        """
        body = {
            'data': items,
        }

        if delete_by is not None:
            body['delete_by'] = delete_by

        self.__connection.post('/datasets/' + self.__id + '/data', body)

        return True

    def delete(self):
        """
        Delete the dataset

        Returns
        -------
        bool
            True if the dataset was successfully updated

        Raises
        ------
        ConnectionError
            If you could not connect to the Geckoboard API
        """
        self.__connection.delete('/datasets/' + self.__id)

        return True
