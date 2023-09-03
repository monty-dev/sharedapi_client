# MelanieEmoji


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**animated** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**dispaly_name** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.melanie_emoji import MelanieEmoji

# TODO update the JSON string below
json = "{}"
# create an instance of MelanieEmoji from a JSON string
melanie_emoji_instance = MelanieEmoji.from_json(json)
# print the JSON string representation of the object
print MelanieEmoji.to_json()

# convert the object into a dict
melanie_emoji_dict = melanie_emoji_instance.to_dict()
# create an instance of MelanieEmoji from a dict
melanie_emoji_form_dict = melanie_emoji.from_dict(melanie_emoji_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


