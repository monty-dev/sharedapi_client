# MMRData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 
**tag** | **object** |  | [optional] 
**current_data** | [**CurrentData**](CurrentData.md) |  | [optional] 
**highest_rank** | [**HighestRank**](HighestRank.md) |  | [optional] 
**by_season** | [**Dict[str, E1A1]**](E1A1.md) |  | [optional] 

## Example

```python
from sharedapi_client.models.mmr_data import MMRData

# TODO update the JSON string below
json = "{}"
# create an instance of MMRData from a JSON string
mmr_data_instance = MMRData.from_json(json)
# print the JSON string representation of the object
print MMRData.to_json()

# convert the object into a dict
mmr_data_dict = mmr_data_instance.to_dict()
# create an instance of MMRData from a dict
mmr_data_form_dict = mmr_data.from_dict(mmr_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


