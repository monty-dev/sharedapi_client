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

from sharedapi_client.models.valorant_profile_response import ValorantProfileResponse  # noqa: E501

class TestValorantProfileResponse(unittest.TestCase):
    """ValorantProfileResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValorantProfileResponse:
        """Test ValorantProfileResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValorantProfileResponse`
        """
        model = ValorantProfileResponse()  # noqa: E501
        if include_optional:
            return ValorantProfileResponse(
                name = None,
                tag = None,
                puuid = None,
                current_rating = None,
                peak_rating = None,
                peak_rating_act = None,
                avatar_url = None,
                card = sharedapi_client.models.card.Card(
                    small = null, 
                    large = null, 
                    wide = null, 
                    id = null, ),
                account_level = None,
                kd_ratio = None,
                damage_round_ratio = None,
                headshot_percent = None,
                win_percent = None,
                wins = None,
                lost = None,
                matches_played = None,
                region = None,
                kills = None,
                deaths = None,
                last_update = None
            )
        else:
            return ValorantProfileResponse(
        )
        """

    def testValorantProfileResponse(self):
        """Test ValorantProfileResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
