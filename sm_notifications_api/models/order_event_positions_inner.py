# coding: utf-8


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from sm_notifications_api.models.order_event_positions_inner_marking_code_inner import OrderEventPositionsInnerMarkingCodeInner
from typing import Optional, Set
from typing_extensions import Self

class OrderEventPositionsInner(BaseModel):
    """
    Позиция заказа
    """ # noqa: E501
    id: StrictStr = Field(description="SKU товара в системе партнера")
    quantity: Union[StrictFloat, StrictInt] = Field(description="Количество товара в заказе")
    weight: Optional[StrictStr] = Field(default=None, description="Вес в граммах для весовой и фасованной позиции. Обязателен для весовых позиций")
    marking_code: Optional[List[OrderEventPositionsInnerMarkingCodeInner]] = Field(default=None, alias="markingCode")
    replaced_by_id: Optional[StrictStr] = Field(default=None, description="SKU товара, которым заменён этот товар", alias="replacedByID")
    __properties: ClassVar[List[str]] = ["id", "quantity", "weight", "markingCode", "replacedByID"]

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
        """Create an instance of OrderEventPositionsInner from a JSON string"""
        return cls.model_validate_json(json_str)

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
        # override the default output from pydantic by calling `to_dict()` of each item in marking_code (list)
        _items = []
        if self.marking_code:
            for _item in self.marking_code:
                if _item:
                    _items.append(_item.to_dict())
            _dict['markingCode'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderEventPositionsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "quantity": obj.get("quantity"),
            "weight": obj.get("weight"),
            "markingCode": [OrderEventPositionsInnerMarkingCodeInner.from_dict(_item) for _item in obj["markingCode"]] if obj.get("markingCode") is not None else None,
            "replacedByID": obj.get("replacedByID")
        })
        return _obj


