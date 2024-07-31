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

from freeclimb.model.conference_participant_result_all_of import ConferenceParticipantResultAllOf  # noqa: E501

class TestConferenceParticipantResultAllOf(unittest.TestCase):
    """ConferenceParticipantResultAllOf unit test stubs"""

    def setUp(self):
        self.model = ConferenceParticipantResultAllOf(
        )
    
    def test_account_id(self):
        """Test ConferenceParticipantResultAllOf.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.get("account_id") == "TEST_STRING"

    def test_conference_id(self):
        """Test ConferenceParticipantResultAllOf.conference_id"""
        self.model.conference_id = "TEST_STRING"
        assert self.model.get("conference_id") == "TEST_STRING"

    def test_call_id(self):
        """Test ConferenceParticipantResultAllOf.call_id"""
        self.model.call_id = "TEST_STRING"
        assert self.model.get("call_id") == "TEST_STRING"

    def test_talk(self):
        """Test ConferenceParticipantResultAllOf.talk"""
        self.model.talk = False
        assert self.model.get("talk") == False

    def test_listen(self):
        """Test ConferenceParticipantResultAllOf.listen"""
        self.model.listen = False
        assert self.model.get("listen") == False

    def test_start_conf_on_enter(self):
        """Test ConferenceParticipantResultAllOf.start_conf_on_enter"""
        self.model.start_conf_on_enter = False
        assert self.model.get("start_conf_on_enter") == False


if __name__ == '__main__':
    unittest.main()