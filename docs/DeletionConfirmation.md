# DeletionConfirmation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **object** |  | 
**confirmed_by** | **object** |  | [optional] 
**deleted_items** | **object** |  | [optional] 
**sig** | **object** |  | 

## Example

```python
from sharedapi_client.models.deletion_confirmation import DeletionConfirmation

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionConfirmation from a JSON string
deletion_confirmation_instance = DeletionConfirmation.from_json(json)
# print the JSON string representation of the object
print DeletionConfirmation.to_json()

# convert the object into a dict
deletion_confirmation_dict = deletion_confirmation_instance.to_dict()
# create an instance of DeletionConfirmation from a dict
deletion_confirmation_form_dict = deletion_confirmation.from_dict(deletion_confirmation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


