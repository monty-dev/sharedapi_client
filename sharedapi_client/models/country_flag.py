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


class CountryFlag(BaseModel):
    """CountryFlag."""

    emoji: Optional[Any] = None
    unicode: Optional[Any] = None
    __properties = ["emoji", "unicode"]

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
    def from_json(cls, json_str: str) -> CountryFlag:
        """Create an instance of CountryFlag from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if emoji (nullable) is None
        # and __fields_set__ contains the field
        if self.emoji is None and "emoji" in self.__fields_set__:
            _dict["emoji"] = None

        # set to None if unicode (nullable) is None
        # and __fields_set__ contains the field
        if self.unicode is None and "unicode" in self.__fields_set__:
            _dict["unicode"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CountryFlag:
        """Create an instance of CountryFlag from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CountryFlag.parse_obj(obj)

        _obj = CountryFlag.parse_obj({"emoji": obj.get("emoji"), "unicode": obj.get("unicode")})
        return _obj
