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
from freeclimb.models.application_result import ApplicationResult


class TestApplicationResult(unittest.TestCase):
    """ApplicationResult unit test stubs"""

    def setUp(self):
        self.model = ApplicationResult()

    def test_uri(self):
        """Test ApplicationResult.uri"""
        self.model.uri = "TEST_STRING"
        assert self.model.uri == "TEST_STRING"

    def test_date_created(self):
        """Test ApplicationResult.date_created"""
        self.model.date_created = "TEST_STRING"
        assert self.model.date_created == "TEST_STRING"

    def test_date_updated(self):
        """Test ApplicationResult.date_updated"""
        self.model.date_updated = "TEST_STRING"
        assert self.model.date_updated == "TEST_STRING"

    def test_revision(self):
        """Test ApplicationResult.revision"""
        self.model.revision = 1
        assert self.model.revision == 1

    def test_account_id(self):
        """Test ApplicationResult.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.account_id == "TEST_STRING"

    def test_application_id(self):
        """Test ApplicationResult.application_id"""
        self.model.application_id = "TEST_STRING"
        assert self.model.application_id == "TEST_STRING"

    def test_alias(self):
        """Test ApplicationResult.alias"""
        self.model.alias = "TEST_STRING"
        assert self.model.alias == "TEST_STRING"

    def test_voice_url(self):
        """Test ApplicationResult.voice_url"""
        self.model.voice_url = "TEST_STRING"
        assert self.model.voice_url == "TEST_STRING"

    def test_voice_fallback_url(self):
        """Test ApplicationResult.voice_fallback_url"""
        self.model.voice_fallback_url = "TEST_STRING"
        assert self.model.voice_fallback_url == "TEST_STRING"

    def test_call_connect_url(self):
        """Test ApplicationResult.call_connect_url"""
        self.model.call_connect_url = "TEST_STRING"
        assert self.model.call_connect_url == "TEST_STRING"

    def test_status_callback_url(self):
        """Test ApplicationResult.status_callback_url"""
        self.model.status_callback_url = "TEST_STRING"
        assert self.model.status_callback_url == "TEST_STRING"

    def test_sms_url(self):
        """Test ApplicationResult.sms_url"""
        self.model.sms_url = "TEST_STRING"
        assert self.model.sms_url == "TEST_STRING"

    def test_sms_fallback_url(self):
        """Test ApplicationResult.sms_fallback_url"""
        self.model.sms_fallback_url = "TEST_STRING"
        assert self.model.sms_fallback_url == "TEST_STRING"


if __name__ == "__main__":
    unittest.main()
