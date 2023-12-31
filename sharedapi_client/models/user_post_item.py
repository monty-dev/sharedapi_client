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

class UserPostItem(BaseModel):
    """
    UserPostItem
    """
    id: Optional[Any] = None
    shortcode: Optional[Any] = None
    url: Optional[Any] = None
    is_video: Optional[Any] = None
    taken_at_timestamp: Optional[Any] = None
    title: Optional[Any] = None
    __properties = ["id", "shortcode", "url", "is_video", "taken_at_timestamp", "title"]

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
    def from_json(cls, json_str: str) -> UserPostItem:
        """Create an instance of UserPostItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if shortcode (nullable) is None
        # and __fields_set__ contains the field
        if self.shortcode is None and "shortcode" in self.__fields_set__:
            _dict['shortcode'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if is_video (nullable) is None
        # and __fields_set__ contains the field
        if self.is_video is None and "is_video" in self.__fields_set__:
            _dict['is_video'] = None

        # set to None if taken_at_timestamp (nullable) is None
        # and __fields_set__ contains the field
        if self.taken_at_timestamp is None and "taken_at_timestamp" in self.__fields_set__:
            _dict['taken_at_timestamp'] = None

        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserPostItem:
        """Create an instance of UserPostItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserPostItem.parse_obj(obj)

        _obj = UserPostItem.parse_obj({
            "id": obj.get("id"),
            "shortcode": obj.get("shortcode"),
            "url": obj.get("url"),
            "is_video": obj.get("is_video"),
            "taken_at_timestamp": obj.get("taken_at_timestamp"),
            "title": obj.get("title")
        })
        return _obj


