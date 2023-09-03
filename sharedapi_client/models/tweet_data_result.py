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
from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_highlights_info import MelanieModelsSharedapiTwitterUserTweetsHighlightsInfo
from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_legacy import MelanieModelsSharedapiTwitterUserTweetsLegacy
from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_legacy_extended_profile import MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile
from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_unavailable_message import MelanieModelsSharedapiTwitterUserTweetsUnavailableMessage
from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_verification_info import MelanieModelsSharedapiTwitterUserTweetsVerificationInfo

class TweetDataResult(BaseModel):
    """
    TweetDataResult
    """
    typename: Optional[Any] = Field(None, alias="__typename")
    id: Optional[Any] = None
    rest_id: Optional[Any] = None
    affiliates_highlighted_label: Optional[Any] = None
    has_graduated_access: Optional[Any] = None
    is_blue_verified: Optional[Any] = None
    profile_image_shape: Optional[Any] = None
    legacy: Optional[MelanieModelsSharedapiTwitterUserTweetsLegacy] = None
    smart_blocked_by: Optional[Any] = None
    smart_blocking: Optional[Any] = None
    legacy_extended_profile: Optional[MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile] = None
    is_profile_translatable: Optional[Any] = None
    has_hidden_subscriptions_on_profile: Optional[Any] = None
    verification_info: Optional[MelanieModelsSharedapiTwitterUserTweetsVerificationInfo] = None
    highlights_info: Optional[MelanieModelsSharedapiTwitterUserTweetsHighlightsInfo] = None
    business_account: Optional[Any] = None
    creator_subscriptions_count: Optional[Any] = None
    unavailable_message: Optional[MelanieModelsSharedapiTwitterUserTweetsUnavailableMessage] = None
    reason: Optional[Any] = None
    __properties = ["__typename", "id", "rest_id", "affiliates_highlighted_label", "has_graduated_access", "is_blue_verified", "profile_image_shape", "legacy", "smart_blocked_by", "smart_blocking", "legacy_extended_profile", "is_profile_translatable", "has_hidden_subscriptions_on_profile", "verification_info", "highlights_info", "business_account", "creator_subscriptions_count", "unavailable_message", "reason"]

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
    def from_json(cls, json_str: str) -> TweetDataResult:
        """Create an instance of TweetDataResult from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TweetDataResult:
        """Create an instance of TweetDataResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TweetDataResult.parse_obj(obj)

        _obj = TweetDataResult.parse_obj({
            "typename": obj.get("__typename"),
            "id": obj.get("id"),
            "rest_id": obj.get("rest_id"),
            "affiliates_highlighted_label": obj.get("affiliates_highlighted_label"),
            "has_graduated_access": obj.get("has_graduated_access"),
            "is_blue_verified": obj.get("is_blue_verified"),
            "profile_image_shape": obj.get("profile_image_shape"),
            "legacy": MelanieModelsSharedapiTwitterUserTweetsLegacy.from_dict(obj.get("legacy")) if obj.get("legacy") is not None else None,
            "smart_blocked_by": obj.get("smart_blocked_by"),
            "smart_blocking": obj.get("smart_blocking"),
            "legacy_extended_profile": MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile.from_dict(obj.get("legacy_extended_profile")) if obj.get("legacy_extended_profile") is not None else None,
            "is_profile_translatable": obj.get("is_profile_translatable"),
            "has_hidden_subscriptions_on_profile": obj.get("has_hidden_subscriptions_on_profile"),
            "verification_info": MelanieModelsSharedapiTwitterUserTweetsVerificationInfo.from_dict(obj.get("verification_info")) if obj.get("verification_info") is not None else None,
            "highlights_info": MelanieModelsSharedapiTwitterUserTweetsHighlightsInfo.from_dict(obj.get("highlights_info")) if obj.get("highlights_info") is not None else None,
            "business_account": obj.get("business_account"),
            "creator_subscriptions_count": obj.get("creator_subscriptions_count"),
            "unavailable_message": MelanieModelsSharedapiTwitterUserTweetsUnavailableMessage.from_dict(obj.get("unavailable_message")) if obj.get("unavailable_message") is not None else None,
            "reason": obj.get("reason")
        })
        return _obj


