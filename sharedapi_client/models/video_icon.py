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

class VideoIcon(BaseModel):
    """
    VideoIcon
    """
    url_list: Optional[Any] = None
    image_width: Optional[Any] = None
    image_height: Optional[Any] = None
    __properties = ["url_list", "image_width", "image_height"]

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
    def from_json(cls, json_str: str) -> VideoIcon:
        """Create an instance of VideoIcon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if url_list (nullable) is None
        # and __fields_set__ contains the field
        if self.url_list is None and "url_list" in self.__fields_set__:
            _dict['url_list'] = None

        # set to None if image_width (nullable) is None
        # and __fields_set__ contains the field
        if self.image_width is None and "image_width" in self.__fields_set__:
            _dict['image_width'] = None

        # set to None if image_height (nullable) is None
        # and __fields_set__ contains the field
        if self.image_height is None and "image_height" in self.__fields_set__:
            _dict['image_height'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VideoIcon:
        """Create an instance of VideoIcon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VideoIcon.parse_obj(obj)

        _obj = VideoIcon.parse_obj({
            "url_list": obj.get("url_list"),
            "image_width": obj.get("image_width"),
            "image_height": obj.get("image_height")
        })
        return _obj


