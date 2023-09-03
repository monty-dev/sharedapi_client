# PinterestReverseResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | [optional] 
**items** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.pinterest_reverse_response import PinterestReverseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PinterestReverseResponse from a JSON string
pinterest_reverse_response_instance = PinterestReverseResponse.from_json(json)
# print the JSON string representation of the object
print PinterestReverseResponse.to_json()

# convert the object into a dict
pinterest_reverse_response_dict = pinterest_reverse_response_instance.to_dict()
# create an instance of PinterestReverseResponse from a dict
pinterest_reverse_response_form_dict = pinterest_reverse_response.from_dict(pinterest_reverse_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


