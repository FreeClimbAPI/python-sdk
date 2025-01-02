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
from freeclimb.models.message_request import MessageRequest


class TestMessageRequest(unittest.TestCase):
    """MessageRequest unit test stubs"""

    def setUp(self):
        self.model = MessageRequest(
            var_from="",
            to="",
            text="",
        )

    def test_uri(self):
        """Test MessageRequest.uri"""
        self.model.uri = "TEST_STRING"
        assert self.model.uri == "TEST_STRING"

    def test_date_created(self):
        """Test MessageRequest.date_created"""
        self.model.date_created = "TEST_STRING"
        assert self.model.date_created == "TEST_STRING"

    def test_date_updated(self):
        """Test MessageRequest.date_updated"""
        self.model.date_updated = "TEST_STRING"
        assert self.model.date_updated == "TEST_STRING"

    def test_revision(self):
        """Test MessageRequest.revision"""
        self.model.revision = 1
        assert self.model.revision == 1

    def test_var_from(self):
        """Test MessageRequest.var_from"""
        self.model.var_from = "TEST_STRING"
        assert self.model.var_from == "TEST_STRING"

    def test_to(self):
        """Test MessageRequest.to"""
        self.model.to = "TEST_STRING"
        assert self.model.to == "TEST_STRING"

    def test_text(self):
        """Test MessageRequest.text"""
        self.model.text = "TEST_STRING"
        assert self.model.text == "TEST_STRING"

    def test_notification_url(self):
        """Test MessageRequest.notification_url"""
        self.model.notification_url = "TEST_STRING"
        assert self.model.notification_url == "TEST_STRING"

    def test_media_urls(self):
        """Test MessageRequest.media_urls"""
        testList = []
        self.model.media_urls = testList
        assert self.model.media_urls == testList


if __name__ == "__main__":
    unittest.main()
