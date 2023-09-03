# ConnectedAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**name** | **object** |  | [optional] 
**verified** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.connected_account import ConnectedAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccount from a JSON string
connected_account_instance = ConnectedAccount.from_json(json)
# print the JSON string representation of the object
print ConnectedAccount.to_json()

# convert the object into a dict
connected_account_dict = connected_account_instance.to_dict()
# create an instance of ConnectedAccount from a dict
connected_account_form_dict = connected_account.from_dict(connected_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


