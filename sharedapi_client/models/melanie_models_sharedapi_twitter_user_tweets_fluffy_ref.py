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

class MelanieModelsSharedapiTwitterUserTweetsFluffyRef(BaseModel):
    """
    MelanieModelsSharedapiTwitterUserTweetsFluffyRef
    """
    url: Optional[Any] = None
    url_type: Optional[Any] = None
    __properties = ["url", "url_type"]

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
    def from_json(cls, json_str: str) -> MelanieModelsSharedapiTwitterUserTweetsFluffyRef:
        """Create an instance of MelanieModelsSharedapiTwitterUserTweetsFluffyRef from a JSON string"""
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

        # set to None if url_type (nullable) is None
        # and __fields_set__ contains the field
        if self.url_type is None and "url_type" in self.__fields_set__:
            _dict['url_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieModelsSharedapiTwitterUserTweetsFluffyRef:
        """Create an instance of MelanieModelsSharedapiTwitterUserTweetsFluffyRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieModelsSharedapiTwitterUserTweetsFluffyRef.parse_obj(obj)

        _obj = MelanieModelsSharedapiTwitterUserTweetsFluffyRef.parse_obj({
            "url": obj.get("url"),
            "url_type": obj.get("url_type")
        })
        return _obj


