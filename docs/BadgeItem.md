# BadgeItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**name** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**image_url** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.badge_item import BadgeItem

# TODO update the JSON string below
json = "{}"
# create an instance of BadgeItem from a JSON string
badge_item_instance = BadgeItem.from_json(json)
# print the JSON string representation of the object
print BadgeItem.to_json()

# convert the object into a dict
badge_item_dict = badge_item_instance.to_dict()
# create an instance of BadgeItem from a dict
badge_item_form_dict = badge_item.from_dict(badge_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


