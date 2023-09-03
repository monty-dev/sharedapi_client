# TikTokVideoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aweme_id** | **object** |  | [optional] 
**avatar_bytes** | **object** |  | [optional] 
**video_url** | **object** |  | [optional] 
**author_id** | **object** |  | [optional] 
**author** | [**Author**](Author.md) |  | [optional] 
**avatar_thumb** | **object** |  | [optional] 
**create_time** | **object** |  | [optional] 
**desc** | **object** |  | [optional] 
**direct_download_urls** | **object** |  | [optional] 
**filename** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**music** | [**Music**](Music.md) |  | [optional] 
**nickname** | **object** |  | [optional] 
**statistics** | [**Statistics**](Statistics.md) |  | [optional] 
**video_bytes** | **object** |  | [optional] 
**share_url** | **object** |  | [optional] 
**video** | [**Video**](Video.md) |  | [optional] 
**cover_image_url** | **object** |  | [optional] 
**image_post_info** | [**ImagePostInfo**](ImagePostInfo.md) |  | [optional] 
**embed_color** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.tik_tok_video_response import TikTokVideoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TikTokVideoResponse from a JSON string
tik_tok_video_response_instance = TikTokVideoResponse.from_json(json)
# print the JSON string representation of the object
print TikTokVideoResponse.to_json()

# convert the object into a dict
tik_tok_video_response_dict = tik_tok_video_response_instance.to_dict()
# create an instance of TikTokVideoResponse from a dict
tik_tok_video_response_form_dict = tik_tok_video_response.from_dict(tik_tok_video_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


