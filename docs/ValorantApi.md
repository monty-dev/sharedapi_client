# sharedapi_client.ValorantApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_valorantuser**](ValorantApi.md#get_valorantuser) | **GET** /api/valorant/{agent}/{tag} | Get Valorant User


# **get_valorantuser**
> ValorantProfileResponse get_valorantuser(agent, tag)

Get Valorant User

Fetch a Valorant user!

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.valorant_profile_response import ValorantProfileResponse
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
    api_instance = sharedapi_client.ValorantApi(api_client)
    agent = None # object | Valorant username
    tag = None # object | Valorant player's tag/discrim

    try:
        # Get Valorant User
        api_response = await api_instance.get_valorantuser(agent, tag)
        print("The response of ValorantApi->get_valorantuser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_valorantuser: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | [**object**](.md)| Valorant username | 
 **tag** | [**object**](.md)| Valorant player&#39;s tag/discrim | 

### Return type

[**ValorantProfileResponse**](ValorantProfileResponse.md)

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

