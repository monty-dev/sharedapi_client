# ValorantProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_level** | **object** |  | [optional] 
**avatar_url** | **object** |  | [optional] 
**card** | [**MelanieModelsSharedapiValorantCard**](MelanieModelsSharedapiValorantCard.md) |  | [optional] 
**current_rating** | **object** |  | [optional] 
**damage_round_ratio** | **object** |  | [optional] 
**deaths** | **object** |  | [optional] 
**headshot_percent** | **object** |  | [optional] 
**info** | [**UserinfoData**](UserinfoData.md) |  | [optional] 
**kd_ratio** | **object** |  | [optional] 
**kills** | **object** |  | [optional] 
**last_update** | **object** |  | [optional] 
**lost** | **object** |  | [optional] 
**matches_played** | **object** |  | [optional] 
**mmr** | [**MMRData**](MMRData.md) |  | [optional] 
**name** | **object** |  | [optional] 
**peak_rating_act** | **object** |  | [optional] 
**peak_rating** | **object** |  | [optional] 
**puuid** | **object** |  | [optional] 
**region** | **object** |  | [optional] 
**tag** | **object** |  | [optional] 
**win_percent** | **object** |  | [optional] 
**wins** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.valorant_profile_response import ValorantProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValorantProfileResponse from a JSON string
valorant_profile_response_instance = ValorantProfileResponse.from_json(json)
# print the JSON string representation of the object
print ValorantProfileResponse.to_json()

# convert the object into a dict
valorant_profile_response_dict = valorant_profile_response_instance.to_dict()
# create an instance of ValorantProfileResponse from a dict
valorant_profile_response_form_dict = valorant_profile_response.from_dict(valorant_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


