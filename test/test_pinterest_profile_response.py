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

from sharedapi_client.models.pinterest_profile_response import PinterestProfileResponse  # noqa: E501

class TestPinterestProfileResponse(unittest.TestCase):
    """PinterestProfileResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PinterestProfileResponse:
        """Test PinterestProfileResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PinterestProfileResponse`
        """
        model = PinterestProfileResponse()  # noqa: E501
        if include_optional:
            return PinterestProfileResponse(
                username = None,
                description = None,
                followers = None,
                following = None,
                pins = None,
                url = None,
                avatar_url = None
            )
        else:
            return PinterestProfileResponse(
                username = None,
        )
        """

    def testPinterestProfileResponse(self):
        """Test PinterestProfileResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
