# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sharedapi_client.models.melanie_emoji import MelanieEmoji  # noqa: E501

class TestMelanieEmoji(unittest.TestCase):
    """MelanieEmoji unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MelanieEmoji:
        """Test MelanieEmoji
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MelanieEmoji`
        """
        model = MelanieEmoji()  # noqa: E501
        if include_optional:
            return MelanieEmoji(
                name = None,
                id = None,
                animated = None,
                url = None,
                dispaly_name = None
            )
        else:
            return MelanieEmoji(
        )
        """

    def testMelanieEmoji(self):
        """Test MelanieEmoji"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
