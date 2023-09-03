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

from pydantic import BaseModel


class User1(BaseModel):
    """User1."""

    id: Optional[Any] = None
    username: Optional[Any] = None
    avatar: Optional[Any] = None
    avatar_decoration: Optional[Any] = None
    discriminator: Optional[Any] = None
    public_flags: Optional[Any] = None
    __properties = ["id", "username", "avatar", "avatar_decoration", "discriminator", "public_flags"]

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
    def from_json(cls, json_str: str) -> User1:
        """Create an instance of User1 from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict["id"] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict["username"] = None

        # set to None if avatar (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar is None and "avatar" in self.__fields_set__:
            _dict["avatar"] = None

        # set to None if avatar_decoration (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar_decoration is None and "avatar_decoration" in self.__fields_set__:
            _dict["avatar_decoration"] = None

        # set to None if discriminator (nullable) is None
        # and __fields_set__ contains the field
        if self.discriminator is None and "discriminator" in self.__fields_set__:
            _dict["discriminator"] = None

        # set to None if public_flags (nullable) is None
        # and __fields_set__ contains the field
        if self.public_flags is None and "public_flags" in self.__fields_set__:
            _dict["public_flags"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User1:
        """Create an instance of User1 from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User1.parse_obj(obj)

        _obj = User1.parse_obj(
            {
                "id": obj.get("id"),
                "username": obj.get("username"),
                "avatar": obj.get("avatar"),
                "avatar_decoration": obj.get("avatar_decoration"),
                "discriminator": obj.get("discriminator"),
                "public_flags": obj.get("public_flags"),
            },
        )
        return _obj
