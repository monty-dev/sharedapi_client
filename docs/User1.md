# User1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**username** | **object** |  | [optional] 
**avatar** | **object** |  | [optional] 
**avatar_decoration** | **object** |  | [optional] 
**discriminator** | **object** |  | [optional] 
**public_flags** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.user1 import User1

# TODO update the JSON string below
json = "{}"
# create an instance of User1 from a JSON string
user1_instance = User1.from_json(json)
# print the JSON string representation of the object
print User1.to_json()

# convert the object into a dict
user1_dict = user1_instance.to_dict()
# create an instance of User1 from a dict
user1_form_dict = user1.from_dict(user1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


