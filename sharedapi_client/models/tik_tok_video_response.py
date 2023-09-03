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
from sharedapi_client.models.author import Author
from sharedapi_client.models.image_post_info import ImagePostInfo
from sharedapi_client.models.music import Music
from sharedapi_client.models.statistics import Statistics
from sharedapi_client.models.video import Video

class TikTokVideoResponse(BaseModel):
    """
    TikTokVideoResponse
    """
    aweme_id: Optional[Any] = None
    avatar_bytes: Optional[Any] = None
    video_url: Optional[Any] = None
    author_id: Optional[Any] = None
    author: Optional[Author] = None
    avatar_thumb: Optional[Any] = None
    create_time: Optional[Any] = None
    desc: Optional[Any] = None
    direct_download_urls: Optional[Any] = None
    filename: Optional[Any] = None
    id: Optional[Any] = None
    music: Optional[Music] = None
    nickname: Optional[Any] = None
    statistics: Optional[Statistics] = None
    video_bytes: Optional[Any] = None
    share_url: Optional[Any] = None
    video: Optional[Video] = None
    cover_image_url: Optional[Any] = None
    image_post_info: Optional[ImagePostInfo] = None
    embed_color: Optional[Any] = None
    __properties = ["aweme_id", "avatar_bytes", "video_url", "author_id", "author", "avatar_thumb", "create_time", "desc", "direct_download_urls", "filename", "id", "music", "nickname", "statistics", "video_bytes", "share_url", "video", "cover_image_url", "image_post_info", "embed_color"]

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
    def from_json(cls, json_str: str) -> TikTokVideoResponse:
        """Create an instance of TikTokVideoResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of music
        if self.music:
            _dict['music'] = self.music.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video
        if self.video:
            _dict['video'] = self.video.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image_post_info
        if self.image_post_info:
            _dict['image_post_info'] = self.image_post_info.to_dict()
        # set to None if aweme_id (nullable) is None
        # and __fields_set__ contains the field
        if self.aweme_id is None and "aweme_id" in self.__fields_set__:
            _dict['aweme_id'] = None

        # set to None if avatar_bytes (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar_bytes is None and "avatar_bytes" in self.__fields_set__:
            _dict['avatar_bytes'] = None

        # set to None if video_url (nullable) is None
        # and __fields_set__ contains the field
        if self.video_url is None and "video_url" in self.__fields_set__:
            _dict['video_url'] = None

        # set to None if author_id (nullable) is None
        # and __fields_set__ contains the field
        if self.author_id is None and "author_id" in self.__fields_set__:
            _dict['author_id'] = None

        # set to None if avatar_thumb (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar_thumb is None and "avatar_thumb" in self.__fields_set__:
            _dict['avatar_thumb'] = None

        # set to None if create_time (nullable) is None
        # and __fields_set__ contains the field
        if self.create_time is None and "create_time" in self.__fields_set__:
            _dict['create_time'] = None

        # set to None if desc (nullable) is None
        # and __fields_set__ contains the field
        if self.desc is None and "desc" in self.__fields_set__:
            _dict['desc'] = None

        # set to None if direct_download_urls (nullable) is None
        # and __fields_set__ contains the field
        if self.direct_download_urls is None and "direct_download_urls" in self.__fields_set__:
            _dict['direct_download_urls'] = None

        # set to None if filename (nullable) is None
        # and __fields_set__ contains the field
        if self.filename is None and "filename" in self.__fields_set__:
            _dict['filename'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if nickname (nullable) is None
        # and __fields_set__ contains the field
        if self.nickname is None and "nickname" in self.__fields_set__:
            _dict['nickname'] = None

        # set to None if video_bytes (nullable) is None
        # and __fields_set__ contains the field
        if self.video_bytes is None and "video_bytes" in self.__fields_set__:
            _dict['video_bytes'] = None

        # set to None if share_url (nullable) is None
        # and __fields_set__ contains the field
        if self.share_url is None and "share_url" in self.__fields_set__:
            _dict['share_url'] = None

        # set to None if cover_image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.cover_image_url is None and "cover_image_url" in self.__fields_set__:
            _dict['cover_image_url'] = None

        # set to None if embed_color (nullable) is None
        # and __fields_set__ contains the field
        if self.embed_color is None and "embed_color" in self.__fields_set__:
            _dict['embed_color'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TikTokVideoResponse:
        """Create an instance of TikTokVideoResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TikTokVideoResponse.parse_obj(obj)

        _obj = TikTokVideoResponse.parse_obj({
            "aweme_id": obj.get("aweme_id"),
            "avatar_bytes": obj.get("avatar_bytes"),
            "video_url": obj.get("video_url"),
            "author_id": obj.get("author_id"),
            "author": Author.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "avatar_thumb": obj.get("avatar_thumb"),
            "create_time": obj.get("create_time"),
            "desc": obj.get("desc"),
            "direct_download_urls": obj.get("direct_download_urls"),
            "filename": obj.get("filename"),
            "id": obj.get("id"),
            "music": Music.from_dict(obj.get("music")) if obj.get("music") is not None else None,
            "nickname": obj.get("nickname"),
            "statistics": Statistics.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None,
            "video_bytes": obj.get("video_bytes"),
            "share_url": obj.get("share_url"),
            "video": Video.from_dict(obj.get("video")) if obj.get("video") is not None else None,
            "cover_image_url": obj.get("cover_image_url"),
            "image_post_info": ImagePostInfo.from_dict(obj.get("image_post_info")) if obj.get("image_post_info") is not None else None,
            "embed_color": obj.get("embed_color")
        })
        return _obj


