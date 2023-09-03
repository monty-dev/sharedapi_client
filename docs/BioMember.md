# BioMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**username** | **object** |  | [optional] 
**avatar** | **object** |  | [optional] 
**avatar_decoration** | **object** |  | [optional] 
**discriminator** | **object** |  | [optional] 
**public_flags** | **object** |  | [optional] 
**flags** | **object** |  | [optional] 
**banner** | [**BannerType**](BannerType.md) |  | [optional] 
**banner_color** | **object** |  | [optional] 
**accent_color** | **object** |  | [optional] 
**bio** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.bio_member import BioMember

# TODO update the JSON string below
json = "{}"
# create an instance of BioMember from a JSON string
bio_member_instance = BioMember.from_json(json)
# print the JSON string representation of the object
print BioMember.to_json()

# convert the object into a dict
bio_member_dict = bio_member_instance.to_dict()
# create an instance of BioMember from a dict
bio_member_form_dict = bio_member.from_dict(bio_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


