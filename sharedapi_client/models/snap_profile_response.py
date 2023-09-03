# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class SnapProfileResponse(BaseModel):
    """
    SnapProfileResponse
    """
    username: Optional[Any] = Field(...)
    bio: Optional[Any] = None
    subscriber_count: Optional[Any] = None
    profile_image_url: Optional[Any] = None
    hero_image_url: Optional[Any] = None
    display_name: Optional[Any] = Field(None, description="The in-app name the user has set for their account.")
    snapcode_image_url: Optional[Any] = Field(None, description="Snap QR code.")
    bitmoji_url: Optional[Any] = Field(None, description="Bitmoji, rendered as PNG. Transparent background.")
    bitmoji_background_url: Optional[Any] = Field(None, description="The bitmoji background shown within the Snapchat application")
    one_click_url: Optional[Any] = Field(None, description="Direct link that will open the Snapchat app and allow the user to be added.")
    share_image_url: Optional[Any] = Field(None, description="A Combo image of the user's bitmoji and snapcode")
    story_media: Optional[Any] = None
    spotlight_media: Optional[Any] = None
    __properties = ["username", "bio", "subscriber_count", "profile_image_url", "hero_image_url", "display_name", "snapcode_image_url", "bitmoji_url", "bitmoji_background_url", "one_click_url", "share_image_url", "story_media", "spotlight_media"]

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
    def from_json(cls, json_str: str) -> SnapProfileResponse:
        """Create an instance of SnapProfileResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        # set to None if bio (nullable) is None
        # and __fields_set__ contains the field
        if self.bio is None and "bio" in self.__fields_set__:
            _dict['bio'] = None

        # set to None if subscriber_count (nullable) is None
        # and __fields_set__ contains the field
        if self.subscriber_count is None and "subscriber_count" in self.__fields_set__:
            _dict['subscriber_count'] = None

        # set to None if profile_image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.profile_image_url is None and "profile_image_url" in self.__fields_set__:
            _dict['profile_image_url'] = None

        # set to None if hero_image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.hero_image_url is None and "hero_image_url" in self.__fields_set__:
            _dict['hero_image_url'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['display_name'] = None

        # set to None if snapcode_image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.snapcode_image_url is None and "snapcode_image_url" in self.__fields_set__:
            _dict['snapcode_image_url'] = None

        # set to None if bitmoji_url (nullable) is None
        # and __fields_set__ contains the field
        if self.bitmoji_url is None and "bitmoji_url" in self.__fields_set__:
            _dict['bitmoji_url'] = None

        # set to None if bitmoji_background_url (nullable) is None
        # and __fields_set__ contains the field
        if self.bitmoji_background_url is None and "bitmoji_background_url" in self.__fields_set__:
            _dict['bitmoji_background_url'] = None

        # set to None if one_click_url (nullable) is None
        # and __fields_set__ contains the field
        if self.one_click_url is None and "one_click_url" in self.__fields_set__:
            _dict['one_click_url'] = None

        # set to None if share_image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.share_image_url is None and "share_image_url" in self.__fields_set__:
            _dict['share_image_url'] = None

        # set to None if story_media (nullable) is None
        # and __fields_set__ contains the field
        if self.story_media is None and "story_media" in self.__fields_set__:
            _dict['story_media'] = None

        # set to None if spotlight_media (nullable) is None
        # and __fields_set__ contains the field
        if self.spotlight_media is None and "spotlight_media" in self.__fields_set__:
            _dict['spotlight_media'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SnapProfileResponse:
        """Create an instance of SnapProfileResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SnapProfileResponse.parse_obj(obj)

        _obj = SnapProfileResponse.parse_obj({
            "username": obj.get("username"),
            "bio": obj.get("bio"),
            "subscriber_count": obj.get("subscriber_count"),
            "profile_image_url": obj.get("profile_image_url"),
            "hero_image_url": obj.get("hero_image_url"),
            "display_name": obj.get("display_name"),
            "snapcode_image_url": obj.get("snapcode_image_url"),
            "bitmoji_url": obj.get("bitmoji_url"),
            "bitmoji_background_url": obj.get("bitmoji_background_url"),
            "one_click_url": obj.get("one_click_url"),
            "share_image_url": obj.get("share_image_url"),
            "story_media": obj.get("story_media"),
            "spotlight_media": obj.get("spotlight_media")
        })
        return _obj


