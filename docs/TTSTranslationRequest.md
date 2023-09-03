# TTSTranslationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **object** |  | 
**speaker_name** | [**Speakers**](Speakers.md) |  | 

## Example

```python
from sharedapi_client.models.tts_translation_request import TTSTranslationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TTSTranslationRequest from a JSON string
tts_translation_request_instance = TTSTranslationRequest.from_json(json)
# print the JSON string representation of the object
print TTSTranslationRequest.to_json()

# convert the object into a dict
tts_translation_request_dict = tts_translation_request_instance.to_dict()
# create an instance of TTSTranslationRequest from a dict
tts_translation_request_form_dict = tts_translation_request.from_dict(tts_translation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


