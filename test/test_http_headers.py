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

from sharedapi_client.models.http_headers import HttpHeaders  # noqa: E501

class TestHttpHeaders(unittest.TestCase):
    """HttpHeaders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpHeaders:
        """Test HttpHeaders
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpHeaders`
        """
        model = HttpHeaders()  # noqa: E501
        if include_optional:
            return HttpHeaders(
                user_agent = None,
                accept = None,
                accept_language = None,
                sec_fetch_mode = None
            )
        else:
            return HttpHeaders(
        )
        """

    def testHttpHeaders(self):
        """Test HttpHeaders"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
