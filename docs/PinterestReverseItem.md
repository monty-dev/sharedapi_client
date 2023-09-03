# PinterestReverseItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_uploaded** | **object** |  | [optional] 
**image_large_url** | **object** |  | [optional] 
**type** | **object** |  | [optional] 
**is_repin** | **object** |  | [optional] 
**link** | **object** |  | [optional] 
**is_video** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**repin_count** | **object** |  | [optional] 
**domain** | **object** |  | [optional] 
**title** | **object** |  | [optional] 
**comment_count** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.pinterest_reverse_item import PinterestReverseItem

# TODO update the JSON string below
json = "{}"
# create an instance of PinterestReverseItem from a JSON string
pinterest_reverse_item_instance = PinterestReverseItem.from_json(json)
# print the JSON string representation of the object
print PinterestReverseItem.to_json()

# convert the object into a dict
pinterest_reverse_item_dict = pinterest_reverse_item_instance.to_dict()
# create an instance of PinterestReverseItem from a dict
pinterest_reverse_item_form_dict = pinterest_reverse_item.from_dict(pinterest_reverse_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


