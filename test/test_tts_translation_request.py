# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.models.tts_translation_request import TTSTranslationRequest  # noqa: E501


class TestTTSTranslationRequest(unittest.TestCase):
    """TTSTranslationRequest unit test stubs."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TTSTranslationRequest:
        """Test TTSTranslationRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included.
        """
        # uncomment below to create an instance of `TTSTranslationRequest`
        """
        model = TTSTranslationRequest()  # noqa: E501
        if include_optional:
            return TTSTranslationRequest(
                text = None,
                speaker_name = en-US-Ana
            )
        else:
            return TTSTranslationRequest(
                text = None,
                speaker_name = en-US-Ana,
        )
        """

    def testTTSTranslationRequest(self):
        """Test TTSTranslationRequest."""


if __name__ == "__main__":
    unittest.main()
