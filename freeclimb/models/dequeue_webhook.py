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

from pydantic import ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from freeclimb.models.call_direction import CallDirection
from freeclimb.models.call_status import CallStatus
from freeclimb.models.webhook import Webhook
from typing import Optional, Set
from typing_extensions import Self

class DequeueWebhook(Webhook):
    """
    A queued call has been dequeued and the actionUrl of the corresponding Enqueue action is being invoked. A PerCL response is expected.
    """ # noqa: E501
        
    request_type: Optional[StrictStr] = Field(default=None, description="Context or reason why this request is being made. Will be dequeue - A queued call has been dequeued and the actionUrl of the corresponding Enqueue action is being invoked.", alias="requestType")

        
    call_id: Optional[StrictStr] = Field(default=None, description="Unique ID for this Call, generated by FreeClimb.", alias="callId")

        
    account_id: Optional[StrictStr] = Field(default=None, description="Account ID associated with your account.", alias="accountId")

        
    var_from: Optional[StrictStr] = Field(default=None, description="Phone number of the party that initiated the Call (in E.164 format).", alias="from")

        
    to: Optional[StrictStr] = Field(default=None, description="Phone number provisioned to you and to which this Call is directed (in E.164 format).")

        

        

        
    conference_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the Conference.", alias="conferenceId")

        
    queue_id: Optional[StrictStr] = Field(default=None, description="This is only populated if the request pertains to a Queue. Otherwise, it is set to null.", alias="queueId")

        
    queue_result: Optional[StrictStr] = Field(default=None, description="The final result of the enqueued Call. Valid values are: •dequeued - Enqueued caller exited the Queue via a Dequeue action (Dequeue command or Queue Members POST REST API).", alias="queueResult")

        
    queue_time: Optional[StrictInt] = Field(default=None, description="Time (in seconds) the call spent in the Queue. This is only available if the Call was actually enqueued.", alias="queueTime")

    __properties: ClassVar[List[str]] = ["requestType", "callId", "accountId", "from", "to", "callStatus", "direction", "conferenceId", "queueId", "queueResult", "queueTime"]

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
        """Create an instance of DequeueWebhook from a JSON string"""
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
        # set to None if call_status (nullable) is None
        # and model_fields_set contains the field
        if self.call_status is None and "call_status" in self.model_fields_set:
            _dict['callStatus'] = None

        # set to None if direction (nullable) is None
        # and model_fields_set contains the field
        if self.direction is None and "direction" in self.model_fields_set:
            _dict['direction'] = None

        # set to None if queue_id (nullable) is None
        # and model_fields_set contains the field
        if self.queue_id is None and "queue_id" in self.model_fields_set:
            _dict['queueId'] = None

        # set to None if queue_time (nullable) is None
        # and model_fields_set contains the field
        if self.queue_time is None and "queue_time" in self.model_fields_set:
            _dict['queueTime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DequeueWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "requestType": obj.get("requestType"),
            "callId": obj.get("callId"),
            "accountId": obj.get("accountId"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "callStatus": obj.get("callStatus"),
            "direction": obj.get("direction"),
            "conferenceId": obj.get("conferenceId"),
            "queueId": obj.get("queueId"),
            "queueResult": obj.get("queueResult"),
            "queueTime": obj.get("queueTime")
        })
        return _obj

