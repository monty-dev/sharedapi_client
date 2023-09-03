# OCRRquest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **object** | URL of the image to be read. PNG or JPEG supported. Must be larger than 50x50 | 

## Example

```python
from sharedapi_client.models.ocr_rquest import OCRRquest

# TODO update the JSON string below
json = "{}"
# create an instance of OCRRquest from a JSON string
ocr_rquest_instance = OCRRquest.from_json(json)
# print the JSON string representation of the object
print OCRRquest.to_json()

# convert the object into a dict
ocr_rquest_dict = ocr_rquest_instance.to_dict()
# create an instance of OCRRquest from a dict
ocr_rquest_form_dict = ocr_rquest.from_dict(ocr_rquest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


