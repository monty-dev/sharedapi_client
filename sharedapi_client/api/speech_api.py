# coding: utf-8

"""Melanie Data API.

A high performance & centrally cached API service for premium bots.

The version of the OpenAPI document:  commit 5b04d15 url_mime @ Aug 30 1:59 pm
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
from typing import Any, Awaitable, Optional, Union, overload

from pydantic import Field, validate_arguments
from typing_extensions import Annotated

from sharedapi_client.api_client import ApiClient
from sharedapi_client.api_response import ApiResponse
from sharedapi_client.exceptions import ApiTypeError, ApiValueError  # noqa: F401
from sharedapi_client.models.stt_result import STTResult
from sharedapi_client.models.tts_result import TTSResult
from sharedapi_client.models.tts_translation_request import TTSTranslationRequest


class SpeechApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def perform_speechto_text(
        self,
        url: Annotated[Any, Field(..., description="URL of the audio or video file.")],
        translate: Annotated[Optional[Any], Field(description="Perform the operation with smart translation")] = None,
        source_langs: Optional[Any] = None,
        target_lang: Optional[Any] = None,
        **kwargs,
    ) -> STTResult:  # noqa: E501
        ...

    @overload
    def perform_speechto_text(
        self,
        url: Annotated[Any, Field(..., description="URL of the audio or video file.")],
        translate: Annotated[Optional[Any], Field(description="Perform the operation with smart translation")] = None,
        source_langs: Optional[Any] = None,
        target_lang: Optional[Any] = None,
        async_req: Optional[bool] = True,
        **kwargs,
    ) -> STTResult:  # noqa: E501
        ...

    @validate_arguments
    def perform_speechto_text(
        self,
        url: Annotated[Any, Field(..., description="URL of the audio or video file.")],
        translate: Annotated[Optional[Any], Field(description="Perform the operation with smart translation")] = None,
        source_langs: Optional[Any] = None,
        target_lang: Optional[Any] = None,
        async_req: Optional[bool] = None,
        **kwargs,
    ) -> Union[STTResult, Awaitable[STTResult]]:  # noqa: E501
        """Perform Speech To Text  # noqa: E501.

        Return the text content of an audio file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.perform_speechto_text(url, translate, source_langs, target_lang, async_req=True)
        >>> result = thread.get()

        :param url: URL of the audio or video file. (required)
        :type url: object
        :param translate: Perform the operation with smart translation
        :type translate: object
        :param source_langs:
        :type source_langs: object
        :param target_lang:
        :type target_lang: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: STTResult
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the perform_speechto_text_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.perform_speechto_text_with_http_info(url, translate, source_langs, target_lang, **kwargs)  # noqa: E501

    @validate_arguments
    def perform_speechto_text_with_http_info(
        self,
        url: Annotated[Any, Field(..., description="URL of the audio or video file.")],
        translate: Annotated[Optional[Any], Field(description="Perform the operation with smart translation")] = None,
        source_langs: Optional[Any] = None,
        target_lang: Optional[Any] = None,
        **kwargs,
    ) -> ApiResponse:  # noqa: E501
        """Perform Speech To Text  # noqa: E501.

        Return the text content of an audio file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.perform_speechto_text_with_http_info(url, translate, source_langs, target_lang, async_req=True)
        >>> result = thread.get()

        :param url: URL of the audio or video file. (required)
        :type url: object
        :param translate: Perform the operation with smart translation
        :type translate: object
        :param source_langs:
        :type source_langs: object
        :param target_lang:
        :type target_lang: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(STTResult, status_code(int), headers(HTTPHeaderDict))
        """
        _params = locals()

        _all_params = [
            "url",
            "translate",
            "source_langs",
            "target_lang",
            "async_req",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
            "_request_auth",
            "_content_type",
            "_headers",
        ]
        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                msg = f"Got an unexpected keyword argument '{_key}' to method perform_speechto_text"
                raise ApiTypeError(msg)
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("url") is not None:  # noqa: E501
            _query_params.append(("url", _params["url"]))

        if _params.get("translate") is not None:  # noqa: E501
            _query_params.append(("translate", _params["translate"]))

        if _params.get("source_langs") is not None:  # noqa: E501
            _query_params.append(("source_langs", _params["source_langs"]))

        if _params.get("target_lang") is not None:  # noqa: E501
            _query_params.append(("target_lang", _params["target_lang"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {"200": "STTResult", "422": "HTTPValidationError"}

        return self.api_client.call_api(
            "/api/speech/stt",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )  # noqa: E501

    @overload
    async def perform_textto_speech(self, tts_translation_request: TTSTranslationRequest, user_id: Optional[Any] = None, **kwargs) -> TTSResult:  # noqa: E501
        ...

    @overload
    def perform_textto_speech(
        self,
        tts_translation_request: TTSTranslationRequest,
        user_id: Optional[Any] = None,
        async_req: Optional[bool] = True,
        **kwargs,
    ) -> TTSResult:  # noqa: E501
        ...

    @validate_arguments
    def perform_textto_speech(
        self,
        tts_translation_request: TTSTranslationRequest,
        user_id: Optional[Any] = None,
        async_req: Optional[bool] = None,
        **kwargs,
    ) -> Union[TTSResult, Awaitable[TTSResult]]:  # noqa: E501
        """Perform Text To Speech  # noqa: E501.

        Generate an MP3 of text input  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.perform_textto_speech(tts_translation_request, user_id, async_req=True)
        >>> result = thread.get()

        :param tts_translation_request: (required)
        :type tts_translation_request: TTSTranslationRequest
        :param user_id:
        :type user_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TTSResult
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the perform_textto_speech_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.perform_textto_speech_with_http_info(tts_translation_request, user_id, **kwargs)  # noqa: E501

    @validate_arguments
    def perform_textto_speech_with_http_info(
        self,
        tts_translation_request: TTSTranslationRequest,
        user_id: Optional[Any] = None,
        **kwargs,
    ) -> ApiResponse:  # noqa: E501
        """Perform Text To Speech  # noqa: E501.

        Generate an MP3 of text input  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.perform_textto_speech_with_http_info(tts_translation_request, user_id, async_req=True)
        >>> result = thread.get()

        :param tts_translation_request: (required)
        :type tts_translation_request: TTSTranslationRequest
        :param user_id:
        :type user_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TTSResult, status_code(int), headers(HTTPHeaderDict))
        """
        _params = locals()

        _all_params = [
            "tts_translation_request",
            "user_id",
            "async_req",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
            "_request_auth",
            "_content_type",
            "_headers",
        ]
        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                msg = f"Got an unexpected keyword argument '{_key}' to method perform_textto_speech"
                raise ApiTypeError(msg)
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("user_id") is not None:  # noqa: E501
            _query_params.append(("user_id", _params["user_id"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["tts_translation_request"] is not None:
            _body_params = _params["tts_translation_request"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        if _content_types_list := _params.get("_content_type", self.api_client.select_header_content_type(["application/json"])):
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {"200": "TTSResult", "422": "HTTPValidationError"}

        return self.api_client.call_api(
            "/api/speech/tts",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )  # noqa: E501
