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
from sharedapi_client.models.tik_tok_user_profile_response import TikTokUserProfileResponse

class TiktokTopUserVideoResults(BaseModel):
    """
    TiktokTopUserVideoResults
    """
    count: Optional[Any] = Field(...)
    author: Optional[TikTokUserProfileResponse] = None
    items: Optional[Any] = None
    __properties = ["count", "author", "items"]

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
    def from_json(cls, json_str: str) -> TiktokTopUserVideoResults:
        """Create an instance of TiktokTopUserVideoResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # set to None if count (nullable) is None
        # and __fields_set__ contains the field
        if self.count is None and "count" in self.__fields_set__:
            _dict['count'] = None

        # set to None if items (nullable) is None
        # and __fields_set__ contains the field
        if self.items is None and "items" in self.__fields_set__:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TiktokTopUserVideoResults:
        """Create an instance of TiktokTopUserVideoResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TiktokTopUserVideoResults.parse_obj(obj)

        _obj = TiktokTopUserVideoResults.parse_obj({
            "count": obj.get("count"),
            "author": TikTokUserProfileResponse.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "items": obj.get("items")
        })
        return _obj

