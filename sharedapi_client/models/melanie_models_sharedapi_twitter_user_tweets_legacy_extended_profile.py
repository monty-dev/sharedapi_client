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
from typing import Optional

from pydantic import BaseModel

from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_birthdate import MelanieModelsSharedapiTwitterUserTweetsBirthdate


class MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile(BaseModel):
    """MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile."""

    birthdate: Optional[MelanieModelsSharedapiTwitterUserTweetsBirthdate] = None
    __properties = ["birthdate"]

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
    def from_json(cls, json_str: str) -> MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile:
        """Create an instance of MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias."""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of birthdate
        if self.birthdate:
            _dict["birthdate"] = self.birthdate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile:
        """Create an instance of MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile.parse_obj(obj)

        return MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile.parse_obj(
            {"birthdate": MelanieModelsSharedapiTwitterUserTweetsBirthdate.from_dict(obj.get("birthdate")) if obj.get("birthdate") is not None else None},
        )
