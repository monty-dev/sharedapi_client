# TweetDataResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | **object** |  | [optional] 
**id** | **object** |  | [optional] 
**rest_id** | **object** |  | [optional] 
**affiliates_highlighted_label** | **object** |  | [optional] 
**has_graduated_access** | **object** |  | [optional] 
**is_blue_verified** | **object** |  | [optional] 
**profile_image_shape** | **object** |  | [optional] 
**legacy** | [**MelanieModelsSharedapiTwitterUserTweetsLegacy**](MelanieModelsSharedapiTwitterUserTweetsLegacy.md) |  | [optional] 
**smart_blocked_by** | **object** |  | [optional] 
**smart_blocking** | **object** |  | [optional] 
**legacy_extended_profile** | [**MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile**](MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile.md) |  | [optional] 
**is_profile_translatable** | **object** |  | [optional] 
**has_hidden_subscriptions_on_profile** | **object** |  | [optional] 
**verification_info** | [**MelanieModelsSharedapiTwitterUserTweetsVerificationInfo**](MelanieModelsSharedapiTwitterUserTweetsVerificationInfo.md) |  | [optional] 
**highlights_info** | [**MelanieModelsSharedapiTwitterUserTweetsHighlightsInfo**](MelanieModelsSharedapiTwitterUserTweetsHighlightsInfo.md) |  | [optional] 
**business_account** | **object** |  | [optional] 
**creator_subscriptions_count** | **object** |  | [optional] 
**unavailable_message** | [**MelanieModelsSharedapiTwitterUserTweetsUnavailableMessage**](MelanieModelsSharedapiTwitterUserTweetsUnavailableMessage.md) |  | [optional] 
**reason** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.tweet_data_result import TweetDataResult

# TODO update the JSON string below
json = "{}"
# create an instance of TweetDataResult from a JSON string
tweet_data_result_instance = TweetDataResult.from_json(json)
# print the JSON string representation of the object
print TweetDataResult.to_json()

# convert the object into a dict
tweet_data_result_dict = tweet_data_result_instance.to_dict()
# create an instance of TweetDataResult from a dict
tweet_data_result_form_dict = tweet_data_result.from_dict(tweet_data_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


