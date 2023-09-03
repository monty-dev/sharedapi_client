# Card


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**small** | **object** |  | [optional] 
**large** | **object** |  | [optional] 
**wide** | **object** |  | [optional] 
**id** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.card import Card

# TODO update the JSON string below
json = "{}"
# create an instance of Card from a JSON string
card_instance = Card.from_json(json)
# print the JSON string representation of the object
print Card.to_json()

# convert the object into a dict
card_dict = card_instance.to_dict()
# create an instance of Card from a dict
card_form_dict = card.from_dict(card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


