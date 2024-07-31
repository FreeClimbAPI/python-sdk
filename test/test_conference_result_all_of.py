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
from freeclimb.model.conference_status import ConferenceStatus
from freeclimb.model.play_beep import PlayBeep
globals()['ConferenceStatus'] = ConferenceStatus
globals()['PlayBeep'] = PlayBeep

from freeclimb.model.conference_result_all_of import ConferenceResultAllOf  # noqa: E501

class TestConferenceResultAllOf(unittest.TestCase):
    """ConferenceResultAllOf unit test stubs"""

    def setUp(self):
        self.model = ConferenceResultAllOf(
        )
    
    def test_conference_id(self):
        """Test ConferenceResultAllOf.conference_id"""
        self.model.conference_id = "TEST_STRING"
        assert self.model.get("conference_id") == "TEST_STRING"

    def test_account_id(self):
        """Test ConferenceResultAllOf.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.get("account_id") == "TEST_STRING"

    def test_alias(self):
        """Test ConferenceResultAllOf.alias"""
        self.model.alias = "TEST_STRING"
        assert self.model.get("alias") == "TEST_STRING"

    def test_play_beep(self):
        """Test ConferenceResultAllOf.play_beep"""
        self.model.play_beep = PlayBeep.ALWAYS
        assert self.model.get("play_beep") == PlayBeep.ALWAYS
        self.model.play_beep = PlayBeep.NEVER
        assert self.model.get("play_beep") == PlayBeep.NEVER
        self.model.play_beep = PlayBeep.ENTRY_ONLY
        assert self.model.get("play_beep") == PlayBeep.ENTRY_ONLY
        self.model.play_beep = PlayBeep.EXIT_ONLY
        assert self.model.get("play_beep") == PlayBeep.EXIT_ONLY

    def test_record(self):
        """Test ConferenceResultAllOf.record"""
        self.model.record = False
        assert self.model.get("record") == False

    def test_status(self):
        """Test ConferenceResultAllOf.status"""
        self.model.status = ConferenceStatus.EMPTY
        assert self.model.get("status") == ConferenceStatus.EMPTY
        self.model.status = ConferenceStatus.POPULATED
        assert self.model.get("status") == ConferenceStatus.POPULATED
        self.model.status = ConferenceStatus.IN_PROGRESS
        assert self.model.get("status") == ConferenceStatus.IN_PROGRESS
        self.model.status = ConferenceStatus.TERMINATED
        assert self.model.get("status") == ConferenceStatus.TERMINATED

    def test_wait_url(self):
        """Test ConferenceResultAllOf.wait_url"""
        self.model.wait_url = "TEST_STRING"
        assert self.model.get("wait_url") == "TEST_STRING"

    def test_action_url(self):
        """Test ConferenceResultAllOf.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.get("action_url") == "TEST_STRING"

    def test_status_callback_url(self):
        """Test ConferenceResultAllOf.status_callback_url"""
        self.model.status_callback_url = "TEST_STRING"
        assert self.model.get("status_callback_url") == "TEST_STRING"

    def test_subresource_uris(self):
        """Test ConferenceResultAllOf.subresource_uris"""
        testObject = {}
        self.model.subresource_uris = testObject
        assert self.model.get("subresource_uris") == testObject


if __name__ == '__main__':
    unittest.main()