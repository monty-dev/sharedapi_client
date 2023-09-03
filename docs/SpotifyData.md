# SpotifyData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_cover_url** | **object** |  | [optional] 
**tile** | **object** |  | [optional] 
**artist** | **object** |  | [optional] 
**album** | **object** |  | [optional] 
**track_id** | **object** |  | [optional] 
**start** | **object** |  | [optional] 
**end** | **object** |  | [optional] 
**duration** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.spotify_data import SpotifyData

# TODO update the JSON string below
json = "{}"
# create an instance of SpotifyData from a JSON string
spotify_data_instance = SpotifyData.from_json(json)
# print the JSON string representation of the object
print SpotifyData.to_json()

# convert the object into a dict
spotify_data_dict = spotify_data_instance.to_dict()
# create an instance of SpotifyData from a dict
spotify_data_form_dict = spotify_data.from_dict(spotify_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


