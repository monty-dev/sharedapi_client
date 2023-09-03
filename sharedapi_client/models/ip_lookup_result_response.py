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
from sharedapi_client.models.country_currency import CountryCurrency
from sharedapi_client.models.country_flag import CountryFlag
from sharedapi_client.models.ip_scam_score import IpScamScore

class IPLookupResultResponse(BaseModel):
    """
    IPLookupResultResponse
    """
    ip: Optional[Any] = None
    fraud_score: Optional[IpScamScore] = None
    hostname: Optional[Any] = None
    city: Optional[Any] = None
    region: Optional[Any] = None
    country: Optional[Any] = None
    country_name: Optional[Any] = None
    country_flag: Optional[CountryFlag] = None
    country_currency: Optional[CountryCurrency] = None
    loc: Optional[Any] = None
    org: Optional[Any] = None
    postal: Optional[Any] = None
    timezone: Optional[Any] = None
    __properties = ["ip", "fraud_score", "hostname", "city", "region", "country", "country_name", "country_flag", "country_currency", "loc", "org", "postal", "timezone"]

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
    def from_json(cls, json_str: str) -> IPLookupResultResponse:
        """Create an instance of IPLookupResultResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of fraud_score
        if self.fraud_score:
            _dict['fraud_score'] = self.fraud_score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country_flag
        if self.country_flag:
            _dict['country_flag'] = self.country_flag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country_currency
        if self.country_currency:
            _dict['country_currency'] = self.country_currency.to_dict()
        # set to None if ip (nullable) is None
        # and __fields_set__ contains the field
        if self.ip is None and "ip" in self.__fields_set__:
            _dict['ip'] = None

        # set to None if hostname (nullable) is None
        # and __fields_set__ contains the field
        if self.hostname is None and "hostname" in self.__fields_set__:
            _dict['hostname'] = None

        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        # set to None if region (nullable) is None
        # and __fields_set__ contains the field
        if self.region is None and "region" in self.__fields_set__:
            _dict['region'] = None

        # set to None if country (nullable) is None
        # and __fields_set__ contains the field
        if self.country is None and "country" in self.__fields_set__:
            _dict['country'] = None

        # set to None if country_name (nullable) is None
        # and __fields_set__ contains the field
        if self.country_name is None and "country_name" in self.__fields_set__:
            _dict['country_name'] = None

        # set to None if loc (nullable) is None
        # and __fields_set__ contains the field
        if self.loc is None and "loc" in self.__fields_set__:
            _dict['loc'] = None

        # set to None if org (nullable) is None
        # and __fields_set__ contains the field
        if self.org is None and "org" in self.__fields_set__:
            _dict['org'] = None

        # set to None if postal (nullable) is None
        # and __fields_set__ contains the field
        if self.postal is None and "postal" in self.__fields_set__:
            _dict['postal'] = None

        # set to None if timezone (nullable) is None
        # and __fields_set__ contains the field
        if self.timezone is None and "timezone" in self.__fields_set__:
            _dict['timezone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IPLookupResultResponse:
        """Create an instance of IPLookupResultResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IPLookupResultResponse.parse_obj(obj)

        _obj = IPLookupResultResponse.parse_obj({
            "ip": obj.get("ip"),
            "fraud_score": IpScamScore.from_dict(obj.get("fraud_score")) if obj.get("fraud_score") is not None else None,
            "hostname": obj.get("hostname"),
            "city": obj.get("city"),
            "region": obj.get("region"),
            "country": obj.get("country"),
            "country_name": obj.get("country_name"),
            "country_flag": CountryFlag.from_dict(obj.get("country_flag")) if obj.get("country_flag") is not None else None,
            "country_currency": CountryCurrency.from_dict(obj.get("country_currency")) if obj.get("country_currency") is not None else None,
            "loc": obj.get("loc"),
            "org": obj.get("org"),
            "postal": obj.get("postal"),
            "timezone": obj.get("timezone")
        })
        return _obj


