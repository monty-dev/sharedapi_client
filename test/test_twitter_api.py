# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.api.twitter_api import TwitterApi  # noqa: E501


class TestTwitterApi(unittest.TestCase):
    """TwitterApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TwitterApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_fetch_twitteruser(self) -> None:
        """Test case for fetch_twitteruser

        Fetch Twitter User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
