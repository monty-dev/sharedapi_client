# InstagramStoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**InstagramUserResponse**](InstagramUserResponse.md) |  | [optional] 
**items** | **object** |  | [optional] 
**item_count** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.instagram_story_response import InstagramStoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramStoryResponse from a JSON string
instagram_story_response_instance = InstagramStoryResponse.from_json(json)
# print the JSON string representation of the object
print InstagramStoryResponse.to_json()

# convert the object into a dict
instagram_story_response_dict = instagram_story_response_instance.to_dict()
# create an instance of InstagramStoryResponse from a dict
instagram_story_response_form_dict = instagram_story_response.from_dict(instagram_story_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


