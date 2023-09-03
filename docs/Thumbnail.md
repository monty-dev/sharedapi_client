# Thumbnail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **object** |  | [optional] 
**preference** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**height** | **object** |  | [optional] 
**width** | **object** |  | [optional] 
**resolution** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.thumbnail import Thumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of Thumbnail from a JSON string
thumbnail_instance = Thumbnail.from_json(json)
# print the JSON string representation of the object
print Thumbnail.to_json()

# convert the object into a dict
thumbnail_dict = thumbnail_instance.to_dict()
# create an instance of Thumbnail from a dict
thumbnail_form_dict = thumbnail.from_dict(thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


