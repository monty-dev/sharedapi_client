# sharedapi_client.WebApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cashappprofile**](WebApi.md#get_cashappprofile) | **GET** /api/cashapp/{username} | Get Cashapp Profile
[**get_telegram_u_ser**](WebApi.md#get_telegram_u_ser) | **GET** /api/web/telegram/{username} | Get Telegram User
[**i_plookup**](WebApi.md#i_plookup) | **GET** /api/web/ip/{address} | Ip Lookup
[**loada_spotifyplaylist**](WebApi.md#loada_spotifyplaylist) | **GET** /api/spotify/playlist/{playlist_id} | Load A Spotify Playlist
[**screenshotweb**](WebApi.md#screenshotweb) | **GET** /api/web/screenshot | Screenshot Web
[**streamaudio**](WebApi.md#streamaudio) | **GET** /fragementStream | Stream Audio


# **get_cashappprofile**
> CashappProfileResponse get_cashappprofile(username)

Get Cashapp Profile

Fetch a Cashapp user!

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.cashapp_profile_response import CashappProfileResponse
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
    api_instance = sharedapi_client.WebApi(api_client)
    username = None # object | 

    try:
        # Get Cashapp Profile
        api_response = await api_instance.get_cashappprofile(username)
        print("The response of WebApi->get_cashappprofile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebApi->get_cashappprofile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 

### Return type

[**CashappProfileResponse**](CashappProfileResponse.md)

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

# **get_telegram_u_ser**
> TelegramProfileResponse get_telegram_u_ser(username)

Get Telegram User

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.telegram_profile_response import TelegramProfileResponse
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
    api_instance = sharedapi_client.WebApi(api_client)
    username = None # object | 

    try:
        # Get Telegram User
        api_response = await api_instance.get_telegram_u_ser(username)
        print("The response of WebApi->get_telegram_u_ser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebApi->get_telegram_u_ser: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 

### Return type

[**TelegramProfileResponse**](TelegramProfileResponse.md)

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

# **i_plookup**
> IPLookupResultResponse i_plookup(address)

Ip Lookup

Get information on an IP address

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.ip_lookup_result_response import IPLookupResultResponse
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
    api_instance = sharedapi_client.WebApi(api_client)
    address = None # object | Full IP address or range to query info on

    try:
        # Ip Lookup
        api_response = await api_instance.i_plookup(address)
        print("The response of WebApi->i_plookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebApi->i_plookup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**object**](.md)| Full IP address or range to query info on | 

### Return type

[**IPLookupResultResponse**](IPLookupResultResponse.md)

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

# **loada_spotifyplaylist**
> object loada_spotifyplaylist(playlist_id, plain=plain, transform=transform, name=name, clean=clean)

Load A Spotify Playlist

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
    api_instance = sharedapi_client.WebApi(api_client)
    playlist_id = None # object | 
    plain = None # object |  (optional)
    transform = None # object |  (optional)
    name = None # object |  (optional)
    clean = None # object |  (optional)

    try:
        # Load A Spotify Playlist
        api_response = await api_instance.loada_spotifyplaylist(playlist_id, plain=plain, transform=transform, name=name, clean=clean)
        print("The response of WebApi->loada_spotifyplaylist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebApi->loada_spotifyplaylist: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | [**object**](.md)|  | 
 **plain** | [**object**](.md)|  | [optional] 
 **transform** | [**object**](.md)|  | [optional] 
 **name** | [**object**](.md)|  | [optional] 
 **clean** | [**object**](.md)|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screenshotweb**
> object screenshotweb(url, user_id=user_id, safe=safe, until=until, nsfw_check=nsfw_check, full_page=full_page, image_type=image_type, imgerr=imgerr)

Screenshot Web

Screenshot a webpage with Chrome

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
    api_instance = sharedapi_client.WebApi(api_client)
    url = None # object | URL to screnshot
    user_id = None # object | User ID requesting the screenshot. (optional)
    safe = None # object | Check the URL's domain against porn malware lists. (optional)
    until = sharedapi_client.PuppeteerLoadMethod() # PuppeteerLoadMethod | puppeteer wait method. (optional)
    nsfw_check = None # object | Run the image result through AI content moderation   (optional)
    full_page = None # object | Waits for page to load, scrolls to bottom (optional)
    image_type = None # object | png or jpeg (optional)
    imgerr = None # object | OK to return an image on failure or send HTTP error code (optional)

    try:
        # Screenshot Web
        api_response = await api_instance.screenshotweb(url, user_id=user_id, safe=safe, until=until, nsfw_check=nsfw_check, full_page=full_page, image_type=image_type, imgerr=imgerr)
        print("The response of WebApi->screenshotweb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebApi->screenshotweb: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| URL to screnshot | 
 **user_id** | [**object**](.md)| User ID requesting the screenshot. | [optional] 
 **safe** | [**object**](.md)| Check the URL&#39;s domain against porn malware lists. | [optional] 
 **until** | [**PuppeteerLoadMethod**](.md)| puppeteer wait method. | [optional] 
 **nsfw_check** | [**object**](.md)| Run the image result through AI content moderation   | [optional] 
 **full_page** | [**object**](.md)| Waits for page to load, scrolls to bottom | [optional] 
 **image_type** | [**object**](.md)| png or jpeg | [optional] 
 **imgerr** | [**object**](.md)| OK to return an image on failure or send HTTP error code | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streamaudio**
> object streamaudio(url)

Stream Audio

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
    api_instance = sharedapi_client.WebApi(api_client)
    url = None # object | 

    try:
        # Stream Audio
        api_response = await api_instance.streamaudio(url)
        print("The response of WebApi->streamaudio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebApi->streamaudio: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

