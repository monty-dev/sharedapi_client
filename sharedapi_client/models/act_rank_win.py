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

class ActRankWin(BaseModel):
    """
    ActRankWin
    """
    patched_tier: Optional[Any] = None
    tier: Optional[Any] = None
    __properties = ["patched_tier", "tier"]

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
    def from_json(cls, json_str: str) -> ActRankWin:
        """Create an instance of ActRankWin from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if patched_tier (nullable) is None
        # and __fields_set__ contains the field
        if self.patched_tier is None and "patched_tier" in self.__fields_set__:
            _dict['patched_tier'] = None

        # set to None if tier (nullable) is None
        # and __fields_set__ contains the field
        if self.tier is None and "tier" in self.__fields_set__:
            _dict['tier'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActRankWin:
        """Create an instance of ActRankWin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActRankWin.parse_obj(obj)

        _obj = ActRankWin.parse_obj({
            "patched_tier": obj.get("patched_tier"),
            "tier": obj.get("tier")
        })
        return _obj

