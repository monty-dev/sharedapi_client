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


class ConnectedAccount(BaseModel):
    """ConnectedAccount."""

    type: Optional[Any] = None
    id: Optional[Any] = None
    name: Optional[Any] = None
    verified: Optional[Any] = None
    __properties = ["type", "id", "name", "verified"]

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
    def from_json(cls, json_str: str) -> ConnectedAccount:
        """Create an instance of ConnectedAccount from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict["type"] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict["id"] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict["name"] = None

        # set to None if verified (nullable) is None
        # and __fields_set__ contains the field
        if self.verified is None and "verified" in self.__fields_set__:
            _dict["verified"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConnectedAccount:
        """Create an instance of ConnectedAccount from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConnectedAccount.parse_obj(obj)

        _obj = ConnectedAccount.parse_obj({"type": obj.get("type"), "id": obj.get("id"), "name": obj.get("name"), "verified": obj.get("verified")})
        return _obj
