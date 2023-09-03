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


class IpScamScore(BaseModel):
    """IpScamScore."""

    ip: Optional[Any] = Field(...)
    score: Optional[Any] = Field(...)
    risk: Optional[Any] = Field(...)
    __properties = ["ip", "score", "risk"]

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
    def from_json(cls, json_str: str) -> IpScamScore:
        """Create an instance of IpScamScore from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if ip (nullable) is None
        # and __fields_set__ contains the field
        if self.ip is None and "ip" in self.__fields_set__:
            _dict["ip"] = None

        # set to None if score (nullable) is None
        # and __fields_set__ contains the field
        if self.score is None and "score" in self.__fields_set__:
            _dict["score"] = None

        # set to None if risk (nullable) is None
        # and __fields_set__ contains the field
        if self.risk is None and "risk" in self.__fields_set__:
            _dict["risk"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IpScamScore:
        """Create an instance of IpScamScore from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IpScamScore.parse_obj(obj)

        _obj = IpScamScore.parse_obj({"ip": obj.get("ip"), "score": obj.get("score"), "risk": obj.get("risk")})
        return _obj
