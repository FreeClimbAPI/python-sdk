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
from freeclimb.models.conference_list import ConferenceList


class TestConferenceList(unittest.TestCase):
    """ConferenceList unit test stubs"""

    def setUp(self):
        self.model = ConferenceList()

    def test_total(self):
        """Test ConferenceList.total"""
        self.model.total = 1
        assert self.model.total == 1

    def test_start(self):
        """Test ConferenceList.start"""
        self.model.start = 1
        assert self.model.start == 1

    def test_end(self):
        """Test ConferenceList.end"""
        self.model.end = 1
        assert self.model.end == 1

    def test_page(self):
        """Test ConferenceList.page"""
        self.model.page = 1
        assert self.model.page == 1

    def test_num_pages(self):
        """Test ConferenceList.num_pages"""
        self.model.num_pages = 1
        assert self.model.num_pages == 1

    def test_page_size(self):
        """Test ConferenceList.page_size"""
        self.model.page_size = 1
        assert self.model.page_size == 1

    def test_next_page_uri(self):
        """Test ConferenceList.next_page_uri"""

        self.model.next_page_uri = "TEST_STRING"
        assert self.model.next_page_uri == "TEST_STRING"

    def test_conferences(self):
        """Test ConferenceList.conferences"""
        testList = []
        self.model.conferences = testList
        assert self.model.conferences == testList


if __name__ == "__main__":
    unittest.main()
