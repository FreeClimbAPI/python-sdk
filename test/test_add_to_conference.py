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
from freeclimb.model.add_to_conference import AddToConference
from freeclimb.model.add_to_conference_all_of import AddToConferenceAllOf
from freeclimb.model.create_conference import CreateConference
from freeclimb.model.dequeue import Dequeue
from freeclimb.model.enqueue import Enqueue
from freeclimb.model.get_digits import GetDigits
from freeclimb.model.get_speech import GetSpeech
from freeclimb.model.hangup import Hangup
from freeclimb.model.out_dial import OutDial
from freeclimb.model.park import Park
from freeclimb.model.pause import Pause
from freeclimb.model.percl_command import PerclCommand
from freeclimb.model.play import Play
from freeclimb.model.play_early_media import PlayEarlyMedia
from freeclimb.model.record_utterance import RecordUtterance
from freeclimb.model.redirect import Redirect
from freeclimb.model.reject import Reject
from freeclimb.model.remove_from_conference import RemoveFromConference
from freeclimb.model.say import Say
from freeclimb.model.send_digits import SendDigits
from freeclimb.model.set_listen import SetListen
from freeclimb.model.set_talk import SetTalk
from freeclimb.model.sms import Sms
from freeclimb.model.start_record_call import StartRecordCall
from freeclimb.model.terminate_conference import TerminateConference
from freeclimb.model.unpark import Unpark
globals()['AddToConference'] = AddToConference
globals()['AddToConferenceAllOf'] = AddToConferenceAllOf
globals()['CreateConference'] = CreateConference
globals()['Dequeue'] = Dequeue
globals()['Enqueue'] = Enqueue
globals()['GetDigits'] = GetDigits
globals()['GetSpeech'] = GetSpeech
globals()['Hangup'] = Hangup
globals()['OutDial'] = OutDial
globals()['Park'] = Park
globals()['Pause'] = Pause
globals()['PerclCommand'] = PerclCommand
globals()['Play'] = Play
globals()['PlayEarlyMedia'] = PlayEarlyMedia
globals()['RecordUtterance'] = RecordUtterance
globals()['Redirect'] = Redirect
globals()['Reject'] = Reject
globals()['RemoveFromConference'] = RemoveFromConference
globals()['Say'] = Say
globals()['SendDigits'] = SendDigits
globals()['SetListen'] = SetListen
globals()['SetTalk'] = SetTalk
globals()['Sms'] = Sms
globals()['StartRecordCall'] = StartRecordCall
globals()['TerminateConference'] = TerminateConference
globals()['Unpark'] = Unpark

from freeclimb.model.add_to_conference import AddToConference  # noqa: E501

class TestAddToConference(unittest.TestCase):
    """AddToConference unit test stubs"""

    def setUp(self):
        self.model = AddToConference(
            conference_id="",
            
        )
    
    def test_allow_call_control(self):
        """Test AddToConference.allow_call_control"""
        self.model.allow_call_control = False
        assert self.model.get("allow_call_control") == False

    def test_call_control_sequence(self):
        """Test AddToConference.call_control_sequence"""
        self.model.call_control_sequence = "TEST_STRING"
        assert self.model.get("call_control_sequence") == "TEST_STRING"

    def test_call_control_url(self):
        """Test AddToConference.call_control_url"""
        self.model.call_control_url = "TEST_STRING"
        assert self.model.get("call_control_url") == "TEST_STRING"

    def test_conference_id(self):
        """Test AddToConference.conference_id"""
        self.model.conference_id = "TEST_STRING"
        assert self.model.get("conference_id") == "TEST_STRING"

    def test_call_id(self):
        """Test AddToConference.call_id"""
        self.model.call_id = "TEST_STRING"
        assert self.model.get("call_id") == "TEST_STRING"

    def test_leave_conference_url(self):
        """Test AddToConference.leave_conference_url"""
        self.model.leave_conference_url = "TEST_STRING"
        assert self.model.get("leave_conference_url") == "TEST_STRING"

    def test_listen(self):
        """Test AddToConference.listen"""
        self.model.listen = False
        assert self.model.get("listen") == False

    def test_notification_url(self):
        """Test AddToConference.notification_url"""
        self.model.notification_url = "TEST_STRING"
        assert self.model.get("notification_url") == "TEST_STRING"

    def test_start_conf_on_enter(self):
        """Test AddToConference.start_conf_on_enter"""
        self.model.start_conf_on_enter = False
        assert self.model.get("start_conf_on_enter") == False

    def test_talk(self):
        """Test AddToConference.talk"""
        self.model.talk = False
        assert self.model.get("talk") == False

    def test_command_test(self):
        assert self.model.command == "AddToConference"

if __name__ == '__main__':
    unittest.main()
