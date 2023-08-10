"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
import datetime

import freeclimb
from freeclimb.model.if_machine import IfMachine
globals()['IfMachine'] = IfMachine

from freeclimb.model.out_dial_all_of import OutDialAllOf  # noqa: E501


class TestOutDialAllOf(unittest.TestCase):
    """OutDialAllOf unit test stubs"""

    def setUp(self):
        self.model = OutDialAllOf(action_url="TEST_URL", call_connect_url="TEST_URL",
                                  calling_number="+11231231234", destination="+11231231234")

    def test_action_url(self):
        """Test OutDialAllOf.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.get("action_url") == "TEST_STRING"

    def test_call_connect_url(self):
        """Test OutDialAllOf.call_connect_url"""
        self.model.call_connect_url = "TEST_STRING"
        assert self.model.get("call_connect_url") == "TEST_STRING"

    def test_calling_number(self):
        """Test OutDialAllOf.calling_number"""
        self.model.calling_number = "TEST_STRING"
        assert self.model.get("calling_number") == "TEST_STRING"

    def test_destination(self):
        """Test OutDialAllOf.destination"""
        self.model.destination = "TEST_STRING"
        assert self.model.get("destination") == "TEST_STRING"

    def test_if_machine(self):
        """Test OutDialAllOf.if_machine"""
        self.model.if_machine = IfMachine.REDIRECT
        assert self.model.get("if_machine") == IfMachine.REDIRECT
        self.model.if_machine = IfMachine.HANGUP
        assert self.model.get("if_machine") == IfMachine.HANGUP

    def test_if_machine_url(self):
        """Test OutDialAllOf.if_machine_url"""
        self.model.if_machine_url = "TEST_STRING"
        assert self.model.get("if_machine_url") == "TEST_STRING"

    def test_send_digits(self):
        """Test OutDialAllOf.send_digits"""
        self.model.send_digits = "TEST_STRING"
        assert self.model.get("send_digits") == "TEST_STRING"

    def test_status_callback_url(self):
        """Test OutDialAllOf.status_callback_url"""
        self.model.status_callback_url = "TEST_STRING"
        assert self.model.get("status_callback_url") == "TEST_STRING"

    def test_timeout(self):
        """Test OutDialAllOf.timeout"""

        self.model.timeout = 1
        assert self.model.get("timeout") == 1

    def test_privacy_mode(self):
        """Test OutDialAllOf.privacy_mode"""
        self.model.privacy_mode = False
        assert self.model.get("privacy_mode") == False


if __name__ == '__main__':
    unittest.main()
