"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest
from datetime import datetime, date
import pytest

import freeclimb

from freeclimb.model.play_all_of import PlayAllOf  # noqa: E501


class TestPlayAllOf(unittest.TestCase):
    """PlayAllOf unit test stubs"""

    def setUp(self):
        self.model = PlayAllOf(
            file="",
        )

    def test_file(self):
        """Test PlayAllOf.file"""
        self.model.file = "TEST_STRING"
        assert self.model.get("file") == "TEST_STRING"

    def test_loop(self):
        """Test PlayAllOf.loop"""
        self.model.loop = 1
        assert self.model.get("loop") == 1

    def test_privacy_mode(self):
        """Test PlayAllOf.privacy_mode"""
        self.model.privacy_mode = False
        assert self.model.get("privacy_mode") == False


if __name__ == "__main__":
    unittest.main()
