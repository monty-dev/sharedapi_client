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
from sharedapi_client.models.caption import Caption

class InstagramPostItem(BaseModel):
    """
    InstagramPostItem
    """
    id: Optional[Any] = None
    title: Optional[Any] = None
    reply_count: Optional[Any] = None
    taken_at: Optional[Any] = None
    comment_count: Optional[Any] = None
    is_video: Optional[Any] = None
    like_count: Optional[Any] = None
    view_count: Optional[Any] = None
    sidecars: Optional[Any] = None
    sidecar_count: Optional[Any] = None
    image_url: Optional[Any] = None
    image_filename: Optional[Any] = None
    video_url: Optional[Any] = None
    video_filename: Optional[Any] = None
    video_duration: Optional[Any] = None
    caption: Optional[Caption] = None
    preview_image_url: Optional[Any] = None
    preview_image_filename: Optional[Any] = None
    __properties = ["id", "title", "reply_count", "taken_at", "comment_count", "is_video", "like_count", "view_count", "sidecars", "sidecar_count", "image_url", "image_filename", "video_url", "video_filename", "video_duration", "caption", "preview_image_url", "preview_image_filename"]

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
    def from_json(cls, json_str: str) -> InstagramPostItem:
        """Create an instance of InstagramPostItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of caption
        if self.caption:
            _dict['caption'] = self.caption.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        # set to None if reply_count (nullable) is None
        # and __fields_set__ contains the field
        if self.reply_count is None and "reply_count" in self.__fields_set__:
            _dict['reply_count'] = None

        # set to None if taken_at (nullable) is None
        # and __fields_set__ contains the field
        if self.taken_at is None and "taken_at" in self.__fields_set__:
            _dict['taken_at'] = None

        # set to None if comment_count (nullable) is None
        # and __fields_set__ contains the field
        if self.comment_count is None and "comment_count" in self.__fields_set__:
            _dict['comment_count'] = None

        # set to None if is_video (nullable) is None
        # and __fields_set__ contains the field
        if self.is_video is None and "is_video" in self.__fields_set__:
            _dict['is_video'] = None

        # set to None if like_count (nullable) is None
        # and __fields_set__ contains the field
        if self.like_count is None and "like_count" in self.__fields_set__:
            _dict['like_count'] = None

        # set to None if view_count (nullable) is None
        # and __fields_set__ contains the field
        if self.view_count is None and "view_count" in self.__fields_set__:
            _dict['view_count'] = None

        # set to None if sidecars (nullable) is None
        # and __fields_set__ contains the field
        if self.sidecars is None and "sidecars" in self.__fields_set__:
            _dict['sidecars'] = None

        # set to None if sidecar_count (nullable) is None
        # and __fields_set__ contains the field
        if self.sidecar_count is None and "sidecar_count" in self.__fields_set__:
            _dict['sidecar_count'] = None

        # set to None if image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_url is None and "image_url" in self.__fields_set__:
            _dict['image_url'] = None

        # set to None if image_filename (nullable) is None
        # and __fields_set__ contains the field
        if self.image_filename is None and "image_filename" in self.__fields_set__:
            _dict['image_filename'] = None

        # set to None if video_url (nullable) is None
        # and __fields_set__ contains the field
        if self.video_url is None and "video_url" in self.__fields_set__:
            _dict['video_url'] = None

        # set to None if video_filename (nullable) is None
        # and __fields_set__ contains the field
        if self.video_filename is None and "video_filename" in self.__fields_set__:
            _dict['video_filename'] = None

        # set to None if video_duration (nullable) is None
        # and __fields_set__ contains the field
        if self.video_duration is None and "video_duration" in self.__fields_set__:
            _dict['video_duration'] = None

        # set to None if preview_image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.preview_image_url is None and "preview_image_url" in self.__fields_set__:
            _dict['preview_image_url'] = None

        # set to None if preview_image_filename (nullable) is None
        # and __fields_set__ contains the field
        if self.preview_image_filename is None and "preview_image_filename" in self.__fields_set__:
            _dict['preview_image_filename'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstagramPostItem:
        """Create an instance of InstagramPostItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstagramPostItem.parse_obj(obj)

        _obj = InstagramPostItem.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "reply_count": obj.get("reply_count"),
            "taken_at": obj.get("taken_at"),
            "comment_count": obj.get("comment_count"),
            "is_video": obj.get("is_video"),
            "like_count": obj.get("like_count"),
            "view_count": obj.get("view_count"),
            "sidecars": obj.get("sidecars"),
            "sidecar_count": obj.get("sidecar_count"),
            "image_url": obj.get("image_url"),
            "image_filename": obj.get("image_filename"),
            "video_url": obj.get("video_url"),
            "video_filename": obj.get("video_filename"),
            "video_duration": obj.get("video_duration"),
            "caption": Caption.from_dict(obj.get("caption")) if obj.get("caption") is not None else None,
            "preview_image_url": obj.get("preview_image_url"),
            "preview_image_filename": obj.get("preview_image_filename")
        })
        return _obj


