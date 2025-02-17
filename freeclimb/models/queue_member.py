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
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class QueueMember(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    QueueMember
    """  # noqa: E501

    uri: Optional[StrictStr] = Field(
        default=None,
        description="URI for this Queue Member resource, relative to the API base URL.",
    )
    call_id: Optional[StrictStr] = Field(
        default=None,
        description="ID of the Call associated with this Queue Member.",
        alias="callId",
    )
    wait_time: Optional[StrictInt] = Field(
        default=None,
        description="Number of seconds the Member has been in the queue.",
        alias="waitTime",
    )
    position: Optional[StrictInt] = Field(
        default=None, description="Member's current position in the Queue, 1 indexed."
    )
    date_enqueued: Optional[StrictStr] = Field(
        default=None,
        description="Date that the Member was enqueued (GMT), given in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).",
        alias="dateEnqueued",
    )

    __properties: ClassVar[List[str]] = [
        "uri",
        "callId",
        "waitTime",
        "position",
        "dateEnqueued",
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
        """Create an instance of QueueMember from a JSON string"""
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
        # set to None if uri (nullable) is None
        # and model_fields_set contains the field
        if self.uri is None and "uri" in self.model_fields_set:
            _dict["uri"] = None

        # set to None if call_id (nullable) is None
        # and model_fields_set contains the field
        if self.call_id is None and "call_id" in self.model_fields_set:
            _dict["callId"] = None

        # set to None if wait_time (nullable) is None
        # and model_fields_set contains the field
        if self.wait_time is None and "wait_time" in self.model_fields_set:
            _dict["waitTime"] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict["position"] = None

        # set to None if date_enqueued (nullable) is None
        # and model_fields_set contains the field
        if self.date_enqueued is None and "date_enqueued" in self.model_fields_set:
            _dict["dateEnqueued"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueueMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "uri": obj.get("uri"),
                "callId": obj.get("callId"),
                "waitTime": obj.get("waitTime"),
                "position": obj.get("position"),
                "dateEnqueued": obj.get("dateEnqueued"),
            }
        )
        return _obj
