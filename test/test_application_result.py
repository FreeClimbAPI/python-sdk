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
from freeclimb.models.application_result import ApplicationResult  # noqa: E501
from freeclimb.rest import ApiException


class TestApplicationResult(unittest.TestCase):
    """ApplicationResult unit test stubs"""

    def setUp(self):
        self.application_result = ApplicationResult()

    def tearDown(self):
        pass

    def testApplicationResult(self):
        """Test ApplicationResult"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.application_result.ApplicationResult()  # noqa: E501
        self.assertTrue(isinstance(self.application_result, ApplicationResult))


if __name__ == '__main__':
    unittest.main()