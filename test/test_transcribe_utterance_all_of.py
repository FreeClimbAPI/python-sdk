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
from freeclimb.model.transcribe_utterance_all_of_record import TranscribeUtteranceAllOfRecord
globals()['TranscribeUtteranceAllOfRecord'] = TranscribeUtteranceAllOfRecord

from freeclimb.model.transcribe_utterance_all_of import TranscribeUtteranceAllOf  # noqa: E501

class TestTranscribeUtteranceAllOf(unittest.TestCase):
    """TranscribeUtteranceAllOf unit test stubs"""

    def setUp(self):
        self.model = TranscribeUtteranceAllOf(
            action_url="",
        )
    
    def test_action_url(self):
        """Test TranscribeUtteranceAllOf.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.get("action_url") == "TEST_STRING"

    def test_play_beep(self):
        """Test TranscribeUtteranceAllOf.play_beep"""
        self.model.play_beep = False
        assert self.model.get("play_beep") == False

    def test_record(self):
        """Test TranscribeUtteranceAllOf.record"""
        object = TranscribeUtteranceAllOfRecord(
        save_recording=False,
        max_length_sec=60,
        rcrd_termination_silence_time_ms=0,
    )
        self.model.record = object
        assert self.model.get("record", object)

    def test_privacy_for_logging(self):
        """Test TranscribeUtteranceAllOf.privacy_for_logging"""
        self.model.privacy_for_logging = False
        assert self.model.get("privacy_for_logging") == False

    def test_privacy_for_recording(self):
        """Test TranscribeUtteranceAllOf.privacy_for_recording"""
        self.model.privacy_for_recording = False
        assert self.model.get("privacy_for_recording") == False

    def test_prompts(self):
        """Test TranscribeUtteranceAllOf.prompts"""
        testList = []
        self.model.prompts = testList
        assert self.model.get("prompts") == testList


if __name__ == '__main__':
    unittest.main()