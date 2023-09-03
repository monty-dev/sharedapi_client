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

from sharedapi_client.models.format import Format  # noqa: E501

class TestFormat(unittest.TestCase):
    """Format unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Format:
        """Test Format
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Format`
        """
        model = Format()  # noqa: E501
        if include_optional:
            return Format(
                format_id = None,
                format_note = None,
                ext = None,
                protocol = None,
                acodec = None,
                vcodec = None,
                url = None,
                width = None,
                height = None,
                fps = None,
                rows = None,
                columns = None,
                fragments = None,
                audio_ext = None,
                video_ext = None,
                format = None,
                resolution = None,
                http_headers = sharedapi_client.models.http_headers.HttpHeaders(
                    user_agent = null, 
                    accept = null, 
                    accept_language = null, 
                    sec_fetch_mode = null, ),
                asr = None,
                filesize = None,
                source_preference = None,
                audio_channels = None,
                quality = None,
                has_drm = None,
                tbr = None,
                language = None,
                language_preference = None,
                preference = None,
                dynamic_range = None,
                abr = None,
                downloader_options = sharedapi_client.models.downloader_options.DownloaderOptions(
                    http_chunk_size = null, ),
                container = None,
                vbr = None,
                filesize_approx = None
            )
        else:
            return Format(
        )
        """

    def testFormat(self):
        """Test Format"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
