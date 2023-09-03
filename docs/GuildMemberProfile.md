# GuildMemberProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guild_id** | **object** |  | [optional] 
**bio** | **object** |  | [optional] 
**banner** | **object** |  | [optional] 
**accent_color** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.guild_member_profile import GuildMemberProfile

# TODO update the JSON string below
json = "{}"
# create an instance of GuildMemberProfile from a JSON string
guild_member_profile_instance = GuildMemberProfile.from_json(json)
# print the JSON string representation of the object
print GuildMemberProfile.to_json()

# convert the object into a dict
guild_member_profile_dict = guild_member_profile_instance.to_dict()
# create an instance of GuildMemberProfile from a dict
guild_member_profile_form_dict = guild_member_profile.from_dict(guild_member_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


