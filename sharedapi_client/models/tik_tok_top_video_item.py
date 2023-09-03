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

class TikTokTopVideoItem(BaseModel):
    """
    TikTokTopVideoItem
    """
    title: Optional[Any] = Field(...)
    plays: Optional[Any] = Field(...)
    url: Optional[Any] = Field(...)
    comments: Optional[Any] = Field(...)
    var_date: Optional[Any] = Field(..., alias="date")
    id: Optional[Any] = Field(...)
    __properties = ["title", "plays", "url", "comments", "date", "id"]

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
    def from_json(cls, json_str: str) -> TikTokTopVideoItem:
        """Create an instance of TikTokTopVideoItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        # set to None if plays (nullable) is None
        # and __fields_set__ contains the field
        if self.plays is None and "plays" in self.__fields_set__:
            _dict['plays'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if comments (nullable) is None
        # and __fields_set__ contains the field
        if self.comments is None and "comments" in self.__fields_set__:
            _dict['comments'] = None

        # set to None if var_date (nullable) is None
        # and __fields_set__ contains the field
        if self.var_date is None and "var_date" in self.__fields_set__:
            _dict['date'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TikTokTopVideoItem:
        """Create an instance of TikTokTopVideoItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TikTokTopVideoItem.parse_obj(obj)

        _obj = TikTokTopVideoItem.parse_obj({
            "title": obj.get("title"),
            "plays": obj.get("plays"),
            "url": obj.get("url"),
            "comments": obj.get("comments"),
            "var_date": obj.get("date"),
            "id": obj.get("id")
        })
        return _obj


