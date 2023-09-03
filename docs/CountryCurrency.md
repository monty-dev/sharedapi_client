# CountryCurrency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** |  | [optional] 
**symbol** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.country_currency import CountryCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of CountryCurrency from a JSON string
country_currency_instance = CountryCurrency.from_json(json)
# print the JSON string representation of the object
print CountryCurrency.to_json()

# convert the object into a dict
country_currency_dict = country_currency_instance.to_dict()
# create an instance of CountryCurrency from a dict
country_currency_form_dict = country_currency.from_dict(country_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


