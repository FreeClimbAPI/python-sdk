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
from freeclimb.models.sms_ten_dlc_partner_campaign_brand import (
    SMSTenDLCPartnerCampaignBrand,
)


class TestSMSTenDLCPartnerCampaignBrand(unittest.TestCase):
    """SMSTenDLCPartnerCampaignBrand unit test stubs"""

    def setUp(self):
        self.model = SMSTenDLCPartnerCampaignBrand(
            phone="TS",
            email="TS",
        )

    def test_account_id(self):
        """Test SMSTenDLCPartnerCampaignBrand.account_id"""

        self.model.account_id = "TEST_STRING"
        assert self.model.account_id == "TEST_STRING"

    def test_brand_id(self):
        """Test SMSTenDLCPartnerCampaignBrand.brand_id"""

        self.model.brand_id = "TEST_STRING"
        assert self.model.brand_id == "TEST_STRING"

    def test_first_name(self):
        """Test SMSTenDLCPartnerCampaignBrand.first_name"""
        self.model.first_name = "T" * 100
        assert self.model.first_name == "T" * 100

        with self.assertRaises(pydantic_core._pydantic_core.ValidationError) as info:
            self.model.first_name = "T" * (100 + 1)

    def test_last_name(self):
        """Test SMSTenDLCPartnerCampaignBrand.last_name"""
        self.model.last_name = "T" * 100
        assert self.model.last_name == "T" * 100

        with self.assertRaises(pydantic_core._pydantic_core.ValidationError) as info:
            self.model.last_name = "T" * (100 + 1)

    def test_display_name(self):
        """Test SMSTenDLCPartnerCampaignBrand.display_name"""
        self.model.display_name = "T" * 255
        assert self.model.display_name == "T" * 255

        with self.assertRaises(pydantic_core._pydantic_core.ValidationError) as info:
            self.model.display_name = "T" * (255 + 1)

    def test_company_name(self):
        """Test SMSTenDLCPartnerCampaignBrand.company_name"""
        self.model.company_name = "T" * 255
        assert self.model.company_name == "T" * 255

        with self.assertRaises(pydantic_core._pydantic_core.ValidationError) as info:
            self.model.company_name = "T" * (255 + 1)

    def test_phone(self):
        """Test SMSTenDLCPartnerCampaignBrand.phone"""
        self.model.phone = "T" * 20
        assert self.model.phone == "T" * 20

        with self.assertRaises(pydantic_core._pydantic_core.ValidationError) as info:
            self.model.phone = "T" * (20 + 1)

    def test_email(self):
        """Test SMSTenDLCPartnerCampaignBrand.email"""
        self.model.email = "T" * 100
        assert self.model.email == "T" * 100

        with self.assertRaises(pydantic_core._pydantic_core.ValidationError) as info:
            self.model.email = "T" * (100 + 1)

    def test_website(self):
        """Test SMSTenDLCPartnerCampaignBrand.website"""
        self.model.website = "T" * 100
        assert self.model.website == "T" * 100

        with self.assertRaises(pydantic_core._pydantic_core.ValidationError) as info:
            self.model.website = "T" * (100 + 1)

    def test_optional_attributes(self):
        """Test SMSTenDLCPartnerCampaignBrand.optional_attributes"""
        object = {}
        self.model.optional_attributes = object
        assert self.model.optional_attributes == object

    def test_evp_vetting_score(self):
        """Test SMSTenDLCPartnerCampaignBrand.evp_vetting_score"""
        self.model.evp_vetting_score = 1
        assert self.model.evp_vetting_score == 1


if __name__ == "__main__":
    unittest.main()
