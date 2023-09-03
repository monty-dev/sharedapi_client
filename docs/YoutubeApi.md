# sharedapi_client.YoutubeApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_you_tube**](YoutubeApi.md#search_you_tube) | **POST** /api/youtube/search | Search Youtube


# **search_you_tube**
> YoutubeSearchResults search_you_tube(yt_search_request)

Search Youtube

Search Youtube for videos given a query

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.yt_search_request import YTSearchRequest
from sharedapi_client.models.youtube_search_results import YoutubeSearchResults
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
    api_instance = sharedapi_client.YoutubeApi(api_client)
    yt_search_request = sharedapi_client.YTSearchRequest() # YTSearchRequest | 

    try:
        # Search Youtube
        api_response = await api_instance.search_you_tube(yt_search_request)
        print("The response of YoutubeApi->search_you_tube:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YoutubeApi->search_you_tube: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yt_search_request** | [**YTSearchRequest**](YTSearchRequest.md)|  | 

### Return type

[**YoutubeSearchResults**](YoutubeSearchResults.md)

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

