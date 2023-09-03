# Video


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ratio** | **object** |  | [optional] 
**height** | **object** |  | [optional] 
**width** | **object** |  | [optional] 
**dynamic_cover** | **object** |  | [optional] 
**origin_cover** | **object** |  | [optional] 
**duration** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.video import Video

# TODO update the JSON string below
json = "{}"
# create an instance of Video from a JSON string
video_instance = Video.from_json(json)
# print the JSON string representation of the object
print Video.to_json()

# convert the object into a dict
video_dict = video_instance.to_dict()
# create an instance of Video from a dict
video_form_dict = video.from_dict(video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


