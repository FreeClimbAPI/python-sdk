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

from freeclimb.model.application_request import ApplicationRequest  # noqa: E501


class TestApplicationRequest(unittest.TestCase):
    """ApplicationRequest unit test stubs"""

    def setUp(self):
        self.model = ApplicationRequest()

    def test_alias(self):
        """Test ApplicationRequest.alias"""
        self.model.alias = "TEST_STRING"
        assert self.model.get("alias") == "TEST_STRING"

    def test_voice_url(self):
        """Test ApplicationRequest.voice_url"""
        self.model.voice_url = "TEST_STRING"
        assert self.model.get("voice_url") == "TEST_STRING"

    def test_voice_fallback_url(self):
        """Test ApplicationRequest.voice_fallback_url"""
        self.model.voice_fallback_url = "TEST_STRING"
        assert self.model.get("voice_fallback_url") == "TEST_STRING"

    def test_call_connect_url(self):
        """Test ApplicationRequest.call_connect_url"""
        self.model.call_connect_url = "TEST_STRING"
        assert self.model.get("call_connect_url") == "TEST_STRING"

    def test_status_callback_url(self):
        """Test ApplicationRequest.status_callback_url"""
        self.model.status_callback_url = "TEST_STRING"
        assert self.model.get("status_callback_url") == "TEST_STRING"

    def test_sms_url(self):
        """Test ApplicationRequest.sms_url"""
        self.model.sms_url = "TEST_STRING"
        assert self.model.get("sms_url") == "TEST_STRING"

    def test_sms_fallback_url(self):
        """Test ApplicationRequest.sms_fallback_url"""
        self.model.sms_fallback_url = "TEST_STRING"
        assert self.model.get("sms_fallback_url") == "TEST_STRING"


if __name__ == '__main__':
    unittest.main()
