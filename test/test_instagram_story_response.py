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

from sharedapi_client.models.instagram_story_response import InstagramStoryResponse  # noqa: E501

class TestInstagramStoryResponse(unittest.TestCase):
    """InstagramStoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstagramStoryResponse:
        """Test InstagramStoryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstagramStoryResponse`
        """
        model = InstagramStoryResponse()  # noqa: E501
        if include_optional:
            return InstagramStoryResponse(
                author = sharedapi_client.models.instagram_user_response.InstagramUserResponse(
                    username = null, 
                    full_name = null, 
                    is_private = null, 
                    avatar_filename = null, 
                    avatar_url = null, 
                    is_verified = null, ),
                items = None,
                item_count = None,
                created_at = None
            )
        else:
            return InstagramStoryResponse(
        )
        """

    def testInstagramStoryResponse(self):
        """Test InstagramStoryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()