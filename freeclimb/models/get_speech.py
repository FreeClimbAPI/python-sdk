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

from pydantic import ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from freeclimb.models.grammar_type import GrammarType
from freeclimb.models.percl_command import PerclCommand
from typing import Optional, Set
from typing_extensions import Self

class GetSpeech(PerclCommand):
    """
    The `GetSpeech` command enables the Caller to respond to the application using a supported language. Unlike DTMF entry, which implicitly restricts the user to using the available buttons on the phone key pad, speech input allows for flexible audio inputs based on grammar. FreeClimb supports grammars written using GRXML compatible with the Microsoft Speech Platform. `GetSpeech` is only supported on a single call leg. It is not supported when there are two or more call legs connected (as in within a Conference).
    """ # noqa: E501
        
    action_url: StrictStr = Field(description="When the caller has finished speaking or the command has timed out, FreeClimb will make a POST request to this URL. A PerCL response is expected to continue handling the call.", alias="actionUrl")

        

        
    grammar_file: StrictStr = Field(description="The grammar file to use for speech recognition. If grammarType is set to URL, this attribute is specified as a download URL.", alias="grammarFile")

        
    grammar_rule: Optional[StrictStr] = Field(default=None, description="The grammar rule within the specified grammar file to use for speech recognition. This attribute is optional if `grammarType` is `URL` and ignored if `grammarType` is `BUILTIN`.", alias="grammarRule")

        
    play_beep: Optional[StrictBool] = Field(default=None, description="Indicates whether a beep should be played just before speech recognition is initiated so that the speaker can start to speak.", alias="playBeep")

        
    prompts: Optional[List[PerclCommand]] = Field(default=None, description="The JSON array of PerCL commands to nest within the `GetSpeech` command. The `Say`, `Play`, and `Pause` commands can be used. The nested actions are executed while FreeClimb is waiting for input from the caller. This allows for playing menu options to the caller and to prompt for the expected input. These commands stop executing when the caller begins to input speech.")

        
    no_input_timeout_ms: Optional[StrictInt] = Field(default=None, description="When recognition is started and there is no speech detected for `noInputTimeoutMs` milliseconds, the recognizer will terminate the recognition operation.", alias="noInputTimeoutMs")

        
    recognition_timeout_ms: Optional[StrictInt] = Field(default=None, description="When playback of prompts ends and there is no match for `recognitionTimeoutMs` milliseconds, the recognizer will terminate the recognition operation.", alias="recognitionTimeoutMs")

        
    confidence_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="When a recognition resource recognizes a spoken phrase, it associates a confidence level with that match. Parameter `confidenceThreshold` specifies what confidence level is considered a successful match. Values are between 0.0 and 1.0.", alias="confidenceThreshold")

        
    sensitivity_level: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The speech recognizer supports a variable level of sound sensitivity. The sensitivityLevel attribute allows for filtering out background noise, so it is not mistaken for speech. Values are between 0.0 and 1.0 ", alias="sensitivityLevel")

        
    speech_complete_timeout_ms: Optional[StrictInt] = Field(default=None, description="Parameter `speechCompleteTimeoutMs` specifies the length of silence required following user speech before the speech recognizer finalizes a result. This timeout applies when the recognizer currently has a complete match against an active grammar. Reasonable speech complete timeout values are typically in the range of 0.3 seconds to 1.0 seconds.", alias="speechCompleteTimeoutMs")

        
    speech_incomplete_timeout_ms: Optional[StrictInt] = Field(default=None, description="Parameter `speechIncompleteTimeoutMs` specifies the length of silence following user speech after which a recognizer finalizes a result. This timeout applies when the speech prior to the silence is an incomplete match of all active grammars. Timeout `speechIncompleteTimeoutMs` is usually longer than `speechCompleteTimeoutMs` to allow users to pause mid-utterance.", alias="speechIncompleteTimeoutMs")

        
    privacy_mode: Optional[StrictBool] = Field(default=None, description="Parameter privacyMode will not log the `text` as required by PCI compliance.", alias="privacyMode")

    __properties: ClassVar[List[str]] = ["command", "actionUrl", "grammarType", "grammarFile", "grammarRule", "playBeep", "prompts", "noInputTimeoutMs", "recognitionTimeoutMs", "confidenceThreshold", "sensitivityLevel", "speechCompleteTimeoutMs", "speechIncompleteTimeoutMs", "privacyMode"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetSpeech from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in prompts (list)
        _items = []
        if self.prompts:
            for _item_prompts in self.prompts:
                if _item_prompts:
                    _items.append(_item_prompts.to_dict())
            _dict['prompts'] = _items
        # set to None if grammar_type (nullable) is None
        # and model_fields_set contains the field
        if self.grammar_type is None and "grammar_type" in self.model_fields_set:
            _dict['grammarType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSpeech from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "command": obj.get("command"),
            "actionUrl": obj.get("actionUrl"),
            "grammarType": obj.get("grammarType"),
            "grammarFile": obj.get("grammarFile"),
            "grammarRule": obj.get("grammarRule"),
            "playBeep": obj.get("playBeep"),
            "prompts": [PerclCommand.from_dict(_item) for _item in obj["prompts"]] if obj.get("prompts") is not None else None,
            "noInputTimeoutMs": obj.get("noInputTimeoutMs"),
            "recognitionTimeoutMs": obj.get("recognitionTimeoutMs"),
            "confidenceThreshold": obj.get("confidenceThreshold"),
            "sensitivityLevel": obj.get("sensitivityLevel"),
            "speechCompleteTimeoutMs": obj.get("speechCompleteTimeoutMs"),
            "speechIncompleteTimeoutMs": obj.get("speechIncompleteTimeoutMs"),
            "privacyMode": obj.get("privacyMode")
        })
        return _obj

