# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class BioRequest(BaseModel):
    """
    BioRequest
    """
    user_id: Optional[Any] = Field(...)
    guild_id: Optional[Any] = None
    sig: Optional[Any] = None
    req_user_id: Optional[Any] = None
    timestamp: Optional[Any] = None
    __properties = ["user_id", "guild_id", "sig", "req_user_id", "timestamp"]

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
    def from_json(cls, json_str: str) -> BioRequest:
        """Create an instance of BioRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id is None and "user_id" in self.__fields_set__:
            _dict['user_id'] = None

        # set to None if guild_id (nullable) is None
        # and __fields_set__ contains the field
        if self.guild_id is None and "guild_id" in self.__fields_set__:
            _dict['guild_id'] = None

        # set to None if sig (nullable) is None
        # and __fields_set__ contains the field
        if self.sig is None and "sig" in self.__fields_set__:
            _dict['sig'] = None

        # set to None if req_user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.req_user_id is None and "req_user_id" in self.__fields_set__:
            _dict['req_user_id'] = None

        # set to None if timestamp (nullable) is None
        # and __fields_set__ contains the field
        if self.timestamp is None and "timestamp" in self.__fields_set__:
            _dict['timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BioRequest:
        """Create an instance of BioRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BioRequest.parse_obj(obj)

        _obj = BioRequest.parse_obj({
            "user_id": obj.get("user_id"),
            "guild_id": obj.get("guild_id"),
            "sig": obj.get("sig"),
            "req_user_id": obj.get("req_user_id"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


