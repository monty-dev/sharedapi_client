# HttpHeaders1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agent** | **object** |  | [optional] 
**accept** | **object** |  | [optional] 
**accept_language** | **object** |  | [optional] 
**sec_fetch_mode** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.http_headers1 import HttpHeaders1

# TODO update the JSON string below
json = "{}"
# create an instance of HttpHeaders1 from a JSON string
http_headers1_instance = HttpHeaders1.from_json(json)
# print the JSON string representation of the object
print HttpHeaders1.to_json()

# convert the object into a dict
http_headers1_dict = http_headers1_instance.to_dict()
# create an instance of HttpHeaders1 from a dict
http_headers1_form_dict = http_headers1.from_dict(http_headers1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


