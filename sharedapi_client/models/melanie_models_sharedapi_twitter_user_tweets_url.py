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

class MelanieModelsSharedapiTwitterUserTweetsURL(BaseModel):
    """
    MelanieModelsSharedapiTwitterUserTweetsURL
    """
    display_url: Optional[Any] = None
    expanded_url: Optional[Any] = None
    url: Optional[Any] = None
    indices: Optional[Any] = None
    __properties = ["display_url", "expanded_url", "url", "indices"]

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
    def from_json(cls, json_str: str) -> MelanieModelsSharedapiTwitterUserTweetsURL:
        """Create an instance of MelanieModelsSharedapiTwitterUserTweetsURL from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if display_url (nullable) is None
        # and __fields_set__ contains the field
        if self.display_url is None and "display_url" in self.__fields_set__:
            _dict['display_url'] = None

        # set to None if expanded_url (nullable) is None
        # and __fields_set__ contains the field
        if self.expanded_url is None and "expanded_url" in self.__fields_set__:
            _dict['expanded_url'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if indices (nullable) is None
        # and __fields_set__ contains the field
        if self.indices is None and "indices" in self.__fields_set__:
            _dict['indices'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieModelsSharedapiTwitterUserTweetsURL:
        """Create an instance of MelanieModelsSharedapiTwitterUserTweetsURL from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieModelsSharedapiTwitterUserTweetsURL.parse_obj(obj)

        _obj = MelanieModelsSharedapiTwitterUserTweetsURL.parse_obj({
            "display_url": obj.get("display_url"),
            "expanded_url": obj.get("expanded_url"),
            "url": obj.get("url"),
            "indices": obj.get("indices")
        })
        return _obj


