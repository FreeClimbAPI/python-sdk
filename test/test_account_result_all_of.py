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
from freeclimb.model.account_status import AccountStatus
from freeclimb.model.account_type import AccountType
globals()['AccountStatus'] = AccountStatus
globals()['AccountType'] = AccountType

from freeclimb.model.account_result_all_of import AccountResultAllOf  # noqa: E501

class TestAccountResultAllOf(unittest.TestCase):
    """AccountResultAllOf unit test stubs"""

    def setUp(self):
        self.model = AccountResultAllOf(
        )
    
    def test_account_id(self):
        """Test AccountResultAllOf.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.get("account_id") == "TEST_STRING"

    def test_api_key(self):
        """Test AccountResultAllOf.api_key"""
        self.model.api_key = "TEST_STRING"
        assert self.model.get("api_key") == "TEST_STRING"

    def test_alias(self):
        """Test AccountResultAllOf.alias"""
        self.model.alias = "TEST_STRING"
        assert self.model.get("alias") == "TEST_STRING"

    def test_label(self):
        """Test AccountResultAllOf.label"""
        self.model.label = "TEST_STRING"
        assert self.model.get("label") == "TEST_STRING"

    def test_type(self):
        """Test AccountResultAllOf.type"""
        self.model.type = AccountType.TRIAL
        assert self.model.get("type") == AccountType.TRIAL
        self.model.type = AccountType.FULL
        assert self.model.get("type") == AccountType.FULL

    def test_status(self):
        """Test AccountResultAllOf.status"""
        self.model.status = AccountStatus.CLOSED
        assert self.model.get("status") == AccountStatus.CLOSED
        self.model.status = AccountStatus.SUSPENDED
        assert self.model.get("status") == AccountStatus.SUSPENDED
        self.model.status = AccountStatus.ACTIVE
        assert self.model.get("status") == AccountStatus.ACTIVE

    def test_subresource_uris(self):
        """Test AccountResultAllOf.subresource_uris"""
        testObject = {}
        self.model.subresource_uris = testObject
        assert self.model.get("subresource_uris") == testObject


if __name__ == '__main__':
    unittest.main()