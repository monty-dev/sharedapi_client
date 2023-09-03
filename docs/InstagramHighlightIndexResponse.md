# InstagramHighlightIndexResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **object** |  | [optional] 
**highlights** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.instagram_highlight_index_response import InstagramHighlightIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramHighlightIndexResponse from a JSON string
instagram_highlight_index_response_instance = InstagramHighlightIndexResponse.from_json(json)
# print the JSON string representation of the object
print InstagramHighlightIndexResponse.to_json()

# convert the object into a dict
instagram_highlight_index_response_dict = instagram_highlight_index_response_instance.to_dict()
# create an instance of InstagramHighlightIndexResponse from a dict
instagram_highlight_index_response_form_dict = instagram_highlight_index_response.from_dict(instagram_highlight_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


