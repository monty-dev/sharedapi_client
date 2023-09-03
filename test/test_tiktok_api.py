# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.api.tiktok_api import TiktokApi  # noqa: E501


class TestTiktokApi(unittest.TestCase):
    """TiktokApi unit test stubs."""

    def setUp(self) -> None:
        self.api = TiktokApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_download_tik_tok_post(self) -> None:
        """Test case for download_tik_tok_post.

        Download Tiktok Post  # noqa: E501
        """

    def test_fetch_user_top_tik_toks(self) -> None:
        """Test case for fetch_user_top_tik_toks.

        Fetch User Top Tiktoks  # noqa: E501
        """

    def test_get_tik_tok_user(self) -> None:
        """Test case for get_tik_tok_user.

        Get Tiktok User  # noqa: E501
        """

    def test_getrecentuser_tik_toks(self) -> None:
        """Test case for getrecentuser_tik_toks.

        Get Recent User Tiktoks  # noqa: E501
        """


if __name__ == "__main__":
    unittest.main()
