# ErrorsObjectErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип ошибки | 
**field** | **str** | Поле указывающее на ошибку | 
**message** | **str** | Описание ошибки | 

## Example

```python
from sm_notifications_api.models.errors_object_errors_inner import ErrorsObjectErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsObjectErrorsInner from a JSON string
errors_object_errors_inner_instance = ErrorsObjectErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ErrorsObjectErrorsInner.to_json())

# convert the object into a dict
errors_object_errors_inner_dict = errors_object_errors_inner_instance.to_dict()
# create an instance of ErrorsObjectErrorsInner from a dict
errors_object_errors_inner_form_dict = errors_object_errors_inner.from_dict(errors_object_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


