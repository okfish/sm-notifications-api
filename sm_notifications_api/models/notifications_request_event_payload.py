# coding: utf-8


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Set
from typing_extensions import Annotated, Self
from sm_notifications_api.models.order_event import OrderEvent


class NotificationsRequestEventPayload(BaseModel):
    """
    Параметры события
    """ # noqa: E501
    order_id: Annotated[str, Field(strict=True, max_length=255)] = Field(description="Идентификатор заказа в формате СМ (H1234567890) Обязательным полем является или `order_id`, или `orderUUID` ")
    order_uuid: Optional[Annotated[str, Field(strict=True,
                                              max_length=255)]] = Field(default=None,
                                                                        description="Уникальный идентификатор заказа. "
                                                                                    "Используется при работе с внешними"
                                                                                    " витринами. "
                                                                                    "Обязательным полем является или "
                                                                                    "`order_id`, или `orderUUID` ",
                                                                        alias="orderUUID")
    code: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Только для нотификации order.pickup_code_created")
    handout_code: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Только для нотификаций order.accepted, order.in_work, order.ready_for_delivery", alias="handoutCode")
    estimated_assembly_at: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Только для нотификации order.accepted")
    number: Optional[StrictStr] = Field(default=None, description="Только для нотификации order.accepted")
    order: Optional[OrderEvent] = None
    __properties: ClassVar[List[str]] = ["order_id", "orderUUID", "code", "handoutCode", "estimated_assembly_at", "number", "order"]

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
        """Create an instance of NotificationsRequestEventPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationsRequestEventPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "order_id": obj.get("order_id"),
            "orderUUID": obj.get("orderUUID"),
            "code": obj.get("code"),
            "handoutCode": obj.get("handoutCode"),
            "estimated_assembly_at": obj.get("estimated_assembly_at"),
            "number": obj.get("number"),
            "order": OrderEvent.from_dict(obj["order"]) if obj.get("order") is not None else None
        })
        return _obj


