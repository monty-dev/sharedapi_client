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


class HttpHeaders1(BaseModel):
    """HttpHeaders1."""

    user_agent: Optional[Any] = Field(None, alias="User-Agent")
    accept: Optional[Any] = Field(None, alias="Accept")
    accept_language: Optional[Any] = Field(None, alias="Accept-Language")
    sec_fetch_mode: Optional[Any] = Field(None, alias="Sec-Fetch-Mode")
    __properties = ["User-Agent", "Accept", "Accept-Language", "Sec-Fetch-Mode"]

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
    def from_json(cls, json_str: str) -> HttpHeaders1:
        """Create an instance of HttpHeaders1 from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if user_agent (nullable) is None
        # and __fields_set__ contains the field
        if self.user_agent is None and "user_agent" in self.__fields_set__:
            _dict["User-Agent"] = None

        # set to None if accept (nullable) is None
        # and __fields_set__ contains the field
        if self.accept is None and "accept" in self.__fields_set__:
            _dict["Accept"] = None

        # set to None if accept_language (nullable) is None
        # and __fields_set__ contains the field
        if self.accept_language is None and "accept_language" in self.__fields_set__:
            _dict["Accept-Language"] = None

        # set to None if sec_fetch_mode (nullable) is None
        # and __fields_set__ contains the field
        if self.sec_fetch_mode is None and "sec_fetch_mode" in self.__fields_set__:
            _dict["Sec-Fetch-Mode"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HttpHeaders1:
        """Create an instance of HttpHeaders1 from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HttpHeaders1.parse_obj(obj)

        _obj = HttpHeaders1.parse_obj(
            {
                "user_agent": obj.get("User-Agent"),
                "accept": obj.get("Accept"),
                "accept_language": obj.get("Accept-Language"),
                "sec_fetch_mode": obj.get("Sec-Fetch-Mode"),
            },
        )
        return _obj
