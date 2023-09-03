# GuildMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **object** |  | [optional] 
**is_pending** | **object** |  | [optional] 
**joined_at** | **object** |  | [optional] 
**nick** | **object** |  | [optional] 
**pending** | **object** |  | [optional] 
**premium_since** | **object** |  | [optional] 
**roles** | **object** |  | [optional] 
**user** | [**User1**](User1.md) |  | [optional] 
**bio** | **object** |  | [optional] 
**banner** | **object** |  | [optional] 
**mute** | **object** |  | [optional] 
**deaf** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.guild_member import GuildMember

# TODO update the JSON string below
json = "{}"
# create an instance of GuildMember from a JSON string
guild_member_instance = GuildMember.from_json(json)
# print the JSON string representation of the object
print GuildMember.to_json()

# convert the object into a dict
guild_member_dict = guild_member_instance.to_dict()
# create an instance of GuildMember from a dict
guild_member_form_dict = guild_member.from_dict(guild_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


