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

from sharedapi_client.models.tweet_data_result import TweetDataResult  # noqa: E501

class TestTweetDataResult(unittest.TestCase):
    """TweetDataResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TweetDataResult:
        """Test TweetDataResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetDataResult`
        """
        model = TweetDataResult()  # noqa: E501
        if include_optional:
            return TweetDataResult(
                typename = None,
                id = None,
                rest_id = None,
                affiliates_highlighted_label = None,
                has_graduated_access = None,
                is_blue_verified = None,
                profile_image_shape = None,
                legacy = sharedapi_client.models.legacy.Legacy(
                    protected = null, 
                    can_dm = null, 
                    can_media_tag = null, 
                    created_at = null, 
                    default_profile = null, 
                    default_profile_image = null, 
                    description = null, 
                    entities = sharedapi_client.models.entities.Entities(
                        description = sharedapi_client.models.url_class.URLClass(
                            urls = null, ), 
                        url = sharedapi_client.models.url_class.URLClass(
                            urls = null, ), ), 
                    fast_followers_count = null, 
                    favourites_count = null, 
                    followers_count = null, 
                    friends_count = null, 
                    has_custom_timelines = null, 
                    is_translator = null, 
                    listed_count = null, 
                    location = null, 
                    media_count = null, 
                    name = null, 
                    normal_followers_count = null, 
                    pinned_tweet_ids_str = null, 
                    possibly_sensitive = null, 
                    profile_image_url_https = null, 
                    profile_interstitial_type = null, 
                    screen_name = null, 
                    statuses_count = null, 
                    translator_type = null, 
                    verified = null, 
                    want_retweets = null, 
                    withheld_in_countries = null, 
                    profile_banner_url = null, 
                    url = null, 
                    verified_type = null, ),
                smart_blocked_by = None,
                smart_blocking = None,
                legacy_extended_profile = sharedapi_client.models.legacy_extended_profile.LegacyExtendedProfile(
                    birthdate = sharedapi_client.models.birthdate.Birthdate(
                        day = null, 
                        month = null, 
                        visibility = null, 
                        year_visibility = null, ), ),
                is_profile_translatable = None,
                has_hidden_subscriptions_on_profile = None,
                verification_info = sharedapi_client.models.verification_info.VerificationInfo(
                    reason = sharedapi_client.models.reason.Reason(
                        description = sharedapi_client.models.reason_description.ReasonDescription(
                            text = null, 
                            entities = null, ), 
                        verified_since_msec = null, ), ),
                highlights_info = sharedapi_client.models.highlights_info.HighlightsInfo(
                    can_highlight_tweets = null, 
                    highlighted_tweets = null, ),
                business_account = None,
                creator_subscriptions_count = None,
                unavailable_message = sharedapi_client.models.unavailable_message.UnavailableMessage(
                    rtl = null, 
                    text = null, 
                    entities = null, ),
                reason = None
            )
        else:
            return TweetDataResult(
        )
        """

    def testTweetDataResult(self):
        """Test TweetDataResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
