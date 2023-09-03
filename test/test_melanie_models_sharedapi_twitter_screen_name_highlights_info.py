# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_highlights_info import (
    MelanieModelsSharedapiTwitterScreenNameHighlightsInfo,  # noqa: E501
)


class TestMelanieModelsSharedapiTwitterScreenNameHighlightsInfo(unittest.TestCase):
    """MelanieModelsSharedapiTwitterScreenNameHighlightsInfo unit test stubs."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MelanieModelsSharedapiTwitterScreenNameHighlightsInfo:
        """Test MelanieModelsSharedapiTwitterScreenNameHighlightsInfo
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included.
        """
        # uncomment below to create an instance of `MelanieModelsSharedapiTwitterScreenNameHighlightsInfo`
        """
        model = MelanieModelsSharedapiTwitterScreenNameHighlightsInfo()  # noqa: E501
        if include_optional:
            return MelanieModelsSharedapiTwitterScreenNameHighlightsInfo(
                can_highlight_tweets = None,
                highlighted_tweets = None
            )
        else:
            return MelanieModelsSharedapiTwitterScreenNameHighlightsInfo(
        )
        """

    def testMelanieModelsSharedapiTwitterScreenNameHighlightsInfo(self):
        """Test MelanieModelsSharedapiTwitterScreenNameHighlightsInfo."""


if __name__ == "__main__":
    unittest.main()
