# CurrentData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currenttier** | **object** |  | [optional] 
**currenttierpatched** | **object** |  | [optional] 
**images** | [**DatumImages**](DatumImages.md) |  | [optional] 
**ranking_in_tier** | **object** |  | [optional] 
**mmr_change_to_last_game** | **object** |  | [optional] 
**elo** | **object** |  | [optional] 
**games_needed_for_rating** | **object** |  | [optional] 
**old** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.current_data import CurrentData

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentData from a JSON string
current_data_instance = CurrentData.from_json(json)
# print the JSON string representation of the object
print CurrentData.to_json()

# convert the object into a dict
current_data_dict = current_data_instance.to_dict()
# create an instance of CurrentData from a dict
current_data_form_dict = current_data.from_dict(current_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


