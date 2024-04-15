# coding: utf-8


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from sm_notifications_api.models.notifications_request_event_payload import NotificationsRequestEventPayload
from typing import Optional, Set
from typing_extensions import Self

class NotificationsRequestEvent(BaseModel):
    """
    Событие
    """ # noqa: E501
    type: Annotated[str, Field(strict=True, max_length=255)] = Field(description="Тип события:   * `order.accepted` - Заказ принят, обязательное событие   * `order.in_work` - Заказ взят в работу, обязательное событие   * `order.assembled` - Заказ собран, необязательное событие   * `order.pickup_code_created` - Создан код выдачи заказа. Должен быть отправлен до order.ready_for_delivery   * `order.ready_for_delivery` - Готов к доставке, обязательное событие   * `order.delivering` - Заказ доставляется. Не может быть отправлено до `order.ready_for_delivery`. Принимается только в случае типа интеграции «Сборка и доставка ритейлером».   * `order.delivered` - Заказ доставлен. Не может быть отправлено до `order.ready_for_delivery`. Обязательное событие при самовывозе для схемы «Сборка ритейлера, доставка Сбермаркета» и для схемы «Сборка и доставка ритейлером» при любом типе доставки.   * `order.canceled` - Заказ отменен ")
    payload: NotificationsRequestEventPayload
    __properties: ClassVar[List[str]] = ["type", "payload"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['order.accepted', 'order.in_work', 'order.assembled', 'order.pickup_code_created', 'order.ready_for_delivery', 'order.delivering', 'order.delivered', 'order.canceled']):
            raise ValueError("must be one of enum values ('order.accepted', 'order.in_work', 'order.assembled', 'order.pickup_code_created', 'order.ready_for_delivery', 'order.delivering', 'order.delivered', 'order.canceled')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NotificationsRequestEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of payload
        if self.payload:
            _dict['payload'] = self.payload.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationsRequestEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "payload": NotificationsRequestEventPayload.from_dict(obj["payload"]) if obj.get("payload") is not None else None
        })
        return _obj


