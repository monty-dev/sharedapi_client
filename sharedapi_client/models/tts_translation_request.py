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

from sharedapi_client.models.speakers import Speakers


class TTSTranslationRequest(BaseModel):
    """TTSTranslationRequest."""

    text: Optional[Any] = Field(...)
    speaker_name: Speakers = Field(...)
    __properties = ["text", "speaker_name"]

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
    def from_json(cls, json_str: str) -> TTSTranslationRequest:
        """Create an instance of TTSTranslationRequest from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if text (nullable) is None
        # and __fields_set__ contains the field
        if self.text is None and "text" in self.__fields_set__:
            _dict["text"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TTSTranslationRequest:
        """Create an instance of TTSTranslationRequest from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TTSTranslationRequest.parse_obj(obj)

        _obj = TTSTranslationRequest.parse_obj({"text": obj.get("text"), "speaker_name": obj.get("speaker_name")})
        return _obj
