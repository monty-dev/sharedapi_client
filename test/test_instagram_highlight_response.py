# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.models.instagram_highlight_response import InstagramHighlightResponse  # noqa: E501


class TestInstagramHighlightResponse(unittest.TestCase):
    """InstagramHighlightResponse unit test stubs."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstagramHighlightResponse:
        """Test InstagramHighlightResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included.
        """
        # uncomment below to create an instance of `InstagramHighlightResponse`
        """
        model = InstagramHighlightResponse()  # noqa: E501
        if include_optional:
            return InstagramHighlightResponse(
                id = None,
                created_at = None,
                latest_reel_media = None,
                media_count = None,
                items = None
            )
        else:
            return InstagramHighlightResponse(
                id = None,
        )
        """

    def testInstagramHighlightResponse(self):
        """Test InstagramHighlightResponse."""


if __name__ == "__main__":
    unittest.main()
