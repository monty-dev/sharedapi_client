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

from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_legacy import MelanieModelsSharedapiTwitterScreenNameLegacy  # noqa: E501

class TestMelanieModelsSharedapiTwitterScreenNameLegacy(unittest.TestCase):
    """MelanieModelsSharedapiTwitterScreenNameLegacy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MelanieModelsSharedapiTwitterScreenNameLegacy:
        """Test MelanieModelsSharedapiTwitterScreenNameLegacy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MelanieModelsSharedapiTwitterScreenNameLegacy`
        """
        model = MelanieModelsSharedapiTwitterScreenNameLegacy()  # noqa: E501
        if include_optional:
            return MelanieModelsSharedapiTwitterScreenNameLegacy(
                protected = None,
                can_dm = None,
                can_media_tag = None,
                created_at = None,
                default_profile = None,
                default_profile_image = None,
                description = None,
                entities = sharedapi_client.models.entities.Entities(
                    description = sharedapi_client.models.url_class.URLClass(
                        urls = null, ), 
                    url = sharedapi_client.models.url_class.URLClass(
                        urls = null, ), ),
                fast_followers_count = None,
                favourites_count = None,
                followers_count = None,
                friends_count = None,
                has_custom_timelines = None,
                is_translator = None,
                listed_count = None,
                location = None,
                media_count = None,
                name = None,
                normal_followers_count = None,
                pinned_tweet_ids_str = None,
                possibly_sensitive = None,
                profile_image_url_https = None,
                profile_interstitial_type = None,
                screen_name = None,
                statuses_count = None,
                translator_type = None,
                verified = None,
                want_retweets = None,
                withheld_in_countries = None,
                profile_banner_url = None,
                url = None,
                verified_type = None
            )
        else:
            return MelanieModelsSharedapiTwitterScreenNameLegacy(
        )
        """

    def testMelanieModelsSharedapiTwitterScreenNameLegacy(self):
        """Test MelanieModelsSharedapiTwitterScreenNameLegacy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()