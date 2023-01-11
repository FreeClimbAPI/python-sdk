"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from freeclimb.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from freeclimb.exceptions import ApiAttributeError



from enum import Enum

# class syntax
class RequestType(str, Enum):
    INBOUND_CALL= "inboundCall",
    RECORD= "record",
    GET_DIGITS= "getDigits",
    GET_SPEECH= "getSpeech",
    REDIRECT= "redirect",
    PAUSE= "pause",
    OUT_DIAL_START= "outDialStart",
    OUT_DIAL_CONNECT= "outDialConnect",
    OUT_DIAL_API_CONNECT= "outDialApiConnect",
    MACHINE_DETECTED= "machineDetected",
    DEQUEUE= "dequeue",
    QUEUE_WAIT= "queueWait",
    ADD_TO_QUEUE_NOTIFICATION= "addToQueueNotification",
    REMOVE_FROM_QUEUE_NOTIFICATION= "removeFromQueueNotification",
    CALL_STATUS= "callStatus",
    CREATE_CONFERENCE= "createConference",
    CONFERENCE_STATUS= "conferenceStatus",
    LEAVE_CONFERENCE= "leaveConference",
    ADD_TO_CONFERENCE_NOTIFICATION= "addToConferenceNotification",
    CONFERENCE_RECORDING_STATUS= "conferenceRecordingStatus",
    CONFERENCE_CALL_CONTROL= "conferenceCallControl",
    MESSAGE_DELIVERY= "messageDelivery",
    MESSAGE_STATUS= "messageStatus",


