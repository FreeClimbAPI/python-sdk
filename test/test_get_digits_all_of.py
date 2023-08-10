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
import decimal

import freeclimb
from freeclimb.model.percl_command import PerclCommand
globals()['PerclCommand'] = PerclCommand

from freeclimb.model.get_digits_all_of import GetDigitsAllOf  # noqa: E501


class TestGetDigitsAllOf(unittest.TestCase):
    """GetDigitsAllOf unit test stubs"""

    def setUp(self):
        self.model = GetDigitsAllOf(action_url="TEST_URL")

    def test_action_url(self):
        """Test GetDigitsAllOf.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.get("action_url") == "TEST_STRING"

    def test_digit_timeout_ms(self):
        """Test GetDigitsAllOf.digit_timeout_ms"""

        self.model.digit_timeout_ms = 1
        assert self.model.get("digit_timeout_ms") == 1

    def test_finish_on_key(self):
        """Test GetDigitsAllOf.finish_on_key"""
        self.model.finish_on_key = "TEST_STRING"
        assert self.model.get("finish_on_key") == "TEST_STRING"

    def test_flush_buffer(self):
        """Test GetDigitsAllOf.flush_buffer"""
        self.model.flush_buffer = False
        assert self.model.get("flush_buffer") == False

    def test_initial_timeout_ms(self):
        """Test GetDigitsAllOf.initial_timeout_ms"""
        self.model.initial_timeout_ms = "TEST_STRING"
        assert self.model.get("initial_timeout_ms") == "TEST_STRING"

    def test_max_digits(self):
        """Test GetDigitsAllOf.max_digits"""

        self.model.max_digits = 1
        assert self.model.get("max_digits") == 1

    def test_min_digits(self):
        """Test GetDigitsAllOf.min_digits"""

        self.model.min_digits = 1
        assert self.model.get("min_digits") == 1

    def test_prompts(self):
        """Test GetDigitsAllOf.prompts"""

        testList = []
        self.model.prompts = testList
        assert self.model.get("prompts") == testList

    def test_privacy_mode(self):
        """Test GetDigitsAllOf.privacy_mode"""
        self.model.privacy_mode = False
        assert self.model.get("privacy_mode") == False


if __name__ == '__main__':
    unittest.main()
