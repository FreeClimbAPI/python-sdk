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
import decimal

import freeclimb

from freeclimb.model.account_status import AccountStatus  # noqa: E501


class TestAccountStatus(unittest.TestCase):
    """AccountStatus unit test stubs"""

    def test_CLOSED_should_serialize_to_enum(self):
        expected = AccountStatus.CLOSED
        calculated = AccountStatus['CLOSED']
        assert expected == calculated

    def test_CLOSED_should_deserialize_to_string(self):
        test = AccountStatus.CLOSED
        expected = "closed"
        calculated = test.value
        assert expected == calculated

    def test_SUSPENDED_should_serialize_to_enum(self):
        expected = AccountStatus.SUSPENDED
        calculated = AccountStatus['SUSPENDED']
        assert expected == calculated

    def test_SUSPENDED_should_deserialize_to_string(self):
        test = AccountStatus.SUSPENDED
        expected = "suspended"
        calculated = test.value
        assert expected == calculated

    def test_ACTIVE_should_serialize_to_enum(self):
        expected = AccountStatus.ACTIVE
        calculated = AccountStatus['ACTIVE']
        assert expected == calculated

    def test_ACTIVE_should_deserialize_to_string(self):
        test = AccountStatus.ACTIVE
        expected = "active"
        calculated = test.value
        assert expected == calculated


if __name__ == '__main__':
    unittest.main()
