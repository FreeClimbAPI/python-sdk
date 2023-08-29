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
from freeclimb.model.create_conference import CreateConference
from freeclimb.model.dequeue import Dequeue
from freeclimb.model.enqueue import Enqueue
from freeclimb.model.get_digits import GetDigits
from freeclimb.model.get_speech import GetSpeech
from freeclimb.model.hangup import Hangup
from freeclimb.model.if_machine import IfMachine
from freeclimb.model.out_dial import OutDial
from freeclimb.model.out_dial_all_of import OutDialAllOf
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
globals()['CreateConference'] = CreateConference
globals()['Dequeue'] = Dequeue
globals()['Enqueue'] = Enqueue
globals()['GetDigits'] = GetDigits
globals()['GetSpeech'] = GetSpeech
globals()['Hangup'] = Hangup
globals()['IfMachine'] = IfMachine
globals()['OutDial'] = OutDial
globals()['OutDialAllOf'] = OutDialAllOf
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

from freeclimb.model.out_dial import OutDial  # noqa: E501

class TestOutDial(unittest.TestCase):
    """OutDial unit test stubs"""

    def setUp(self):
        self.model = OutDial(
            action_url="",
            call_connect_url="",
            calling_number="",
            destination="",
        )
    
    def test_action_url(self):
        """Test OutDial.action_url"""
        self.model.action_url = "TEST_STRING"
        assert self.model.get("action_url") == "TEST_STRING"

    def test_call_connect_url(self):
        """Test OutDial.call_connect_url"""
        self.model.call_connect_url = "TEST_STRING"
        assert self.model.get("call_connect_url") == "TEST_STRING"

    def test_calling_number(self):
        """Test OutDial.calling_number"""
        self.model.calling_number = "TEST_STRING"
        assert self.model.get("calling_number") == "TEST_STRING"

    def test_destination(self):
        """Test OutDial.destination"""
        self.model.destination = "TEST_STRING"
        assert self.model.get("destination") == "TEST_STRING"

    def test_if_machine(self):
        """Test OutDial.if_machine"""
        self.model.if_machine = IfMachine.REDIRECT
        assert self.model.get("if_machine") == IfMachine.REDIRECT
        self.model.if_machine = IfMachine.HANGUP
        assert self.model.get("if_machine") == IfMachine.HANGUP

    def test_if_machine_url(self):
        """Test OutDial.if_machine_url"""
        self.model.if_machine_url = "TEST_STRING"
        assert self.model.get("if_machine_url") == "TEST_STRING"

    def test_send_digits(self):
        """Test OutDial.send_digits"""
        self.model.send_digits = "TEST_STRING"
        assert self.model.get("send_digits") == "TEST_STRING"

    def test_status_callback_url(self):
        """Test OutDial.status_callback_url"""
        self.model.status_callback_url = "TEST_STRING"
        assert self.model.get("status_callback_url") == "TEST_STRING"

    def test_timeout(self):
        """Test OutDial.timeout"""
        self.model.timeout = 1
        assert self.model.get("timeout") == 1

    def test_privacy_mode(self):
        """Test OutDial.privacy_mode"""
        self.model.privacy_mode = False
        assert self.model.get("privacy_mode") == False

    def test_command_test(self):
        assert self.model.command == "OutDial"

if __name__ == '__main__':
    unittest.main()
