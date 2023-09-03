# sharedapi_client.AiApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createartwithdalle2**](AiApi.md#createartwithdalle2) | **GET** /api/ai/dalle-2 | Create Art With Dalle-2
[**createcyberpunkavatar**](AiApi.md#createcyberpunkavatar) | **GET** /api/ai/cyberpunk | Create Cyberpunk Avatar
[**createfantasyartavatar**](AiApi.md#createfantasyartavatar) | **GET** /api/ai/creative | Create Fantasy Art Avatar
[**createpixelavatar**](AiApi.md#createpixelavatar) | **GET** /api/ai/avatar | Create Pixel Avatar
[**evaluate_image_safety**](AiApi.md#evaluate_image_safety) | **GET** /api/ai/nsfw_check | Evaluate Image Safety
[**read_textfrom_image**](AiApi.md#read_textfrom_image) | **POST** /api/ai/ocr | Read Text From Image
[**removebackgroundsfromimage**](AiApi.md#removebackgroundsfromimage) | **GET** /api/ai/segment_bg | Remove Backgrounds From Image


# **createartwithdalle2**
> AIImageGenerationResponse createartwithdalle2(idea)

Create Art With Dalle-2

Creative dalle-2 generator

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.ai_image_generation_response import AIImageGenerationResponse
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
    api_instance = sharedapi_client.AiApi(api_client)
    idea = None # object | AI generation prompt

    try:
        # Create Art With Dalle-2
        api_response = await api_instance.createartwithdalle2(idea)
        print("The response of AiApi->createartwithdalle2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->createartwithdalle2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea** | [**object**](.md)| AI generation prompt | 

### Return type

[**AIImageGenerationResponse**](AIImageGenerationResponse.md)

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

# **createcyberpunkavatar**
> AIImageGenerationResponse createcyberpunkavatar(idea)

Create Cyberpunk Avatar

Create a Cyberpunk avatar

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.ai_image_generation_response import AIImageGenerationResponse
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
    api_instance = sharedapi_client.AiApi(api_client)
    idea = None # object | AI generation prompt

    try:
        # Create Cyberpunk Avatar
        api_response = await api_instance.createcyberpunkavatar(idea)
        print("The response of AiApi->createcyberpunkavatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->createcyberpunkavatar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea** | [**object**](.md)| AI generation prompt | 

### Return type

[**AIImageGenerationResponse**](AIImageGenerationResponse.md)

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

# **createfantasyartavatar**
> AIImageGenerationResponse createfantasyartavatar(idea)

Create Fantasy Art Avatar

Creative image generator

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.ai_image_generation_response import AIImageGenerationResponse
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
    api_instance = sharedapi_client.AiApi(api_client)
    idea = None # object | AI generation prompt

    try:
        # Create Fantasy Art Avatar
        api_response = await api_instance.createfantasyartavatar(idea)
        print("The response of AiApi->createfantasyartavatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->createfantasyartavatar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea** | [**object**](.md)| AI generation prompt | 

### Return type

[**AIImageGenerationResponse**](AIImageGenerationResponse.md)

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

# **createpixelavatar**
> AIImageGenerationResponse createpixelavatar(idea)

Create Pixel Avatar

Create a colorful pixel art totally avatar

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.ai_image_generation_response import AIImageGenerationResponse
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
    api_instance = sharedapi_client.AiApi(api_client)
    idea = None # object | AI generation prompt

    try:
        # Create Pixel Avatar
        api_response = await api_instance.createpixelavatar(idea)
        print("The response of AiApi->createpixelavatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->createpixelavatar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea** | [**object**](.md)| AI generation prompt | 

### Return type

[**AIImageGenerationResponse**](AIImageGenerationResponse.md)

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

# **evaluate_image_safety**
> ImageEvaluationResult evaluate_image_safety(url)

Evaluate Image Safety

Returns probabilities of the image containing racy or adult content

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.image_evaluation_result import ImageEvaluationResult
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
    api_instance = sharedapi_client.AiApi(api_client)
    url = None # object | 

    try:
        # Evaluate Image Safety
        api_response = await api_instance.evaluate_image_safety(url)
        print("The response of AiApi->evaluate_image_safety:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->evaluate_image_safety: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)|  | 

### Return type

[**ImageEvaluationResult**](ImageEvaluationResult.md)

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

# **read_textfrom_image**
> OCRReadResponse read_textfrom_image(ocr_rquest)

Read Text From Image

Perform OCR on a text image. Responses may take up to 10 seconds to return!

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.ocr_read_response import OCRReadResponse
from sharedapi_client.models.ocr_rquest import OCRRquest
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
    api_instance = sharedapi_client.AiApi(api_client)
    ocr_rquest = sharedapi_client.OCRRquest() # OCRRquest | 

    try:
        # Read Text From Image
        api_response = await api_instance.read_textfrom_image(ocr_rquest)
        print("The response of AiApi->read_textfrom_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->read_textfrom_image: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_rquest** | [**OCRRquest**](OCRRquest.md)|  | 

### Return type

[**OCRReadResponse**](OCRReadResponse.md)

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

# **removebackgroundsfromimage**
> removebackgroundsfromimage(url)

Remove Backgrounds From Image

Performs AI based image segmentation that is more powerful than traditional rembg tooling.

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
    api_instance = sharedapi_client.AiApi(api_client)
    url = None # object | 

    try:
        # Remove Backgrounds From Image
        await api_instance.removebackgroundsfromimage(url)
    except Exception as e:
        print("Exception when calling AiApi->removebackgroundsfromimage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

