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

from freeclimb.model.queue_result_all_of import QueueResultAllOf  # noqa: E501


class TestQueueResultAllOf(unittest.TestCase):
    """QueueResultAllOf unit test stubs"""

    def setUp(self):
        self.model = QueueResultAllOf()

    def test_account_id(self):
        """Test QueueResultAllOf.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.get("account_id") == "TEST_STRING"

    def test_queue_id(self):
        """Test QueueResultAllOf.queue_id"""
        self.model.queue_id = "TEST_STRING"
        assert self.model.get("queue_id") == "TEST_STRING"

    def test_alias(self):
        """Test QueueResultAllOf.alias"""
        self.model.alias = "TEST_STRING"
        assert self.model.get("alias") == "TEST_STRING"

    def test_max_size(self):
        """Test QueueResultAllOf.max_size"""
        self.model.max_size = 1
        assert self.model.get("max_size") == 1

    def test_current_size(self):
        """Test QueueResultAllOf.current_size"""
        self.model.current_size = 1
        assert self.model.get("current_size") == 1

    def test_average_queue_removal_time(self):
        """Test QueueResultAllOf.average_queue_removal_time"""
        self.model.average_queue_removal_time = 1
        assert self.model.get("average_queue_removal_time") == 1

    def test_subresource_uris(self):
        """Test QueueResultAllOf.subresource_uris"""
        testObject = {}
        self.model.subresource_uris = testObject
        assert self.model.get("subresource_uris") == testObject


if __name__ == "__main__":
    unittest.main()
