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

class InstagramHighlightIndexResponse(BaseModel):
    """
    InstagramHighlightIndexResponse
    """
    count: Optional[Any] = None
    highlights: Optional[Any] = None
    __properties = ["count", "highlights"]

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
    def from_json(cls, json_str: str) -> InstagramHighlightIndexResponse:
        """Create an instance of InstagramHighlightIndexResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if count (nullable) is None
        # and __fields_set__ contains the field
        if self.count is None and "count" in self.__fields_set__:
            _dict['count'] = None

        # set to None if highlights (nullable) is None
        # and __fields_set__ contains the field
        if self.highlights is None and "highlights" in self.__fields_set__:
            _dict['highlights'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstagramHighlightIndexResponse:
        """Create an instance of InstagramHighlightIndexResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstagramHighlightIndexResponse.parse_obj(obj)

        _obj = InstagramHighlightIndexResponse.parse_obj({
            "count": obj.get("count"),
            "highlights": obj.get("highlights")
        })
        return _obj


