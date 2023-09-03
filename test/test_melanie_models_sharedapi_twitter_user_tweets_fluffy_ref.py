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

from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_fluffy_ref import MelanieModelsSharedapiTwitterUserTweetsFluffyRef  # noqa: E501

class TestMelanieModelsSharedapiTwitterUserTweetsFluffyRef(unittest.TestCase):
    """MelanieModelsSharedapiTwitterUserTweetsFluffyRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MelanieModelsSharedapiTwitterUserTweetsFluffyRef:
        """Test MelanieModelsSharedapiTwitterUserTweetsFluffyRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MelanieModelsSharedapiTwitterUserTweetsFluffyRef`
        """
        model = MelanieModelsSharedapiTwitterUserTweetsFluffyRef()  # noqa: E501
        if include_optional:
            return MelanieModelsSharedapiTwitterUserTweetsFluffyRef(
                url = None,
                url_type = None
            )
        else:
            return MelanieModelsSharedapiTwitterUserTweetsFluffyRef(
        )
        """

    def testMelanieModelsSharedapiTwitterUserTweetsFluffyRef(self):
        """Test MelanieModelsSharedapiTwitterUserTweetsFluffyRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
