# TelegramProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** |  | 
**name** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**avatar_url** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.telegram_profile_response import TelegramProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramProfileResponse from a JSON string
telegram_profile_response_instance = TelegramProfileResponse.from_json(json)
# print the JSON string representation of the object
print TelegramProfileResponse.to_json()

# convert the object into a dict
telegram_profile_response_dict = telegram_profile_response_instance.to_dict()
# create an instance of TelegramProfileResponse from a dict
telegram_profile_response_form_dict = telegram_profile_response.from_dict(telegram_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


