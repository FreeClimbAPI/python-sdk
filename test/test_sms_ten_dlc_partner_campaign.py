"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from datetime import datetime, date
import pytest

import freeclimb
from freeclimb.model.sms_ten_dlc_partner_campaign_brand import SMSTenDLCPartnerCampaignBrand
globals()['SMSTenDLCPartnerCampaignBrand'] = SMSTenDLCPartnerCampaignBrand

from freeclimb.model.sms_ten_dlc_partner_campaign import SMSTenDLCPartnerCampaign  # noqa: E501


class TestSMSTenDLCPartnerCampaign(unittest.TestCase):
    """SMSTenDLCPartnerCampaign unit test stubs"""

    def setUp(self):
        self.model = SMSTenDLCPartnerCampaign(campaign_id="TEST_STRING",
                                              brand_id="TEST_STR",
                                              usecase="TEST_STRING",
                                              description="TEST_STRING")

    def test_account_id(self):
        """Test SMSTenDLCPartnerCampaign.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.get("account_id") == "TEST_STRING"

    def test_campaign_id(self):
        """Test SMSTenDLCPartnerCampaign.campaign_id"""
        self.model.campaign_id = "TEST_STRING"
        assert self.model.get("campaign_id") == "TEST_STRING"

    def test_status(self):
        """Test SMSTenDLCPartnerCampaign.status"""

        self.model.status = "ACTIVE"
        assert self.model.get("status") == "ACTIVE"

        self.model.status = "EXPIRED"
        assert self.model.get("status") == "EXPIRED"

    def test_status_throws_on_invalid_enum(self):
        with pytest.raises(Exception) as info:
            self.model.status = "INVALID_ENUM"
        exception_raised = info.value
        assert exception_raised.__class__.__name__ == freeclimb.ApiValueError.__name__

    def test_create_date(self):
        """Test SMSTenDLCPartnerCampaign.create_date"""
        self.model.create_date = datetime.fromtimestamp(1691592436)
        assert self.model.get(
            "create_date") == datetime.fromtimestamp(1691592436)

    def test_brand_id(self):
        """Test SMSTenDLCPartnerCampaign.brand_id"""
        self.model.brand_id = "TEST_STR"
        assert self.model.get("brand_id") == "TEST_STR"

    def test_usecase(self):
        """Test SMSTenDLCPartnerCampaign.usecase"""
        self.model.usecase = "TEST_STRING"
        assert self.model.get("usecase") == "TEST_STRING"

    def test_description(self):
        """Test SMSTenDLCPartnerCampaign.description"""
        self.model.description = "TEST_STRING"
        assert self.model.get("description") == "TEST_STRING"

    def test_embedded_link(self):
        """Test SMSTenDLCPartnerCampaign.embedded_link"""
        self.model.embedded_link = False
        assert self.model.get("embedded_link") == False

    def test_embedded_phone(self):
        """Test SMSTenDLCPartnerCampaign.embedded_phone"""
        self.model.embedded_phone = False
        assert self.model.get("embedded_phone") == False

    def test_affiliate_marketing(self):
        """Test SMSTenDLCPartnerCampaign.affiliate_marketing"""
        self.model.affiliate_marketing = False
        assert self.model.get("affiliate_marketing") == False

    def test_number_pool(self):
        """Test SMSTenDLCPartnerCampaign.number_pool"""
        self.model.number_pool = False
        assert self.model.get("number_pool") == False

    def test_age_gated(self):
        """Test SMSTenDLCPartnerCampaign.age_gated"""
        self.model.age_gated = False
        assert self.model.get("age_gated") == False

    def test_direct_lending(self):
        """Test SMSTenDLCPartnerCampaign.direct_lending"""
        self.model.direct_lending = False
        assert self.model.get("direct_lending") == False

    def test_subscriber_optin(self):
        """Test SMSTenDLCPartnerCampaign.subscriber_optin"""
        self.model.subscriber_optin = False
        assert self.model.get("subscriber_optin") == False

    def test_subscriber_optout(self):
        """Test SMSTenDLCPartnerCampaign.subscriber_optout"""
        self.model.subscriber_optout = False
        assert self.model.get("subscriber_optout") == False

    def test_subscriber_help(self):
        """Test SMSTenDLCPartnerCampaign.subscriber_help"""
        self.model.subscriber_help = False
        assert self.model.get("subscriber_help") == False

    def test_sample1(self):
        """Test SMSTenDLCPartnerCampaign.sample1"""
        self.model.sample1 = "TEST_STRING"
        assert self.model.get("sample1") == "TEST_STRING"

    def test_sample2(self):
        """Test SMSTenDLCPartnerCampaign.sample2"""
        self.model.sample2 = "TEST_STRING"
        assert self.model.get("sample2") == "TEST_STRING"

    def test_sample3(self):
        """Test SMSTenDLCPartnerCampaign.sample3"""
        self.model.sample3 = "TEST_STRING"
        assert self.model.get("sample3") == "TEST_STRING"

    def test_sample4(self):
        """Test SMSTenDLCPartnerCampaign.sample4"""
        self.model.sample4 = "TEST_STRING"
        assert self.model.get("sample4") == "TEST_STRING"

    def test_sample5(self):
        """Test SMSTenDLCPartnerCampaign.sample5"""
        self.model.sample5 = "TEST_STRING"
        assert self.model.get("sample5") == "TEST_STRING"

    def test_message_flow(self):
        """Test SMSTenDLCPartnerCampaign.message_flow"""
        self.model.message_flow = "TEST_STRING"
        assert self.model.get("message_flow") == "TEST_STRING"

    def test_help_message(self):
        """Test SMSTenDLCPartnerCampaign.help_message"""
        self.model.help_message = "TEST_STRING"
        assert self.model.get("help_message") == "TEST_STRING"

    def test_optin_keywords(self):
        """Test SMSTenDLCPartnerCampaign.optin_keywords"""
        self.model.optin_keywords = "TEST_STRING"
        assert self.model.get("optin_keywords") == "TEST_STRING"

    def test_optout_keywords(self):
        """Test SMSTenDLCPartnerCampaign.optout_keywords"""
        self.model.optout_keywords = "TEST_STRING"
        assert self.model.get("optout_keywords") == "TEST_STRING"

    def test_help_keywords(self):
        """Test SMSTenDLCPartnerCampaign.help_keywords"""
        self.model.help_keywords = "TEST_STRING"
        assert self.model.get("help_keywords") == "TEST_STRING"

    def test_optin_message(self):
        """Test SMSTenDLCPartnerCampaign.optin_message"""
        self.model.optin_message = "TEST_STRING"
        assert self.model.get("optin_message") == "TEST_STRING"

    def test_optout_message(self):
        """Test SMSTenDLCPartnerCampaign.optout_message"""
        self.model.optout_message = "TEST_STRING"
        assert self.model.get("optout_message") == "TEST_STRING"

    def test_brand(self):
        """Test SMSTenDLCPartnerCampaign.brand"""
        object = SMSTenDLCPartnerCampaignBrand(
            phone="TEST_STRING", email="TEST_STRING")
        self.model.brand = object
        assert self.model.get("brand", object)


if __name__ == '__main__':
    unittest.main()
