# STTResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **object** |  | [optional] 
**display_text** | **object** |  | [optional] 
**offset** | **object** |  | [optional] 
**duration** | **object** |  | [optional] 
**detected_languages** | **object** |  | [optional] 
**translated_text** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.stt_result import STTResult

# TODO update the JSON string below
json = "{}"
# create an instance of STTResult from a JSON string
stt_result_instance = STTResult.from_json(json)
# print the JSON string representation of the object
print STTResult.to_json()

# convert the object into a dict
stt_result_dict = stt_result_instance.to_dict()
# create an instance of STTResult from a dict
stt_result_form_dict = stt_result.from_dict(stt_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


