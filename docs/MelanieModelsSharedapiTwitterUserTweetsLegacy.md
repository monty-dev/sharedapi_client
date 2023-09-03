# MelanieModelsSharedapiTwitterUserTweetsLegacy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected** | **object** |  | [optional] 
**can_dm** | **object** |  | [optional] 
**can_media_tag** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] 
**default_profile** | **object** |  | [optional] 
**default_profile_image** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**entities** | [**MelanieModelsSharedapiTwitterUserTweetsEntities**](MelanieModelsSharedapiTwitterUserTweetsEntities.md) |  | [optional] 
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
from sharedapi_client.models.melanie_models_sharedapi_twitter_user_tweets_legacy import MelanieModelsSharedapiTwitterUserTweetsLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of MelanieModelsSharedapiTwitterUserTweetsLegacy from a JSON string
melanie_models_sharedapi_twitter_user_tweets_legacy_instance = MelanieModelsSharedapiTwitterUserTweetsLegacy.from_json(json)
# print the JSON string representation of the object
print MelanieModelsSharedapiTwitterUserTweetsLegacy.to_json()

# convert the object into a dict
melanie_models_sharedapi_twitter_user_tweets_legacy_dict = melanie_models_sharedapi_twitter_user_tweets_legacy_instance.to_dict()
# create an instance of MelanieModelsSharedapiTwitterUserTweetsLegacy from a dict
melanie_models_sharedapi_twitter_user_tweets_legacy_form_dict = melanie_models_sharedapi_twitter_user_tweets_legacy.from_dict(melanie_models_sharedapi_twitter_user_tweets_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


