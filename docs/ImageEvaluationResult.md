# ImageEvaluationResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **object** | Indicates if an image is classified as adult. | [optional] 
**racy** | **object** | Indicates if the image is classified as racy. | [optional] 
**adult_classification_score** | **object** | Probability image is adult. | [optional] 
**racy_classification_score** | **object** | Probability image is racy. | [optional] 
**advanced_info** | **object** |  | [optional] 

## Example

```python
from sharedapi_client.models.image_evaluation_result import ImageEvaluationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ImageEvaluationResult from a JSON string
image_evaluation_result_instance = ImageEvaluationResult.from_json(json)
# print the JSON string representation of the object
print ImageEvaluationResult.to_json()

# convert the object into a dict
image_evaluation_result_dict = image_evaluation_result_instance.to_dict()
# create an instance of ImageEvaluationResult from a dict
image_evaluation_result_form_dict = image_evaluation_result.from_dict(image_evaluation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


