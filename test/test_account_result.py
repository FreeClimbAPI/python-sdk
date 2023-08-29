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
from freeclimb.model.account_result_all_of import AccountResultAllOf
from freeclimb.model.account_status import AccountStatus
from freeclimb.model.account_type import AccountType
from freeclimb.model.mutable_resource_model import MutableResourceModel
globals()['AccountResultAllOf'] = AccountResultAllOf
globals()['AccountStatus'] = AccountStatus
globals()['AccountType'] = AccountType
globals()['MutableResourceModel'] = MutableResourceModel

from freeclimb.model.account_result import AccountResult  # noqa: E501

class TestAccountResult(unittest.TestCase):
    """AccountResult unit test stubs"""

    def setUp(self):
        self.model = AccountResult(
        )
    
    def test_uri(self):
        """Test AccountResult.uri"""
        self.model.uri = "TEST_STRING"
        assert self.model.get("uri") == "TEST_STRING"

    def test_date_created(self):
        """Test AccountResult.date_created"""
        self.model.date_created = "TEST_STRING"
        assert self.model.get("date_created") == "TEST_STRING"

    def test_date_updated(self):
        """Test AccountResult.date_updated"""
        self.model.date_updated = "TEST_STRING"
        assert self.model.get("date_updated") == "TEST_STRING"

    def test_revision(self):
        """Test AccountResult.revision"""
        self.model.revision = 1
        assert self.model.get("revision") == 1

    def test_account_id(self):
        """Test AccountResult.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.get("account_id") == "TEST_STRING"

    def test_api_key(self):
        """Test AccountResult.api_key"""
        self.model.api_key = "TEST_STRING"
        assert self.model.get("api_key") == "TEST_STRING"

    def test_alias(self):
        """Test AccountResult.alias"""
        self.model.alias = "TEST_STRING"
        assert self.model.get("alias") == "TEST_STRING"

    def test_label(self):
        """Test AccountResult.label"""
        self.model.label = "TEST_STRING"
        assert self.model.get("label") == "TEST_STRING"

    def test_type(self):
        """Test AccountResult.type"""
        self.model.type = AccountType.TRIAL
        assert self.model.get("type") == AccountType.TRIAL
        self.model.type = AccountType.FULL
        assert self.model.get("type") == AccountType.FULL

    def test_status(self):
        """Test AccountResult.status"""
        self.model.status = AccountStatus.CLOSED
        assert self.model.get("status") == AccountStatus.CLOSED
        self.model.status = AccountStatus.SUSPENDED
        assert self.model.get("status") == AccountStatus.SUSPENDED
        self.model.status = AccountStatus.ACTIVE
        assert self.model.get("status") == AccountStatus.ACTIVE

    def test_subresource_uris(self):
        """Test AccountResult.subresource_uris"""
        testObject = {}
        self.model.subresource_uris = testObject
        assert self.model.get("subresource_uris") == testObject

if __name__ == '__main__':
    unittest.main()
