# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit e9b768a rl @ Sep 3 3:07 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sharedapi_client.models.melanie_models_sharedapi_valorant2_card import MelanieModelsSharedapiValorant2Card  # noqa: E501

class TestMelanieModelsSharedapiValorant2Card(unittest.TestCase):
    """MelanieModelsSharedapiValorant2Card unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MelanieModelsSharedapiValorant2Card:
        """Test MelanieModelsSharedapiValorant2Card
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MelanieModelsSharedapiValorant2Card`
        """
        model = MelanieModelsSharedapiValorant2Card()  # noqa: E501
        if include_optional:
            return MelanieModelsSharedapiValorant2Card(
                small = None,
                large = None,
                wide = None,
                id = None
            )
        else:
            return MelanieModelsSharedapiValorant2Card(
        )
        """

    def testMelanieModelsSharedapiValorant2Card(self):
        """Test MelanieModelsSharedapiValorant2Card"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()