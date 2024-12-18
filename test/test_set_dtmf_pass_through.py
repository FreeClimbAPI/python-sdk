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
from freeclimb.model.set_dtmf_pass_through import SetDTMFPassThrough
from freeclimb.model.set_dtmf_pass_through_all_of import SetDTMFPassThroughAllOf
from freeclimb.model.set_listen import SetListen
from freeclimb.model.set_talk import SetTalk
from freeclimb.model.sms import Sms
from freeclimb.model.start_record_call import StartRecordCall
from freeclimb.model.terminate_conference import TerminateConference
from freeclimb.model.transcribe_utterance import TranscribeUtterance
from freeclimb.model.unpark import Unpark
globals()['AddToConference'] = AddToConference
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
globals()['SetDTMFPassThrough'] = SetDTMFPassThrough
globals()['SetDTMFPassThroughAllOf'] = SetDTMFPassThroughAllOf
globals()['SetListen'] = SetListen
globals()['SetTalk'] = SetTalk
globals()['Sms'] = Sms
globals()['StartRecordCall'] = StartRecordCall
globals()['TerminateConference'] = TerminateConference
globals()['TranscribeUtterance'] = TranscribeUtterance
globals()['Unpark'] = Unpark

from freeclimb.model.set_dtmf_pass_through import SetDTMFPassThrough  # noqa: E501

class TestSetDTMFPassThrough(unittest.TestCase):
    """SetDTMFPassThrough unit test stubs"""

    def setUp(self):
        self.model = SetDTMFPassThrough(
        )
    
    def test_dtmf_pass_through(self):
        """Test SetDTMFPassThrough.dtmf_pass_through"""
        self.model.dtmf_pass_through = False
        assert self.model.get("dtmf_pass_through") == False


    def test_command_test(self):
        assert self.model.command == "SetDTMFPassThrough"

if __name__ == '__main__':
    unittest.main()