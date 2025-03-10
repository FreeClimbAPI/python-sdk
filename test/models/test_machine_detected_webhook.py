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
from freeclimb.models.machine_detected_webhook import MachineDetectedWebhook


class TestMachineDetectedWebhook(unittest.TestCase):
    """MachineDetectedWebhook unit test stubs"""

    def setUp(self):
        self.model = MachineDetectedWebhook()

    def test_request_type(self):
        """Test MachineDetectedWebhook.request_type"""

    def test_call_id(self):
        """Test MachineDetectedWebhook.call_id"""

        self.model.call_id = "TEST_STRING"
        assert self.model.call_id == "TEST_STRING"

    def test_account_id(self):
        """Test MachineDetectedWebhook.account_id"""

        self.model.account_id = "TEST_STRING"
        assert self.model.account_id == "TEST_STRING"

    def test_var_from(self):
        """Test MachineDetectedWebhook.var_from"""

        self.model.var_from = "TEST_STRING"
        assert self.model.var_from == "TEST_STRING"

    def test_to(self):
        """Test MachineDetectedWebhook.to"""

        self.model.to = "TEST_STRING"
        assert self.model.to == "TEST_STRING"

    def test_call_status(self):
        """Test MachineDetectedWebhook.call_status"""
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

    def test_direction(self):
        """Test MachineDetectedWebhook.direction"""
        self.model.direction = CallDirection.INBOUND
        assert self.model.direction == CallDirection.INBOUND
        self.model.direction = CallDirection.OUTBOUND_API
        assert self.model.direction == CallDirection.OUTBOUND_API
        self.model.direction = CallDirection.OUTBOUND_DIAL
        assert self.model.direction == CallDirection.OUTBOUND_DIAL

    def test_conference_id(self):
        """Test MachineDetectedWebhook.conference_id"""

        self.model.conference_id = "TEST_STRING"
        assert self.model.conference_id == "TEST_STRING"

    def test_queue_id(self):
        """Test MachineDetectedWebhook.queue_id"""

        self.model.queue_id = "TEST_STRING"
        assert self.model.queue_id == "TEST_STRING"

    def test_parent_call_id(self):
        """Test MachineDetectedWebhook.parent_call_id"""

        self.model.parent_call_id = "TEST_STRING"
        assert self.model.parent_call_id == "TEST_STRING"

    def test_machine_type(self):
        """Test MachineDetectedWebhook.machine_type"""
        self.model.machine_type = MachineType.ANSWERING_MACHINE
        assert self.model.machine_type == MachineType.ANSWERING_MACHINE
        self.model.machine_type = MachineType.FAX_MODEM
        assert self.model.machine_type == MachineType.FAX_MODEM

    def test_deserialize(self):
        payload = '{ "requestType": "machineDetected" }'
        assert isinstance(
            MachineDetectedWebhook.deserialize(payload), MachineDetectedWebhook
        )


if __name__ == "__main__":
    unittest.main()
