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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class SMSTenDLCPartnerCampaignBrand(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    SMSTenDLCPartnerCampaignBrand
    """  # noqa: E501

    account_id: Optional[StrictStr] = Field(
        default=None,
        description="ID of the account that created this Queue.",
        alias="accountId",
    )
    brand_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier assigned to the brand by the registry.",
        alias="brandId",
    )
    first_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(
        default=None, description="First or given name. ", alias="firstName"
    )
    last_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(
        default=None, description="Last or Surname.", alias="lastName"
    )
    display_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None,
        description="Display or marketing name of the brand.",
        alias="displayName",
    )
    company_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None,
        description="(Required for Non-profit/private/public) Legal company name.",
        alias="companyName",
    )
    phone: Annotated[str, Field(strict=True, max_length=20)] = Field(
        description="Valid phone number in e.164 international format."
    )
    email: Annotated[str, Field(strict=True, max_length=100)] = Field(
        description="Valid email address of brand support contact."
    )
    website: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(
        default=None, description="Brand website URL."
    )
    optional_attributes: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional brand attributes. Please refer to GET /enum/optionalAttributeNames for dictionary of optional attribute names.",
        alias="optionalAttributes",
    )
    evp_vetting_score: Optional[StrictInt] = Field(
        default=None, description="External vetting score.", alias="evpVettingScore"
    )

    __properties: ClassVar[List[str]] = [
        "accountId",
        "brandId",
        "firstName",
        "lastName",
        "displayName",
        "companyName",
        "phone",
        "email",
        "website",
        "optionalAttributes",
        "evpVettingScore",
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
        """Create an instance of SMSTenDLCPartnerCampaignBrand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "brand_id",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if account_id (nullable) is None
        # and model_fields_set contains the field
        if self.account_id is None and "account_id" in self.model_fields_set:
            _dict["accountId"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SMSTenDLCPartnerCampaignBrand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "accountId": obj.get("accountId"),
                "brandId": obj.get("brandId"),
                "firstName": obj.get("firstName"),
                "lastName": obj.get("lastName"),
                "displayName": obj.get("displayName"),
                "companyName": obj.get("companyName"),
                "phone": obj.get("phone"),
                "email": obj.get("email"),
                "website": obj.get("website"),
                "optionalAttributes": obj.get("optionalAttributes"),
                "evpVettingScore": obj.get("evpVettingScore"),
            }
        )
        return _obj
