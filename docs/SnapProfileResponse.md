# SnapProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** |  | 
**bio** | **object** |  | [optional] 
**subscriber_count** | **object** |  | [optional] 
**profile_image_url** | **object** |  | [optional] 
**hero_image_url** | **object** |  | [optional] 
**display_name** | **object** | The in-app name the user has set for their account. | [optional] 
**snapcode_image_url** | **object** | Snap QR code. | [optional] 
**bitmoji_url** | **object** | Bitmoji, rendered as PNG. Transparent background. | [optional] 
**bitmoji_background_url** | **object** | The bitmoji background shown within the Snapchat application | [optional] 
**one_click_url** | **object** | Direct link that will open the Snapchat app and allow the user to be added. | [optional] 
**share_image_url** | **object** | A Combo image of the user&#39;s bitmoji and snapcode | [optional] 
**story_media** | **object** |  | [optional] 
**spotlight_media** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.snap_profile_response import SnapProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapProfileResponse from a JSON string
snap_profile_response_instance = SnapProfileResponse.from_json(json)
# print the JSON string representation of the object
print SnapProfileResponse.to_json()

# convert the object into a dict
snap_profile_response_dict = snap_profile_response_instance.to_dict()
# create an instance of SnapProfileResponse from a dict
snap_profile_response_form_dict = snap_profile_response.from_dict(snap_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


