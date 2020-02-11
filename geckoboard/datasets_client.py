"""
Public class: DatasetsClient
"""

from geckoboard.dataset import Dataset


class DatasetsClient:
    """
    The datasets API client

    The datasets API client can find, create and delete your datasets.
    """

    def __init__(self, connection):
        self.__connection = connection

    def find_or_create(self, dataset_id, fields, unique_by=None):
        """
        Creates a new, or returns an existing dataset

        Searches for a dataset with a matching ID and schema. If a
        match is found that dataset is returned. Otherwise, a new
        dataset is created and returned.

        The dataset instance that is returned allows you
        to update or delete that dataset.

        Parameters
        ----------
        dataset_id : str
            The name of the dataset

        fields : dict
            The dataset schema (see https://developer.geckoboard.com/api-reference/python/#types)

        unique_by : list
            A list of schema keys (fields) that must have unique values for each entry

        Returns
        -------
        Dataset
            A new dataset instance

        Raises
        ------
        Exception
            If your API key is invalid or an existing dataset is found
            with a schema that doesn't match the one provided

        ConnectionError
            If you could not connect to the Geckoboard API
        """
        body = {
            'fields': fields,
        }

        if unique_by is not None:
            body['unique_by'] = unique_by

        self.__connection.put('/datasets/' + dataset_id, body)

        return Dataset(dataset_id, self.__connection)

    def delete(self, dataset_id):
        """
        Deletes a dataset by ID

        Allows you to delete a dataset with a given ID. You can
        also delete a dataset by calling the `delete` method
        on the dataset instance.

        Parameters
        ----------
        dataset_id : str
            The name of the dataset

        Returns
        -------
        bool
            True if the dataset was successfully deleted

        Raises
        ------
        Exception
            If your API key is invalid or no dataset was found
            that matches the ID provided

        ConnectionError
            If you could not connect to the Geckoboard API
        """
        self.__connection.delete('/datasets/' + dataset_id)

        return True
