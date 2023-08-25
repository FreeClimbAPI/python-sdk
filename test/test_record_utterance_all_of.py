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

from freeclimb.model.record_utterance_all_of import RecordUtteranceAllOf  # noqa: E501

class TestRecordUtteranceAllOf(unittest.TestCase):
    """RecordUtteranceAllOf unit test stubs"""

    def setUp(self):
        self.model = RecordUtteranceAllOf(
            action_url="",
        )
    
    def test_action_url(self):
        """Test RecordUtteranceAllOf.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.get("action_url") == "TEST_STRING"

    def test_silence_timeout_ms(self):
        """Test RecordUtteranceAllOf.silence_timeout_ms"""
        self.model.silence_timeout_ms = 1
        assert self.model.get("silence_timeout_ms") == 1

    def test_finish_on_key(self):
        """Test RecordUtteranceAllOf.finish_on_key"""
        self.model.finish_on_key = "TEST_STRING"
        assert self.model.get("finish_on_key") == "TEST_STRING"

    def test_max_length_sec(self):
        """Test RecordUtteranceAllOf.max_length_sec"""
        self.model.max_length_sec = 1
        assert self.model.get("max_length_sec") == 1

    def test_play_beep(self):
        """Test RecordUtteranceAllOf.play_beep"""
        self.model.play_beep = False
        assert self.model.get("play_beep") == False

    def test_auto_start(self):
        """Test RecordUtteranceAllOf.auto_start"""
        self.model.auto_start = False
        assert self.model.get("auto_start") == False

    def test_privacy_mode(self):
        """Test RecordUtteranceAllOf.privacy_mode"""
        self.model.privacy_mode = False
        assert self.model.get("privacy_mode") == False

if __name__ == '__main__':
    unittest.main()
