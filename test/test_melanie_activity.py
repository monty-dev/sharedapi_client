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

from sharedapi_client.models.melanie_activity import MelanieActivity  # noqa: E501

class TestMelanieActivity(unittest.TestCase):
    """MelanieActivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MelanieActivity:
        """Test MelanieActivity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MelanieActivity`
        """
        model = MelanieActivity()  # noqa: E501
        if include_optional:
            return MelanieActivity(
                name = None,
                primary = None,
                emoji = sharedapi_client.models.melanie_emoji.MelanieEmoji(
                    name = null, 
                    id = null, 
                    animated = null, 
                    url = null, 
                    dispaly_name = null, ),
                created_at = None,
                url = None,
                assets = sharedapi_client.models.activity_asset.ActivityAsset(
                    small_text = null, 
                    large_text = null, 
                    small_image = null, 
                    large_image = null, ),
                spotify_data = sharedapi_client.models.spotify_data.SpotifyData(
                    album_cover_url = null, 
                    tile = null, 
                    artist = null, 
                    album = null, 
                    track_id = null, 
                    start = null, 
                    end = null, 
                    duration = null, ),
                state = None,
                flags = None,
                type = None,
                color = sharedapi_client.models.color_palette.ColorPalette(
                    colors = null, ),
                application_id = None,
                session_id = None
            )
        else:
            return MelanieActivity(
        )
        """

    def testMelanieActivity(self):
        """Test MelanieActivity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
