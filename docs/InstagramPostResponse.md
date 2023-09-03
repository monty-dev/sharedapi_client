# InstagramPostResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_results** | **object** |  | [optional] 
**share_url** | **object** |  | [optional] 
**author** | [**InstagramUserResponse**](InstagramUserResponse.md) |  | [optional] 
**items** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.instagram_post_response import InstagramPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramPostResponse from a JSON string
instagram_post_response_instance = InstagramPostResponse.from_json(json)
# print the JSON string representation of the object
print InstagramPostResponse.to_json()

# convert the object into a dict
instagram_post_response_dict = instagram_post_response_instance.to_dict()
# create an instance of InstagramPostResponse from a dict
instagram_post_response_form_dict = instagram_post_response.from_dict(instagram_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


