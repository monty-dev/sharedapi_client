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
from sharedapi_client.models.melanie_models_sharedapi_twitter_screen_name_reason import MelanieModelsSharedapiTwitterScreenNameReason

class MelanieModelsSharedapiTwitterScreenNameVerificationInfo(BaseModel):
    """
    MelanieModelsSharedapiTwitterScreenNameVerificationInfo
    """
    reason: Optional[MelanieModelsSharedapiTwitterScreenNameReason] = None
    __properties = ["reason"]

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
    def from_json(cls, json_str: str) -> MelanieModelsSharedapiTwitterScreenNameVerificationInfo:
        """Create an instance of MelanieModelsSharedapiTwitterScreenNameVerificationInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reason
        if self.reason:
            _dict['reason'] = self.reason.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MelanieModelsSharedapiTwitterScreenNameVerificationInfo:
        """Create an instance of MelanieModelsSharedapiTwitterScreenNameVerificationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MelanieModelsSharedapiTwitterScreenNameVerificationInfo.parse_obj(obj)

        _obj = MelanieModelsSharedapiTwitterScreenNameVerificationInfo.parse_obj({
            "reason": MelanieModelsSharedapiTwitterScreenNameReason.from_dict(obj.get("reason")) if obj.get("reason") is not None else None
        })
        return _obj


