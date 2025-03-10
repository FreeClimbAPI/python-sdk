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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from freeclimb.models.play_beep import PlayBeep
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class CreateConferenceRequest(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    CreateConferenceRequest
    """  # noqa: E501

    alias: Optional[StrictStr] = Field(
        default=None,
        description="A description for this Conference. Maximum 64 characters.",
    )
    play_beep: Optional[PlayBeep] = Field(default=None, alias="playBeep")
    record: Optional[StrictBool] = Field(
        default=None, description="Setting to `true` records the entire Conference."
    )
    wait_url: Optional[StrictStr] = Field(
        default=None,
        description="If specified, a URL for the audio file that provides custom hold music for the Conference when it is in the populated state. Otherwise, FreeClimb uses a system default audio file. This is always fetched using HTTP GET and is fetched just once &mdash; when the Conference is created.",
        alias="waitUrl",
    )
    status_callback_url: StrictStr = Field(
        description="This URL is invoked when the status of the Conference changes. For more information, see **statusCallbackUrl** (below).",
        alias="statusCallbackUrl",
    )

    __properties: ClassVar[List[str]] = [
        "alias",
        "playBeep",
        "record",
        "waitUrl",
        "statusCallbackUrl",
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
        """Create an instance of CreateConferenceRequest from a JSON string"""
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
        # set to None if play_beep (nullable) is None
        # and model_fields_set contains the field
        if self.play_beep is None and "play_beep" in self.model_fields_set:
            _dict["playBeep"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateConferenceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "alias": obj.get("alias"),
                "playBeep": obj.get("playBeep"),
                "record": obj.get("record"),
                "waitUrl": obj.get("waitUrl"),
                "statusCallbackUrl": obj.get("statusCallbackUrl"),
            }
        )
        return _obj
