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
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_url_class import MelanieModelsSharedapiTwitterScreenNameURLClass

class MelanieModelsSharedapiTwitterScreenNameEntities(BaseModel):
    """
    MelanieModelsSharedapiTwitterScreenNameEntities
    """
    description: Optional[MelanieModelsSharedapiTwitterScreenNameURLClass] = None
    url: Optional[MelanieModelsSharedapiTwitterScreenNameURLClass] = None
    __properties = ["description", "url"]

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
    def from_json(cls, json_str: str) -> MelanieModelsSharedapiTwitterScreenNameEntities:
        """Create an instance of MelanieModelsSharedapiTwitterScreenNameEntities from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of url
        if self.url:
            _dict['url'] = self.url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieModelsSharedapiTwitterScreenNameEntities:
        """Create an instance of MelanieModelsSharedapiTwitterScreenNameEntities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieModelsSharedapiTwitterScreenNameEntities.parse_obj(obj)

        _obj = MelanieModelsSharedapiTwitterScreenNameEntities.parse_obj({
            "description": MelanieModelsSharedapiTwitterScreenNameURLClass.from_dict(obj.get("description")) if obj.get("description") is not None else None,
            "url": MelanieModelsSharedapiTwitterScreenNameURLClass.from_dict(obj.get("url")) if obj.get("url") is not None else None
        })
        return _obj


