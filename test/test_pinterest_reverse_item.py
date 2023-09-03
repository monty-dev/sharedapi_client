# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.models.pinterest_reverse_item import PinterestReverseItem  # noqa: E501


class TestPinterestReverseItem(unittest.TestCase):
    """PinterestReverseItem unit test stubs."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PinterestReverseItem:
        """Test PinterestReverseItem
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included.
        """
        # uncomment below to create an instance of `PinterestReverseItem`
        """
        model = PinterestReverseItem()  # noqa: E501
        if include_optional:
            return PinterestReverseItem(
                is_uploaded = None,
                image_large_url = None,
                type = None,
                is_repin = None,
                link = None,
                is_video = None,
                id = None,
                repin_count = None,
                domain = None,
                title = None,
                comment_count = None,
                description = None,
                created_at = None
            )
        else:
            return PinterestReverseItem(
        )
        """

    def testPinterestReverseItem(self):
        """Test PinterestReverseItem."""


if __name__ == "__main__":
    unittest.main()
