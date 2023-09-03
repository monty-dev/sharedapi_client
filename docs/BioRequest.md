# BioRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **object** |  | 
**guild_id** | **object** |  | [optional] 
**sig** | **object** |  | [optional] 
**req_user_id** | **object** |  | [optional] 
**timestamp** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.bio_request import BioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BioRequest from a JSON string
bio_request_instance = BioRequest.from_json(json)
# print the JSON string representation of the object
print BioRequest.to_json()

# convert the object into a dict
bio_request_dict = bio_request_instance.to_dict()
# create an instance of BioRequest from a dict
bio_request_form_dict = bio_request.from_dict(bio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


