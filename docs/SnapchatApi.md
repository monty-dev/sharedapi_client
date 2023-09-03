# sharedapi_client.SnapchatApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snapuser**](SnapchatApi.md#get_snapuser) | **GET** /api/snap/{username} | Get Snapuser


# **get_snapuser**
> SnapProfileResponse get_snapuser(username)

Get Snapuser

Fetch a snap user!

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.snap_profile_response import SnapProfileResponse
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
    api_instance = sharedapi_client.SnapchatApi(api_client)
    username = None # object | 

    try:
        # Get Snapuser
        api_response = await api_instance.get_snapuser(username)
        print("The response of SnapchatApi->get_snapuser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapchatApi->get_snapuser: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 

### Return type

[**SnapProfileResponse**](SnapProfileResponse.md)

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

