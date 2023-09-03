# YoutubeSearchResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **object** |  | 

## Example

```python
from sharedapi_client.models.youtube_search_results import YoutubeSearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeSearchResults from a JSON string
youtube_search_results_instance = YoutubeSearchResults.from_json(json)
# print the JSON string representation of the object
print YoutubeSearchResults.to_json()

# convert the object into a dict
youtube_search_results_dict = youtube_search_results_instance.to_dict()
# create an instance of YoutubeSearchResults from a dict
youtube_search_results_form_dict = youtube_search_results.from_dict(youtube_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


