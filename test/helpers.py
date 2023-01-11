import urllib3
import json

from freeclimb.model.account_request import AccountRequest
from freeclimb.model.application_request import ApplicationRequest
from freeclimb.model.buy_incoming_number_request import BuyIncomingNumberRequest
from freeclimb.model.create_conference_request import CreateConferenceRequest
from freeclimb.model.incoming_number_request import IncomingNumberRequest
from freeclimb.model.make_call_request import MakeCallRequest
from freeclimb.model.message_request import MessageRequest
from freeclimb.model.queue_request import QueueRequest
from freeclimb.model.update_call_request import UpdateCallRequest
from freeclimb.model.update_conference_participant_request import UpdateConferenceParticipantRequest
from freeclimb.model.update_conference_request import UpdateConferenceRequest
from freeclimb.model.filter_logs_request import FilterLogsRequest
from freeclimb.model_utils import model_to_dict, ModelComposed, ModelNormal, ModelSimple
from freeclimb.model.play_beep import PlayBeep
from freeclimb.model.update_call_request_status import UpdateCallRequestStatus
from freeclimb.model.call_status import CallStatus


class TestHelpers(object):
    @staticmethod
    def build_url(url, path_params):
        for key, value in path_params.items():
            url = url.replace('{' + key + '}', value)
        return url

    @staticmethod
    def build_path_param(param):
        return 'TEST_' + param.upper()
    
    @staticmethod
    def build_query_param(param):
        if param == 'voice_enabled':
            return True
        if param == 'sms_enabled':
            return True
        if param == 'capabilities_voice':
            return True
        if param == 'capabilities_sms':
            return True
        if param == 'capabilities_toll_free':
            return True
        if param == 'capabilities_ten_dlc':
            return True
        if param == 'capabilities_short_code':
            return True
        if param == 'active':
            return False
        if param == 'has_application':
            return False
        if param == 'talk':
            return True
        if param == 'listen':
            return True
        if param == 'status':
            return 'empty'
        if param == 'statusEnum':
            return json.dumps(CallStatus.COMPLETED)
        if param == 'direction':
            return 'inbound'
        if param == 'offnet':
            return True
        return 'TEST_' + param.upper()

    @staticmethod
    def build_body_param(param, klassName):
        if klassName == BuyIncomingNumberRequest:
            return BuyIncomingNumberRequest(
                phone_number="TEST_PHONE_NUMBER",
                application_id='TEST_APPLICATION_ID',
                alias='TEST_ALIAS'
            )
        if klassName == IncomingNumberRequest:
            return IncomingNumberRequest(
                application_id='TEST_APPLICATION_ID',
                alias='TEST_ALIAS'
            )
        if klassName == ApplicationRequest:
            return ApplicationRequest(
                alias = 'TEST_ALIAS',
                voice_url = 'TEST_VOICE_URL',
                voice_fallback_url = 'TEST_VOICE_FALLBACK_URL',
                call_connect_url = 'TEST_CALL_CONNECT_URL',
                status_callback_url = 'TEST_STATUS_CALLBACK_URL',
                sms_url = 'TEST_SMS_URL',
                sms_fallback_url = 'TEST_SMS_FALLBACK_URL'
            )
        if klassName == AccountRequest:
            return AccountRequest(
                alias = 'TEST_ALIAS',
                label = 'TEST_LABEL'
            )
        if klassName == QueueRequest:
            return QueueRequest(
                alias = 'TEST_ALIAS',
                max_size = 10
            )
        if klassName == UpdateConferenceParticipantRequest:
            return UpdateConferenceParticipantRequest(
                talk = True,
                listen = True
            )
        if klassName == UpdateConferenceRequest:
            return UpdateConferenceRequest(
                alias = 'TEST_ALIAS',
                play_beep = json.dumps(PlayBeep.ALWAYS),
                status = 'empty'
            )
        if klassName == MakeCallRequest:
            return MakeCallRequest(
                _from = 'TEST_FROM',
                to = 'TEST_TO',
                application_id = 'TEST_APPLICATION_ID',
                send_digits = 'TEST_SEND_DIGITS',
                if_machine = 'TEST_IF_MACHINE',
                if_machine_url = 'TEST_IF_MACHINE_URL',
                timeout = 10,
                parent_call_id = 'TEST_PARENT_CALL_ID',
                privacy_mode = False,
                call_connect_url = 'TEST_CALL_CONNECT_URL',
            )
        if klassName == CreateConferenceRequest:
            return CreateConferenceRequest(
                alias = 'TEST_ALIAS',
                play_beep = json.dumps(PlayBeep.ALWAYS),
                record = False,
                wait_url = 'TEST_WAIT_URL',
                status_callback_url = 'TEST_STATUS_CALLBACK_URL'
            )
        if klassName == FilterLogsRequest:
            return FilterLogsRequest(
                pql="TEST_PQL"
            )
        if klassName == UpdateCallRequest:
            return UpdateCallRequest(
                status=json.dumps(UpdateCallRequestStatus.COMPLETED)
            )
        if klassName == MessageRequest:
            return MessageRequest(
                _from="TEST_FROM_NUMBER",
                to="TEST_TO_NUMBER",
                text="TEST_TEXT"
            )
        return 'TEST_' + param.upper()
    
    @staticmethod
    def serialize_body_param(param):
        if isinstance(param, ModelSimple) or isinstance(param, ModelNormal) or isinstance(param, ModelComposed):
            print ("Parameters:", param)
            data = model_to_dict(param)
            if len(data) == 0:
                return None
            return json.dumps(data)
        return param

    @staticmethod
    def serialize_query_params(query_params):
        next_params = {}
        for key, value in query_params.items():
            if key == '_from':
                key = 'from'
            if key == 'capabilitiesVoice':
                key = 'capabilities.voice'
            if key == 'capabilitiesSms':
                key = 'capabilities.sms'
            if key == 'capabilitiesTollFree':
                key = 'capabilities.tollFree'
            if key == 'capabilitiesTenDlc':
                key = 'capabilities.tenDLC'
            if key == 'capabilitiesShortCode':
                key = 'capabilities.shortCode'
            next_params[key] = value
        return [(key, value) for key,value in next_params.items()]




class MockPoolManager(object):
    def __init__(self, tc):
        self._tc = tc
        self._reqs = []

    def expect_request(self, *args, **kwargs):
        method = args[0]
        if method == 'GET':
            kwargs.pop('body')
        if method != 'GET':
            kwargs.pop('fields')
        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS'] and 'Content-Type' not in kwargs['headers'].keys():
            kwargs['headers']['Content-Type'] = 'application/json'

        self._reqs.append((args, kwargs))

    def request(self, *args, **kwargs):
        self._tc.assertTrue(len(self._reqs) > 0)
        r = self._reqs.pop(0)
        self._tc.maxDiff = None
        self._tc.assertEqual(r[0], args)
        self._tc.assertEqual(r[1], kwargs)
        return urllib3.HTTPResponse(status=200, body=b'{}')