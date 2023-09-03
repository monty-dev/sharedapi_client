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


class InstagramHighlightMediaItem(BaseModel):
    """InstagramHighlightMediaItem."""

    taken_at: Optional[Any] = None
    is_video: Optional[Any] = Field(...)
    url: Optional[Any] = Field(...)
    __properties = ["taken_at", "is_video", "url"]

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
    def from_json(cls, json_str: str) -> InstagramHighlightMediaItem:
        """Create an instance of InstagramHighlightMediaItem from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if taken_at (nullable) is None
        # and __fields_set__ contains the field
        if self.taken_at is None and "taken_at" in self.__fields_set__:
            _dict["taken_at"] = None

        # set to None if is_video (nullable) is None
        # and __fields_set__ contains the field
        if self.is_video is None and "is_video" in self.__fields_set__:
            _dict["is_video"] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict["url"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstagramHighlightMediaItem:
        """Create an instance of InstagramHighlightMediaItem from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstagramHighlightMediaItem.parse_obj(obj)

        _obj = InstagramHighlightMediaItem.parse_obj({"taken_at": obj.get("taken_at"), "is_video": obj.get("is_video"), "url": obj.get("url")})
        return _obj
