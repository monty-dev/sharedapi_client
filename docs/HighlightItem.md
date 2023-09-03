# HighlightItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_img** | **object** |  | [optional] 
**title** | **object** |  | [optional] 
**id** | **object** |  | 

## Example

```python
from sharedapi_client.models.highlight_item import HighlightItem

# TODO update the JSON string below
json = "{}"
# create an instance of HighlightItem from a JSON string
highlight_item_instance = HighlightItem.from_json(json)
# print the JSON string representation of the object
print HighlightItem.to_json()

# convert the object into a dict
highlight_item_dict = highlight_item_instance.to_dict()
# create an instance of HighlightItem from a dict
highlight_item_form_dict = highlight_item.from_dict(highlight_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


