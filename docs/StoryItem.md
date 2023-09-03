# StoryItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**is_video** | **object** |  | [optional] 
**filename** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**taken_at** | **object** |  | [optional] 
**video_bytes** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.story_item import StoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of StoryItem from a JSON string
story_item_instance = StoryItem.from_json(json)
# print the JSON string representation of the object
print StoryItem.to_json()

# convert the object into a dict
story_item_dict = story_item_instance.to_dict()
# create an instance of StoryItem from a dict
story_item_form_dict = story_item.from_dict(story_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


