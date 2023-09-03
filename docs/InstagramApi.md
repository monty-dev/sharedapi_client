# sharedapi_client.InstagramApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_instagram_post**](InstagramApi.md#download_instagram_post) | **POST** /api/instagram/post | Download Instagram Post
[**fetch_stories**](InstagramApi.md#fetch_stories) | **GET** /api/instagram/story/{username} | Fetch Stories
[**get_highlightby_id**](InstagramApi.md#get_highlightby_id) | **GET** /api/instagram/highlight/{highlight_id} | Get Highlight By Id
[**get_highlights**](InstagramApi.md#get_highlights) | **GET** /api/instagram/highlights/{username} | Get Highlights
[**get_instagram_user**](InstagramApi.md#get_instagram_user) | **GET** /api/instagram/{username} | Get Instagram User


# **download_instagram_post**
> InstagramPostResponse download_instagram_post(instagram_post_request)

Download Instagram Post

Fetch an Instagram post, story, reel or other media type.

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.instagram_post_request import InstagramPostRequest
from sharedapi_client.models.instagram_post_response import InstagramPostResponse
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
    api_instance = sharedapi_client.InstagramApi(api_client)
    instagram_post_request = sharedapi_client.InstagramPostRequest() # InstagramPostRequest | 

    try:
        # Download Instagram Post
        api_response = await api_instance.download_instagram_post(instagram_post_request)
        print("The response of InstagramApi->download_instagram_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstagramApi->download_instagram_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instagram_post_request** | [**InstagramPostRequest**](InstagramPostRequest.md)|  | 

### Return type

[**InstagramPostResponse**](InstagramPostResponse.md)

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

# **fetch_stories**
> InstagramStoryResponse fetch_stories(username, force=force)

Fetch Stories

Fetch a users current Instagram story. Does not mark a view on the instagram user.

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.instagram_story_response import InstagramStoryResponse
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
    api_instance = sharedapi_client.InstagramApi(api_client)
    username = None # object | 
    force = None # object | Bypass cache and fetch the latest user stories (optional)

    try:
        # Fetch Stories
        api_response = await api_instance.fetch_stories(username, force=force)
        print("The response of InstagramApi->fetch_stories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstagramApi->fetch_stories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 
 **force** | [**object**](.md)| Bypass cache and fetch the latest user stories | [optional] 

### Return type

[**InstagramStoryResponse**](InstagramStoryResponse.md)

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

# **get_highlightby_id**
> InstagramHighlightResponse get_highlightby_id(highlight_id, force=force)

Get Highlight By Id

Load the media of a highlight

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.instagram_highlight_response import InstagramHighlightResponse
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
    api_instance = sharedapi_client.InstagramApi(api_client)
    highlight_id = None # object | 
    force = None # object |  (optional)

    try:
        # Get Highlight By Id
        api_response = await api_instance.get_highlightby_id(highlight_id, force=force)
        print("The response of InstagramApi->get_highlightby_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstagramApi->get_highlightby_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **highlight_id** | [**object**](.md)|  | 
 **force** | [**object**](.md)|  | [optional] 

### Return type

[**InstagramHighlightResponse**](InstagramHighlightResponse.md)

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

# **get_highlights**
> InstagramHighlightIndexResponse get_highlights(username)

Get Highlights

Fetch a users Instagram highlights

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.instagram_highlight_index_response import InstagramHighlightIndexResponse
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
    api_instance = sharedapi_client.InstagramApi(api_client)
    username = None # object | 

    try:
        # Get Highlights
        api_response = await api_instance.get_highlights(username)
        print("The response of InstagramApi->get_highlights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstagramApi->get_highlights: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 

### Return type

[**InstagramHighlightIndexResponse**](InstagramHighlightIndexResponse.md)

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

# **get_instagram_user**
> InstagramProfileModelResponse get_instagram_user(username, force=force, preload_posts=preload_posts)

Get Instagram User

Fetch an Instagram user's profile with full metadata.

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.instagram_profile_model_response import InstagramProfileModelResponse
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
    api_instance = sharedapi_client.InstagramApi(api_client)
    username = None # object | 
    force = None # object | Force refresh or use cached result (optional)
    preload_posts = None # object | Whether posts should be preemptively loaded into cache on user fetch (optional)

    try:
        # Get Instagram User
        api_response = await api_instance.get_instagram_user(username, force=force, preload_posts=preload_posts)
        print("The response of InstagramApi->get_instagram_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstagramApi->get_instagram_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 
 **force** | [**object**](.md)| Force refresh or use cached result | [optional] 
 **preload_posts** | [**object**](.md)| Whether posts should be preemptively loaded into cache on user fetch | [optional] 

### Return type

[**InstagramProfileModelResponse**](InstagramProfileModelResponse.md)

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

