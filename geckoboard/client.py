"""
Public class: Client
"""

from geckoboard.connection import Connection
from geckoboard.datasets_client import DatasetsClient


class Client():
    """
    The Geckoboard API client

    The Geckoboard API client can authenticate you and connect you
    to our datasets API.

    Note
    ----
    You can find your API key by logging into the Geckoboard application
    and visiting the Account section.

    Parameters
    ----------
    api_key : str
        Your Geckoboard API key

    Attributes
    ----------
    datasets : DatasetsClient
        The datasets client can find, create and delete your datasets
    """

    def __init__(self, api_key):
        connection = Connection(api_key)

        self.__connection = connection
        self.datasets = DatasetsClient(connection)

    def ping(self):
        """
        Checks that your API key is valid and that you can reach the Geckoboard API

        Returns
        -------
        bool
            True if you are authenticated successfully

        Raises
        ------
        Exception
            If your API key is invalid

        ConnectionError
            If you could not connect to the Geckoboard API
        """
        self.__connection.get('/')

        return True
