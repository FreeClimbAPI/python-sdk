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
from freeclimb.models.queue_list_all_of import QueueListAllOf  # noqa: E501
from freeclimb.rest import ApiException


class TestQueueListAllOf(unittest.TestCase):
    """QueueListAllOf unit test stubs"""

    def setUp(self):
        self.queue_list_all_of = QueueListAllOf()

    def tearDown(self):
        pass

    def testQueueListAllOf(self):
        """Test QueueListAllOf"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.queue_list_all_of.QueueListAllOf()  # noqa: E501
        self.assertTrue(isinstance(self.queue_list_all_of, QueueListAllOf))


if __name__ == '__main__':
    unittest.main()
