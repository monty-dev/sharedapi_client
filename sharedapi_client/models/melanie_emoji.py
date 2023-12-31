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

class MelanieEmoji(BaseModel):
    """
    MelanieEmoji
    """
    name: Optional[Any] = None
    id: Optional[Any] = None
    animated: Optional[Any] = None
    url: Optional[Any] = None
    dispaly_name: Optional[Any] = None
    __properties = ["name", "id", "animated", "url", "dispaly_name"]

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
    def from_json(cls, json_str: str) -> MelanieEmoji:
        """Create an instance of MelanieEmoji from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if animated (nullable) is None
        # and __fields_set__ contains the field
        if self.animated is None and "animated" in self.__fields_set__:
            _dict['animated'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if dispaly_name (nullable) is None
        # and __fields_set__ contains the field
        if self.dispaly_name is None and "dispaly_name" in self.__fields_set__:
            _dict['dispaly_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieEmoji:
        """Create an instance of MelanieEmoji from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieEmoji.parse_obj(obj)

        _obj = MelanieEmoji.parse_obj({
            "name": obj.get("name"),
            "id": obj.get("id"),
            "animated": obj.get("animated"),
            "url": obj.get("url"),
            "dispaly_name": obj.get("dispaly_name")
        })
        return _obj


