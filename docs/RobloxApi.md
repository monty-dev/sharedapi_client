# sharedapi_client.RobloxApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_robloxuser**](RobloxApi.md#get_robloxuser) | **GET** /api/roblox/{username} | Get Roblox User


# **get_robloxuser**
> RobloxUserProfileResponse get_robloxuser(username, user_id=user_id)

Get Roblox User

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.roblox_user_profile_response import RobloxUserProfileResponse
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
    api_instance = sharedapi_client.RobloxApi(api_client)
    username = None # object | 
    user_id = None # object |  (optional)

    try:
        # Get Roblox User
        api_response = await api_instance.get_robloxuser(username, user_id=user_id)
        print("The response of RobloxApi->get_robloxuser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobloxApi->get_robloxuser: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 
 **user_id** | [**object**](.md)|  | [optional] 

### Return type

[**RobloxUserProfileResponse**](RobloxUserProfileResponse.md)

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

