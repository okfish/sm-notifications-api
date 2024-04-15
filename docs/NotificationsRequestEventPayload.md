# NotificationsRequestEventPayload

Параметры события

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Идентификатор заказа в формате СМ (H1234567890) Обязательным полем является или &#x60;order_id&#x60;, или &#x60;orderUUID&#x60;  | 
**order_uuid** | **str** | Уникальный идентификатор заказа. Используется при работе с внешними витринами. Обязательным полем является или &#x60;order_id&#x60;, или &#x60;orderUUID&#x60;  | 
**code** | **str** | Только для нотификации order.pickup_code_created | [optional] 
**handout_code** | **str** | Только для нотификаций order.accepted, order.in_work, order.ready_for_delivery | [optional] 
**estimated_assembly_at** | **str** | Только для нотификации order.accepted | [optional] 
**number** | **str** | Только для нотификации order.accepted | [optional] 
**order** | [**OrderEvent**](OrderEvent.md) |  | [optional] 

## Example

```python
from sm_notifications_api.models.notifications_request_event_payload import NotificationsRequestEventPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsRequestEventPayload from a JSON string
notifications_request_event_payload_instance = NotificationsRequestEventPayload.from_json(json)
# print the JSON string representation of the object
print(NotificationsRequestEventPayload.to_json())

# convert the object into a dict
notifications_request_event_payload_dict = notifications_request_event_payload_instance.to_dict()
# create an instance of NotificationsRequestEventPayload from a dict
notifications_request_event_payload_form_dict = notifications_request_event_payload.from_dict(notifications_request_event_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


