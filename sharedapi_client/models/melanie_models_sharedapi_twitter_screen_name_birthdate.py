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


class MelanieModelsSharedapiTwitterScreenNameBirthdate(BaseModel):
    """MelanieModelsSharedapiTwitterScreenNameBirthdate."""

    day: Optional[Any] = None
    month: Optional[Any] = None
    visibility: Optional[Any] = None
    year_visibility: Optional[Any] = None
    __properties = ["day", "month", "visibility", "year_visibility"]

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
    def from_json(cls, json_str: str) -> MelanieModelsSharedapiTwitterScreenNameBirthdate:
        """Create an instance of MelanieModelsSharedapiTwitterScreenNameBirthdate from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if day (nullable) is None
        # and __fields_set__ contains the field
        if self.day is None and "day" in self.__fields_set__:
            _dict["day"] = None

        # set to None if month (nullable) is None
        # and __fields_set__ contains the field
        if self.month is None and "month" in self.__fields_set__:
            _dict["month"] = None

        # set to None if visibility (nullable) is None
        # and __fields_set__ contains the field
        if self.visibility is None and "visibility" in self.__fields_set__:
            _dict["visibility"] = None

        # set to None if year_visibility (nullable) is None
        # and __fields_set__ contains the field
        if self.year_visibility is None and "year_visibility" in self.__fields_set__:
            _dict["year_visibility"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieModelsSharedapiTwitterScreenNameBirthdate:
        """Create an instance of MelanieModelsSharedapiTwitterScreenNameBirthdate from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieModelsSharedapiTwitterScreenNameBirthdate.parse_obj(obj)

        return MelanieModelsSharedapiTwitterScreenNameBirthdate.parse_obj(
            {"day": obj.get("day"), "month": obj.get("month"), "visibility": obj.get("visibility"), "year_visibility": obj.get("year_visibility")},
        )
