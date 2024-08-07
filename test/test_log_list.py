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
from freeclimb.model.log_list_all_of import LogListAllOf
from freeclimb.model.log_result import LogResult
from freeclimb.model.pagination_model import PaginationModel
globals()['LogListAllOf'] = LogListAllOf
globals()['LogResult'] = LogResult
globals()['PaginationModel'] = PaginationModel

from freeclimb.model.log_list import LogList  # noqa: E501

class TestLogList(unittest.TestCase):
    """LogList unit test stubs"""

    def setUp(self):
        self.model = LogList(
        )
    
    def test_total(self):
        """Test LogList.total"""
        self.model.total = 1
        assert self.model.get("total") == 1

    def test_start(self):
        """Test LogList.start"""
        self.model.start = 1
        assert self.model.get("start") == 1

    def test_end(self):
        """Test LogList.end"""
        self.model.end = 1
        assert self.model.get("end") == 1

    def test_page(self):
        """Test LogList.page"""
        self.model.page = 1
        assert self.model.get("page") == 1

    def test_num_pages(self):
        """Test LogList.num_pages"""
        self.model.num_pages = 1
        assert self.model.get("num_pages") == 1

    def test_page_size(self):
        """Test LogList.page_size"""
        self.model.page_size = 1
        assert self.model.get("page_size") == 1

    def test_next_page_uri(self):
        """Test LogList.next_page_uri"""
        self.model.next_page_uri = "TEST_STRING"
        assert self.model.get("next_page_uri") == "TEST_STRING"

    def test_logs(self):
        """Test LogList.logs"""
        testList = []
        self.model.logs = testList
        assert self.model.get("logs") == testList


if __name__ == '__main__':
    unittest.main()