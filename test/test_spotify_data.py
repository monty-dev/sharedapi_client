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

from sharedapi_client.models.spotify_data import SpotifyData  # noqa: E501

class TestSpotifyData(unittest.TestCase):
    """SpotifyData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotifyData:
        """Test SpotifyData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotifyData`
        """
        model = SpotifyData()  # noqa: E501
        if include_optional:
            return SpotifyData(
                album_cover_url = None,
                tile = None,
                artist = None,
                album = None,
                track_id = None,
                start = None,
                end = None,
                duration = None
            )
        else:
            return SpotifyData(
        )
        """

    def testSpotifyData(self):
        """Test SpotifyData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
