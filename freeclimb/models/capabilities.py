# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class Capabilities(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    Details for which features this number may be used.
    """  # noqa: E501

    voice: Optional[StrictBool] = Field(
        description="Indicates whether a number can be used for voice calls. Replaces voiceEnabled."
    )
    sms: Optional[StrictBool] = Field(
        description="Indicates whether a number can be used SMS messaging. Replaces smsEnabled."
    )
    toll_free: Optional[StrictBool] = Field(
        description="Indicates that a number is toll-free and will make toll-free calls, and when enabled, toll-free messages.",
        alias="tollFree",
    )
    ten_dlc: Optional[StrictBool] = Field(
        description="Indicates that a number, if sms is true, will be used for 10DLC messaging",
        alias="tenDLC",
    )
    short_code: Optional[StrictBool] = Field(
        description="Indicates that a number is a short code and can be used for short code messaging",
        alias="shortCode",
    )

    __properties: ClassVar[List[str]] = [
        "voice",
        "sms",
        "tollFree",
        "tenDLC",
        "shortCode",
    ]

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Capabilities from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if voice (nullable) is None
        # and model_fields_set contains the field
        if self.voice is None and "voice" in self.model_fields_set:
            _dict["voice"] = None

        # set to None if sms (nullable) is None
        # and model_fields_set contains the field
        if self.sms is None and "sms" in self.model_fields_set:
            _dict["sms"] = None

        # set to None if toll_free (nullable) is None
        # and model_fields_set contains the field
        if self.toll_free is None and "toll_free" in self.model_fields_set:
            _dict["tollFree"] = None

        # set to None if ten_dlc (nullable) is None
        # and model_fields_set contains the field
        if self.ten_dlc is None and "ten_dlc" in self.model_fields_set:
            _dict["tenDLC"] = None

        # set to None if short_code (nullable) is None
        # and model_fields_set contains the field
        if self.short_code is None and "short_code" in self.model_fields_set:
            _dict["shortCode"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Capabilities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "voice": obj.get("voice"),
                "sms": obj.get("sms"),
                "tollFree": obj.get("tollFree"),
                "tenDLC": obj.get("tenDLC"),
                "shortCode": obj.get("shortCode"),
            }
        )
        return _obj
