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
from pydantic import BaseModel, Field

class OCRRquest(BaseModel):
    """
    OCRRquest
    """
    url: Optional[Any] = Field(..., description="URL of the image to be read. PNG or JPEG supported. Must be larger than 50x50")
    __properties = ["url"]

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
    def from_json(cls, json_str: str) -> OCRRquest:
        """Create an instance of OCRRquest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OCRRquest:
        """Create an instance of OCRRquest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OCRRquest.parse_obj(obj)

        _obj = OCRRquest.parse_obj({
            "url": obj.get("url")
        })
        return _obj


