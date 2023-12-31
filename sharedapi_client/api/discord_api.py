# coding: utf-8

"""
    Melanie Data API 

    A high performance & centrally cached API service for premium bots. 

    The version of the OpenAPI document:  commit e9b768a rl @ Sep 3 3:07 pm
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated
from typing import overload, Optional, Union, Awaitable

from typing import Any, Optional

from sharedapi_client.models.bio_response import BioResponse
from sharedapi_client.models.deletion_confirmation import DeletionConfirmation

from sharedapi_client.api_client import ApiClient
from sharedapi_client.api_response import ApiResponse
from sharedapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DiscordApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def fetch_discord_bio(self, user_id : Any, guild_id : Optional[Any] = None, **kwargs) -> BioResponse:  # noqa: E501
        ...

    @overload
    def fetch_discord_bio(self, user_id : Any, guild_id : Optional[Any] = None, async_req: Optional[bool]=True, **kwargs) -> BioResponse:  # noqa: E501
        ...

    @validate_arguments
    def fetch_discord_bio(self, user_id : Any, guild_id : Optional[Any] = None, async_req: Optional[bool]=None, **kwargs) -> Union[BioResponse, Awaitable[BioResponse]]:  # noqa: E501
        """Fetch Discord Bio  # noqa: E501

        fetch a user's bio & server banner  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_discord_bio(user_id, guild_id, async_req=True)
        >>> result = thread.get()

        :param user_id: (required)
        :type user_id: object
        :param guild_id:
        :type guild_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BioResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the fetch_discord_bio_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.fetch_discord_bio_with_http_info(user_id, guild_id, **kwargs)  # noqa: E501

    @validate_arguments
    def fetch_discord_bio_with_http_info(self, user_id : Any, guild_id : Optional[Any] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Fetch Discord Bio  # noqa: E501

        fetch a user's bio & server banner  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_discord_bio_with_http_info(user_id, guild_id, async_req=True)
        >>> result = thread.get()

        :param user_id: (required)
        :type user_id: object
        :param guild_id:
        :type guild_id: object
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
        :rtype: tuple(BioResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'user_id',
            'guild_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_discord_bio" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('user_id') is not None:  # noqa: E501
            _query_params.append(('user_id', _params['user_id']))

        if _params.get('guild_id') is not None:  # noqa: E501
            _query_params.append(('guild_id', _params['guild_id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "BioResponse",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/api/discord/bio', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def issue_clear_snipe(self, channel_id : Any, **kwargs) -> DeletionConfirmation:  # noqa: E501
        ...

    @overload
    def issue_clear_snipe(self, channel_id : Any, async_req: Optional[bool]=True, **kwargs) -> DeletionConfirmation:  # noqa: E501
        ...

    @validate_arguments
    def issue_clear_snipe(self, channel_id : Any, async_req: Optional[bool]=None, **kwargs) -> Union[DeletionConfirmation, Awaitable[DeletionConfirmation]]:  # noqa: E501
        """Issue Clear Snipe  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issue_clear_snipe(channel_id, async_req=True)
        >>> result = thread.get()

        :param channel_id: (required)
        :type channel_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeletionConfirmation
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the issue_clear_snipe_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.issue_clear_snipe_with_http_info(channel_id, **kwargs)  # noqa: E501

    @validate_arguments
    def issue_clear_snipe_with_http_info(self, channel_id : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Issue Clear Snipe  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issue_clear_snipe_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param channel_id: (required)
        :type channel_id: object
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
        :rtype: tuple(DeletionConfirmation, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'channel_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method issue_clear_snipe" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('channel_id') is not None:  # noqa: E501
            _query_params.append(('channel_id', _params['channel_id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "DeletionConfirmation",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/api/discord/clearsnipe', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
