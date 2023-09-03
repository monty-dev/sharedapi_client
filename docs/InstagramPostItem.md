# InstagramPostItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**title** | **object** |  | [optional] 
**reply_count** | **object** |  | [optional] 
**taken_at** | **object** |  | [optional] 
**comment_count** | **object** |  | [optional] 
**is_video** | **object** |  | [optional] 
**like_count** | **object** |  | [optional] 
**view_count** | **object** |  | [optional] 
**sidecars** | **object** |  | [optional] 
**sidecar_count** | **object** |  | [optional] 
**image_url** | **object** |  | [optional] 
**image_filename** | **object** |  | [optional] 
**video_url** | **object** |  | [optional] 
**video_filename** | **object** |  | [optional] 
**video_duration** | **object** |  | [optional] 
**caption** | [**Caption**](Caption.md) |  | [optional] 
**preview_image_url** | **object** |  | [optional] 
**preview_image_filename** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.instagram_post_item import InstagramPostItem

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramPostItem from a JSON string
instagram_post_item_instance = InstagramPostItem.from_json(json)
# print the JSON string representation of the object
print InstagramPostItem.to_json()

# convert the object into a dict
instagram_post_item_dict = instagram_post_item_instance.to_dict()
# create an instance of InstagramPostItem from a dict
instagram_post_item_form_dict = instagram_post_item.from_dict(instagram_post_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


