# TiktokTopUserVideoResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **object** |  | 
**author** | [**TikTokUserProfileResponse**](TikTokUserProfileResponse.md) |  | [optional] 
**items** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.tiktok_top_user_video_results import TiktokTopUserVideoResults

# TODO update the JSON string below
json = "{}"
# create an instance of TiktokTopUserVideoResults from a JSON string
tiktok_top_user_video_results_instance = TiktokTopUserVideoResults.from_json(json)
# print the JSON string representation of the object
print TiktokTopUserVideoResults.to_json()

# convert the object into a dict
tiktok_top_user_video_results_dict = tiktok_top_user_video_results_instance.to_dict()
# create an instance of TiktokTopUserVideoResults from a dict
tiktok_top_user_video_results_form_dict = tiktok_top_user_video_results.from_dict(tiktok_top_user_video_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


