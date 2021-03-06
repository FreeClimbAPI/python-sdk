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
from freeclimb.models.make_call_request import MakeCallRequest  # noqa: E501
from freeclimb.rest import ApiException


class TestMakeCallRequest(unittest.TestCase):
    """MakeCallRequest unit test stubs"""

    def setUp(self):
        self.make_call_request = MakeCallRequest(_from='+12223334444', to='+13332224444', application_id='fake_application_id')

    def tearDown(self):
        pass

    def testMakeCallRequest(self):
        """Test MakeCallRequest"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.make_call_request.MakeCallRequest()  # noqa: E501
        self.assertTrue(isinstance(self.make_call_request, MakeCallRequest))


if __name__ == '__main__':
    unittest.main()
