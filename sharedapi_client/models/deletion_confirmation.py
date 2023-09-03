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
from pydantic import BaseModel, Field

class DeletionConfirmation(BaseModel):
    """
    DeletionConfirmation
    """
    confirmed: Optional[Any] = Field(...)
    confirmed_by: Optional[Any] = None
    deleted_items: Optional[Any] = None
    sig: Optional[Any] = Field(...)
    __properties = ["confirmed", "confirmed_by", "deleted_items", "sig"]

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
    def from_json(cls, json_str: str) -> DeletionConfirmation:
        """Create an instance of DeletionConfirmation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if confirmed (nullable) is None
        # and __fields_set__ contains the field
        if self.confirmed is None and "confirmed" in self.__fields_set__:
            _dict['confirmed'] = None

        # set to None if confirmed_by (nullable) is None
        # and __fields_set__ contains the field
        if self.confirmed_by is None and "confirmed_by" in self.__fields_set__:
            _dict['confirmed_by'] = None

        # set to None if deleted_items (nullable) is None
        # and __fields_set__ contains the field
        if self.deleted_items is None and "deleted_items" in self.__fields_set__:
            _dict['deleted_items'] = None

        # set to None if sig (nullable) is None
        # and __fields_set__ contains the field
        if self.sig is None and "sig" in self.__fields_set__:
            _dict['sig'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeletionConfirmation:
        """Create an instance of DeletionConfirmation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeletionConfirmation.parse_obj(obj)

        _obj = DeletionConfirmation.parse_obj({
            "confirmed": obj.get("confirmed"),
            "confirmed_by": obj.get("confirmed_by"),
            "deleted_items": obj.get("deleted_items"),
            "sig": obj.get("sig")
        })
        return _obj


