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

from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_verification_info import MelanieModelsSharedapiTwitterUserTweetsVerificationInfo  # noqa: E501

class TestMelanieModelsSharedapiTwitterUserTweetsVerificationInfo(unittest.TestCase):
    """MelanieModelsSharedapiTwitterUserTweetsVerificationInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MelanieModelsSharedapiTwitterUserTweetsVerificationInfo:
        """Test MelanieModelsSharedapiTwitterUserTweetsVerificationInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MelanieModelsSharedapiTwitterUserTweetsVerificationInfo`
        """
        model = MelanieModelsSharedapiTwitterUserTweetsVerificationInfo()  # noqa: E501
        if include_optional:
            return MelanieModelsSharedapiTwitterUserTweetsVerificationInfo(
                reason = sharedapi_client.models.reason.Reason(
                    description = sharedapi_client.models.reason_description.ReasonDescription(
                        text = null, 
                        entities = null, ), 
                    verified_since_msec = null, )
            )
        else:
            return MelanieModelsSharedapiTwitterUserTweetsVerificationInfo(
        )
        """

    def testMelanieModelsSharedapiTwitterUserTweetsVerificationInfo(self):
        """Test MelanieModelsSharedapiTwitterUserTweetsVerificationInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
