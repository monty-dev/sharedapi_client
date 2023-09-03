# InstagramCarouselMediaResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **object** |  | [optional] 
**preview_image_url** | **object** |  | [optional] 
**preview_image_filename** | **object** |  | [optional] 
**is_video** | **object** |  | [optional] 
**filename** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.instagram_carousel_media_response import InstagramCarouselMediaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramCarouselMediaResponse from a JSON string
instagram_carousel_media_response_instance = InstagramCarouselMediaResponse.from_json(json)
# print the JSON string representation of the object
print InstagramCarouselMediaResponse.to_json()

# convert the object into a dict
instagram_carousel_media_response_dict = instagram_carousel_media_response_instance.to_dict()
# create an instance of InstagramCarouselMediaResponse from a dict
instagram_carousel_media_response_form_dict = instagram_carousel_media_response.from_dict(instagram_carousel_media_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


