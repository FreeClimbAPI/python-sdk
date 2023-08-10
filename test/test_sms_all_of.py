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

from freeclimb.model.sms_all_of import SmsAllOf  # noqa: E501


class TestSmsAllOf(unittest.TestCase):
    """SmsAllOf unit test stubs"""

    def setUp(self):
        self.model = SmsAllOf(
            to="+11231231234", _from="+11231231234", text="TEST_STRING")

    def test_to(self):
        """Test SmsAllOf.to"""
        self.model.to = "TEST_STRING"
        assert self.model.get("to") == "TEST_STRING"

    def test__from(self):
        """Test SmsAllOf._from"""
        self.model._from = "TEST_STRING"
        assert self.model.get("_from") == "TEST_STRING"

    def test_text(self):
        """Test SmsAllOf.text"""
        self.model.text = "TEST_STRING"
        assert self.model.get("text") == "TEST_STRING"

    def test_notification_url(self):
        """Test SmsAllOf.notification_url"""
        self.model.notification_url = "TEST_STRING"
        assert self.model.get("notification_url") == "TEST_STRING"


if __name__ == '__main__':
    unittest.main()
