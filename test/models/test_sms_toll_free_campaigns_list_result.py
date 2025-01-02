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
from freeclimb.models.sms_toll_free_campaigns_list_result import (
    SMSTollFreeCampaignsListResult,
)


class TestSMSTollFreeCampaignsListResult(unittest.TestCase):
    """SMSTollFreeCampaignsListResult unit test stubs"""

    def setUp(self):
        self.model = SMSTollFreeCampaignsListResult()

    def test_total(self):
        """Test SMSTollFreeCampaignsListResult.total"""
        self.model.total = 1
        assert self.model.total == 1

    def test_start(self):
        """Test SMSTollFreeCampaignsListResult.start"""
        self.model.start = 1
        assert self.model.start == 1

    def test_end(self):
        """Test SMSTollFreeCampaignsListResult.end"""
        self.model.end = 1
        assert self.model.end == 1

    def test_page(self):
        """Test SMSTollFreeCampaignsListResult.page"""
        self.model.page = 1
        assert self.model.page == 1

    def test_num_pages(self):
        """Test SMSTollFreeCampaignsListResult.num_pages"""
        self.model.num_pages = 1
        assert self.model.num_pages == 1

    def test_page_size(self):
        """Test SMSTollFreeCampaignsListResult.page_size"""
        self.model.page_size = 1
        assert self.model.page_size == 1

    def test_next_page_uri(self):
        """Test SMSTollFreeCampaignsListResult.next_page_uri"""
        self.model.next_page_uri = "TEST_STRING"
        assert self.model.next_page_uri == "TEST_STRING"

    def test_brands(self):
        """Test SMSTollFreeCampaignsListResult.brands"""
        testList = []
        self.model.brands = testList
        assert self.model.brands == testList


if __name__ == "__main__":
    unittest.main()
