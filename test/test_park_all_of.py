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

from freeclimb.model.park_all_of import ParkAllOf  # noqa: E501


class TestParkAllOf(unittest.TestCase):
    """ParkAllOf unit test stubs"""

    def setUp(self):
        self.model = ParkAllOf(wait_url="TEST_URL", action_url="TEST_URL")

    def test_wait_url(self):
        """Test ParkAllOf.wait_url"""
        self.model.wait_url = "TEST_STRING"
        assert self.model.get("wait_url") == "TEST_STRING"

    def test_action_url(self):
        """Test ParkAllOf.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.get("action_url") == "TEST_STRING"

    def test_notification_url(self):
        """Test ParkAllOf.notification_url"""
        self.model.notification_url = "TEST_STRING"
        assert self.model.get("notification_url") == "TEST_STRING"


if __name__ == '__main__':
    unittest.main()
