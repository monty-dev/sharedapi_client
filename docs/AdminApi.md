# sharedapi_client.AdminApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteamediacacheobject**](AdminApi.md#deleteamediacacheobject) | **DELETE** /api/admin/cache/{target} | Delete A Media Cache Object
[**get_rp_cendpoint**](AdminApi.md#get_rp_cendpoint) | **GET** /api/admin/rpc | Get Rpc Endpoint


# **deleteamediacacheobject**
> CacheDelete deleteamediacacheobject(target)

Delete A Media Cache Object

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.cache_delete import CacheDelete
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
    api_instance = sharedapi_client.AdminApi(api_client)
    target = None # object | 

    try:
        # Delete A Media Cache Object
        api_response = await api_instance.deleteamediacacheobject(target)
        print("The response of AdminApi->deleteamediacacheobject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->deleteamediacacheobject: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | [**object**](.md)|  | 

### Return type

[**CacheDelete**](CacheDelete.md)

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

# **get_rp_cendpoint**
> object get_rp_cendpoint()

Get Rpc Endpoint

Retrive the RPC endpoint that was set at startup

### Example

```python
import time
import os
import sharedapi_client
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
    api_instance = sharedapi_client.AdminApi(api_client)

    try:
        # Get Rpc Endpoint
        api_response = await api_instance.get_rp_cendpoint()
        print("The response of AdminApi->get_rp_cendpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_rp_cendpoint: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

