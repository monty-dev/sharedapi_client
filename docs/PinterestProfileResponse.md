# PinterestProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** |  | 
**description** | **object** |  | [optional] 
**followers** | **object** |  | [optional] 
**following** | **object** |  | [optional] 
**pins** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**avatar_url** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.pinterest_profile_response import PinterestProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PinterestProfileResponse from a JSON string
pinterest_profile_response_instance = PinterestProfileResponse.from_json(json)
# print the JSON string representation of the object
print PinterestProfileResponse.to_json()

# convert the object into a dict
pinterest_profile_response_dict = pinterest_profile_response_instance.to_dict()
# create an instance of PinterestProfileResponse from a dict
pinterest_profile_response_form_dict = pinterest_profile_response.from_dict(pinterest_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


