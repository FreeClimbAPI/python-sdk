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
from freeclimb.models.message_request_all_of import MessageRequestAllOf  # noqa: E501
from freeclimb.rest import ApiException


class TestMessageRequestAllOf(unittest.TestCase):
    """MessageRequestAllOf unit test stubs"""

    def setUp(self):
        self.message_request_all_of = MessageRequestAllOf(_from='+12223334444', to='+13332224444', text='Test message')

    def tearDown(self):
        pass

    def testMessageRequestAllOf(self):
        """Test MessageRequestAllOf"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.message_request_all_of.MessageRequestAllOf()  # noqa: E501
        self.assertTrue(isinstance(self.message_request_all_of, MessageRequestAllOf))


if __name__ == '__main__':
    unittest.main()
