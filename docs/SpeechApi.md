# sharedapi_client.SpeechApi

All URIs are relative to *https://dev.melaniebot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_speechto_text**](SpeechApi.md#perform_speechto_text) | **GET** /api/speech/stt | Perform Speech To Text
[**perform_textto_speech**](SpeechApi.md#perform_textto_speech) | **POST** /api/speech/tts | Perform Text To Speech


# **perform_speechto_text**
> STTResult perform_speechto_text(url, translate=translate, source_langs=source_langs, target_lang=target_lang)

Perform Speech To Text

Return the text content of an audio file

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.stt_result import STTResult
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
    api_instance = sharedapi_client.SpeechApi(api_client)
    url = None # object | URL of the audio or video file.
    translate = None # object | Perform the operation with smart translation (optional)
    source_langs = None # object |  (optional)
    target_lang = None # object |  (optional)

    try:
        # Perform Speech To Text
        api_response = await api_instance.perform_speechto_text(url, translate=translate, source_langs=source_langs, target_lang=target_lang)
        print("The response of SpeechApi->perform_speechto_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpeechApi->perform_speechto_text: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| URL of the audio or video file. | 
 **translate** | [**object**](.md)| Perform the operation with smart translation | [optional] 
 **source_langs** | [**object**](.md)|  | [optional] 
 **target_lang** | [**object**](.md)|  | [optional] 

### Return type

[**STTResult**](STTResult.md)

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

# **perform_textto_speech**
> TTSResult perform_textto_speech(tts_translation_request, user_id=user_id)

Perform Text To Speech

Generate an MP3 of text input

### Example

```python
import time
import os
import sharedapi_client
from sharedapi_client.models.tts_result import TTSResult
from sharedapi_client.models.tts_translation_request import TTSTranslationRequest
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
    api_instance = sharedapi_client.SpeechApi(api_client)
    tts_translation_request = sharedapi_client.TTSTranslationRequest() # TTSTranslationRequest | 
    user_id = None # object |  (optional)

    try:
        # Perform Text To Speech
        api_response = await api_instance.perform_textto_speech(tts_translation_request, user_id=user_id)
        print("The response of SpeechApi->perform_textto_speech:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpeechApi->perform_textto_speech: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tts_translation_request** | [**TTSTranslationRequest**](TTSTranslationRequest.md)|  | 
 **user_id** | [**object**](.md)|  | [optional] 

### Return type

[**TTSResult**](TTSResult.md)

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

