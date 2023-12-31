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

from sharedapi_client.models.thumbnail import Thumbnail  # noqa: E501

class TestThumbnail(unittest.TestCase):
    """Thumbnail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Thumbnail:
        """Test Thumbnail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Thumbnail`
        """
        model = Thumbnail()  # noqa: E501
        if include_optional:
            return Thumbnail(
                url = None,
                preference = None,
                id = None,
                height = None,
                width = None,
                resolution = None
            )
        else:
            return Thumbnail(
        )
        """

    def testThumbnail(self):
        """Test Thumbnail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
