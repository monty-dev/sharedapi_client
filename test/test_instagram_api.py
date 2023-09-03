# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.api.instagram_api import InstagramApi  # noqa: E501


class TestInstagramApi(unittest.TestCase):
    """InstagramApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InstagramApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_download_instagram_post(self) -> None:
        """Test case for download_instagram_post

        Download Instagram Post  # noqa: E501
        """
        pass

    def test_fetch_stories(self) -> None:
        """Test case for fetch_stories

        Fetch Stories  # noqa: E501
        """
        pass

    def test_get_highlightby_id(self) -> None:
        """Test case for get_highlightby_id

        Get Highlight By Id  # noqa: E501
        """
        pass

    def test_get_highlights(self) -> None:
        """Test case for get_highlights

        Get Highlights  # noqa: E501
        """
        pass

    def test_get_instagram_user(self) -> None:
        """Test case for get_instagram_user

        Get Instagram User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
