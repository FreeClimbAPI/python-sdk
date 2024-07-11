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

from freeclimb.model.message_request_all_of import MessageRequestAllOf  # noqa: E501

class TestMessageRequestAllOf(unittest.TestCase):
    """MessageRequestAllOf unit test stubs"""

    def setUp(self):
        self.model = MessageRequestAllOf(
            _from="",
            to="",
            text="",
        )
    
    def test__from(self):
        """Test MessageRequestAllOf._from"""
        self.model._from = "TEST_STRING"
        assert self.model.get("_from") == "TEST_STRING"

    def test_to(self):
        """Test MessageRequestAllOf.to"""
        self.model.to = "TEST_STRING"
        assert self.model.get("to") == "TEST_STRING"

    def test_text(self):
        """Test MessageRequestAllOf.text"""
        self.model.text = "TEST_STRING"
        assert self.model.get("text") == "TEST_STRING"

    def test_notification_url(self):
        """Test MessageRequestAllOf.notification_url"""
        self.model.notification_url = "TEST_STRING"
        assert self.model.get("notification_url") == "TEST_STRING"

    def test_media_urls(self):
        """Test MessageRequestAllOf.media_urls"""
        testArray = []
        self.model.media_urls = testArray
        assert self.model.get("media_urls") == testArray


if __name__ == '__main__':
    unittest.main()