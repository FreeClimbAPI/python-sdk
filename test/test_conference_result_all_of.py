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
from freeclimb.models.conference_result_all_of import ConferenceResultAllOf  # noqa: E501
from freeclimb.rest import ApiException


class TestConferenceResultAllOf(unittest.TestCase):
    """ConferenceResultAllOf unit test stubs"""

    def setUp(self):
        self.conference_result_all_of = ConferenceResultAllOf()

    def tearDown(self):
        pass

    def testConferenceResultAllOf(self):
        """Test ConferenceResultAllOf"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.conference_result_all_of.ConferenceResultAllOf()  # noqa: E501
        self.assertTrue(isinstance(self.conference_result_all_of, ConferenceResultAllOf))


if __name__ == '__main__':
    unittest.main()
