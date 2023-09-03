# UserPostItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**shortcode** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**is_video** | **object** |  | [optional] 
**taken_at_timestamp** | **object** |  | [optional] 
**title** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.user_post_item import UserPostItem

# TODO update the JSON string below
json = "{}"
# create an instance of UserPostItem from a JSON string
user_post_item_instance = UserPostItem.from_json(json)
# print the JSON string representation of the object
print UserPostItem.to_json()

# convert the object into a dict
user_post_item_dict = user_post_item_instance.to_dict()
# create an instance of UserPostItem from a dict
user_post_item_form_dict = user_post_item.from_dict(user_post_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


