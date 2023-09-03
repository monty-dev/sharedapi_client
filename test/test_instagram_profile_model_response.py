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

from sharedapi_client.models.instagram_profile_model_response import InstagramProfileModelResponse  # noqa: E501

class TestInstagramProfileModelResponse(unittest.TestCase):
    """InstagramProfileModelResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstagramProfileModelResponse:
        """Test InstagramProfileModelResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstagramProfileModelResponse`
        """
        model = InstagramProfileModelResponse()  # noqa: E501
        if include_optional:
            return InstagramProfileModelResponse(
                avatar_filename = None,
                avatar_url = None,
                bio_links = None,
                biography = None,
                external_url = None,
                followed_by_count = None,
                following_count = None,
                full_name = None,
                has_channel = None,
                has_clips = None,
                highlight_reel_count = None,
                id = None,
                is_business_account = None,
                is_joined_recently = None,
                is_private = None,
                is_professional_account = None,
                is_verified = None,
                post_count = None,
                pronouns = None,
                username = None,
                post_items = None,
                created_at = None
            )
        else:
            return InstagramProfileModelResponse(
        )
        """

    def testInstagramProfileModelResponse(self):
        """Test InstagramProfileModelResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
