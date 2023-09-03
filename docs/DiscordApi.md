# sharedapi_client.DiscordApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_discord_bio**](DiscordApi.md#fetch_discord_bio) | **GET** /api/discord/bio | Fetch Discord Bio
[**issue_clear_snipe**](DiscordApi.md#issue_clear_snipe) | **DELETE** /api/discord/clearsnipe | Issue Clear Snipe


# **fetch_discord_bio**
> BioResponse fetch_discord_bio(user_id, guild_id=guild_id)

Fetch Discord Bio

fetch a user's bio & server banner

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.bio_response import BioResponse
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
    api_instance = sharedapi_client.DiscordApi(api_client)
    user_id = None # object | 
    guild_id = None # object |  (optional)

    try:
        # Fetch Discord Bio
        api_response = await api_instance.fetch_discord_bio(user_id, guild_id=guild_id)
        print("The response of DiscordApi->fetch_discord_bio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscordApi->fetch_discord_bio: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 
 **guild_id** | [**object**](.md)|  | [optional] 

### Return type

[**BioResponse**](BioResponse.md)

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

# **issue_clear_snipe**
> DeletionConfirmation issue_clear_snipe(channel_id)

Issue Clear Snipe

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.deletion_confirmation import DeletionConfirmation
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
    api_instance = sharedapi_client.DiscordApi(api_client)
    channel_id = None # object | 

    try:
        # Issue Clear Snipe
        api_response = await api_instance.issue_clear_snipe(channel_id)
        print("The response of DiscordApi->issue_clear_snipe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscordApi->issue_clear_snipe: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 

### Return type

[**DeletionConfirmation**](DeletionConfirmation.md)

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

