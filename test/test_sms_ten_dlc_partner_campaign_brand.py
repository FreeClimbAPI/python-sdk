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

from freeclimb.model.sms_ten_dlc_partner_campaign_brand import SMSTenDLCPartnerCampaignBrand  # noqa: E501

class TestSMSTenDLCPartnerCampaignBrand(unittest.TestCase):
    """SMSTenDLCPartnerCampaignBrand unit test stubs"""

    def setUp(self):
        self.model = SMSTenDLCPartnerCampaignBrand(
            phone="",
            email="",
        )
    
    def test_account_id(self):
        """Test SMSTenDLCPartnerCampaignBrand.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.get("account_id") == "TEST_STRING"

    def test_brand_id(self):
        """Test SMSTenDLCPartnerCampaignBrand.brand_id"""
        self.model.brand_id = "TEST_STRING"
        assert self.model.get("brand_id") == "TEST_STRING"

    def test_first_name(self):
        """Test SMSTenDLCPartnerCampaignBrand.first_name"""
        self.model.first_name = "T" * 100
        assert self.model.get("first_name") == "T" * 100
        
        with pytest.raises(Exception) as info:
            self.model.first_name = "T" * (100 + 1)
        exception_raised = info.value
        assert exception_raised.__class__.__name__ == freeclimb.ApiValueError.__name__

    def test_last_name(self):
        """Test SMSTenDLCPartnerCampaignBrand.last_name"""
        self.model.last_name = "T" * 100
        assert self.model.get("last_name") == "T" * 100
        
        with pytest.raises(Exception) as info:
            self.model.last_name = "T" * (100 + 1)
        exception_raised = info.value
        assert exception_raised.__class__.__name__ == freeclimb.ApiValueError.__name__

    def test_display_name(self):
        """Test SMSTenDLCPartnerCampaignBrand.display_name"""
        self.model.display_name = "T" * 255
        assert self.model.get("display_name") == "T" * 255
        
        with pytest.raises(Exception) as info:
            self.model.display_name = "T" * (255 + 1)
        exception_raised = info.value
        assert exception_raised.__class__.__name__ == freeclimb.ApiValueError.__name__

    def test_company_name(self):
        """Test SMSTenDLCPartnerCampaignBrand.company_name"""
        self.model.company_name = "T" * 255
        assert self.model.get("company_name") == "T" * 255
        
        with pytest.raises(Exception) as info:
            self.model.company_name = "T" * (255 + 1)
        exception_raised = info.value
        assert exception_raised.__class__.__name__ == freeclimb.ApiValueError.__name__

    def test_phone(self):
        """Test SMSTenDLCPartnerCampaignBrand.phone"""
        self.model.phone = "T" * 20
        assert self.model.get("phone") == "T" * 20
        
        with pytest.raises(Exception) as info:
            self.model.phone = "T" * (20 + 1)
        exception_raised = info.value
        assert exception_raised.__class__.__name__ == freeclimb.ApiValueError.__name__

    def test_email(self):
        """Test SMSTenDLCPartnerCampaignBrand.email"""
        self.model.email = "T" * 100
        assert self.model.get("email") == "T" * 100
        
        with pytest.raises(Exception) as info:
            self.model.email = "T" * (100 + 1)
        exception_raised = info.value
        assert exception_raised.__class__.__name__ == freeclimb.ApiValueError.__name__

    def test_website(self):
        """Test SMSTenDLCPartnerCampaignBrand.website"""
        self.model.website = "T" * 100
        assert self.model.get("website") == "T" * 100
        
        with pytest.raises(Exception) as info:
            self.model.website = "T" * (100 + 1)
        exception_raised = info.value
        assert exception_raised.__class__.__name__ == freeclimb.ApiValueError.__name__

    def test_optional_attributes(self):
        """Test SMSTenDLCPartnerCampaignBrand.optional_attributes"""
        self.model.optional_attributes = {}
        assert self.model.get("optional_attributes") == {}

    def test_evp_vetting_score(self):
        """Test SMSTenDLCPartnerCampaignBrand.evp_vetting_score"""
        self.model.evp_vetting_score = 1
        assert self.model.get("evp_vetting_score") == 1


if __name__ == '__main__':
    unittest.main()