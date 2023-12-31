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

class DownloaderOptions1(BaseModel):
    """
    DownloaderOptions1
    """
    http_chunk_size: Optional[Any] = None
    __properties = ["http_chunk_size"]

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
    def from_json(cls, json_str: str) -> DownloaderOptions1:
        """Create an instance of DownloaderOptions1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if http_chunk_size (nullable) is None
        # and __fields_set__ contains the field
        if self.http_chunk_size is None and "http_chunk_size" in self.__fields_set__:
            _dict['http_chunk_size'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DownloaderOptions1:
        """Create an instance of DownloaderOptions1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DownloaderOptions1.parse_obj(obj)

        _obj = DownloaderOptions1.parse_obj({
            "http_chunk_size": obj.get("http_chunk_size")
        })
        return _obj


