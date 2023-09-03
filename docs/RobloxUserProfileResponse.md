# RobloxUserProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 
**follower_count** | **object** |  | [optional] 
**following_count** | **object** |  | [optional] 
**display_name** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**presence** | **object** |  | [optional] 
**has_verified_badge** | **object** |  | [optional] 
**created** | **object** | UTC timestamp of when account was created | [optional] 
**is_banned** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**last_online** | **object** | UTC timestamp of when user last seen online | [optional] 
**last_location** | **object** |  | [optional] 
**avatar_url** | **object** | The Roblox user&#39;s currently wearing image | [optional] 
**badges** | **object** |  | [optional] 
**previous_names** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.roblox_user_profile_response import RobloxUserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RobloxUserProfileResponse from a JSON string
roblox_user_profile_response_instance = RobloxUserProfileResponse.from_json(json)
# print the JSON string representation of the object
print RobloxUserProfileResponse.to_json()

# convert the object into a dict
roblox_user_profile_response_dict = roblox_user_profile_response_instance.to_dict()
# create an instance of RobloxUserProfileResponse from a dict
roblox_user_profile_response_form_dict = roblox_user_profile_response.from_dict(roblox_user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


