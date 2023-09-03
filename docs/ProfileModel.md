# ProfileModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**DiscordUser**](DiscordUser.md) |  | [optional] 
**connected_accounts** | **object** |  | [optional] 
**premium_since** | **object** |  | [optional] 
**premium_type** | **object** |  | [optional] 
**premium_guild_since** | **object** |  | [optional] 
**profile_themes_experiment_bucket** | **object** |  | [optional] 
**guild_member** | [**GuildMember**](GuildMember.md) |  | [optional] 
**user_profile** | [**UserProfile**](UserProfile.md) |  | [optional] 
**guild_member_profile** | [**GuildMemberProfile**](GuildMemberProfile.md) |  | [optional] 

## Example

```python
from sharedapi_client.models.profile_model import ProfileModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileModel from a JSON string
profile_model_instance = ProfileModel.from_json(json)
# print the JSON string representation of the object
print ProfileModel.to_json()

# convert the object into a dict
profile_model_dict = profile_model_instance.to_dict()
# create an instance of ProfileModel from a dict
profile_model_form_dict = profile_model.from_dict(profile_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


