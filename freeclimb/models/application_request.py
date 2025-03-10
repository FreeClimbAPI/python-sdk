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


class ApplicationRequest(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    ApplicationRequest
    """  # noqa: E501

    alias: Optional[StrictStr] = Field(
        default=None,
        description="A human readable description of the application, with maximum length 64 characters.",
    )
    voice_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL that FreeClimb will request when an inbound call arrives on a phone number assigned to this application. Used only for inbound calls.",
        alias="voiceUrl",
    )
    voice_fallback_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL that FreeClimb will request if it times out waiting for a response from the voiceUrl. Used for inbound calls only. Note: A PerCL response is expected to control the inbound call.",
        alias="voiceFallbackUrl",
    )
    call_connect_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL that FreeClimb will request when an outbound call request is complete. Used for outbound calls only.  Note: A PerCL response is expected if the outbound call is connected (status=InProgress) to control the call.",
        alias="callConnectUrl",
    )
    status_callback_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL that FreeClimb will request to pass call status (such as call ended) to the application.  Note: This is a notification only; any PerCL returned will be ignored.",
        alias="statusCallbackUrl",
    )
    sms_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL that FreeClimb will request when a phone number assigned to this application receives an incoming SMS message. Used for inbound SMS only.  Note: Any PerCL returned will be ignored.",
        alias="smsUrl",
    )
    sms_fallback_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL that FreeClimb will request if it times out waiting for a response from the smsUrl. Used for inbound SMS only.  Note: Any PerCL returned will be ignored.",
        alias="smsFallbackUrl",
    )

    __properties: ClassVar[List[str]] = [
        "alias",
        "voiceUrl",
        "voiceFallbackUrl",
        "callConnectUrl",
        "statusCallbackUrl",
        "smsUrl",
        "smsFallbackUrl",
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
        """Create an instance of ApplicationRequest from a JSON string"""
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
        # set to None if voice_url (nullable) is None
        # and model_fields_set contains the field
        if self.voice_url is None and "voice_url" in self.model_fields_set:
            _dict["voiceUrl"] = None

        # set to None if voice_fallback_url (nullable) is None
        # and model_fields_set contains the field
        if (
            self.voice_fallback_url is None
            and "voice_fallback_url" in self.model_fields_set
        ):
            _dict["voiceFallbackUrl"] = None

        # set to None if call_connect_url (nullable) is None
        # and model_fields_set contains the field
        if (
            self.call_connect_url is None
            and "call_connect_url" in self.model_fields_set
        ):
            _dict["callConnectUrl"] = None

        # set to None if status_callback_url (nullable) is None
        # and model_fields_set contains the field
        if (
            self.status_callback_url is None
            and "status_callback_url" in self.model_fields_set
        ):
            _dict["statusCallbackUrl"] = None

        # set to None if sms_url (nullable) is None
        # and model_fields_set contains the field
        if self.sms_url is None and "sms_url" in self.model_fields_set:
            _dict["smsUrl"] = None

        # set to None if sms_fallback_url (nullable) is None
        # and model_fields_set contains the field
        if (
            self.sms_fallback_url is None
            and "sms_fallback_url" in self.model_fields_set
        ):
            _dict["smsFallbackUrl"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "alias": obj.get("alias"),
                "voiceUrl": obj.get("voiceUrl"),
                "voiceFallbackUrl": obj.get("voiceFallbackUrl"),
                "callConnectUrl": obj.get("callConnectUrl"),
                "statusCallbackUrl": obj.get("statusCallbackUrl"),
                "smsUrl": obj.get("smsUrl"),
                "smsFallbackUrl": obj.get("smsFallbackUrl"),
            }
        )
        return _obj
