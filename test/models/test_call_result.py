# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import pydantic_core
from datetime import datetime
import freeclimb
from freeclimb import *
from freeclimb.models.call_result import CallResult


class TestCallResult(unittest.TestCase):
    """CallResult unit test stubs"""

    def setUp(self):
        self.model = CallResult()

    def test_uri(self):
        """Test CallResult.uri"""
        self.model.uri = "TEST_STRING"
        assert self.model.uri == "TEST_STRING"

    def test_date_created(self):
        """Test CallResult.date_created"""
        self.model.date_created = "TEST_STRING"
        assert self.model.date_created == "TEST_STRING"

    def test_date_updated(self):
        """Test CallResult.date_updated"""
        self.model.date_updated = "TEST_STRING"
        assert self.model.date_updated == "TEST_STRING"

    def test_revision(self):
        """Test CallResult.revision"""
        self.model.revision = 1
        assert self.model.revision == 1

    def test_call_id(self):
        """Test CallResult.call_id"""
        self.model.call_id = "TEST_STRING"
        assert self.model.call_id == "TEST_STRING"

    def test_parent_call_id(self):
        """Test CallResult.parent_call_id"""
        self.model.parent_call_id = "TEST_STRING"
        assert self.model.parent_call_id == "TEST_STRING"

    def test_account_id(self):
        """Test CallResult.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.account_id == "TEST_STRING"

    def test_var_from(self):
        """Test CallResult.var_from"""
        self.model.var_from = "TEST_STRING"
        assert self.model.var_from == "TEST_STRING"

    def test_to(self):
        """Test CallResult.to"""
        self.model.to = "TEST_STRING"
        assert self.model.to == "TEST_STRING"

    def test_phone_number_id(self):
        """Test CallResult.phone_number_id"""
        self.model.phone_number_id = "TEST_STRING"
        assert self.model.phone_number_id == "TEST_STRING"

    def test_call_status(self):
        """Test CallResult.call_status"""
        self.model.call_status = CallStatus.QUEUED
        assert self.model.call_status == CallStatus.QUEUED
        self.model.call_status = CallStatus.RINGING
        assert self.model.call_status == CallStatus.RINGING
        self.model.call_status = CallStatus.IN_PROGRESS
        assert self.model.call_status == CallStatus.IN_PROGRESS
        self.model.call_status = CallStatus.CANCELED
        assert self.model.call_status == CallStatus.CANCELED
        self.model.call_status = CallStatus.COMPLETED
        assert self.model.call_status == CallStatus.COMPLETED
        self.model.call_status = CallStatus.FAILED
        assert self.model.call_status == CallStatus.FAILED
        self.model.call_status = CallStatus.BUSY
        assert self.model.call_status == CallStatus.BUSY
        self.model.call_status = CallStatus.NO_ANSWER
        assert self.model.call_status == CallStatus.NO_ANSWER

    def test_start_time(self):
        """Test CallResult.start_time"""
        self.model.start_time = "TEST_STRING"
        assert self.model.start_time == "TEST_STRING"

    def test_connect_time(self):
        """Test CallResult.connect_time"""
        self.model.connect_time = "TEST_STRING"
        assert self.model.connect_time == "TEST_STRING"

    def test_end_time(self):
        """Test CallResult.end_time"""
        self.model.end_time = "TEST_STRING"
        assert self.model.end_time == "TEST_STRING"

    def test_duration(self):
        """Test CallResult.duration"""
        self.model.duration = 1
        assert self.model.duration == 1

    def test_connect_duration(self):
        """Test CallResult.connect_duration"""
        self.model.connect_duration = 1
        assert self.model.connect_duration == 1

    def test_direction(self):
        """Test CallResult.direction"""
        self.model.direction = CallDirection.INBOUND
        assert self.model.direction == CallDirection.INBOUND
        self.model.direction = CallDirection.OUTBOUND_API
        assert self.model.direction == CallDirection.OUTBOUND_API
        self.model.direction = CallDirection.OUTBOUND_DIAL
        assert self.model.direction == CallDirection.OUTBOUND_DIAL

    def test_answered_by(self):
        """Test CallResult.answered_by"""
        self.model.answered_by = AnsweredBy.HUMAN
        assert self.model.answered_by == AnsweredBy.HUMAN
        self.model.answered_by = AnsweredBy.MACHINE
        assert self.model.answered_by == AnsweredBy.MACHINE

    def test_subresource_uris(self):
        """Test CallResult.subresource_uris"""
        testObject = {}
        self.model.subresource_uris = testObject
        assert self.model.subresource_uris == testObject

    def test_application_id(self):
        """Test CallResult.application_id"""
        self.model.application_id = "TEST_STRING"
        assert self.model.application_id == "TEST_STRING"


if __name__ == "__main__":
    unittest.main()
