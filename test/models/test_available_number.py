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
from freeclimb.models.available_number import AvailableNumber


class TestAvailableNumber(unittest.TestCase):
    """AvailableNumber unit test stubs"""

    def setUp(self):
        self.model = AvailableNumber()

    def test_capabilities(self):
        """Test AvailableNumber.capabilities"""
        object = freeclimb.models.capabilities.Capabilities(
            voice=True,
            sms=True,
            toll_free=True,
            ten_dlc=True,
            short_code=True,
        )
        self.model.capabilities = object
        assert self.model.capabilities == object

    def test_campaign_id(self):
        """Test AvailableNumber.campaign_id"""

        self.model.campaign_id = "TEST_STRING"
        assert self.model.campaign_id == "TEST_STRING"

    def test_phone_number(self):
        """Test AvailableNumber.phone_number"""

        self.model.phone_number = "TEST_STRING"
        assert self.model.phone_number == "TEST_STRING"

    def test_voice_enabled(self):
        """Test AvailableNumber.voice_enabled"""
        self.model.voice_enabled = False
        assert self.model.voice_enabled == False

    def test_sms_enabled(self):
        """Test AvailableNumber.sms_enabled"""
        self.model.sms_enabled = False
        assert self.model.sms_enabled == False

    def test_region(self):
        """Test AvailableNumber.region"""

        self.model.region = "TEST_STRING"
        assert self.model.region == "TEST_STRING"

    def test_country(self):
        """Test AvailableNumber.country"""

        self.model.country = "TEST_STRING"
        assert self.model.country == "TEST_STRING"


if __name__ == "__main__":
    unittest.main()
