# ActivityAsset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**small_text** | **object** |  | [optional] 
**large_text** | **object** |  | [optional] 
**small_image** | **object** |  | [optional] 
**large_image** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.activity_asset import ActivityAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityAsset from a JSON string
activity_asset_instance = ActivityAsset.from_json(json)
# print the JSON string representation of the object
print ActivityAsset.to_json()

# convert the object into a dict
activity_asset_dict = activity_asset_instance.to_dict()
# create an instance of ActivityAsset from a dict
activity_asset_form_dict = activity_asset.from_dict(activity_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


