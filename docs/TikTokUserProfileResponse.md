# TikTokUserProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **object** |  | [optional] 
**digg_count** | **object** |  | [optional] 
**follower_count** | **object** |  | [optional] 
**following_count** | **object** |  | [optional] 
**heart** | **object** |  | [optional] 
**unique_id** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**nickname** | **object** |  | [optional] 
**private_account** | **object** |  | [optional] 
**verified** | **object** |  | [optional] 
**video_count** | **object** |  | [optional] 
**signature** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.tik_tok_user_profile_response import TikTokUserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TikTokUserProfileResponse from a JSON string
tik_tok_user_profile_response_instance = TikTokUserProfileResponse.from_json(json)
# print the JSON string representation of the object
print TikTokUserProfileResponse.to_json()

# convert the object into a dict
tik_tok_user_profile_response_dict = tik_tok_user_profile_response_instance.to_dict()
# create an instance of TikTokUserProfileResponse from a dict
tik_tok_user_profile_response_form_dict = tik_tok_user_profile_response.from_dict(tik_tok_user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


