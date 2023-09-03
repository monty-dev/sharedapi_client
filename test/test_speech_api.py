# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.api.speech_api import SpeechApi  # noqa: E501


class TestSpeechApi(unittest.TestCase):
    """SpeechApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SpeechApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_perform_speechto_text(self) -> None:
        """Test case for perform_speechto_text

        Perform Speech To Text  # noqa: E501
        """
        pass

    def test_perform_textto_speech(self) -> None:
        """Test case for perform_textto_speech

        Perform Text To Speech  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
