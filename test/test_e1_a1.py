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

from sharedapi_client.models.e1_a1 import E1A1  # noqa: E501

class TestE1A1(unittest.TestCase):
    """E1A1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> E1A1:
        """Test E1A1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `E1A1`
        """
        model = E1A1()  # noqa: E501
        if include_optional:
            return E1A1(
                wins = None,
                number_of_games = None,
                final_rank = None,
                final_rank_patched = None,
                act_rank_wins = None,
                old = None
            )
        else:
            return E1A1(
        )
        """

    def testE1A1(self):
        """Test E1A1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
