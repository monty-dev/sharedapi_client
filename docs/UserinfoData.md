# UserinfoData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**puuid** | **object** |  | [optional] 
**region** | **object** |  | [optional] 
**account_level** | **object** |  | [optional] 
**name** | **object** |  | [optional] 
**tag** | **object** |  | [optional] 
**card** | [**MelanieModelsSharedapiValorant2Card**](MelanieModelsSharedapiValorant2Card.md) |  | [optional] 
**last_update** | **object** |  | [optional] 
**last_update_raw** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.userinfo_data import UserinfoData

# TODO update the JSON string below
json = "{}"
# create an instance of UserinfoData from a JSON string
userinfo_data_instance = UserinfoData.from_json(json)
# print the JSON string representation of the object
print UserinfoData.to_json()

# convert the object into a dict
userinfo_data_dict = userinfo_data_instance.to_dict()
# create an instance of UserinfoData from a dict
userinfo_data_form_dict = userinfo_data.from_dict(userinfo_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


