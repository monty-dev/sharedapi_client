# DiscordUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**username** | **object** |  | [optional] 
**avatar** | **object** |  | [optional] 
**avatar_decoration** | **object** |  | [optional] 
**discriminator** | **object** |  | [optional] 
**public_flags** | **object** |  | [optional] 
**flags** | **object** |  | [optional] 
**banner** | **object** |  | [optional] 
**banner_color** | **object** |  | [optional] 
**accent_color** | **object** |  | [optional] 
**bio** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.discord_user import DiscordUser

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordUser from a JSON string
discord_user_instance = DiscordUser.from_json(json)
# print the JSON string representation of the object
print DiscordUser.to_json()

# convert the object into a dict
discord_user_dict = discord_user_instance.to_dict()
# create an instance of DiscordUser from a dict
discord_user_form_dict = discord_user.from_dict(discord_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


