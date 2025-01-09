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


class IncomingNumberRequest(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    IncomingNumberRequest
    """  # noqa: E501

    application_id: Optional[StrictStr] = Field(
        default=None,
        description="ID of the Application that should handle calls to this number.",
        alias="applicationId",
    )
    alias: Optional[StrictStr] = Field(
        default=None, description="Description for this phone number."
    )
    campaign_id: Optional[StrictStr] = Field(
        default=None,
        description="The campaign ID generated by the campaign registry",
        alias="campaignId",
    )

    __properties: ClassVar[List[str]] = ["applicationId", "alias", "campaignId"]

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IncomingNumberRequest from a JSON string"""
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
        # set to None if campaign_id (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_id is None and "campaign_id" in self.model_fields_set:
            _dict["campaignId"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IncomingNumberRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "applicationId": obj.get("applicationId"),
                "alias": obj.get("alias"),
                "campaignId": obj.get("campaignId"),
            }
        )
        return _obj
