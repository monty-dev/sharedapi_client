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


class MelanieModelsSharedapiTwitterUserTweetsPurpleRef(BaseModel):
    """MelanieModelsSharedapiTwitterUserTweetsPurpleRef."""

    type: Optional[Any] = None
    url: Optional[Any] = None
    url_type: Optional[Any] = Field(None, alias="urlType")
    __properties = ["type", "url", "urlType"]

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
    def from_json(cls, json_str: str) -> MelanieModelsSharedapiTwitterUserTweetsPurpleRef:
        """Create an instance of MelanieModelsSharedapiTwitterUserTweetsPurpleRef from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict["type"] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict["url"] = None

        # set to None if url_type (nullable) is None
        # and __fields_set__ contains the field
        if self.url_type is None and "url_type" in self.__fields_set__:
            _dict["urlType"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieModelsSharedapiTwitterUserTweetsPurpleRef:
        """Create an instance of MelanieModelsSharedapiTwitterUserTweetsPurpleRef from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieModelsSharedapiTwitterUserTweetsPurpleRef.parse_obj(obj)

        _obj = MelanieModelsSharedapiTwitterUserTweetsPurpleRef.parse_obj({"type": obj.get("type"), "url": obj.get("url"), "url_type": obj.get("urlType")})
        return _obj
