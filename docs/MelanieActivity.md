# MelanieActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 
**primary** | **object** |  | [optional] 
**emoji** | [**MelanieEmoji**](MelanieEmoji.md) |  | [optional] 
**created_at** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**assets** | [**ActivityAsset**](ActivityAsset.md) |  | [optional] 
**spotify_data** | [**SpotifyData**](SpotifyData.md) |  | [optional] 
**state** | **object** |  | [optional] 
**flags** | **object** |  | [optional] 
**type** | **object** |  | [optional] 
**color** | [**ColorPalette**](ColorPalette.md) |  | [optional] 
**application_id** | **object** |  | [optional] 
**session_id** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.melanie_activity import MelanieActivity

# TODO update the JSON string below
json = "{}"
# create an instance of MelanieActivity from a JSON string
melanie_activity_instance = MelanieActivity.from_json(json)
# print the JSON string representation of the object
print MelanieActivity.to_json()

# convert the object into a dict
melanie_activity_dict = melanie_activity_instance.to_dict()
# create an instance of MelanieActivity from a dict
melanie_activity_form_dict = melanie_activity.from_dict(melanie_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


