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
from freeclimb.models.mutable_resource_model import MutableResourceModel  # noqa: E501
from freeclimb.rest import ApiException


class TestMutableResourceModel(unittest.TestCase):
    """MutableResourceModel unit test stubs"""

    def setUp(self):
        self.mutable_resource_model = MutableResourceModel()

    def tearDown(self):
        pass

    def testMutableResourceModel(self):
        """Test MutableResourceModel"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.mutable_resource_model.MutableResourceModel()  # noqa: E501
        self.assertTrue(isinstance(self.mutable_resource_model, MutableResourceModel))


if __name__ == '__main__':
    unittest.main()
