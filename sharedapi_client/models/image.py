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


from typing import Optional
from pydantic import BaseModel
from sharedapi_client.models.video_icon import VideoIcon

class Image(BaseModel):
    """
    Image
    """
    display_image: Optional[VideoIcon] = None
    __properties = ["display_image"]

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
    def from_json(cls, json_str: str) -> Image:
        """Create an instance of Image from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of display_image
        if self.display_image:
            _dict['display_image'] = self.display_image.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Image:
        """Create an instance of Image from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Image.parse_obj(obj)

        _obj = Image.parse_obj({
            "display_image": VideoIcon.from_dict(obj.get("display_image")) if obj.get("display_image") is not None else None
        })
        return _obj


