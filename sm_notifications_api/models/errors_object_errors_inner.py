# coding: utf-8


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ErrorsObjectErrorsInner(BaseModel):
    """
    ErrorsObjectErrorsInner
    """ # noqa: E501
    type: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(description="Тип ошибки")
    field: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(description="Поле указывающее на ошибку")
    message: Annotated[str, Field(strict=True, max_length=65535)] = Field(description="Описание ошибки")
    __properties: ClassVar[List[str]] = ["type", "field", "message"]

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
        """Create an instance of ErrorsObjectErrorsInner from a JSON string"""
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
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if field (nullable) is None
        # and model_fields_set contains the field
        if self.field is None and "field" in self.model_fields_set:
            _dict['field'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ErrorsObjectErrorsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "field": obj.get("field"),
            "message": obj.get("message")
        })
        return _obj


