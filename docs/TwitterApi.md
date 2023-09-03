# sharedapi_client.TwitterApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_twitteruser**](TwitterApi.md#fetch_twitteruser) | **GET** /api/twitter/{username} | Fetch Twitter User


# **fetch_twitteruser**
> TwitterUserDataRaw fetch_twitteruser(username, force=force)

Fetch Twitter User

Fetch a user's profile info and latest tweets

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.twitter_user_data_raw import TwitterUserDataRaw
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
    api_instance = sharedapi_client.TwitterApi(api_client)
    username = None # object | 
    force = None # object | Force cache update (optional)

    try:
        # Fetch Twitter User
        api_response = await api_instance.fetch_twitteruser(username, force=force)
        print("The response of TwitterApi->fetch_twitteruser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwitterApi->fetch_twitteruser: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 
 **force** | [**object**](.md)| Force cache update | [optional] 

### Return type

[**TwitterUserDataRaw**](TwitterUserDataRaw.md)

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

