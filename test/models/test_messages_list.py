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
from freeclimb.models.messages_list import MessagesList  # noqa: E501
from freeclimb.rest import ApiException


class TestMessagesList(unittest.TestCase):
    """MessagesList unit test stubs"""

    def setUp(self):
        self.messages_list = MessagesList()

    def tearDown(self):
        pass

    def testMessagesList(self):
        """Test MessagesList"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.messages_list.MessagesList()  # noqa: E501
        self.assertTrue(isinstance(self.messages_list, MessagesList))


if __name__ == '__main__':
    unittest.main()