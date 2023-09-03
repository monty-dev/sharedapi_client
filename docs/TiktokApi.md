# sharedapi_client.TiktokApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_tik_tok_post**](TiktokApi.md#download_tik_tok_post) | **POST** /api/tiktok/post | Download Tiktok Post
[**fetch_user_top_tik_toks**](TiktokApi.md#fetch_user_top_tik_toks) | **GET** /api/tiktok/{username}/top | Fetch User Top Tiktoks
[**get_tik_tok_user**](TiktokApi.md#get_tik_tok_user) | **GET** /api/tiktok/{username} | Get Tiktok User
[**getrecentuser_tik_toks**](TiktokApi.md#getrecentuser_tik_toks) | **GET** /api/tiktok/{username}/recent | Get Recent User Tiktoks


# **download_tik_tok_post**
> TikTokVideoResponse download_tik_tok_post(tiktok_post_request, user_id=user_id)

Download Tiktok Post

Download a TikTok post and its associated metadata.

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.tik_tok_video_response import TikTokVideoResponse
from sharedapi_client.models.tiktok_post_request import TiktokPostRequest
from sharedapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.melaniebot.net
# See configuration.py for a list of all supported configuration parameters.
configuration = sharedapi_client.Configuration(
    host = "https://dev.melaniebot.net"
)


# Enter a context with an instance of the API client
async with sharedapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sharedapi_client.TiktokApi(api_client)
    tiktok_post_request = sharedapi_client.TiktokPostRequest() # TiktokPostRequest | 
    user_id = None # object |  (optional)

    try:
        # Download Tiktok Post
        api_response = await api_instance.download_tik_tok_post(tiktok_post_request, user_id=user_id)
        print("The response of TiktokApi->download_tik_tok_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiktokApi->download_tik_tok_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tiktok_post_request** | [**TiktokPostRequest**](TiktokPostRequest.md)|  | 
 **user_id** | [**object**](.md)|  | [optional] 

### Return type

[**TikTokVideoResponse**](TikTokVideoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_top_tik_toks**
> TiktokTopUserVideoResults fetch_user_top_tik_toks(username, limit=limit)

Fetch User Top Tiktoks

Fetch all TikToks posted by the user and sort them by play count.

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.tiktok_top_user_video_results import TiktokTopUserVideoResults
from sharedapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.melaniebot.net
# See configuration.py for a list of all supported configuration parameters.
configuration = sharedapi_client.Configuration(
    host = "https://dev.melaniebot.net"
)


# Enter a context with an instance of the API client
async with sharedapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sharedapi_client.TiktokApi(api_client)
    username = None # object | 
    limit = None # object |  (optional)

    try:
        # Fetch User Top Tiktoks
        api_response = await api_instance.fetch_user_top_tik_toks(username, limit=limit)
        print("The response of TiktokApi->fetch_user_top_tik_toks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiktokApi->fetch_user_top_tik_toks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 
 **limit** | [**object**](.md)|  | [optional] 

### Return type

[**TiktokTopUserVideoResults**](TiktokTopUserVideoResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tik_tok_user**
> TikTokUserProfileResponse get_tik_tok_user(username)

Get Tiktok User

Receive full metadata of a user's TikTok profile.

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.tik_tok_user_profile_response import TikTokUserProfileResponse
from sharedapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.melaniebot.net
# See configuration.py for a list of all supported configuration parameters.
configuration = sharedapi_client.Configuration(
    host = "https://dev.melaniebot.net"
)


# Enter a context with an instance of the API client
async with sharedapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sharedapi_client.TiktokApi(api_client)
    username = None # object | 

    try:
        # Get Tiktok User
        api_response = await api_instance.get_tik_tok_user(username)
        print("The response of TiktokApi->get_tik_tok_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiktokApi->get_tik_tok_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 

### Return type

[**TikTokUserProfileResponse**](TikTokUserProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getrecentuser_tik_toks**
> TiktokTopUserVideoResults getrecentuser_tik_toks(username)

Get Recent User Tiktoks

Fetch the inital (most recent) TikToks posted by the user

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.tiktok_top_user_video_results import TiktokTopUserVideoResults
from sharedapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.melaniebot.net
# See configuration.py for a list of all supported configuration parameters.
configuration = sharedapi_client.Configuration(
    host = "https://dev.melaniebot.net"
)


# Enter a context with an instance of the API client
async with sharedapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sharedapi_client.TiktokApi(api_client)
    username = None # object | 

    try:
        # Get Recent User Tiktoks
        api_response = await api_instance.getrecentuser_tik_toks(username)
        print("The response of TiktokApi->getrecentuser_tik_toks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TiktokApi->getrecentuser_tik_toks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 

### Return type

[**TiktokTopUserVideoResults**](TiktokTopUserVideoResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

