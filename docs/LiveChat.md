# LiveChat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **object** |  | [optional] 
**video_id** | **object** |  | [optional] 
**ext** | **object** |  | [optional] 
**protocol** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.live_chat import LiveChat

# TODO update the JSON string below
json = "{}"
# create an instance of LiveChat from a JSON string
live_chat_instance = LiveChat.from_json(json)
# print the JSON string representation of the object
print LiveChat.to_json()

# convert the object into a dict
live_chat_dict = live_chat_instance.to_dict()
# create an instance of LiveChat from a dict
live_chat_form_dict = live_chat.from_dict(live_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


