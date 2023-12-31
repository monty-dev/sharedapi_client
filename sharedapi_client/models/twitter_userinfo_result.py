# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit e9b768a rl @ Sep 3 3:07 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_entities import MelanieModelsSharedapiTwitterScreenNameEntities
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_highlights_info import MelanieModelsSharedapiTwitterScreenNameHighlightsInfo
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_legacy import MelanieModelsSharedapiTwitterScreenNameLegacy
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_legacy_extended_profile import MelanieModelsSharedapiTwitterScreenNameLegacyExtendedProfile
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_unavailable_message import MelanieModelsSharedapiTwitterScreenNameUnavailableMessage
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_verification_info import MelanieModelsSharedapiTwitterScreenNameVerificationInfo

class TwitterUserinfoResult(BaseModel):
    """
    TwitterUserinfoResult
    """
    typename: Optional[Any] = Field(None, alias="__typename")
    id: Optional[Any] = None
    rest_id: Optional[Any] = None
    affiliates_highlighted_label: Optional[Any] = None
    has_graduated_access: Optional[Any] = None
    is_blue_verified: Optional[Any] = None
    profile_image_shape: Optional[Any] = None
    legacy: Optional[MelanieModelsSharedapiTwitterScreenNameLegacy] = None
    smart_blocked_by: Optional[Any] = None
    smart_blocking: Optional[Any] = None
    legacy_extended_profile: Optional[MelanieModelsSharedapiTwitterScreenNameLegacyExtendedProfile] = None
    is_profile_translatable: Optional[Any] = None
    has_hidden_subscriptions_on_profile: Optional[Any] = None
    verification_info: Optional[MelanieModelsSharedapiTwitterScreenNameVerificationInfo] = None
    highlights_info: Optional[MelanieModelsSharedapiTwitterScreenNameHighlightsInfo] = None
    business_account: Optional[Any] = None
    creator_subscriptions_count: Optional[Any] = None
    unavailable_message: Optional[MelanieModelsSharedapiTwitterScreenNameUnavailableMessage] = None
    reason: Optional[Any] = None
    protected: Optional[Any] = None
    can_dm: Optional[Any] = None
    can_media_tag: Optional[Any] = None
    created_at: Optional[Any] = None
    default_profile: Optional[Any] = None
    default_profile_image: Optional[Any] = None
    description: Optional[Any] = None
    entities: Optional[MelanieModelsSharedapiTwitterScreenNameEntities] = None
    fast_followers_count: Optional[Any] = None
    favourites_count: Optional[Any] = None
    followers_count: Optional[Any] = None
    friends_count: Optional[Any] = None
    has_custom_timelines: Optional[Any] = None
    is_translator: Optional[Any] = None
    listed_count: Optional[Any] = None
    location: Optional[Any] = None
    media_count: Optional[Any] = None
    name: Optional[Any] = None
    normal_followers_count: Optional[Any] = None
    pinned_tweet_ids_str: Optional[Any] = None
    possibly_sensitive: Optional[Any] = None
    profile_image_url_https: Optional[Any] = None
    profile_interstitial_type: Optional[Any] = None
    screen_name: Optional[Any] = None
    statuses_count: Optional[Any] = None
    translator_type: Optional[Any] = None
    verified: Optional[Any] = None
    want_retweets: Optional[Any] = None
    withheld_in_countries: Optional[Any] = None
    profile_banner_url: Optional[Any] = None
    url: Optional[Any] = None
    verified_type: Optional[Any] = None
    __properties = ["__typename", "id", "rest_id", "affiliates_highlighted_label", "has_graduated_access", "is_blue_verified", "profile_image_shape", "legacy", "smart_blocked_by", "smart_blocking", "legacy_extended_profile", "is_profile_translatable", "has_hidden_subscriptions_on_profile", "verification_info", "highlights_info", "business_account", "creator_subscriptions_count", "unavailable_message", "reason", "protected", "can_dm", "can_media_tag", "created_at", "default_profile", "default_profile_image", "description", "entities", "fast_followers_count", "favourites_count", "followers_count", "friends_count", "has_custom_timelines", "is_translator", "listed_count", "location", "media_count", "name", "normal_followers_count", "pinned_tweet_ids_str", "possibly_sensitive", "profile_image_url_https", "profile_interstitial_type", "screen_name", "statuses_count", "translator_type", "verified", "want_retweets", "withheld_in_countries", "profile_banner_url", "url", "verified_type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TwitterUserinfoResult:
        """Create an instance of TwitterUserinfoResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of legacy
        if self.legacy:
            _dict['legacy'] = self.legacy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legacy_extended_profile
        if self.legacy_extended_profile:
            _dict['legacy_extended_profile'] = self.legacy_extended_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verification_info
        if self.verification_info:
            _dict['verification_info'] = self.verification_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of highlights_info
        if self.highlights_info:
            _dict['highlights_info'] = self.highlights_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unavailable_message
        if self.unavailable_message:
            _dict['unavailable_message'] = self.unavailable_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entities
        if self.entities:
            _dict['entities'] = self.entities.to_dict()
        # set to None if typename (nullable) is None
        # and __fields_set__ contains the field
        if self.typename is None and "typename" in self.__fields_set__:
            _dict['__typename'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if rest_id (nullable) is None
        # and __fields_set__ contains the field
        if self.rest_id is None and "rest_id" in self.__fields_set__:
            _dict['rest_id'] = None

        # set to None if affiliates_highlighted_label (nullable) is None
        # and __fields_set__ contains the field
        if self.affiliates_highlighted_label is None and "affiliates_highlighted_label" in self.__fields_set__:
            _dict['affiliates_highlighted_label'] = None

        # set to None if has_graduated_access (nullable) is None
        # and __fields_set__ contains the field
        if self.has_graduated_access is None and "has_graduated_access" in self.__fields_set__:
            _dict['has_graduated_access'] = None

        # set to None if is_blue_verified (nullable) is None
        # and __fields_set__ contains the field
        if self.is_blue_verified is None and "is_blue_verified" in self.__fields_set__:
            _dict['is_blue_verified'] = None

        # set to None if profile_image_shape (nullable) is None
        # and __fields_set__ contains the field
        if self.profile_image_shape is None and "profile_image_shape" in self.__fields_set__:
            _dict['profile_image_shape'] = None

        # set to None if smart_blocked_by (nullable) is None
        # and __fields_set__ contains the field
        if self.smart_blocked_by is None and "smart_blocked_by" in self.__fields_set__:
            _dict['smart_blocked_by'] = None

        # set to None if smart_blocking (nullable) is None
        # and __fields_set__ contains the field
        if self.smart_blocking is None and "smart_blocking" in self.__fields_set__:
            _dict['smart_blocking'] = None

        # set to None if is_profile_translatable (nullable) is None
        # and __fields_set__ contains the field
        if self.is_profile_translatable is None and "is_profile_translatable" in self.__fields_set__:
            _dict['is_profile_translatable'] = None

        # set to None if has_hidden_subscriptions_on_profile (nullable) is None
        # and __fields_set__ contains the field
        if self.has_hidden_subscriptions_on_profile is None and "has_hidden_subscriptions_on_profile" in self.__fields_set__:
            _dict['has_hidden_subscriptions_on_profile'] = None

        # set to None if business_account (nullable) is None
        # and __fields_set__ contains the field
        if self.business_account is None and "business_account" in self.__fields_set__:
            _dict['business_account'] = None

        # set to None if creator_subscriptions_count (nullable) is None
        # and __fields_set__ contains the field
        if self.creator_subscriptions_count is None and "creator_subscriptions_count" in self.__fields_set__:
            _dict['creator_subscriptions_count'] = None

        # set to None if reason (nullable) is None
        # and __fields_set__ contains the field
        if self.reason is None and "reason" in self.__fields_set__:
            _dict['reason'] = None

        # set to None if protected (nullable) is None
        # and __fields_set__ contains the field
        if self.protected is None and "protected" in self.__fields_set__:
            _dict['protected'] = None

        # set to None if can_dm (nullable) is None
        # and __fields_set__ contains the field
        if self.can_dm is None and "can_dm" in self.__fields_set__:
            _dict['can_dm'] = None

        # set to None if can_media_tag (nullable) is None
        # and __fields_set__ contains the field
        if self.can_media_tag is None and "can_media_tag" in self.__fields_set__:
            _dict['can_media_tag'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if default_profile (nullable) is None
        # and __fields_set__ contains the field
        if self.default_profile is None and "default_profile" in self.__fields_set__:
            _dict['default_profile'] = None

        # set to None if default_profile_image (nullable) is None
        # and __fields_set__ contains the field
        if self.default_profile_image is None and "default_profile_image" in self.__fields_set__:
            _dict['default_profile_image'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if fast_followers_count (nullable) is None
        # and __fields_set__ contains the field
        if self.fast_followers_count is None and "fast_followers_count" in self.__fields_set__:
            _dict['fast_followers_count'] = None

        # set to None if favourites_count (nullable) is None
        # and __fields_set__ contains the field
        if self.favourites_count is None and "favourites_count" in self.__fields_set__:
            _dict['favourites_count'] = None

        # set to None if followers_count (nullable) is None
        # and __fields_set__ contains the field
        if self.followers_count is None and "followers_count" in self.__fields_set__:
            _dict['followers_count'] = None

        # set to None if friends_count (nullable) is None
        # and __fields_set__ contains the field
        if self.friends_count is None and "friends_count" in self.__fields_set__:
            _dict['friends_count'] = None

        # set to None if has_custom_timelines (nullable) is None
        # and __fields_set__ contains the field
        if self.has_custom_timelines is None and "has_custom_timelines" in self.__fields_set__:
            _dict['has_custom_timelines'] = None

        # set to None if is_translator (nullable) is None
        # and __fields_set__ contains the field
        if self.is_translator is None and "is_translator" in self.__fields_set__:
            _dict['is_translator'] = None

        # set to None if listed_count (nullable) is None
        # and __fields_set__ contains the field
        if self.listed_count is None and "listed_count" in self.__fields_set__:
            _dict['listed_count'] = None

        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict['location'] = None

        # set to None if media_count (nullable) is None
        # and __fields_set__ contains the field
        if self.media_count is None and "media_count" in self.__fields_set__:
            _dict['media_count'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if normal_followers_count (nullable) is None
        # and __fields_set__ contains the field
        if self.normal_followers_count is None and "normal_followers_count" in self.__fields_set__:
            _dict['normal_followers_count'] = None

        # set to None if pinned_tweet_ids_str (nullable) is None
        # and __fields_set__ contains the field
        if self.pinned_tweet_ids_str is None and "pinned_tweet_ids_str" in self.__fields_set__:
            _dict['pinned_tweet_ids_str'] = None

        # set to None if possibly_sensitive (nullable) is None
        # and __fields_set__ contains the field
        if self.possibly_sensitive is None and "possibly_sensitive" in self.__fields_set__:
            _dict['possibly_sensitive'] = None

        # set to None if profile_image_url_https (nullable) is None
        # and __fields_set__ contains the field
        if self.profile_image_url_https is None and "profile_image_url_https" in self.__fields_set__:
            _dict['profile_image_url_https'] = None

        # set to None if profile_interstitial_type (nullable) is None
        # and __fields_set__ contains the field
        if self.profile_interstitial_type is None and "profile_interstitial_type" in self.__fields_set__:
            _dict['profile_interstitial_type'] = None

        # set to None if screen_name (nullable) is None
        # and __fields_set__ contains the field
        if self.screen_name is None and "screen_name" in self.__fields_set__:
            _dict['screen_name'] = None

        # set to None if statuses_count (nullable) is None
        # and __fields_set__ contains the field
        if self.statuses_count is None and "statuses_count" in self.__fields_set__:
            _dict['statuses_count'] = None

        # set to None if translator_type (nullable) is None
        # and __fields_set__ contains the field
        if self.translator_type is None and "translator_type" in self.__fields_set__:
            _dict['translator_type'] = None

        # set to None if verified (nullable) is None
        # and __fields_set__ contains the field
        if self.verified is None and "verified" in self.__fields_set__:
            _dict['verified'] = None

        # set to None if want_retweets (nullable) is None
        # and __fields_set__ contains the field
        if self.want_retweets is None and "want_retweets" in self.__fields_set__:
            _dict['want_retweets'] = None

        # set to None if withheld_in_countries (nullable) is None
        # and __fields_set__ contains the field
        if self.withheld_in_countries is None and "withheld_in_countries" in self.__fields_set__:
            _dict['withheld_in_countries'] = None

        # set to None if profile_banner_url (nullable) is None
        # and __fields_set__ contains the field
        if self.profile_banner_url is None and "profile_banner_url" in self.__fields_set__:
            _dict['profile_banner_url'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if verified_type (nullable) is None
        # and __fields_set__ contains the field
        if self.verified_type is None and "verified_type" in self.__fields_set__:
            _dict['verified_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TwitterUserinfoResult:
        """Create an instance of TwitterUserinfoResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TwitterUserinfoResult.parse_obj(obj)

        _obj = TwitterUserinfoResult.parse_obj({
            "typename": obj.get("__typename"),
            "id": obj.get("id"),
            "rest_id": obj.get("rest_id"),
            "affiliates_highlighted_label": obj.get("affiliates_highlighted_label"),
            "has_graduated_access": obj.get("has_graduated_access"),
            "is_blue_verified": obj.get("is_blue_verified"),
            "profile_image_shape": obj.get("profile_image_shape"),
            "legacy": MelanieModelsSharedapiTwitterScreenNameLegacy.from_dict(obj.get("legacy")) if obj.get("legacy") is not None else None,
            "smart_blocked_by": obj.get("smart_blocked_by"),
            "smart_blocking": obj.get("smart_blocking"),
            "legacy_extended_profile": MelanieModelsSharedapiTwitterScreenNameLegacyExtendedProfile.from_dict(obj.get("legacy_extended_profile")) if obj.get("legacy_extended_profile") is not None else None,
            "is_profile_translatable": obj.get("is_profile_translatable"),
            "has_hidden_subscriptions_on_profile": obj.get("has_hidden_subscriptions_on_profile"),
            "verification_info": MelanieModelsSharedapiTwitterScreenNameVerificationInfo.from_dict(obj.get("verification_info")) if obj.get("verification_info") is not None else None,
            "highlights_info": MelanieModelsSharedapiTwitterScreenNameHighlightsInfo.from_dict(obj.get("highlights_info")) if obj.get("highlights_info") is not None else None,
            "business_account": obj.get("business_account"),
            "creator_subscriptions_count": obj.get("creator_subscriptions_count"),
            "unavailable_message": MelanieModelsSharedapiTwitterScreenNameUnavailableMessage.from_dict(obj.get("unavailable_message")) if obj.get("unavailable_message") is not None else None,
            "reason": obj.get("reason"),
            "protected": obj.get("protected"),
            "can_dm": obj.get("can_dm"),
            "can_media_tag": obj.get("can_media_tag"),
            "created_at": obj.get("created_at"),
            "default_profile": obj.get("default_profile"),
            "default_profile_image": obj.get("default_profile_image"),
            "description": obj.get("description"),
            "entities": MelanieModelsSharedapiTwitterScreenNameEntities.from_dict(obj.get("entities")) if obj.get("entities") is not None else None,
            "fast_followers_count": obj.get("fast_followers_count"),
            "favourites_count": obj.get("favourites_count"),
            "followers_count": obj.get("followers_count"),
            "friends_count": obj.get("friends_count"),
            "has_custom_timelines": obj.get("has_custom_timelines"),
            "is_translator": obj.get("is_translator"),
            "listed_count": obj.get("listed_count"),
            "location": obj.get("location"),
            "media_count": obj.get("media_count"),
            "name": obj.get("name"),
            "normal_followers_count": obj.get("normal_followers_count"),
            "pinned_tweet_ids_str": obj.get("pinned_tweet_ids_str"),
            "possibly_sensitive": obj.get("possibly_sensitive"),
            "profile_image_url_https": obj.get("profile_image_url_https"),
            "profile_interstitial_type": obj.get("profile_interstitial_type"),
            "screen_name": obj.get("screen_name"),
            "statuses_count": obj.get("statuses_count"),
            "translator_type": obj.get("translator_type"),
            "verified": obj.get("verified"),
            "want_retweets": obj.get("want_retweets"),
            "withheld_in_countries": obj.get("withheld_in_countries"),
            "profile_banner_url": obj.get("profile_banner_url"),
            "url": obj.get("url"),
            "verified_type": obj.get("verified_type")
        })
        return _obj


