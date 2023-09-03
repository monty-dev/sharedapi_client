# InstagramUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** |  | [optional] 
**full_name** | **object** |  | [optional] 
**is_private** | **object** |  | [optional] 
**avatar_filename** | **object** |  | [optional] 
**avatar_url** | **object** |  | [optional] 
**is_verified** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.instagram_user_response import InstagramUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramUserResponse from a JSON string
instagram_user_response_instance = InstagramUserResponse.from_json(json)
# print the JSON string representation of the object
print InstagramUserResponse.to_json()

# convert the object into a dict
instagram_user_response_dict = instagram_user_response_instance.to_dict()
# create an instance of InstagramUserResponse from a dict
instagram_user_response_form_dict = instagram_user_response.from_dict(instagram_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


