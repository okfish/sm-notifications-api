# NotificationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**NotificationsRequestEvent**](NotificationsRequestEvent.md) |  | 

## Example

```python
from sm_notifications_api.models.notifications_request import NotificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsRequest from a JSON string
notifications_request_instance = NotificationsRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationsRequest.to_json())

# convert the object into a dict
notifications_request_dict = notifications_request_instance.to_dict()
# create an instance of NotificationsRequest from a dict
notifications_request_form_dict = notifications_request.from_dict(notifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


