# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, Optional

from pydantic import BaseModel, Field


class RobloxUserProfileResponse(BaseModel):
    """RobloxUserProfileResponse."""

    name: Optional[Any] = None
    follower_count: Optional[Any] = None
    following_count: Optional[Any] = None
    display_name: Optional[Any] = None
    description: Optional[Any] = None
    presence: Optional[Any] = None
    has_verified_badge: Optional[Any] = None
    created: Optional[Any] = Field(None, description="UTC timestamp of when account was created")
    is_banned: Optional[Any] = None
    id: Optional[Any] = None
    last_online: Optional[Any] = Field(None, description="UTC timestamp of when user last seen online")
    last_location: Optional[Any] = None
    avatar_url: Optional[Any] = Field(None, description="The Roblox user's currently wearing image")
    badges: Optional[Any] = None
    previous_names: Optional[Any] = None
    __properties = [
        "name",
        "follower_count",
        "following_count",
        "display_name",
        "description",
        "presence",
        "has_verified_badge",
        "created",
        "is_banned",
        "id",
        "last_online",
        "last_location",
        "avatar_url",
        "badges",
        "previous_names",
    ]

    class Config:
        """Pydantic configuration."""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias."""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RobloxUserProfileResponse:
        """Create an instance of RobloxUserProfileResponse from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict["name"] = None

        # set to None if follower_count (nullable) is None
        # and __fields_set__ contains the field
        if self.follower_count is None and "follower_count" in self.__fields_set__:
            _dict["follower_count"] = None

        # set to None if following_count (nullable) is None
        # and __fields_set__ contains the field
        if self.following_count is None and "following_count" in self.__fields_set__:
            _dict["following_count"] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict["display_name"] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict["description"] = None

        # set to None if presence (nullable) is None
        # and __fields_set__ contains the field
        if self.presence is None and "presence" in self.__fields_set__:
            _dict["presence"] = None

        # set to None if has_verified_badge (nullable) is None
        # and __fields_set__ contains the field
        if self.has_verified_badge is None and "has_verified_badge" in self.__fields_set__:
            _dict["has_verified_badge"] = None

        # set to None if created (nullable) is None
        # and __fields_set__ contains the field
        if self.created is None and "created" in self.__fields_set__:
            _dict["created"] = None

        # set to None if is_banned (nullable) is None
        # and __fields_set__ contains the field
        if self.is_banned is None and "is_banned" in self.__fields_set__:
            _dict["is_banned"] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict["id"] = None

        # set to None if last_online (nullable) is None
        # and __fields_set__ contains the field
        if self.last_online is None and "last_online" in self.__fields_set__:
            _dict["last_online"] = None

        # set to None if last_location (nullable) is None
        # and __fields_set__ contains the field
        if self.last_location is None and "last_location" in self.__fields_set__:
            _dict["last_location"] = None

        # set to None if avatar_url (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar_url is None and "avatar_url" in self.__fields_set__:
            _dict["avatar_url"] = None

        # set to None if badges (nullable) is None
        # and __fields_set__ contains the field
        if self.badges is None and "badges" in self.__fields_set__:
            _dict["badges"] = None

        # set to None if previous_names (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_names is None and "previous_names" in self.__fields_set__:
            _dict["previous_names"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RobloxUserProfileResponse:
        """Create an instance of RobloxUserProfileResponse from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RobloxUserProfileResponse.parse_obj(obj)

        return RobloxUserProfileResponse.parse_obj(
            {
                "name": obj.get("name"),
                "follower_count": obj.get("follower_count"),
                "following_count": obj.get("following_count"),
                "display_name": obj.get("display_name"),
                "description": obj.get("description"),
                "presence": obj.get("presence"),
                "has_verified_badge": obj.get("has_verified_badge"),
                "created": obj.get("created"),
                "is_banned": obj.get("is_banned"),
                "id": obj.get("id"),
                "last_online": obj.get("last_online"),
                "last_location": obj.get("last_location"),
                "avatar_url": obj.get("avatar_url"),
                "badges": obj.get("badges"),
                "previous_names": obj.get("previous_names"),
            },
        )
