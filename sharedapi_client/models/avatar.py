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
from pydantic import BaseModel

class Avatar(BaseModel):
    """
    Avatar
    """
    image_url: Optional[Any] = None
    initial: Optional[Any] = None
    accent_color: Optional[Any] = None
    __properties = ["image_url", "initial", "accent_color"]

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
    def from_json(cls, json_str: str) -> Avatar:
        """Create an instance of Avatar from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_url is None and "image_url" in self.__fields_set__:
            _dict['image_url'] = None

        # set to None if initial (nullable) is None
        # and __fields_set__ contains the field
        if self.initial is None and "initial" in self.__fields_set__:
            _dict['initial'] = None

        # set to None if accent_color (nullable) is None
        # and __fields_set__ contains the field
        if self.accent_color is None and "accent_color" in self.__fields_set__:
            _dict['accent_color'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Avatar:
        """Create an instance of Avatar from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Avatar.parse_obj(obj)

        _obj = Avatar.parse_obj({
            "image_url": obj.get("image_url"),
            "initial": obj.get("initial"),
            "accent_color": obj.get("accent_color")
        })
        return _obj

