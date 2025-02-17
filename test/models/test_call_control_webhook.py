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
from freeclimb.models.call_control_webhook import CallControlWebhook


class TestCallControlWebhook(unittest.TestCase):
    """CallControlWebhook unit test stubs"""

    def setUp(self):
        self.model = CallControlWebhook()

    def test_request_type(self):
        """Test CallControlWebhook.request_type"""

    def test_call_id(self):
        """Test CallControlWebhook.call_id"""

        self.model.call_id = "TEST_STRING"
        assert self.model.call_id == "TEST_STRING"

    def test_account_id(self):
        """Test CallControlWebhook.account_id"""

        self.model.account_id = "TEST_STRING"
        assert self.model.account_id == "TEST_STRING"

    def test_conference_id(self):
        """Test CallControlWebhook.conference_id"""

        self.model.conference_id = "TEST_STRING"
        assert self.model.conference_id == "TEST_STRING"

    def test_digits(self):
        """Test CallControlWebhook.digits"""

        self.model.digits = "TEST_STRING"
        assert self.model.digits == "TEST_STRING"

    def test_deserialize(self):
        payload = '{ "requestType": "callControl" }'
        assert isinstance(CallControlWebhook.deserialize(payload), CallControlWebhook)


if __name__ == "__main__":
    unittest.main()
