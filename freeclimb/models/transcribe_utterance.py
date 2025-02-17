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

from pydantic import ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from freeclimb.models.percl_command import PerclCommand
from freeclimb.models.transcribe_utterance_record import TranscribeUtteranceRecord
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class TranscribeUtterance(
    PerclCommand,
    populate_by_name=True,
    validate_assignment=True,
    protected_namespaces=(),
):
    """
    The `TranscribeUtterance` command transcribes the caller’s voice and returns transcription of the audio and optionally returns the recording of the audio transcribed.  `TranscribeUtterance` is blocking and is a terminal command. As such, the actionUrl property is required, and control of the Call picks up using the `PerCL` returned in response of the `actionUrl`. Recording and Transcription information is returned in the actionUrl request. If the reason this command ended was due to the call hanging up, any PerCL returned will not execute.
    """  # noqa: E501

    action_url: StrictStr = Field(alias="actionUrl")
    play_beep: Optional[StrictBool] = Field(default=False, alias="playBeep")
    record: Optional[TranscribeUtteranceRecord] = None
    privacy_for_logging: Optional[StrictBool] = Field(
        default=False, alias="privacyForLogging"
    )
    privacy_for_recording: Optional[StrictBool] = Field(
        default=False, alias="privacyForRecording"
    )
    prompts: Optional[List[PerclCommand]] = None
    command: StrictStr = "TranscribeUtterance"

    __properties: ClassVar[List[str]] = [
        "command",
        "actionUrl",
        "playBeep",
        "record",
        "privacyForLogging",
        "privacyForRecording",
        "prompts",
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
        """Create an instance of TranscribeUtterance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of record
        if self.record:
            _dict["record"] = self.record.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in prompts (list)
        _items = []
        if self.prompts:
            for _item_prompts in self.prompts:
                if _item_prompts:
                    _items.append(_item_prompts.to_dict())
            _dict["prompts"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TranscribeUtterance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "command": obj.get("command"),
                "actionUrl": obj.get("actionUrl"),
                "playBeep": (
                    obj.get("playBeep") if obj.get("playBeep") is not None else False
                ),
                "record": (
                    TranscribeUtteranceRecord.from_dict(obj["record"])
                    if obj.get("record") is not None
                    else None
                ),
                "privacyForLogging": (
                    obj.get("privacyForLogging")
                    if obj.get("privacyForLogging") is not None
                    else False
                ),
                "privacyForRecording": (
                    obj.get("privacyForRecording")
                    if obj.get("privacyForRecording") is not None
                    else False
                ),
                "prompts": (
                    [PerclCommand.from_dict(_item) for _item in obj["prompts"]]
                    if obj.get("prompts") is not None
                    else None
                ),
            }
        )
        return _obj
