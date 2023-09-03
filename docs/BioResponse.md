# BioResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**BioUser**](BioUser.md) |  | [optional] 
**profile_data** | [**ProfileModel**](ProfileModel.md) |  | [optional] 
**member** | [**BioMember**](BioMember.md) |  | [optional] 
**activities** | **object** |  | [optional] 
**request** | [**BioRequest**](BioRequest.md) |  | [optional] 
**status** | [**GatewayUserStatus**](GatewayUserStatus.md) |  | [optional] 
**sig** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.bio_response import BioResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BioResponse from a JSON string
bio_response_instance = BioResponse.from_json(json)
# print the JSON string representation of the object
print BioResponse.to_json()

# convert the object into a dict
bio_response_dict = bio_response_instance.to_dict()
# create an instance of BioResponse from a dict
bio_response_form_dict = bio_response.from_dict(bio_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


