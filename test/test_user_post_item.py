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

from sharedapi_client.models.user_post_item import UserPostItem  # noqa: E501

class TestUserPostItem(unittest.TestCase):
    """UserPostItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserPostItem:
        """Test UserPostItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserPostItem`
        """
        model = UserPostItem()  # noqa: E501
        if include_optional:
            return UserPostItem(
                id = None,
                shortcode = None,
                url = None,
                is_video = None,
                taken_at_timestamp = None,
                title = None
            )
        else:
            return UserPostItem(
        )
        """

    def testUserPostItem(self):
        """Test UserPostItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
