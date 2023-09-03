# InstagramProfileModelResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_filename** | **object** |  | [optional] 
**avatar_url** | **object** |  | [optional] 
**bio_links** | **object** |  | [optional] 
**biography** | **object** |  | [optional] 
**external_url** | **object** |  | [optional] 
**followed_by_count** | **object** |  | [optional] 
**following_count** | **object** |  | [optional] 
**full_name** | **object** |  | [optional] 
**has_channel** | **object** |  | [optional] 
**has_clips** | **object** |  | [optional] 
**highlight_reel_count** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**is_business_account** | **object** |  | [optional] 
**is_joined_recently** | **object** |  | [optional] 
**is_private** | **object** |  | [optional] 
**is_professional_account** | **object** |  | [optional] 
**is_verified** | **object** |  | [optional] 
**post_count** | **object** |  | [optional] 
**pronouns** | **object** |  | [optional] 
**username** | **object** |  | [optional] 
**post_items** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.instagram_profile_model_response import InstagramProfileModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramProfileModelResponse from a JSON string
instagram_profile_model_response_instance = InstagramProfileModelResponse.from_json(json)
# print the JSON string representation of the object
print InstagramProfileModelResponse.to_json()

# convert the object into a dict
instagram_profile_model_response_dict = instagram_profile_model_response_instance.to_dict()
# create an instance of InstagramProfileModelResponse from a dict
instagram_profile_model_response_form_dict = instagram_profile_model_response.from_dict(instagram_profile_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


