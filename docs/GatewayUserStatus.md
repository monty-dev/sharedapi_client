# GatewayUserStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **object** |  | [optional] 
**desktop** | **object** |  | [optional] 
**mobile** | **object** |  | [optional] 
**web** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.gateway_user_status import GatewayUserStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayUserStatus from a JSON string
gateway_user_status_instance = GatewayUserStatus.from_json(json)
# print the JSON string representation of the object
print GatewayUserStatus.to_json()

# convert the object into a dict
gateway_user_status_dict = gateway_user_status_instance.to_dict()
# create an instance of GatewayUserStatus from a dict
gateway_user_status_form_dict = gateway_user_status.from_dict(gateway_user_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


