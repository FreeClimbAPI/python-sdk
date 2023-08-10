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

from freeclimb.model.capabilities import Capabilities  # noqa: E501


class TestCapabilities(unittest.TestCase):
    """Capabilities unit test stubs"""

    def setUp(self):
        self.model = Capabilities(
            sms=False, voice=False, toll_free=False, ten_dlc=False, short_code=False)

    def test_voice(self):
        """Test Capabilities.voice"""
        self.model.voice = False
        assert self.model.get("voice") == False

    def test_sms(self):
        """Test Capabilities.sms"""
        self.model.sms = False
        assert self.model.get("sms") == False

    def test_toll_free(self):
        """Test Capabilities.toll_free"""
        self.model.toll_free = False
        assert self.model.get("toll_free") == False

    def test_ten_dlc(self):
        """Test Capabilities.ten_dlc"""
        self.model.ten_dlc = False
        assert self.model.get("ten_dlc") == False

    def test_short_code(self):
        """Test Capabilities.short_code"""
        self.model.short_code = False
        assert self.model.get("short_code") == False


if __name__ == '__main__':
    unittest.main()
