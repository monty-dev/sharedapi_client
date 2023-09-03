# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from sharedapi_client.models.profile_model import ProfileModel  # noqa: E501


class TestProfileModel(unittest.TestCase):
    """ProfileModel unit test stubs."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProfileModel:
        """Test ProfileModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included.
        """
        # uncomment below to create an instance of `ProfileModel`
        """
        model = ProfileModel()  # noqa: E501
        if include_optional:
            return ProfileModel(
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
                connected_accounts = None,
                premium_since = None,
                premium_type = None,
                premium_guild_since = None,
                profile_themes_experiment_bucket = None,
                guild_member = sharedapi_client.models.guild_member.GuildMember(
                    flags = null,
                    is_pending = null,
                    joined_at = null,
                    nick = null,
                    pending = null,
                    premium_since = null,
                    roles = null,
                    user = sharedapi_client.models.user1.User1(
                        id = null,
                        username = null,
                        avatar = null,
                        avatar_decoration = null,
                        discriminator = null,
                        public_flags = null, ),
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
                    accent_color = null, )
            )
        else:
            return ProfileModel(
        )
        """

    def testProfileModel(self):
        """Test ProfileModel."""


if __name__ == "__main__":
    unittest.main()
