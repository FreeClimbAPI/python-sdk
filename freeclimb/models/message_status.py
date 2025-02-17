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
import json
from enum import Enum
from typing_extensions import Self


class MessageStatus(str, Enum):
    """
    Indicates the state of the message through the message lifecycle including: new, queued, rejected, sending, sent, failed, received, undelivered, expired, deleted, and unknown
    """

    """
    allowed enum values
    """
    NEW = "new"
    QUEUED = "queued"
    REJECTED = "rejected"
    SENDING = "sending"
    SENT = "sent"
    FAILED = "failed"
    RECEIVED = "received"
    UNDELIVERED = "undelivered"
    EXPIRED = "expired"
    DELETED = "deleted"
    UNKNOWN = "unknown"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MessageStatus from a JSON string"""
        return cls(json.loads(json_str))
