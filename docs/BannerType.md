# BannerType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**color** | [**ColorPalette**](ColorPalette.md) |  | [optional] 
**guild_id** | **object** |  | [optional] 
**format** | **object** |  | [optional] 
**user_id** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.banner_type import BannerType

# TODO update the JSON string below
json = "{}"
# create an instance of BannerType from a JSON string
banner_type_instance = BannerType.from_json(json)
# print the JSON string representation of the object
print BannerType.to_json()

# convert the object into a dict
banner_type_dict = banner_type_instance.to_dict()
# create an instance of BannerType from a dict
banner_type_form_dict = banner_type.from_dict(banner_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


