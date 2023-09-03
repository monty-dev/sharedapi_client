# AIImageGenerationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **object** | URL of the image generated. Image should be immediately avaliable. | 
**idea** | **object** |  | 

## Example

```python
from sharedapi_client.models.ai_image_generation_response import AIImageGenerationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIImageGenerationResponse from a JSON string
ai_image_generation_response_instance = AIImageGenerationResponse.from_json(json)
# print the JSON string representation of the object
print AIImageGenerationResponse.to_json()

# convert the object into a dict
ai_image_generation_response_dict = ai_image_generation_response_instance.to_dict()
# create an instance of AIImageGenerationResponse from a dict
ai_image_generation_response_form_dict = ai_image_generation_response.from_dict(ai_image_generation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


