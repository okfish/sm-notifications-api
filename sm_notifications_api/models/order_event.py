# coding: utf-8


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sm_notifications_api.models.order_event_positions_inner import OrderEventPositionsInner
from typing import Optional, Set
from typing_extensions import Self

class OrderEvent(BaseModel):
    """
    OrderEvent
    """ # noqa: E501
    original_order_id: Optional[StrictStr] = Field(default=None, description="Идентификатор заказа в СМ (H1234567890)", alias="originalOrderId")
    positions: Optional[List[OrderEventPositionsInner]] = Field(default=None, description="Описание позиций заказа")
    __properties: ClassVar[List[str]] = ["originalOrderId", "positions"]

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
        """Create an instance of OrderEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in positions (list)
        _items = []
        if self.positions:
            for _item in self.positions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['positions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "originalOrderId": obj.get("originalOrderId"),
            "positions": [OrderEventPositionsInner.from_dict(_item) for _item in obj["positions"]] if obj.get("positions") is not None else None
        })
        return _obj


