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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from freeclimb.models.add_to_conference import AddToConference
    from freeclimb.models.create_conference import CreateConference
    from freeclimb.models.dequeue import Dequeue
    from freeclimb.models.enqueue import Enqueue
    from freeclimb.models.get_digits import GetDigits
    from freeclimb.models.get_speech import GetSpeech
    from freeclimb.models.hangup import Hangup
    from freeclimb.models.out_dial import OutDial
    from freeclimb.models.park import Park
    from freeclimb.models.pause import Pause
    from freeclimb.models.play import Play
    from freeclimb.models.play_early_media import PlayEarlyMedia
    from freeclimb.models.record_utterance import RecordUtterance
    from freeclimb.models.redirect import Redirect
    from freeclimb.models.reject import Reject
    from freeclimb.models.remove_from_conference import RemoveFromConference
    from freeclimb.models.say import Say
    from freeclimb.models.send_digits import SendDigits
    from freeclimb.models.set_listen import SetListen
    from freeclimb.models.set_talk import SetTalk
    from freeclimb.models.sms import Sms
    from freeclimb.models.start_record_call import StartRecordCall
    from freeclimb.models.terminate_conference import TerminateConference
    from freeclimb.models.transcribe_utterance import TranscribeUtterance
    from freeclimb.models.unpark import Unpark

class PerclCommand(BaseModel):
    """
    An individual command used in a PerCLScript.
    """ # noqa: E501
        
    command: Optional[StrictStr] = Field(default=None, description="Name of PerCL Command (this is automatically derived from mapping configuration and should not be manually supplied in any arguments)")

    __properties: ClassVar[List[str]] = ["command"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'command'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'AddToConference': 'AddToConference','CreateConference': 'CreateConference','Dequeue': 'Dequeue','Enqueue': 'Enqueue','GetDigits': 'GetDigits','GetSpeech': 'GetSpeech','Hangup': 'Hangup','OutDial': 'OutDial','Park': 'Park','Pause': 'Pause','Play': 'Play','PlayEarlyMedia': 'PlayEarlyMedia','RecordUtterance': 'RecordUtterance','Redirect': 'Redirect','Reject': 'Reject','RemoveFromConference': 'RemoveFromConference','Say': 'Say','SendDigits': 'SendDigits','SetListen': 'SetListen','SetTalk': 'SetTalk','Sms': 'Sms','StartRecordCall': 'StartRecordCall','TerminateConference': 'TerminateConference','TranscribeUtterance': 'TranscribeUtterance','Unpark': 'Unpark'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[AddToConference, CreateConference, Dequeue, Enqueue, GetDigits, GetSpeech, Hangup, OutDial, Park, Pause, Play, PlayEarlyMedia, RecordUtterance, Redirect, Reject, RemoveFromConference, Say, SendDigits, SetListen, SetTalk, Sms, StartRecordCall, TerminateConference, TranscribeUtterance, Unpark]]:
        """Create an instance of PerclCommand from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AddToConference, CreateConference, Dequeue, Enqueue, GetDigits, GetSpeech, Hangup, OutDial, Park, Pause, Play, PlayEarlyMedia, RecordUtterance, Redirect, Reject, RemoveFromConference, Say, SendDigits, SetListen, SetTalk, Sms, StartRecordCall, TerminateConference, TranscribeUtterance, Unpark]]:
        """Create an instance of PerclCommand from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AddToConference':
            return import_module("freeclimb.models.add_to_conference").AddToConference.from_dict(obj)
        if object_type ==  'CreateConference':
            return import_module("freeclimb.models.create_conference").CreateConference.from_dict(obj)
        if object_type ==  'Dequeue':
            return import_module("freeclimb.models.dequeue").Dequeue.from_dict(obj)
        if object_type ==  'Enqueue':
            return import_module("freeclimb.models.enqueue").Enqueue.from_dict(obj)
        if object_type ==  'GetDigits':
            return import_module("freeclimb.models.get_digits").GetDigits.from_dict(obj)
        if object_type ==  'GetSpeech':
            return import_module("freeclimb.models.get_speech").GetSpeech.from_dict(obj)
        if object_type ==  'Hangup':
            return import_module("freeclimb.models.hangup").Hangup.from_dict(obj)
        if object_type ==  'OutDial':
            return import_module("freeclimb.models.out_dial").OutDial.from_dict(obj)
        if object_type ==  'Park':
            return import_module("freeclimb.models.park").Park.from_dict(obj)
        if object_type ==  'Pause':
            return import_module("freeclimb.models.pause").Pause.from_dict(obj)
        if object_type ==  'Play':
            return import_module("freeclimb.models.play").Play.from_dict(obj)
        if object_type ==  'PlayEarlyMedia':
            return import_module("freeclimb.models.play_early_media").PlayEarlyMedia.from_dict(obj)
        if object_type ==  'RecordUtterance':
            return import_module("freeclimb.models.record_utterance").RecordUtterance.from_dict(obj)
        if object_type ==  'Redirect':
            return import_module("freeclimb.models.redirect").Redirect.from_dict(obj)
        if object_type ==  'Reject':
            return import_module("freeclimb.models.reject").Reject.from_dict(obj)
        if object_type ==  'RemoveFromConference':
            return import_module("freeclimb.models.remove_from_conference").RemoveFromConference.from_dict(obj)
        if object_type ==  'Say':
            return import_module("freeclimb.models.say").Say.from_dict(obj)
        if object_type ==  'SendDigits':
            return import_module("freeclimb.models.send_digits").SendDigits.from_dict(obj)
        if object_type ==  'SetListen':
            return import_module("freeclimb.models.set_listen").SetListen.from_dict(obj)
        if object_type ==  'SetTalk':
            return import_module("freeclimb.models.set_talk").SetTalk.from_dict(obj)
        if object_type ==  'Sms':
            return import_module("freeclimb.models.sms").Sms.from_dict(obj)
        if object_type ==  'StartRecordCall':
            return import_module("freeclimb.models.start_record_call").StartRecordCall.from_dict(obj)
        if object_type ==  'TerminateConference':
            return import_module("freeclimb.models.terminate_conference").TerminateConference.from_dict(obj)
        if object_type ==  'TranscribeUtterance':
            return import_module("freeclimb.models.transcribe_utterance").TranscribeUtterance.from_dict(obj)
        if object_type ==  'Unpark':
            return import_module("freeclimb.models.unpark").Unpark.from_dict(obj)

        raise ValueError("PerclCommand failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

