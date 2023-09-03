# TwitterUserDataRaw


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suspended** | **object** |  | [optional] 
**info** | [**TwitterUserinfoResult**](TwitterUserinfoResult.md) |  | [optional] 
**tweets** | [**TweetDataResult**](TweetDataResult.md) |  | [optional] 

## Example

```python
from sharedapi_client.models.twitter_user_data_raw import TwitterUserDataRaw

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterUserDataRaw from a JSON string
twitter_user_data_raw_instance = TwitterUserDataRaw.from_json(json)
# print the JSON string representation of the object
print TwitterUserDataRaw.to_json()

# convert the object into a dict
twitter_user_data_raw_dict = twitter_user_data_raw_instance.to_dict()
# create an instance of TwitterUserDataRaw from a dict
twitter_user_data_raw_form_dict = twitter_user_data_raw.from_dict(twitter_user_data_raw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


