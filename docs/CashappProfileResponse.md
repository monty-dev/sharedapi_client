# CashappProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**CashAppProfile**](CashAppProfile.md) |  | [optional] 
**qr_image_url** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.cashapp_profile_response import CashappProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashappProfileResponse from a JSON string
cashapp_profile_response_instance = CashappProfileResponse.from_json(json)
# print the JSON string representation of the object
print CashappProfileResponse.to_json()

# convert the object into a dict
cashapp_profile_response_dict = cashapp_profile_response_instance.to_dict()
# create an instance of CashappProfileResponse from a dict
cashapp_profile_response_form_dict = cashapp_profile_response.from_dict(cashapp_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


