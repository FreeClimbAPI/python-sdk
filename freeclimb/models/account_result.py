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
from freeclimb.models.account_status import AccountStatus
from freeclimb.models.account_type import AccountType
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class AccountResult(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    AccountResult
    """  # noqa: E501

    uri: Optional[StrictStr] = Field(
        default=None, description="The URI for this resource, relative to /apiserver."
    )
    date_created: Optional[StrictStr] = Field(
        default=None,
        description="The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).",
        alias="dateCreated",
    )
    date_updated: Optional[StrictStr] = Field(
        default=None,
        description="The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).",
        alias="dateUpdated",
    )
    revision: Optional[StrictInt] = Field(
        default=None,
        description="Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.",
    )
    account_id: Optional[StrictStr] = Field(
        default=None,
        description="String that uniquely identifies this account resource.",
        alias="accountId",
    )
    api_key: Optional[StrictStr] = Field(
        default=None,
        description="The API key assigned to this account. This key must be kept a secret by the customer.",
        alias="apiKey",
    )
    alias: Optional[StrictStr] = Field(
        default=None, description="A description for this account."
    )
    label: Optional[StrictStr] = Field(
        default=None,
        description="A string that identifies a category or group to which the account belongs.",
    )
    type: Optional[AccountType] = None
    status: Optional[AccountStatus] = None
    subresource_uris: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The list of subresources for this account.",
        alias="subresourceUris",
    )

    __properties: ClassVar[List[str]] = [
        "uri",
        "dateCreated",
        "dateUpdated",
        "revision",
        "accountId",
        "apiKey",
        "alias",
        "label",
        "type",
        "status",
        "subresourceUris",
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
        """Create an instance of AccountResult from a JSON string"""
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
        # set to None if account_id (nullable) is None
        # and model_fields_set contains the field
        if self.account_id is None and "account_id" in self.model_fields_set:
            _dict["accountId"] = None

        # set to None if api_key (nullable) is None
        # and model_fields_set contains the field
        if self.api_key is None and "api_key" in self.model_fields_set:
            _dict["apiKey"] = None

        # set to None if alias (nullable) is None
        # and model_fields_set contains the field
        if self.alias is None and "alias" in self.model_fields_set:
            _dict["alias"] = None

        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict["label"] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict["type"] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict["status"] = None

        # set to None if subresource_uris (nullable) is None
        # and model_fields_set contains the field
        if (
            self.subresource_uris is None
            and "subresource_uris" in self.model_fields_set
        ):
            _dict["subresourceUris"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "uri": obj.get("uri"),
                "dateCreated": obj.get("dateCreated"),
                "dateUpdated": obj.get("dateUpdated"),
                "revision": obj.get("revision"),
                "accountId": obj.get("accountId"),
                "apiKey": obj.get("apiKey"),
                "alias": obj.get("alias"),
                "label": obj.get("label"),
                "type": obj.get("type"),
                "status": obj.get("status"),
                "subresourceUris": obj.get("subresourceUris"),
            }
        )
        return _obj
