# Avatar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **object** |  | [optional] 
**initial** | **object** |  | [optional] 
**accent_color** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.avatar import Avatar

# TODO update the JSON string below
json = "{}"
# create an instance of Avatar from a JSON string
avatar_instance = Avatar.from_json(json)
# print the JSON string representation of the object
print Avatar.to_json()

# convert the object into a dict
avatar_dict = avatar_instance.to_dict()
# create an instance of Avatar from a dict
avatar_form_dict = avatar.from_dict(avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


