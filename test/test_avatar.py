# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.models.avatar import Avatar  # noqa: E501


class TestAvatar(unittest.TestCase):
    """Avatar unit test stubs."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Avatar:
        """Test Avatar
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included.
        """
        # uncomment below to create an instance of `Avatar`
        """
        model = Avatar()  # noqa: E501
        if include_optional:
            return Avatar(
                image_url = None,
                initial = None,
                accent_color = None
            )
        else:
            return Avatar(
        )
        """

    def testAvatar(self):
        """Test Avatar."""


if __name__ == "__main__":
    unittest.main()
