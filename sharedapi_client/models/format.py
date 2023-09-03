# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel
from sharedapi_client.models.downloader_options import DownloaderOptions
from sharedapi_client.models.http_headers import HttpHeaders

class Format(BaseModel):
    """
    Format
    """
    format_id: Optional[Any] = None
    format_note: Optional[Any] = None
    ext: Optional[Any] = None
    protocol: Optional[Any] = None
    acodec: Optional[Any] = None
    vcodec: Optional[Any] = None
    url: Optional[Any] = None
    width: Optional[Any] = None
    height: Optional[Any] = None
    fps: Optional[Any] = None
    rows: Optional[Any] = None
    columns: Optional[Any] = None
    fragments: Optional[Any] = None
    audio_ext: Optional[Any] = None
    video_ext: Optional[Any] = None
    format: Optional[Any] = None
    resolution: Optional[Any] = None
    http_headers: Optional[HttpHeaders] = None
    asr: Optional[Any] = None
    filesize: Optional[Any] = None
    source_preference: Optional[Any] = None
    audio_channels: Optional[Any] = None
    quality: Optional[Any] = None
    has_drm: Optional[Any] = None
    tbr: Optional[Any] = None
    language: Optional[Any] = None
    language_preference: Optional[Any] = None
    preference: Optional[Any] = None
    dynamic_range: Optional[Any] = None
    abr: Optional[Any] = None
    downloader_options: Optional[DownloaderOptions] = None
    container: Optional[Any] = None
    vbr: Optional[Any] = None
    filesize_approx: Optional[Any] = None
    __properties = ["format_id", "format_note", "ext", "protocol", "acodec", "vcodec", "url", "width", "height", "fps", "rows", "columns", "fragments", "audio_ext", "video_ext", "format", "resolution", "http_headers", "asr", "filesize", "source_preference", "audio_channels", "quality", "has_drm", "tbr", "language", "language_preference", "preference", "dynamic_range", "abr", "downloader_options", "container", "vbr", "filesize_approx"]

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
    def from_json(cls, json_str: str) -> Format:
        """Create an instance of Format from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of http_headers
        if self.http_headers:
            _dict['http_headers'] = self.http_headers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of downloader_options
        if self.downloader_options:
            _dict['downloader_options'] = self.downloader_options.to_dict()
        # set to None if format_id (nullable) is None
        # and __fields_set__ contains the field
        if self.format_id is None and "format_id" in self.__fields_set__:
            _dict['format_id'] = None

        # set to None if format_note (nullable) is None
        # and __fields_set__ contains the field
        if self.format_note is None and "format_note" in self.__fields_set__:
            _dict['format_note'] = None

        # set to None if ext (nullable) is None
        # and __fields_set__ contains the field
        if self.ext is None and "ext" in self.__fields_set__:
            _dict['ext'] = None

        # set to None if protocol (nullable) is None
        # and __fields_set__ contains the field
        if self.protocol is None and "protocol" in self.__fields_set__:
            _dict['protocol'] = None

        # set to None if acodec (nullable) is None
        # and __fields_set__ contains the field
        if self.acodec is None and "acodec" in self.__fields_set__:
            _dict['acodec'] = None

        # set to None if vcodec (nullable) is None
        # and __fields_set__ contains the field
        if self.vcodec is None and "vcodec" in self.__fields_set__:
            _dict['vcodec'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if width (nullable) is None
        # and __fields_set__ contains the field
        if self.width is None and "width" in self.__fields_set__:
            _dict['width'] = None

        # set to None if height (nullable) is None
        # and __fields_set__ contains the field
        if self.height is None and "height" in self.__fields_set__:
            _dict['height'] = None

        # set to None if fps (nullable) is None
        # and __fields_set__ contains the field
        if self.fps is None and "fps" in self.__fields_set__:
            _dict['fps'] = None

        # set to None if rows (nullable) is None
        # and __fields_set__ contains the field
        if self.rows is None and "rows" in self.__fields_set__:
            _dict['rows'] = None

        # set to None if columns (nullable) is None
        # and __fields_set__ contains the field
        if self.columns is None and "columns" in self.__fields_set__:
            _dict['columns'] = None

        # set to None if fragments (nullable) is None
        # and __fields_set__ contains the field
        if self.fragments is None and "fragments" in self.__fields_set__:
            _dict['fragments'] = None

        # set to None if audio_ext (nullable) is None
        # and __fields_set__ contains the field
        if self.audio_ext is None and "audio_ext" in self.__fields_set__:
            _dict['audio_ext'] = None

        # set to None if video_ext (nullable) is None
        # and __fields_set__ contains the field
        if self.video_ext is None and "video_ext" in self.__fields_set__:
            _dict['video_ext'] = None

        # set to None if format (nullable) is None
        # and __fields_set__ contains the field
        if self.format is None and "format" in self.__fields_set__:
            _dict['format'] = None

        # set to None if resolution (nullable) is None
        # and __fields_set__ contains the field
        if self.resolution is None and "resolution" in self.__fields_set__:
            _dict['resolution'] = None

        # set to None if asr (nullable) is None
        # and __fields_set__ contains the field
        if self.asr is None and "asr" in self.__fields_set__:
            _dict['asr'] = None

        # set to None if filesize (nullable) is None
        # and __fields_set__ contains the field
        if self.filesize is None and "filesize" in self.__fields_set__:
            _dict['filesize'] = None

        # set to None if source_preference (nullable) is None
        # and __fields_set__ contains the field
        if self.source_preference is None and "source_preference" in self.__fields_set__:
            _dict['source_preference'] = None

        # set to None if audio_channels (nullable) is None
        # and __fields_set__ contains the field
        if self.audio_channels is None and "audio_channels" in self.__fields_set__:
            _dict['audio_channels'] = None

        # set to None if quality (nullable) is None
        # and __fields_set__ contains the field
        if self.quality is None and "quality" in self.__fields_set__:
            _dict['quality'] = None

        # set to None if has_drm (nullable) is None
        # and __fields_set__ contains the field
        if self.has_drm is None and "has_drm" in self.__fields_set__:
            _dict['has_drm'] = None

        # set to None if tbr (nullable) is None
        # and __fields_set__ contains the field
        if self.tbr is None and "tbr" in self.__fields_set__:
            _dict['tbr'] = None

        # set to None if language (nullable) is None
        # and __fields_set__ contains the field
        if self.language is None and "language" in self.__fields_set__:
            _dict['language'] = None

        # set to None if language_preference (nullable) is None
        # and __fields_set__ contains the field
        if self.language_preference is None and "language_preference" in self.__fields_set__:
            _dict['language_preference'] = None

        # set to None if preference (nullable) is None
        # and __fields_set__ contains the field
        if self.preference is None and "preference" in self.__fields_set__:
            _dict['preference'] = None

        # set to None if dynamic_range (nullable) is None
        # and __fields_set__ contains the field
        if self.dynamic_range is None and "dynamic_range" in self.__fields_set__:
            _dict['dynamic_range'] = None

        # set to None if abr (nullable) is None
        # and __fields_set__ contains the field
        if self.abr is None and "abr" in self.__fields_set__:
            _dict['abr'] = None

        # set to None if container (nullable) is None
        # and __fields_set__ contains the field
        if self.container is None and "container" in self.__fields_set__:
            _dict['container'] = None

        # set to None if vbr (nullable) is None
        # and __fields_set__ contains the field
        if self.vbr is None and "vbr" in self.__fields_set__:
            _dict['vbr'] = None

        # set to None if filesize_approx (nullable) is None
        # and __fields_set__ contains the field
        if self.filesize_approx is None and "filesize_approx" in self.__fields_set__:
            _dict['filesize_approx'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Format:
        """Create an instance of Format from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Format.parse_obj(obj)

        _obj = Format.parse_obj({
            "format_id": obj.get("format_id"),
            "format_note": obj.get("format_note"),
            "ext": obj.get("ext"),
            "protocol": obj.get("protocol"),
            "acodec": obj.get("acodec"),
            "vcodec": obj.get("vcodec"),
            "url": obj.get("url"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "fps": obj.get("fps"),
            "rows": obj.get("rows"),
            "columns": obj.get("columns"),
            "fragments": obj.get("fragments"),
            "audio_ext": obj.get("audio_ext"),
            "video_ext": obj.get("video_ext"),
            "format": obj.get("format"),
            "resolution": obj.get("resolution"),
            "http_headers": HttpHeaders.from_dict(obj.get("http_headers")) if obj.get("http_headers") is not None else None,
            "asr": obj.get("asr"),
            "filesize": obj.get("filesize"),
            "source_preference": obj.get("source_preference"),
            "audio_channels": obj.get("audio_channels"),
            "quality": obj.get("quality"),
            "has_drm": obj.get("has_drm"),
            "tbr": obj.get("tbr"),
            "language": obj.get("language"),
            "language_preference": obj.get("language_preference"),
            "preference": obj.get("preference"),
            "dynamic_range": obj.get("dynamic_range"),
            "abr": obj.get("abr"),
            "downloader_options": DownloaderOptions.from_dict(obj.get("downloader_options")) if obj.get("downloader_options") is not None else None,
            "container": obj.get("container"),
            "vbr": obj.get("vbr"),
            "filesize_approx": obj.get("filesize_approx")
        })
        return _obj

