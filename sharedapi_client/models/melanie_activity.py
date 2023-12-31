# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit e9b768a rl @ Sep 3 3:07 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel
from sharedapi_client.models.activity_asset import ActivityAsset
from sharedapi_client.models.color_palette import ColorPalette
from sharedapi_client.models.melanie_emoji import MelanieEmoji
from sharedapi_client.models.spotify_data import SpotifyData

class MelanieActivity(BaseModel):
    """
    MelanieActivity
    """
    name: Optional[Any] = None
    primary: Optional[Any] = None
    emoji: Optional[MelanieEmoji] = None
    created_at: Optional[Any] = None
    url: Optional[Any] = None
    assets: Optional[ActivityAsset] = None
    spotify_data: Optional[SpotifyData] = None
    state: Optional[Any] = None
    flags: Optional[Any] = None
    type: Optional[Any] = None
    color: Optional[ColorPalette] = None
    application_id: Optional[Any] = None
    session_id: Optional[Any] = None
    __properties = ["name", "primary", "emoji", "created_at", "url", "assets", "spotify_data", "state", "flags", "type", "color", "application_id", "session_id"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MelanieActivity:
        """Create an instance of MelanieActivity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of emoji
        if self.emoji:
            _dict['emoji'] = self.emoji.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spotify_data
        if self.spotify_data:
            _dict['spotify_data'] = self.spotify_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of color
        if self.color:
            _dict['color'] = self.color.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if primary (nullable) is None
        # and __fields_set__ contains the field
        if self.primary is None and "primary" in self.__fields_set__:
            _dict['primary'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        # set to None if flags (nullable) is None
        # and __fields_set__ contains the field
        if self.flags is None and "flags" in self.__fields_set__:
            _dict['flags'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if application_id (nullable) is None
        # and __fields_set__ contains the field
        if self.application_id is None and "application_id" in self.__fields_set__:
            _dict['application_id'] = None

        # set to None if session_id (nullable) is None
        # and __fields_set__ contains the field
        if self.session_id is None and "session_id" in self.__fields_set__:
            _dict['session_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieActivity:
        """Create an instance of MelanieActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieActivity.parse_obj(obj)

        _obj = MelanieActivity.parse_obj({
            "name": obj.get("name"),
            "primary": obj.get("primary"),
            "emoji": MelanieEmoji.from_dict(obj.get("emoji")) if obj.get("emoji") is not None else None,
            "created_at": obj.get("created_at"),
            "url": obj.get("url"),
            "assets": ActivityAsset.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "spotify_data": SpotifyData.from_dict(obj.get("spotify_data")) if obj.get("spotify_data") is not None else None,
            "state": obj.get("state"),
            "flags": obj.get("flags"),
            "type": obj.get("type"),
            "color": ColorPalette.from_dict(obj.get("color")) if obj.get("color") is not None else None,
            "application_id": obj.get("application_id"),
            "session_id": obj.get("session_id")
        })
        return _obj


