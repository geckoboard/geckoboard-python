"""
The official Geckoboard API client for Python

The Geckoboard API client can authenticate you
and connect you to our datasets API so that
you can create, update and delete datasets.
"""

from geckoboard.client import Client


def client(api_key, timeout=None):
    """
    Creates an instance of a Geckoboard API client

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
    timeout : float
        Optional timeout parameter

    Returns
    -------
    Client
        A Geckoboard API client instance
    """
    return Client(api_key, timeout)
