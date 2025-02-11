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
from freeclimb.models.get_digits import GetDigits


class TestGetDigits(unittest.TestCase):
    """GetDigits unit test stubs"""

    def setUp(self):
        self.model = GetDigits(
            action_url="TS",
        )

    def test_action_url(self):
        """Test GetDigits.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.action_url == "TEST_STRING"

    def test_digit_timeout_ms(self):
        """Test GetDigits.digit_timeout_ms"""
        self.model.digit_timeout_ms = 1
        assert self.model.digit_timeout_ms == 1

    def test_finish_on_key(self):
        """Test GetDigits.finish_on_key"""

        self.model.finish_on_key = "TEST_STRING"
        assert self.model.finish_on_key == "TEST_STRING"

    def test_flush_buffer(self):
        """Test GetDigits.flush_buffer"""
        self.model.flush_buffer = False
        assert self.model.flush_buffer == False

    def test_initial_timeout_ms(self):
        """Test GetDigits.initial_timeout_ms"""
        self.model.initial_timeout_ms = 1
        assert self.model.initial_timeout_ms == 1

    def test_max_digits(self):
        """Test GetDigits.max_digits"""
        self.model.max_digits = 1
        assert self.model.max_digits == 1

    def test_min_digits(self):
        """Test GetDigits.min_digits"""
        self.model.min_digits = 1
        assert self.model.min_digits == 1

    def test_prompts(self):
        """Test GetDigits.prompts"""
        testList = []
        self.model.prompts = testList
        assert self.model.prompts == testList

    def test_privacy_mode(self):
        """Test GetDigits.privacy_mode"""
        self.model.privacy_mode = False
        assert self.model.privacy_mode == False


if __name__ == "__main__":
    unittest.main()
