# IpScamScore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **object** |  | 
**score** | **object** |  | 
**risk** | **object** |  | 

## Example

```python
from sharedapi_client.models.ip_scam_score import IpScamScore

# TODO update the JSON string below
json = "{}"
# create an instance of IpScamScore from a JSON string
ip_scam_score_instance = IpScamScore.from_json(json)
# print the JSON string representation of the object
print IpScamScore.to_json()

# convert the object into a dict
ip_scam_score_dict = ip_scam_score_instance.to_dict()
# create an instance of IpScamScore from a dict
ip_scam_score_form_dict = ip_scam_score.from_dict(ip_scam_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


