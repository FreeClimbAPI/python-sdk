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


class QueueResult(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    QueueResult
    """  # noqa: E501

    uri: Optional[StrictStr] = Field(
        default=None, description="The URI for this resource, relative to /apiserver."
    )
    date_created: Optional[StrictStr] = Field(
        default=None,
        description="The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).",
        alias="dateCreated",
    )
    date_updated: Optional[StrictStr] = Field(
        default=None,
        description="The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).",
        alias="dateUpdated",
    )
    revision: Optional[StrictInt] = Field(
        default=None,
        description="Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.",
    )
    account_id: Optional[StrictStr] = Field(
        default=None,
        description="ID of the account that created this Queue.",
        alias="accountId",
    )
    queue_id: Optional[StrictStr] = Field(
        default=None,
        description="A string that uniquely identifies this Queue resource.",
        alias="queueId",
    )
    alias: Optional[StrictStr] = Field(
        default=None, description="A description for this Queue."
    )
    max_size: Optional[StrictInt] = Field(
        default=None,
        description="The maximum number of Calls permitted in the Queue. Default is 100. Maximum is 1000.",
        alias="maxSize",
    )
    current_size: Optional[StrictInt] = Field(
        default=None,
        description="Count of Calls currently in the Queue.",
        alias="currentSize",
    )
    average_queue_removal_time: Optional[StrictInt] = Field(
        default=None,
        description="The average amount of time (in seconds) for a call to be removed from the queue.",
        alias="averageQueueRemovalTime",
    )
    subresource_uris: Optional[Dict[str, Any]] = Field(
        default=None,
        description="List of subresources for this Queue (which includes Queue members).",
        alias="subresourceUris",
    )

    __properties: ClassVar[List[str]] = [
        "uri",
        "dateCreated",
        "dateUpdated",
        "revision",
        "accountId",
        "queueId",
        "alias",
        "maxSize",
        "currentSize",
        "averageQueueRemovalTime",
        "subresourceUris",
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
        """Create an instance of QueueResult from a JSON string"""
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
        # set to None if account_id (nullable) is None
        # and model_fields_set contains the field
        if self.account_id is None and "account_id" in self.model_fields_set:
            _dict["accountId"] = None

        # set to None if queue_id (nullable) is None
        # and model_fields_set contains the field
        if self.queue_id is None and "queue_id" in self.model_fields_set:
            _dict["queueId"] = None

        # set to None if alias (nullable) is None
        # and model_fields_set contains the field
        if self.alias is None and "alias" in self.model_fields_set:
            _dict["alias"] = None

        # set to None if max_size (nullable) is None
        # and model_fields_set contains the field
        if self.max_size is None and "max_size" in self.model_fields_set:
            _dict["maxSize"] = None

        # set to None if current_size (nullable) is None
        # and model_fields_set contains the field
        if self.current_size is None and "current_size" in self.model_fields_set:
            _dict["currentSize"] = None

        # set to None if average_queue_removal_time (nullable) is None
        # and model_fields_set contains the field
        if (
            self.average_queue_removal_time is None
            and "average_queue_removal_time" in self.model_fields_set
        ):
            _dict["averageQueueRemovalTime"] = None

        # set to None if subresource_uris (nullable) is None
        # and model_fields_set contains the field
        if (
            self.subresource_uris is None
            and "subresource_uris" in self.model_fields_set
        ):
            _dict["subresourceUris"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueueResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "uri": obj.get("uri"),
                "dateCreated": obj.get("dateCreated"),
                "dateUpdated": obj.get("dateUpdated"),
                "revision": obj.get("revision"),
                "accountId": obj.get("accountId"),
                "queueId": obj.get("queueId"),
                "alias": obj.get("alias"),
                "maxSize": obj.get("maxSize"),
                "currentSize": obj.get("currentSize"),
                "averageQueueRemovalTime": obj.get("averageQueueRemovalTime"),
                "subresourceUris": obj.get("subresourceUris"),
            }
        )
        return _obj
