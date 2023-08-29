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
from freeclimb.model.sms_ten_dlc_campaign import SMSTenDLCCampaign
globals()['SMSTenDLCCampaign'] = SMSTenDLCCampaign

from freeclimb.model.sms_ten_dlc_campaigns_list_result_all_of import SMSTenDLCCampaignsListResultAllOf  # noqa: E501

class TestSMSTenDLCCampaignsListResultAllOf(unittest.TestCase):
    """SMSTenDLCCampaignsListResultAllOf unit test stubs"""

    def setUp(self):
        self.model = SMSTenDLCCampaignsListResultAllOf(
        )
    
    def test_campaigns(self):
        """Test SMSTenDLCCampaignsListResultAllOf.campaigns"""
        testList = []
        self.model.campaigns = testList
        assert self.model.get("campaigns") == testList

if __name__ == '__main__':
    unittest.main()
