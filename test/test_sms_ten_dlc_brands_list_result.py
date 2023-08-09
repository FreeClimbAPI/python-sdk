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

import freeclimb
from freeclimb.model.pagination_model import PaginationModel
from freeclimb.model.sms_ten_dlc_brand import SMSTenDLCBrand
from freeclimb.model.sms_ten_dlc_brands_list_result_all_of import SMSTenDLCBrandsListResultAllOf
globals()['PaginationModel'] = PaginationModel
globals()['SMSTenDLCBrand'] = SMSTenDLCBrand
globals()['SMSTenDLCBrandsListResultAllOf'] = SMSTenDLCBrandsListResultAllOf

from freeclimb.model.sms_ten_dlc_brands_list_result import SMSTenDLCBrandsListResult  # noqa: E501


class TestSMSTenDLCBrandsListResult(unittest.TestCase):
    """SMSTenDLCBrandsListResult unit test stubs"""

    def setUp(self):
        self.model = SMSTenDLCBrandsListResult()

    def test_total(self):
        """Test SMSTenDLCBrandsListResult.total"""

        self.model.total = 1
        assert self.model.get("total") == 1

    def test_start(self):
        """Test SMSTenDLCBrandsListResult.start"""

        self.model.start = 1
        assert self.model.get("start") == 1

    def test_end(self):
        """Test SMSTenDLCBrandsListResult.end"""

        self.model.end = 1
        assert self.model.get("end") == 1

    def test_page(self):
        """Test SMSTenDLCBrandsListResult.page"""

        self.model.page = 1
        assert self.model.get("page") == 1

    def test_num_pages(self):
        """Test SMSTenDLCBrandsListResult.num_pages"""

        self.model.num_pages = 1
        assert self.model.get("num_pages") == 1

    def test_page_size(self):
        """Test SMSTenDLCBrandsListResult.page_size"""

        self.model.page_size = 1
        assert self.model.get("page_size") == 1

    def test_next_page_uri(self):
        """Test SMSTenDLCBrandsListResult.next_page_uri"""
        self.model.next_page_uri = "TEST_STRING"
        assert self.model.get("next_page_uri") == "TEST_STRING"

    def test_brands(self):
        """Test SMSTenDLCBrandsListResult.brands"""

        testList = []
        self.model.brands = testList
        assert self.model.get("brands") == testList


if __name__ == '__main__':
    unittest.main()
