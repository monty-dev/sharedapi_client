# Music


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **object** |  | [optional] 
**album** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**title** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.music import Music

# TODO update the JSON string below
json = "{}"
# create an instance of Music from a JSON string
music_instance = Music.from_json(json)
# print the JSON string representation of the object
print Music.to_json()

# convert the object into a dict
music_dict = music_instance.to_dict()
# create an instance of Music from a dict
music_form_dict = music.from_dict(music_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


