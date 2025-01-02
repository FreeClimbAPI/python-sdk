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
from freeclimb.models.transcribe_utterance import TranscribeUtterance


class TestTranscribeUtterance(unittest.TestCase):
    """TranscribeUtterance unit test stubs"""

    def setUp(self):
        self.model = TranscribeUtterance(
            action_url="",
        )

    def test_action_url(self):
        """Test TranscribeUtterance.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.action_url == "TEST_STRING"

    def test_play_beep(self):
        """Test TranscribeUtterance.play_beep"""
        self.model.play_beep = False
        assert self.model.play_beep == False

    def test_record(self):
        """Test TranscribeUtterance.record"""
        object = freeclimb.models.transcribe_utterance_record.TranscribeUtteranceRecord(
            save_recording=True,
            max_length_sec=1,
            rcrd_termination_silence_time_ms=1,
        )
        self.model.record = object
        assert self.model.record == object

    def test_privacy_for_logging(self):
        """Test TranscribeUtterance.privacy_for_logging"""
        self.model.privacy_for_logging = False
        assert self.model.privacy_for_logging == False

    def test_privacy_for_recording(self):
        """Test TranscribeUtterance.privacy_for_recording"""
        self.model.privacy_for_recording = False
        assert self.model.privacy_for_recording == False

    def test_prompts(self):
        """Test TranscribeUtterance.prompts"""
        testList = []
        self.model.prompts = testList
        assert self.model.prompts == testList


if __name__ == "__main__":
    unittest.main()
