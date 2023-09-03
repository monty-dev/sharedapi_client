# Format


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format_id** | **object** |  | [optional] 
**format_note** | **object** |  | [optional] 
**ext** | **object** |  | [optional] 
**protocol** | **object** |  | [optional] 
**acodec** | **object** |  | [optional] 
**vcodec** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**width** | **object** |  | [optional] 
**height** | **object** |  | [optional] 
**fps** | **object** |  | [optional] 
**rows** | **object** |  | [optional] 
**columns** | **object** |  | [optional] 
**fragments** | **object** |  | [optional] 
**audio_ext** | **object** |  | [optional] 
**video_ext** | **object** |  | [optional] 
**format** | **object** |  | [optional] 
**resolution** | **object** |  | [optional] 
**http_headers** | [**HttpHeaders**](HttpHeaders.md) |  | [optional] 
**asr** | **object** |  | [optional] 
**filesize** | **object** |  | [optional] 
**source_preference** | **object** |  | [optional] 
**audio_channels** | **object** |  | [optional] 
**quality** | **object** |  | [optional] 
**has_drm** | **object** |  | [optional] 
**tbr** | **object** |  | [optional] 
**language** | **object** |  | [optional] 
**language_preference** | **object** |  | [optional] 
**preference** | **object** |  | [optional] 
**dynamic_range** | **object** |  | [optional] 
**abr** | **object** |  | [optional] 
**downloader_options** | [**DownloaderOptions**](DownloaderOptions.md) |  | [optional] 
**container** | **object** |  | [optional] 
**vbr** | **object** |  | [optional] 
**filesize_approx** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.format import Format

# TODO update the JSON string below
json = "{}"
# create an instance of Format from a JSON string
format_instance = Format.from_json(json)
# print the JSON string representation of the object
print Format.to_json()

# convert the object into a dict
format_dict = format_instance.to_dict()
# create an instance of Format from a dict
format_form_dict = format.from_dict(format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


