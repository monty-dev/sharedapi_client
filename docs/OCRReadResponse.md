# OCRReadResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_text** | **object** |  | [optional] 
**lines** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.ocr_read_response import OCRReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OCRReadResponse from a JSON string
ocr_read_response_instance = OCRReadResponse.from_json(json)
# print the JSON string representation of the object
print OCRReadResponse.to_json()

# convert the object into a dict
ocr_read_response_dict = ocr_read_response_instance.to_dict()
# create an instance of OCRReadResponse from a dict
ocr_read_response_form_dict = ocr_read_response.from_dict(ocr_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


