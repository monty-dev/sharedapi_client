# InstagramHighlightResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**created_at** | **object** |  | [optional] 
**latest_reel_media** | **object** |  | [optional] 
**media_count** | **object** |  | [optional] 
**items** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.instagram_highlight_response import InstagramHighlightResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramHighlightResponse from a JSON string
instagram_highlight_response_instance = InstagramHighlightResponse.from_json(json)
# print the JSON string representation of the object
print InstagramHighlightResponse.to_json()

# convert the object into a dict
instagram_highlight_response_dict = instagram_highlight_response_instance.to_dict()
# create an instance of InstagramHighlightResponse from a dict
instagram_highlight_response_form_dict = instagram_highlight_response.from_dict(instagram_highlight_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


