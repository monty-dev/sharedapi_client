# IPLookupResultResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **object** |  | [optional] 
**fraud_score** | [**IpScamScore**](IpScamScore.md) |  | [optional] 
**hostname** | **object** |  | [optional] 
**city** | **object** |  | [optional] 
**region** | **object** |  | [optional] 
**country** | **object** |  | [optional] 
**country_name** | **object** |  | [optional] 
**country_flag** | [**CountryFlag**](CountryFlag.md) |  | [optional] 
**country_currency** | [**CountryCurrency**](CountryCurrency.md) |  | [optional] 
**loc** | **object** |  | [optional] 
**org** | **object** |  | [optional] 
**postal** | **object** |  | [optional] 
**timezone** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.ip_lookup_result_response import IPLookupResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IPLookupResultResponse from a JSON string
ip_lookup_result_response_instance = IPLookupResultResponse.from_json(json)
# print the JSON string representation of the object
print IPLookupResultResponse.to_json()

# convert the object into a dict
ip_lookup_result_response_dict = ip_lookup_result_response_instance.to_dict()
# create an instance of IPLookupResultResponse from a dict
ip_lookup_result_response_form_dict = ip_lookup_result_response.from_dict(ip_lookup_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


