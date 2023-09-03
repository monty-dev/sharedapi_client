# DownloaderOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_chunk_size** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.downloader_options import DownloaderOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DownloaderOptions from a JSON string
downloader_options_instance = DownloaderOptions.from_json(json)
# print the JSON string representation of the object
print DownloaderOptions.to_json()

# convert the object into a dict
downloader_options_dict = downloader_options_instance.to_dict()
# create an instance of DownloaderOptions from a dict
downloader_options_form_dict = downloader_options.from_dict(downloader_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


