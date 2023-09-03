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

from pydantic import BaseModel


class PuppeteerLoadMethod(BaseModel):
    """An enumeration."""

    __properties = []

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
    def from_json(cls, json_str: str) -> PuppeteerLoadMethod:
        """Create an instance of PuppeteerLoadMethod from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> PuppeteerLoadMethod:
        """Create an instance of PuppeteerLoadMethod from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PuppeteerLoadMethod.parse_obj(obj)

        return PuppeteerLoadMethod.parse_obj({})
