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
from freeclimb.models.incoming_number_result import IncomingNumberResult


class TestIncomingNumberResult(unittest.TestCase):
    """IncomingNumberResult unit test stubs"""

    def setUp(self):
        self.model = IncomingNumberResult()

    def test_uri(self):
        """Test IncomingNumberResult.uri"""

        self.model.uri = "TEST_STRING"
        assert self.model.uri == "TEST_STRING"

    def test_date_created(self):
        """Test IncomingNumberResult.date_created"""

        self.model.date_created = "TEST_STRING"
        assert self.model.date_created == "TEST_STRING"

    def test_date_updated(self):
        """Test IncomingNumberResult.date_updated"""

        self.model.date_updated = "TEST_STRING"
        assert self.model.date_updated == "TEST_STRING"

    def test_revision(self):
        """Test IncomingNumberResult.revision"""
        self.model.revision = 1
        assert self.model.revision == 1

    def test_capabilities(self):
        """Test IncomingNumberResult.capabilities"""
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
        """Test IncomingNumberResult.campaign_id"""

        self.model.campaign_id = "TEST_STRING"
        assert self.model.campaign_id == "TEST_STRING"

    def test_phone_number_id(self):
        """Test IncomingNumberResult.phone_number_id"""

        self.model.phone_number_id = "TEST_STRING"
        assert self.model.phone_number_id == "TEST_STRING"

    def test_account_id(self):
        """Test IncomingNumberResult.account_id"""

        self.model.account_id = "TEST_STRING"
        assert self.model.account_id == "TEST_STRING"

    def test_application_id(self):
        """Test IncomingNumberResult.application_id"""

        self.model.application_id = "TEST_STRING"
        assert self.model.application_id == "TEST_STRING"

    def test_phone_number(self):
        """Test IncomingNumberResult.phone_number"""

        self.model.phone_number = "TEST_STRING"
        assert self.model.phone_number == "TEST_STRING"

    def test_alias(self):
        """Test IncomingNumberResult.alias"""

        self.model.alias = "TEST_STRING"
        assert self.model.alias == "TEST_STRING"

    def test_region(self):
        """Test IncomingNumberResult.region"""

        self.model.region = "TEST_STRING"
        assert self.model.region == "TEST_STRING"

    def test_country(self):
        """Test IncomingNumberResult.country"""

        self.model.country = "TEST_STRING"
        assert self.model.country == "TEST_STRING"

    def test_voice_enabled(self):
        """Test IncomingNumberResult.voice_enabled"""
        self.model.voice_enabled = False
        assert self.model.voice_enabled == False

    def test_sms_enabled(self):
        """Test IncomingNumberResult.sms_enabled"""
        self.model.sms_enabled = False
        assert self.model.sms_enabled == False

    def test_offnet(self):
        """Test IncomingNumberResult.offnet"""
        self.model.offnet = False
        assert self.model.offnet == False

    def test_tfn(self):
        """Test IncomingNumberResult.tfn"""
        object = freeclimb.models.tfn.TFN(
            campaign_id="",
        )
        self.model.tfn = object
        assert self.model.tfn == object


if __name__ == "__main__":
    unittest.main()
