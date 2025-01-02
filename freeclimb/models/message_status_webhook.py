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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from freeclimb.models.message_status import MessageStatus
from freeclimb.models.webhook import Webhook
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class MessageStatusWebhook(
    Webhook, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    An outbound SMS has changed status and the notificationUrl from the Sms command or Send an SMS request is being invoked. A PerCL response will be ignored.
    """  # noqa: E501

    request_type: Optional[StrictStr] = Field(
        default=None,
        description="Value will be messageStatus - An outbound SMS has changed status and the Sms command's notificationUrl is being invoked.",
        alias="requestType",
    )
    account_id: Optional[StrictStr] = Field(
        default=None,
        description="Account ID associated with your account.",
        alias="accountId",
    )
    message_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique ID for this message, generated by FreeClimb.",
        alias="messageId",
    )
    call_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique ID for the Call in the context of which the Sms PerCL command was issued.",
        alias="callId",
    )
    var_from: Optional[StrictStr] = Field(
        default=None,
        description="aPhone number used to initiate the SMS message (in E.164 format).",
        alias="from",
    )
    to: Optional[StrictStr] = Field(
        default=None,
        description="Destination number of the SMS message (in E.164 format).",
    )
    text: Optional[StrictStr] = Field(
        default=None, description="Body of the SMS message."
    )
    direction: Optional[StrictStr] = Field(
        default=None,
        description="Value will be outbound to indicate an outgoing SMS from FreeClimb.",
    )
    application_id: Optional[StrictStr] = Field(
        default=None,
        description="ID of the application to which the destination number is assigned. May be null if the originating number is invalid in some way or is not registered to an application.",
        alias="applicationId",
    )
    status: Optional[MessageStatus] = None
    phone_number_id: Optional[StrictStr] = Field(
        default=None,
        description="ID of the destination phone number.",
        alias="phoneNumberId",
    )

    __properties: ClassVar[List[str]] = [
        "requestType",
        "accountId",
        "messageId",
        "callId",
        "from",
        "to",
        "text",
        "direction",
        "applicationId",
        "status",
        "phoneNumberId",
    ]

    @classmethod
    def deserialize(cls, payload: str) -> Optional[Self]:
        return cls.from_json(payload)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MessageStatusWebhook from a JSON string"""
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
        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict["status"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MessageStatusWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "requestType": obj.get("requestType"),
                "accountId": obj.get("accountId"),
                "messageId": obj.get("messageId"),
                "callId": obj.get("callId"),
                "from": obj.get("from"),
                "to": obj.get("to"),
                "text": obj.get("text"),
                "direction": obj.get("direction"),
                "applicationId": obj.get("applicationId"),
                "status": obj.get("status"),
                "phoneNumberId": obj.get("phoneNumberId"),
            }
        )
        return _obj
