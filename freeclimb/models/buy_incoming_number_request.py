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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class BuyIncomingNumberRequest(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    BuyIncomingNumberRequest
    """  # noqa: E501

    phone_number: StrictStr = Field(
        description="Phone number to purchase in E.164 format (as returned in the list of Available Phone Numbers).",
        alias="phoneNumber",
    )
    alias: Optional[StrictStr] = Field(
        default=None,
        description="Description for this new incoming phone number (max 64 characters).",
    )
    application_id: Optional[StrictStr] = Field(
        default=None,
        description="ID of the application that should handle phone calls to the number.",
        alias="applicationId",
    )

    __properties: ClassVar[List[str]] = ["phoneNumber", "alias", "applicationId"]

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BuyIncomingNumberRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BuyIncomingNumberRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "phoneNumber": obj.get("phoneNumber"),
                "alias": obj.get("alias"),
                "applicationId": obj.get("applicationId"),
            }
        )
        return _obj
