# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import pydantic_core
from datetime import datetime
import freeclimb
from freeclimb import *
from freeclimb.models.create_web_rtc_token import CreateWebRTCToken


class TestCreateWebRTCToken(unittest.TestCase):
    """CreateWebRTCToken unit test stubs"""

    def setUp(self):
        self.model = CreateWebRTCToken(
            to="",
            var_from="",
            uses=1,
        )

    def test_to(self):
        """Test CreateWebRTCToken.to"""
        self.model.to = "TEST_STRING"
        assert self.model.to == "TEST_STRING"

    def test_var_from(self):
        """Test CreateWebRTCToken.var_from"""
        self.model.var_from = "TEST_STRING"
        assert self.model.var_from == "TEST_STRING"

    def test_uses(self):
        """Test CreateWebRTCToken.uses"""
        self.model.uses = 1
        assert self.model.uses == 1


if __name__ == "__main__":
    unittest.main()
