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
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_fluffy_ref import MelanieModelsSharedapiTwitterScreenNameFluffyRef

class MelanieModelsSharedapiTwitterScreenNameDescriptionEntity(BaseModel):
    """
    MelanieModelsSharedapiTwitterScreenNameDescriptionEntity
    """
    from_index: Optional[Any] = None
    to_index: Optional[Any] = None
    ref: Optional[MelanieModelsSharedapiTwitterScreenNameFluffyRef] = None
    __properties = ["from_index", "to_index", "ref"]

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
    def from_json(cls, json_str: str) -> MelanieModelsSharedapiTwitterScreenNameDescriptionEntity:
        """Create an instance of MelanieModelsSharedapiTwitterScreenNameDescriptionEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ref
        if self.ref:
            _dict['ref'] = self.ref.to_dict()
        # set to None if from_index (nullable) is None
        # and __fields_set__ contains the field
        if self.from_index is None and "from_index" in self.__fields_set__:
            _dict['from_index'] = None

        # set to None if to_index (nullable) is None
        # and __fields_set__ contains the field
        if self.to_index is None and "to_index" in self.__fields_set__:
            _dict['to_index'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieModelsSharedapiTwitterScreenNameDescriptionEntity:
        """Create an instance of MelanieModelsSharedapiTwitterScreenNameDescriptionEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieModelsSharedapiTwitterScreenNameDescriptionEntity.parse_obj(obj)

        _obj = MelanieModelsSharedapiTwitterScreenNameDescriptionEntity.parse_obj({
            "from_index": obj.get("from_index"),
            "to_index": obj.get("to_index"),
            "ref": MelanieModelsSharedapiTwitterScreenNameFluffyRef.from_dict(obj.get("ref")) if obj.get("ref") is not None else None
        })
        return _obj


