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

from freeclimb.model.if_machine import IfMachine  # noqa: E501

class TestIfMachine(unittest.TestCase):
    """IfMachine unit test stubs"""

    
    def test_REDIRECT_should_serialize_to_enum(self):
        expected = IfMachine.REDIRECT
        calculated = IfMachine['REDIRECT']
        assert expected == calculated

    def test_REDIRECT_should_deserialize_to_string(self):
        test = IfMachine.REDIRECT
        expected = "redirect"
        calculated = test.value
        assert expected == calculated

    def test_HANGUP_should_serialize_to_enum(self):
        expected = IfMachine.HANGUP
        calculated = IfMachine['HANGUP']
        assert expected == calculated

    def test_HANGUP_should_deserialize_to_string(self):
        test = IfMachine.HANGUP
        expected = "hangup"
        calculated = test.value
        assert expected == calculated

    
if __name__ == '__main__':
    unittest.main()