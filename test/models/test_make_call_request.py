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
from freeclimb.models.make_call_request import MakeCallRequest


class TestMakeCallRequest(unittest.TestCase):
    """MakeCallRequest unit test stubs"""

    def setUp(self):
        self.model = MakeCallRequest(
            var_from="",
            to="",
        )

    def test_var_from(self):
        """Test MakeCallRequest.var_from"""
        self.model.var_from = "TEST_STRING"
        assert self.model.var_from == "TEST_STRING"

    def test_to(self):
        """Test MakeCallRequest.to"""
        self.model.to = "TEST_STRING"
        assert self.model.to == "TEST_STRING"

    def test_application_id(self):
        """Test MakeCallRequest.application_id"""
        self.model.application_id = "TEST_STRING"
        assert self.model.application_id == "TEST_STRING"

    def test_send_digits(self):
        """Test MakeCallRequest.send_digits"""
        self.model.send_digits = "TEST_STRING"
        assert self.model.send_digits == "TEST_STRING"

    def test_if_machine(self):
        """Test MakeCallRequest.if_machine"""
        self.model.if_machine = "TEST_STRING"
        assert self.model.if_machine == "TEST_STRING"

    def test_if_machine_url(self):
        """Test MakeCallRequest.if_machine_url"""
        self.model.if_machine_url = "TEST_STRING"
        assert self.model.if_machine_url == "TEST_STRING"

    def test_timeout(self):
        """Test MakeCallRequest.timeout"""
        self.model.timeout = 1
        assert self.model.timeout == 1

    def test_parent_call_id(self):
        """Test MakeCallRequest.parent_call_id"""
        self.model.parent_call_id = "TEST_STRING"
        assert self.model.parent_call_id == "TEST_STRING"

    def test_privacy_mode(self):
        """Test MakeCallRequest.privacy_mode"""
        self.model.privacy_mode = False
        assert self.model.privacy_mode == False

    def test_call_connect_url(self):
        """Test MakeCallRequest.call_connect_url"""
        self.model.call_connect_url = "TEST_STRING"
        assert self.model.call_connect_url == "TEST_STRING"


if __name__ == "__main__":
    unittest.main()
