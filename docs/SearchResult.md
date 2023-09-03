# SearchResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**title** | **object** |  | [optional] 
**formats** | **object** |  | [optional] 
**thumbnails** | **object** |  | [optional] 
**thumbnail** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**uploader** | **object** |  | [optional] 
**uploader_id** | **object** |  | [optional] 
**uploader_url** | **object** |  | [optional] 
**channel_id** | **object** |  | [optional] 
**channel_url** | **object** |  | [optional] 
**duration** | **object** |  | [optional] 
**view_count** | **object** |  | [optional] 
**average_rating** | **object** |  | [optional] 
**age_limit** | **object** |  | [optional] 
**webpage_url** | **object** |  | [optional] 
**categories** | **object** |  | [optional] 
**tags** | **object** |  | [optional] 
**playable_in_embed** | **object** |  | [optional] 
**is_live** | **object** |  | [optional] 
**was_live** | **object** |  | [optional] 
**live_status** | **object** |  | [optional] 
**release_timestamp** | **object** |  | [optional] 
**automatic_captions** | **Dict[str, object]** |  | [optional] 
**subtitles** | [**Subtitles**](Subtitles.md) |  | [optional] 
**comment_count** | **object** |  | [optional] 
**chapters** | **object** |  | [optional] 
**like_count** | **object** |  | [optional] 
**channel** | **object** |  | [optional] 
**channel_follower_count** | **object** |  | [optional] 
**upload_date** | **object** |  | [optional] 
**availability** | **object** |  | [optional] 
**original_url** | **object** |  | [optional] 
**webpage_url_basename** | **object** |  | [optional] 
**webpage_url_domain** | **object** |  | [optional] 
**extractor** | **object** |  | [optional] 
**extractor_key** | **object** |  | [optional] 
**playlist_count** | **object** |  | [optional] 
**playlist** | **object** |  | [optional] 
**playlist_id** | **object** |  | [optional] 
**playlist_title** | **object** |  | [optional] 
**playlist_uploader** | **object** |  | [optional] 
**playlist_uploader_id** | **object** |  | [optional] 
**n_entries** | **object** |  | [optional] 
**playlist_index** | **object** |  | [optional] 
**playlist_autonumber** | **object** |  | [optional] 
**display_id** | **object** |  | [optional] 
**fulltitle** | **object** |  | [optional] 
**duration_string** | **object** |  | [optional] 
**release_date** | **object** |  | [optional] 
**requested_subtitles** | **object** |  | [optional] 
**asr** | **object** |  | [optional] 
**filesize** | **object** |  | [optional] 
**format_id** | **object** |  | [optional] 
**format_note** | **object** |  | [optional] 
**source_preference** | **object** |  | [optional] 
**fps** | **object** |  | [optional] 
**audio_channels** | **object** |  | [optional] 
**height** | **object** |  | [optional] 
**quality** | **object** |  | [optional] 
**has_drm** | **object** |  | [optional] 
**tbr** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**width** | **object** |  | [optional] 
**language** | **object** |  | [optional] 
**language_preference** | **object** |  | [optional] 
**ext** | **object** |  | [optional] 
**vcodec** | **object** |  | [optional] 
**acodec** | **object** |  | [optional] 
**abr** | **object** |  | [optional] 
**downloader_options** | [**DownloaderOptions1**](DownloaderOptions1.md) |  | [optional] 
**container** | **object** |  | [optional] 
**protocol** | **object** |  | [optional] 
**audio_ext** | **object** |  | [optional] 
**video_ext** | **object** |  | [optional] 
**format** | **object** |  | [optional] 
**resolution** | **object** |  | [optional] 
**http_headers** | [**HttpHeaders1**](HttpHeaders1.md) |  | [optional] 

## Example

```python
from sharedapi_client.models.search_result import SearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResult from a JSON string
search_result_instance = SearchResult.from_json(json)
# print the JSON string representation of the object
print SearchResult.to_json()

# convert the object into a dict
search_result_dict = search_result_instance.to_dict()
# create an instance of SearchResult from a dict
search_result_form_dict = search_result.from_dict(search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


