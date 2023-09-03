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

from sharedapi_client.models.bio_response import BioResponse  # noqa: E501

class TestBioResponse(unittest.TestCase):
    """BioResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BioResponse:
        """Test BioResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BioResponse`
        """
        model = BioResponse()  # noqa: E501
        if include_optional:
            return BioResponse(
                user = sharedapi_client.models.bio_user.BioUser(
                    id = null, 
                    username = null, 
                    avatar = null, 
                    avatar_decoration = null, 
                    discriminator = null, 
                    public_flags = null, 
                    flags = null, 
                    banner = sharedapi_client.models.banner_type.BannerType(
                        url = null, 
                        color = sharedapi_client.models.color_palette.ColorPalette(
                            colors = null, ), 
                        guild_id = null, 
                        format = null, 
                        user_id = null, ), 
                    banner_color = null, 
                    accent_color = null, 
                    bio = null, ),
                profile_data = sharedapi_client.models.profile_model.ProfileModel(
                    user = sharedapi_client.models.discord_user.DiscordUser(
                        id = null, 
                        username = null, 
                        avatar = null, 
                        avatar_decoration = null, 
                        discriminator = null, 
                        public_flags = null, 
                        flags = null, 
                        banner = null, 
                        banner_color = null, 
                        accent_color = null, 
                        bio = null, ), 
                    connected_accounts = null, 
                    premium_since = null, 
                    premium_type = null, 
                    premium_guild_since = null, 
                    profile_themes_experiment_bucket = null, 
                    guild_member = sharedapi_client.models.guild_member.GuildMember(
                        flags = null, 
                        is_pending = null, 
                        joined_at = null, 
                        nick = null, 
                        pending = null, 
                        premium_since = null, 
                        roles = null, 
                        bio = null, 
                        banner = null, 
                        mute = null, 
                        deaf = null, ), 
                    user_profile = sharedapi_client.models.user_profile.UserProfile(
                        bio = null, 
                        accent_color = null, 
                        banner = null, ), 
                    guild_member_profile = sharedapi_client.models.guild_member_profile.GuildMemberProfile(
                        guild_id = null, 
                        bio = null, 
                        banner = null, 
                        accent_color = null, ), ),
                member = sharedapi_client.models.bio_member.BioMember(
                    id = null, 
                    username = null, 
                    avatar = null, 
                    avatar_decoration = null, 
                    discriminator = null, 
                    public_flags = null, 
                    flags = null, 
                    banner = sharedapi_client.models.banner_type.BannerType(
                        url = null, 
                        color = sharedapi_client.models.color_palette.ColorPalette(
                            colors = null, ), 
                        guild_id = null, 
                        format = null, 
                        user_id = null, ), 
                    banner_color = null, 
                    accent_color = null, 
                    bio = null, ),
                activities = None,
                request = sharedapi_client.models.bio_request.BioRequest(
                    user_id = null, 
                    guild_id = null, 
                    sig = null, 
                    req_user_id = null, 
                    timestamp = null, ),
                status = sharedapi_client.models.gateway_user_status.GatewayUserStatus(
                    primary = null, 
                    desktop = null, 
                    mobile = null, 
                    web = null, ),
                sig = None
            )
        else:
            return BioResponse(
        )
        """

    def testBioResponse(self):
        """Test BioResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()