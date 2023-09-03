# TwitterUserinfoResult


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
**legacy** | [**MelanieModelsSharedapiTwitterScreenNameLegacy**](MelanieModelsSharedapiTwitterScreenNameLegacy.md) |  | [optional] 
**smart_blocked_by** | **object** |  | [optional] 
**smart_blocking** | **object** |  | [optional] 
**legacy_extended_profile** | [**MelanieModelsSharedapiTwitterScreenNameLegacyExtendedProfile**](MelanieModelsSharedapiTwitterScreenNameLegacyExtendedProfile.md) |  | [optional] 
**is_profile_translatable** | **object** |  | [optional] 
**has_hidden_subscriptions_on_profile** | **object** |  | [optional] 
**verification_info** | [**MelanieModelsSharedapiTwitterScreenNameVerificationInfo**](MelanieModelsSharedapiTwitterScreenNameVerificationInfo.md) |  | [optional] 
**highlights_info** | [**MelanieModelsSharedapiTwitterScreenNameHighlightsInfo**](MelanieModelsSharedapiTwitterScreenNameHighlightsInfo.md) |  | [optional] 
**business_account** | **object** |  | [optional] 
**creator_subscriptions_count** | **object** |  | [optional] 
**unavailable_message** | [**MelanieModelsSharedapiTwitterScreenNameUnavailableMessage**](MelanieModelsSharedapiTwitterScreenNameUnavailableMessage.md) |  | [optional] 
**reason** | **object** |  | [optional] 
**protected** | **object** |  | [optional] 
**can_dm** | **object** |  | [optional] 
**can_media_tag** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] 
**default_profile** | **object** |  | [optional] 
**default_profile_image** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**entities** | [**MelanieModelsSharedapiTwitterScreenNameEntities**](MelanieModelsSharedapiTwitterScreenNameEntities.md) |  | [optional] 
**fast_followers_count** | **object** |  | [optional] 
**favourites_count** | **object** |  | [optional] 
**followers_count** | **object** |  | [optional] 
**friends_count** | **object** |  | [optional] 
**has_custom_timelines** | **object** |  | [optional] 
**is_translator** | **object** |  | [optional] 
**listed_count** | **object** |  | [optional] 
**location** | **object** |  | [optional] 
**media_count** | **object** |  | [optional] 
**name** | **object** |  | [optional] 
**normal_followers_count** | **object** |  | [optional] 
**pinned_tweet_ids_str** | **object** |  | [optional] 
**possibly_sensitive** | **object** |  | [optional] 
**profile_image_url_https** | **object** |  | [optional] 
**profile_interstitial_type** | **object** |  | [optional] 
**screen_name** | **object** |  | [optional] 
**statuses_count** | **object** |  | [optional] 
**translator_type** | **object** |  | [optional] 
**verified** | **object** |  | [optional] 
**want_retweets** | **object** |  | [optional] 
**withheld_in_countries** | **object** |  | [optional] 
**profile_banner_url** | **object** |  | [optional] 
**url** | **object** |  | [optional] 
**verified_type** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.twitter_userinfo_result import TwitterUserinfoResult

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterUserinfoResult from a JSON string
twitter_userinfo_result_instance = TwitterUserinfoResult.from_json(json)
# print the JSON string representation of the object
print TwitterUserinfoResult.to_json()

# convert the object into a dict
twitter_userinfo_result_dict = twitter_userinfo_result_instance.to_dict()
# create an instance of TwitterUserinfoResult from a dict
twitter_userinfo_result_form_dict = twitter_userinfo_result.from_dict(twitter_userinfo_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


