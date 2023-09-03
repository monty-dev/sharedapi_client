# CashAppProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **object** |  | [optional] 
**formatted_cashtag** | **object** |  | [optional] 
**is_verified_account** | **object** |  | [optional] 
**rate_plan** | **object** |  | [optional] 
**payment_button_type** | **object** |  | [optional] 
**country_code** | **object** |  | [optional] 
**avatar** | [**Avatar**](Avatar.md) |  | [optional] 

## Example

```python
from sharedapi_client.models.cash_app_profile import CashAppProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CashAppProfile from a JSON string
cash_app_profile_instance = CashAppProfile.from_json(json)
# print the JSON string representation of the object
print CashAppProfile.to_json()

# convert the object into a dict
cash_app_profile_dict = cash_app_profile_instance.to_dict()
# create an instance of CashAppProfile from a dict
cash_app_profile_form_dict = cash_app_profile.from_dict(cash_app_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


