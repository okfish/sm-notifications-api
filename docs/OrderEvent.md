# OrderEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_order_id** | **str** | Идентификатор заказа в СМ (H1234567890) | [optional] 
**positions** | [**List[OrderEventPositionsInner]**](OrderEventPositionsInner.md) | Описание позиций заказа | 

## Example

```python
from sm_notifications_api.models.order_event import OrderEvent

# TODO update the JSON string below
json = "{}"
# create an instance of OrderEvent from a JSON string
order_event_instance = OrderEvent.from_json(json)
# print the JSON string representation of the object
print(OrderEvent.to_json())

# convert the object into a dict
order_event_dict = order_event_instance.to_dict()
# create an instance of OrderEvent from a dict
order_event_form_dict = order_event.from_dict(order_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


