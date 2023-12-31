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
from sharedapi_client.models.current_data import CurrentData
from sharedapi_client.models.highest_rank import HighestRank

class MMRData(BaseModel):
    """
    MMRData
    """
    name: Optional[Any] = None
    tag: Optional[Any] = None
    current_data: Optional[CurrentData] = None
    highest_rank: Optional[HighestRank] = None
    by_season: Optional[Any] = None
    __properties = ["name", "tag", "current_data", "highest_rank", "by_season"]

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
    def from_json(cls, json_str: str) -> MMRData:
        """Create an instance of MMRData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of current_data
        if self.current_data:
            _dict['current_data'] = self.current_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of highest_rank
        if self.highest_rank:
            _dict['highest_rank'] = self.highest_rank.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if tag (nullable) is None
        # and __fields_set__ contains the field
        if self.tag is None and "tag" in self.__fields_set__:
            _dict['tag'] = None

        # set to None if by_season (nullable) is None
        # and __fields_set__ contains the field
        if self.by_season is None and "by_season" in self.__fields_set__:
            _dict['by_season'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MMRData:
        """Create an instance of MMRData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MMRData.parse_obj(obj)

        _obj = MMRData.parse_obj({
            "name": obj.get("name"),
            "tag": obj.get("tag"),
            "current_data": CurrentData.from_dict(obj.get("current_data")) if obj.get("current_data") is not None else None,
            "highest_rank": HighestRank.from_dict(obj.get("highest_rank")) if obj.get("highest_rank") is not None else None,
        })
        return _obj


