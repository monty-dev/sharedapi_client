# InstagramPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** |  | 
**user_id** | **object** |  | 
**guild_id** | **object** |  | 

## Example

```python
from sharedapi_client.models.instagram_post_request import InstagramPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramPostRequest from a JSON string
instagram_post_request_instance = InstagramPostRequest.from_json(json)
# print the JSON string representation of the object
print InstagramPostRequest.to_json()

# convert the object into a dict
instagram_post_request_dict = instagram_post_request_instance.to_dict()
# create an instance of InstagramPostRequest from a dict
instagram_post_request_form_dict = instagram_post_request.from_dict(instagram_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


