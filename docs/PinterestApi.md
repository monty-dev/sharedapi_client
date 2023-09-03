# sharedapi_client.PinterestApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pinterestuser**](PinterestApi.md#get_pinterestuser) | **GET** /api/pinterest/{username} | Get Pinterest User
[**reverse_imagesearch**](PinterestApi.md#reverse_imagesearch) | **GET** /api/pinterest/reverse | Reverse Image Search


# **get_pinterestuser**
> PinterestProfileResponse get_pinterestuser(username)

Get Pinterest User

Fetch a pinterest user!

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.pinterest_profile_response import PinterestProfileResponse
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
    api_instance = sharedapi_client.PinterestApi(api_client)
    username = None # object | 

    try:
        # Get Pinterest User
        api_response = await api_instance.get_pinterestuser(username)
        print("The response of PinterestApi->get_pinterestuser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PinterestApi->get_pinterestuser: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 

### Return type

[**PinterestProfileResponse**](PinterestProfileResponse.md)

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

# **reverse_imagesearch**
> PinterestReverseResponse reverse_imagesearch(img_url)

Reverse Image Search

Reverse search a photo on pinterest

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.pinterest_reverse_response import PinterestReverseResponse
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
    api_instance = sharedapi_client.PinterestApi(api_client)
    img_url = None # object | 

    try:
        # Reverse Image Search
        api_response = await api_instance.reverse_imagesearch(img_url)
        print("The response of PinterestApi->reverse_imagesearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PinterestApi->reverse_imagesearch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **img_url** | [**object**](.md)|  | 

### Return type

[**PinterestReverseResponse**](PinterestReverseResponse.md)

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

