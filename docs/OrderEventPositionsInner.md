# OrderEventPositionsInner

Позиция заказа

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | SKU товара в системе партнера | 
**quantity** | **float** | Количество товара в заказе | 
**weight** | **str** | Вес в граммах для весовой и фасованной позиции. Обязателен для весовых позиций | [optional] 
**marking_code** | [**List[OrderEventPositionsInnerMarkingCodeInner]**](OrderEventPositionsInnerMarkingCodeInner.md) |  | [optional] 
**replaced_by_id** | **str** | SKU товара, которым заменён этот товар | [optional] 

## Example

```python
from sm_notifications_api.models.order_event_positions_inner import OrderEventPositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderEventPositionsInner from a JSON string
order_event_positions_inner_instance = OrderEventPositionsInner.from_json(json)
# print the JSON string representation of the object
print(OrderEventPositionsInner.to_json())

# convert the object into a dict
order_event_positions_inner_dict = order_event_positions_inner_instance.to_dict()
# create an instance of OrderEventPositionsInner from a dict
order_event_positions_inner_form_dict = order_event_positions_inner.from_dict(order_event_positions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


