# NotificationsRequestEvent

Событие

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип события:   * &#x60;order.accepted&#x60; - Заказ принят, обязательное событие   * &#x60;order.in_work&#x60; - Заказ взят в работу, обязательное событие   * &#x60;order.assembled&#x60; - Заказ собран, необязательное событие   * &#x60;order.pickup_code_created&#x60; - Создан код выдачи заказа. Должен быть отправлен до order.ready_for_delivery   * &#x60;order.ready_for_delivery&#x60; - Готов к доставке, обязательное событие   * &#x60;order.delivering&#x60; - Заказ доставляется. Не может быть отправлено до &#x60;order.ready_for_delivery&#x60;. Принимается только в случае типа интеграции «Сборка и доставка ритейлером».   * &#x60;order.delivered&#x60; - Заказ доставлен. Не может быть отправлено до &#x60;order.ready_for_delivery&#x60;. Обязательное событие при самовывозе для схемы «Сборка ритейлера, доставка Сбермаркета» и для схемы «Сборка и доставка ритейлером» при любом типе доставки.   * &#x60;order.canceled&#x60; - Заказ отменен  | 
**payload** | [**NotificationsRequestEventPayload**](NotificationsRequestEventPayload.md) |  | 

## Example

```python
from sm_notifications_api.models.notifications_request_event import NotificationsRequestEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsRequestEvent from a JSON string
notifications_request_event_instance = NotificationsRequestEvent.from_json(json)
# print the JSON string representation of the object
print(NotificationsRequestEvent.to_json())

# convert the object into a dict
notifications_request_event_dict = notifications_request_event_instance.to_dict()
# create an instance of NotificationsRequestEvent from a dict
notifications_request_event_form_dict = notifications_request_event.from_dict(notifications_request_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


