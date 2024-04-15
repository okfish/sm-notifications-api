# ErrorsObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorsObjectErrorsInner]**](ErrorsObjectErrorsInner.md) | Сообщения об ошибках | 
**code** | **int** | Код ошибки | 

## Example

```python
from sm_notifications_api.models.errors_object import ErrorsObject

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsObject from a JSON string
errors_object_instance = ErrorsObject.from_json(json)
# print the JSON string representation of the object
print(ErrorsObject.to_json())

# convert the object into a dict
errors_object_dict = errors_object_instance.to_dict()
# create an instance of ErrorsObject from a dict
errors_object_form_dict = errors_object.from_dict(errors_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


