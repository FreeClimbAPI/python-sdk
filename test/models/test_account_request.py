# coding: utf-8

"""
    FreeClimb API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import freeclimb
from freeclimb.models.account_request import AccountRequest  # noqa: E501
from freeclimb.rest import ApiException


class TestAccountRequest(unittest.TestCase):
    """AccountRequest unit test stubs"""

    def setUp(self):
        self.account_request = AccountRequest(alias='Test Account')

    def tearDown(self):
        pass

    def testAccountRequest(self):
        """Test AccountRequest"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.account_request.AccountRequest()  # noqa: E501
        self.assertTrue(isinstance(self.account_request, AccountRequest))


if __name__ == '__main__':
    unittest.main()