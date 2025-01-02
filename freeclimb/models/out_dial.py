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

from pydantic import ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from freeclimb.models.if_machine import IfMachine
from freeclimb.models.percl_command import PerclCommand
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class OutDial(
    PerclCommand,
    populate_by_name=True,
    validate_assignment=True,
    protected_namespaces=(),
):
    """
    The OutDial command is used to call a phone number
    """  # noqa: E501

    action_url: StrictStr = Field(
        description="URL to which FreeClimb sends an HTTP POST request. ",
        alias="actionUrl",
    )
    call_connect_url: StrictStr = Field(
        description="URL to which FreeClimb makes an HTTP POST request informing the result of the OutDial.",
        alias="callConnectUrl",
    )
    calling_number: StrictStr = Field(
        description="he caller ID to show to the called party when FreeClimb calls. This can be one of the following: The To or From number provided in the first Webhook to your webserver. Any phone number you have purchased from FreeClimb.",
        alias="callingNumber",
    )
    destination: StrictStr = Field(
        description="E.164 representation of the phone number to Call. "
    )
    if_machine: Optional[IfMachine] = Field(default=None, alias="ifMachine")
    if_machine_url: Optional[StrictStr] = Field(
        default=None,
        description="When the `ifMachine` flag is set to `redirect`, this attribute specifies a URL to which FreeClimb makes a POST request when an answering machine or a fax machine is detected. This URL is required if the `ifMachine` flag is set to `redirect`. Otherwise, it should not be included.",
        alias="ifMachineUrl",
    )
    send_digits: Optional[StrictStr] = Field(
        default=None,
        description="DTMF tones to play to the outdialed Call. This is typically used to dial a number and then dial an extension.",
        alias="sendDigits",
    )
    status_callback_url: Optional[StrictStr] = Field(
        default=None,
        description="When the outdialed Call leg terminates, FreeClimb sends a `callStatus` Webhook to the `statusCallbackUrl`. This is a notification only; any PerCL command returned is ignored.",
        alias="statusCallbackUrl",
    )
    timeout: Optional[StrictInt] = Field(
        default=None,
        description="Maximum time in seconds the `OutDial` command waits for the called party to answer the Call. When a timeout occurs, FreeClimb invokes the `callConnectUrl` Webhook to report that the out-dialed Call has ended with a status of `noAnswer`.",
    )
    privacy_mode: Optional[StrictBool] = Field(
        default=None,
        description="Parameter `privacyMode` will not log the `text` as required by PCI compliance.",
        alias="privacyMode",
    )
    command: StrictStr = "OutDial"

    __properties: ClassVar[List[str]] = [
        "command",
        "actionUrl",
        "callConnectUrl",
        "callingNumber",
        "destination",
        "ifMachine",
        "ifMachineUrl",
        "sendDigits",
        "statusCallbackUrl",
        "timeout",
        "privacyMode",
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
        """Create an instance of OutDial from a JSON string"""
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
        """Create an instance of OutDial from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "command": obj.get("command"),
                "actionUrl": obj.get("actionUrl"),
                "callConnectUrl": obj.get("callConnectUrl"),
                "callingNumber": obj.get("callingNumber"),
                "destination": obj.get("destination"),
                "ifMachine": obj.get("ifMachine"),
                "ifMachineUrl": obj.get("ifMachineUrl"),
                "sendDigits": obj.get("sendDigits"),
                "statusCallbackUrl": obj.get("statusCallbackUrl"),
                "timeout": obj.get("timeout"),
                "privacyMode": obj.get("privacyMode"),
            }
        )
        return _obj
