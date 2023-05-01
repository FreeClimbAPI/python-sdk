"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import unittest
from test.helpers import TestHelpers, MockPoolManager

import freeclimb
from freeclimb.api.default_api import DefaultApi  # noqa: E501

from freeclimb.model.play_beep import PlayBeep
from freeclimb.model.call_status import CallStatus
from freeclimb.model.message_direction import MessageDirection
from freeclimb.model.update_call_request_status import UpdateCallRequestStatus
from freeclimb.model.update_conference_request_status import UpdateConferenceRequestStatus

from freeclimb.model.account_request import AccountRequest
from freeclimb.model.account_result import AccountResult
from freeclimb.model.application_list import ApplicationList
from freeclimb.model.application_request import ApplicationRequest
from freeclimb.model.application_result import ApplicationResult
from freeclimb.model.available_number_list import AvailableNumberList
from freeclimb.model.buy_incoming_number_request import BuyIncomingNumberRequest
from freeclimb.model.call_list import CallList
from freeclimb.model.call_result import CallResult
from freeclimb.model.conference_list import ConferenceList
from freeclimb.model.conference_participant_list import ConferenceParticipantList
from freeclimb.model.conference_participant_result import ConferenceParticipantResult
from freeclimb.model.conference_result import ConferenceResult
from freeclimb.model.create_conference_request import CreateConferenceRequest
from freeclimb.model.filter_logs_request import FilterLogsRequest
from freeclimb.model.incoming_number_list import IncomingNumberList
from freeclimb.model.incoming_number_request import IncomingNumberRequest
from freeclimb.model.incoming_number_result import IncomingNumberResult
from freeclimb.model.log_list import LogList
from freeclimb.model.make_call_request import MakeCallRequest
from freeclimb.model.message_request import MessageRequest
from freeclimb.model.message_result import MessageResult
from freeclimb.model.messages_list import MessagesList
from freeclimb.model.queue_list import QueueList
from freeclimb.model.queue_member import QueueMember
from freeclimb.model.queue_member_list import QueueMemberList
from freeclimb.model.queue_request import QueueRequest
from freeclimb.model.queue_result import QueueResult
from freeclimb.model.recording_list import RecordingList
from freeclimb.model.recording_result import RecordingResult
from freeclimb.model.update_call_request import UpdateCallRequest
from freeclimb.model.update_conference_participant_request import UpdateConferenceParticipantRequest
from freeclimb.model.update_conference_request import UpdateConferenceRequest

from io import BufferedReader as file_type

from freeclimb.model.account_request import AccountRequest
from freeclimb.model.account_result import AccountResult
from freeclimb.model.application_list import ApplicationList
from freeclimb.model.application_request import ApplicationRequest
from freeclimb.model.application_result import ApplicationResult
from freeclimb.model.available_number_list import AvailableNumberList
from freeclimb.model.buy_incoming_number_request import BuyIncomingNumberRequest
from freeclimb.model.call_list import CallList
from freeclimb.model.call_result import CallResult
from freeclimb.model.call_status import CallStatus
from freeclimb.model.conference_list import ConferenceList
from freeclimb.model.conference_participant_list import ConferenceParticipantList
from freeclimb.model.conference_participant_result import ConferenceParticipantResult
from freeclimb.model.conference_result import ConferenceResult
from freeclimb.model.create_conference_request import CreateConferenceRequest
from freeclimb.model.filter_logs_request import FilterLogsRequest
from freeclimb.model.incoming_number_list import IncomingNumberList
from freeclimb.model.incoming_number_request import IncomingNumberRequest
from freeclimb.model.incoming_number_result import IncomingNumberResult
from freeclimb.model.log_list import LogList
from freeclimb.model.make_call_request import MakeCallRequest
from freeclimb.model.message_direction import MessageDirection
from freeclimb.model.message_request import MessageRequest
from freeclimb.model.message_result import MessageResult
from freeclimb.model.messages_list import MessagesList
from freeclimb.model.queue_list import QueueList
from freeclimb.model.queue_member import QueueMember
from freeclimb.model.queue_member_list import QueueMemberList
from freeclimb.model.queue_request import QueueRequest
from freeclimb.model.queue_result import QueueResult
from freeclimb.model.recording_list import RecordingList
from freeclimb.model.recording_result import RecordingResult
from freeclimb.model.update_call_request import UpdateCallRequest
from freeclimb.model.update_conference_participant_request import UpdateConferenceParticipantRequest
from freeclimb.model.update_conference_request import UpdateConferenceRequest

import json

class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        configuration = freeclimb.Configuration(
            host = 'http://127.0.0.1:4010',
            username = 'TEST_ACCOUNT_ID',
            password = 'TEST_API_KEY'
        )

        self.api = DefaultApi(freeclimb.ApiClient(configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_buy_a_phone_number(self):
        """Test case for buy_a_phone_number

        Buy a Phone Number  # noqa: E501
        """

        buy_incoming_number_request = buy_incoming_number_request_buy_a_phone_number_test_value


        api_response = self.api.buy_a_phone_number(buy_incoming_number_request=buy_incoming_number_request)
        
        assert isinstance(api_response, IncomingNumberResult)

    def test_create_a_conference(self):
        """Test case for create_a_conference

        Create a Conference  # noqa: E501
        """

        create_conference_request = create_conference_request_create_a_conference_test_value


        api_response = self.api.create_a_conference(create_conference_request=create_conference_request)
        
        assert isinstance(api_response, ConferenceResult)

    def test_create_a_queue(self):
        """Test case for create_a_queue

        Create a Queue  # noqa: E501
        """

        queue_request = queue_request_create_a_queue_test_value


        api_response = self.api.create_a_queue(queue_request=queue_request)
        
        assert isinstance(api_response, QueueResult)

    def test_create_an_application(self):
        """Test case for create_an_application

        Create an application  # noqa: E501
        """

        application_request = application_request_create_an_application_test_value


        api_response = self.api.create_an_application(application_request=application_request)
        
        assert isinstance(api_response, ApplicationResult)

    def test_delete_a_recording(self):
        """Test case for delete_a_recording

        Delete a Recording  # noqa: E501
        """

        recording_id = recording_id_delete_a_recording_test_value


        api_response = self.api.delete_a_recording(recording_id=recording_id)
        
        

    def test_delete_an_application(self):
        """Test case for delete_an_application

        Delete an application  # noqa: E501
        """

        application_id = application_id_delete_an_application_test_value


        api_response = self.api.delete_an_application(application_id=application_id)
        
        

    def test_delete_an_incoming_number(self):
        """Test case for delete_an_incoming_number

        Delete an Incoming Number  # noqa: E501
        """

        phone_number_id = phone_number_id_delete_an_incoming_number_test_value


        api_response = self.api.delete_an_incoming_number(phone_number_id=phone_number_id)
        
        

    def test_dequeue_a_member(self):
        """Test case for dequeue_a_member

        Dequeue a Member  # noqa: E501
        """

        queue_id = queue_id_dequeue_a_member_test_value
        call_id = call_id_dequeue_a_member_test_value


        api_response = self.api.dequeue_a_member(queue_id=queue_id,call_id=call_id)
        
        assert isinstance(api_response, QueueMember)

    def test_dequeue_head_member(self):
        """Test case for dequeue_head_member

        Dequeue Head Member  # noqa: E501
        """

        queue_id = queue_id_dequeue_head_member_test_value


        api_response = self.api.dequeue_head_member(queue_id=queue_id)
        
        assert isinstance(api_response, QueueMember)

    def test_download_a_recording_file(self):
        """Test case for download_a_recording_file

        Download a Recording File  # noqa: E501
        """

        recording_id = recording_id_download_a_recording_file_test_value


        api_response = self.api.download_a_recording_file(recording_id=recording_id)
        
        assert isinstance(api_response, file_type)

    def test_filter_logs(self):
        """Test case for filter_logs

        Filter Logs  # noqa: E501
        """

        filter_logs_request = filter_logs_request_filter_logs_test_value


        api_response = self.api.filter_logs(filter_logs_request=filter_logs_request)
        
        assert isinstance(api_response, LogList)

    def test_get_a_call(self):
        """Test case for get_a_call

        Get a Call  # noqa: E501
        """

        call_id = call_id_get_a_call_test_value


        api_response = self.api.get_a_call(call_id=call_id)
        
        assert isinstance(api_response, CallResult)

    def test_get_a_conference(self):
        """Test case for get_a_conference

        Get a Conference  # noqa: E501
        """

        conference_id = conference_id_get_a_conference_test_value


        api_response = self.api.get_a_conference(conference_id=conference_id)
        
        assert isinstance(api_response, ConferenceResult)

    def test_get_a_member(self):
        """Test case for get_a_member

        Get a Member  # noqa: E501
        """

        queue_id = queue_id_get_a_member_test_value
        call_id = call_id_get_a_member_test_value


        api_response = self.api.get_a_member(queue_id=queue_id,call_id=call_id)
        
        assert isinstance(api_response, QueueMember)

    def test_get_a_participant(self):
        """Test case for get_a_participant

        Get a Participant  # noqa: E501
        """

        conference_id = conference_id_get_a_participant_test_value
        call_id = call_id_get_a_participant_test_value


        api_response = self.api.get_a_participant(conference_id=conference_id,call_id=call_id)
        
        assert isinstance(api_response, ConferenceParticipantResult)

    def test_get_a_queue(self):
        """Test case for get_a_queue

        Get a Queue  # noqa: E501
        """

        queue_id = queue_id_get_a_queue_test_value


        api_response = self.api.get_a_queue(queue_id=queue_id)
        
        assert isinstance(api_response, QueueResult)

    def test_get_a_recording(self):
        """Test case for get_a_recording

        Get a Recording  # noqa: E501
        """

        recording_id = recording_id_get_a_recording_test_value


        api_response = self.api.get_a_recording(recording_id=recording_id)
        
        assert isinstance(api_response, RecordingResult)

    def test_get_an_account(self):
        """Test case for get_an_account

        Get an Account  # noqa: E501
        """



        api_response = self.api.get_an_account()
        
        assert isinstance(api_response, AccountResult)

    def test_get_an_application(self):
        """Test case for get_an_application

        Get an Application  # noqa: E501
        """

        application_id = application_id_get_an_application_test_value


        api_response = self.api.get_an_application(application_id=application_id)
        
        assert isinstance(api_response, ApplicationResult)

    def test_get_an_incoming_number(self):
        """Test case for get_an_incoming_number

        Get an Incoming Number  # noqa: E501
        """

        phone_number_id = phone_number_id_get_an_incoming_number_test_value


        api_response = self.api.get_an_incoming_number(phone_number_id=phone_number_id)
        
        assert isinstance(api_response, IncomingNumberResult)

    def test_get_an_sms_message(self):
        """Test case for get_an_sms_message

        Get an SMS Message  # noqa: E501
        """

        message_id = message_id_get_an_sms_message_test_value


        api_response = self.api.get_an_sms_message(message_id=message_id)
        
        assert isinstance(api_response, MessageResult)

    def test_get_head_member(self):
        """Test case for get_head_member

        Get Head Member  # noqa: E501
        """

        queue_id = queue_id_get_head_member_test_value


        api_response = self.api.get_head_member(queue_id=queue_id)
        
        assert isinstance(api_response, QueueMember)

    def test_list_active_queues(self):
        """Test case for list_active_queues

        List Active Queues  # noqa: E501
        """

        alias = alias_list_active_queues_test_value


        api_response = self.api.list_active_queues(alias=alias)
        
        assert isinstance(api_response, QueueList)

    def test_list_all_account_logs(self):
        """Test case for list_all_account_logs

        List All Account Logs  # noqa: E501
        """



        api_response = self.api.list_all_account_logs()
        
        assert isinstance(api_response, LogList)

    def test_list_applications(self):
        """Test case for list_applications

        List applications  # noqa: E501
        """

        alias = alias_list_applications_test_value


        api_response = self.api.list_applications(alias=alias)
        
        assert isinstance(api_response, ApplicationList)

    def test_list_available_numbers(self):
        """Test case for list_available_numbers

        List available numbers  # noqa: E501
        """

        phone_number = phone_number_list_available_numbers_test_value
        region = region_list_available_numbers_test_value
        country = country_list_available_numbers_test_value
        voice_enabled = voice_enabled_list_available_numbers_test_value
        sms_enabled = sms_enabled_list_available_numbers_test_value
        capabilities_voice = capabilities_voice_list_available_numbers_test_value
        capabilities_sms = capabilities_sms_list_available_numbers_test_value
        capabilities_toll_free = capabilities_toll_free_list_available_numbers_test_value
        capabilities_ten_dlc = capabilities_ten_dlc_list_available_numbers_test_value
        capabilities_short_code = capabilities_short_code_list_available_numbers_test_value


        api_response = self.api.list_available_numbers(phone_number=phone_number,region=region,country=country,voice_enabled=voice_enabled,sms_enabled=sms_enabled,capabilities_voice=capabilities_voice,capabilities_sms=capabilities_sms,capabilities_toll_free=capabilities_toll_free,capabilities_ten_dlc=capabilities_ten_dlc,capabilities_short_code=capabilities_short_code)
        
        assert isinstance(api_response, AvailableNumberList)

    def test_list_call_logs(self):
        """Test case for list_call_logs

        List Call Logs  # noqa: E501
        """

        call_id = call_id_list_call_logs_test_value


        api_response = self.api.list_call_logs(call_id=call_id)
        
        assert isinstance(api_response, LogList)

    def test_list_call_recordings(self):
        """Test case for list_call_recordings

        List Call Recordings  # noqa: E501
        """

        call_id = call_id_list_call_recordings_test_value
        date_created = date_created_list_call_recordings_test_value


        api_response = self.api.list_call_recordings(call_id=call_id,date_created=date_created)
        
        assert isinstance(api_response, RecordingList)

    def test_list_calls(self):
        """Test case for list_calls

        List Calls  # noqa: E501
        """

        active = active_list_calls_test_value
        to = to_list_calls_test_value
        _from = _from_list_calls_test_value
        status = status_list_calls_test_value
        start_time = start_time_list_calls_test_value
        end_time = end_time_list_calls_test_value
        parent_call_id = parent_call_id_list_calls_test_value
        application_id = application_id_list_calls_test_value


        api_response = self.api.list_calls(active=active,to=to,_from=_from,status=status,start_time=start_time,end_time=end_time,parent_call_id=parent_call_id,application_id=application_id)
        
        assert isinstance(api_response, CallList)

    def test_list_conferences(self):
        """Test case for list_conferences

        List Conferences  # noqa: E501
        """

        status = status_list_conferences_test_value
        alias = alias_list_conferences_test_value
        date_created = date_created_list_conferences_test_value
        date_updated = date_updated_list_conferences_test_value


        api_response = self.api.list_conferences(status=status,alias=alias,date_created=date_created,date_updated=date_updated)
        
        assert isinstance(api_response, ConferenceList)

    def test_list_incoming_numbers(self):
        """Test case for list_incoming_numbers

        List Incoming Numbers  # noqa: E501
        """

        phone_number = phone_number_list_incoming_numbers_test_value
        alias = alias_list_incoming_numbers_test_value
        region = region_list_incoming_numbers_test_value
        country = country_list_incoming_numbers_test_value
        application_id = application_id_list_incoming_numbers_test_value
        has_application = has_application_list_incoming_numbers_test_value
        voice_enabled = voice_enabled_list_incoming_numbers_test_value
        sms_enabled = sms_enabled_list_incoming_numbers_test_value
        capabilities_voice = capabilities_voice_list_incoming_numbers_test_value
        capabilities_sms = capabilities_sms_list_incoming_numbers_test_value
        capabilities_toll_free = capabilities_toll_free_list_incoming_numbers_test_value
        capabilities_ten_dlc = capabilities_ten_dlc_list_incoming_numbers_test_value
        capabilities_short_code = capabilities_short_code_list_incoming_numbers_test_value
        offnet = offnet_list_incoming_numbers_test_value


        api_response = self.api.list_incoming_numbers(phone_number=phone_number,alias=alias,region=region,country=country,application_id=application_id,has_application=has_application,voice_enabled=voice_enabled,sms_enabled=sms_enabled,capabilities_voice=capabilities_voice,capabilities_sms=capabilities_sms,capabilities_toll_free=capabilities_toll_free,capabilities_ten_dlc=capabilities_ten_dlc,capabilities_short_code=capabilities_short_code,offnet=offnet)
        
        assert isinstance(api_response, IncomingNumberList)

    def test_list_members(self):
        """Test case for list_members

        List Members  # noqa: E501
        """

        queue_id = queue_id_list_members_test_value


        api_response = self.api.list_members(queue_id=queue_id)
        
        assert isinstance(api_response, QueueMemberList)

    def test_list_participants(self):
        """Test case for list_participants

        List Participants  # noqa: E501
        """

        conference_id = conference_id_list_participants_test_value
        talk = talk_list_participants_test_value
        listen = listen_list_participants_test_value


        api_response = self.api.list_participants(conference_id=conference_id,talk=talk,listen=listen)
        
        assert isinstance(api_response, ConferenceParticipantList)

    def test_list_recordings(self):
        """Test case for list_recordings

        List Recordings  # noqa: E501
        """

        call_id = call_id_list_recordings_test_value
        conference_id = conference_id_list_recordings_test_value
        date_created = date_created_list_recordings_test_value


        api_response = self.api.list_recordings(call_id=call_id,conference_id=conference_id,date_created=date_created)
        
        assert isinstance(api_response, RecordingList)

    def test_list_sms_messages(self):
        """Test case for list_sms_messages

        List SMS Messages  # noqa: E501
        """

        to = to_list_sms_messages_test_value
        _from = _from_list_sms_messages_test_value
        begin_time = begin_time_list_sms_messages_test_value
        end_time = end_time_list_sms_messages_test_value
        direction = direction_list_sms_messages_test_value


        api_response = self.api.list_sms_messages(to=to,_from=_from,begin_time=begin_time,end_time=end_time,direction=direction)
        
        assert isinstance(api_response, MessagesList)

    def test_make_a_call(self):
        """Test case for make_a_call

        Make a Call  # noqa: E501
        """

        make_call_request = make_call_request_make_a_call_test_value


        api_response = self.api.make_a_call(make_call_request=make_call_request)
        
        assert isinstance(api_response, CallResult)

    def test_remove_a_participant(self):
        """Test case for remove_a_participant

        Remove a Participant  # noqa: E501
        """

        conference_id = conference_id_remove_a_participant_test_value
        call_id = call_id_remove_a_participant_test_value


        api_response = self.api.remove_a_participant(conference_id=conference_id,call_id=call_id)
        
        

    def test_send_an_sms_message(self):
        """Test case for send_an_sms_message

        Send an SMS Message  # noqa: E501
        """

        message_request = message_request_send_an_sms_message_test_value


        api_response = self.api.send_an_sms_message(message_request=message_request)
        
        assert isinstance(api_response, MessageResult)

    def test_stream_a_recording_file(self):
        """Test case for stream_a_recording_file

        Stream a Recording File  # noqa: E501
        """

        recording_id = recording_id_stream_a_recording_file_test_value


        api_response = self.api.stream_a_recording_file(recording_id=recording_id)
        
        assert isinstance(api_response, file_type)

    def test_update_a_conference(self):
        """Test case for update_a_conference

        Update a Conference  # noqa: E501
        """

        conference_id = conference_id_update_a_conference_test_value
        update_conference_request = update_conference_request_update_a_conference_test_value


        api_response = self.api.update_a_conference(conference_id=conference_id,update_conference_request=update_conference_request)
        
        assert isinstance(api_response, ConferenceResult)

    def test_update_a_live_call(self):
        """Test case for update_a_live_call

        Update a Live Call  # noqa: E501
        """

        call_id = call_id_update_a_live_call_test_value
        update_call_request = update_call_request_update_a_live_call_test_value


        api_response = self.api.update_a_live_call(call_id=call_id,update_call_request=update_call_request)
        
        

    def test_update_a_participant(self):
        """Test case for update_a_participant

        Update a Participant  # noqa: E501
        """

        conference_id = conference_id_update_a_participant_test_value
        call_id = call_id_update_a_participant_test_value
        update_conference_participant_request = update_conference_participant_request_update_a_participant_test_value


        api_response = self.api.update_a_participant(conference_id=conference_id,call_id=call_id,update_conference_participant_request=update_conference_participant_request)
        
        assert isinstance(api_response, ConferenceParticipantResult)

    def test_update_a_queue(self):
        """Test case for update_a_queue

        Update a Queue  # noqa: E501
        """

        queue_id = queue_id_update_a_queue_test_value
        queue_request = queue_request_update_a_queue_test_value


        api_response = self.api.update_a_queue(queue_id=queue_id,queue_request=queue_request)
        
        assert isinstance(api_response, QueueResult)

    def test_update_an_account(self):
        """Test case for update_an_account

        Manage an account  # noqa: E501
        """

        account_request = account_request_update_an_account_test_value


        api_response = self.api.update_an_account(account_request=account_request)
        
        

    def test_update_an_application(self):
        """Test case for update_an_application

        Update an application  # noqa: E501
        """

        application_id = application_id_update_an_application_test_value
        application_request = application_request_update_an_application_test_value


        api_response = self.api.update_an_application(application_id=application_id,application_request=application_request)
        
        assert isinstance(api_response, ApplicationResult)

    def test_update_an_incoming_number(self):
        """Test case for update_an_incoming_number

        Update an Incoming Number  # noqa: E501
        """

        phone_number_id = phone_number_id_update_an_incoming_number_test_value
        incoming_number_request = incoming_number_request_update_an_incoming_number_test_value


        api_response = self.api.update_an_incoming_number(phone_number_id=phone_number_id,incoming_number_request=incoming_number_request)
        
        assert isinstance(api_response, IncomingNumberResult)


buy_incoming_number_request_buy_a_phone_number_test_value = BuyIncomingNumberRequest(
            phone_number="phone_number_example",
            alias="alias_example",
            application_id="application_id_example",
)

create_conference_request_create_a_conference_test_value = CreateConferenceRequest(
            alias="alias_example",
            play_beep=PlayBeep.ALWAYS,
            record=True,
            wait_url="wait_url_example",
            status_callback_url="status_callback_url_example",
)

queue_request_create_a_queue_test_value = QueueRequest(
        alias="alias_example",
        max_size=100,
)


application_request_create_an_application_test_value = ApplicationRequest(
            alias="alias_example",
            voice_url="voice_url_example",
            voice_fallback_url="voice_fallback_url_example",
            call_connect_url="call_connect_url_example",
            status_callback_url="status_callback_url_example",
            sms_url="sms_url_example",
            sms_fallback_url="sms_fallback_url_example",
)
    
recording_id_delete_a_recording_test_value = "recordingId_example"

application_id_delete_an_application_test_value = "applicationId_example"

phone_number_id_delete_an_incoming_number_test_value = "phoneNumberId_example"

queue_id_dequeue_a_member_test_value = "queueId_example"

call_id_dequeue_a_member_test_value = "callId_example"

queue_id_dequeue_head_member_test_value = "queueId_example"

recording_id_download_a_recording_file_test_value = "recordingId_example"

filter_logs_request_filter_logs_test_value = FilterLogsRequest(
            pql="pql_example",
)
call_id_get_a_call_test_value = "callId_example"

conference_id_get_a_conference_test_value = "conferenceId_example"

queue_id_get_a_member_test_value = "queueId_example"

call_id_get_a_member_test_value = "callId_example"

conference_id_get_a_participant_test_value = "conferenceId_example"

call_id_get_a_participant_test_value = "callId_example"

queue_id_get_a_queue_test_value = "queueId_example"

recording_id_get_a_recording_test_value = "recordingId_example"

application_id_get_an_application_test_value = "applicationId_example"

phone_number_id_get_an_incoming_number_test_value = "phoneNumberId_example"

message_id_get_an_sms_message_test_value = "messageId_example"

queue_id_get_head_member_test_value = "queueId_example"

alias_list_active_queues_test_value = "alias_example"

alias_list_applications_test_value = "alias_example"

phone_number_list_available_numbers_test_value = "phoneNumberId_example"

region_list_available_numbers_test_value = "region_example"

country_list_available_numbers_test_value = "country_example"

voice_enabled_list_available_numbers_test_value = True

sms_enabled_list_available_numbers_test_value = True

capabilities_voice_list_available_numbers_test_value = True

capabilities_sms_list_available_numbers_test_value = True

capabilities_toll_free_list_available_numbers_test_value = True

capabilities_ten_dlc_list_available_numbers_test_value = True

capabilities_short_code_list_available_numbers_test_value = True

call_id_list_call_logs_test_value = "callId_example"

call_id_list_call_recordings_test_value = "callId_example"

date_created_list_call_recordings_test_value = "dateCreated_example"

active_list_calls_test_value = False 

to_list_calls_test_value = "to_example"

_from_list_calls_test_value = "from_example"

status_list_calls_test_value = CallStatus.QUEUED

start_time_list_calls_test_value = "startTime_example"

end_time_list_calls_test_value = "endTime_example"

parent_call_id_list_calls_test_value = "parentCallId_example"

application_id_list_calls_test_value = ['AP0123456789ABCDEFabcedf000000000000000001','AP0123456789ABCDEFabcedf000000000000000002', 'AP0123456789ABCDEFabcedf000000000000000003']

status_list_conferences_test_value = "status_example"

alias_list_conferences_test_value = "alias_example"

date_created_list_conferences_test_value = "dateCreated_example"

date_updated_list_conferences_test_value = "dateUpdated_example"
    
phone_number_list_incoming_numbers_test_value = "phoneNumberId_example"

alias_list_incoming_numbers_test_value = "alias_example"

region_list_incoming_numbers_test_value = "region_example"

country_list_incoming_numbers_test_value = "country_example"

application_id_list_incoming_numbers_test_value = "applicationId_example"

has_application_list_incoming_numbers_test_value = False

voice_enabled_list_incoming_numbers_test_value = True

sms_enabled_list_incoming_numbers_test_value = True

capabilities_voice_list_incoming_numbers_test_value = True

capabilities_sms_list_incoming_numbers_test_value = True

capabilities_toll_free_list_incoming_numbers_test_value = True

capabilities_ten_dlc_list_incoming_numbers_test_value = True

capabilities_short_code_list_incoming_numbers_test_value = True

queue_id_list_members_test_value = "queueId_example"

conference_id_list_participants_test_value = "conferenceId_example"

talk_list_participants_test_value = True

listen_list_participants_test_value = True

to_list_sms_messages_test_value="to_example"

_from_list_sms_messages_test_value = "from_example"

begin_time_list_sms_messages_test_value = "beginTime_example"

end_time_list_sms_messages_test_value = "endTime_example"

direction_list_sms_messages_test_value = MessageDirection.INBOUND

conference_id_remove_a_participant_test_value = "conferenceId_example"

call_id_remove_a_participant_test_value = "callId_example"

recording_id_stream_a_recording_file_test_value = "recordingId_example"

conference_id_update_a_conference_test_value = "conferenceId_example"

call_id_update_a_live_call_test_value = "callId_example"

conference_id_update_a_participant_test_value = "conferenceId_example"

call_id_update_a_participant_test_value = "callId_example"

queue_id_update_a_queue_test_value = "queueId_example"

application_id_update_an_application_test_value = "applicationId_example"

phone_number_id_update_an_incoming_number_test_value = "phoneNumberId_example"

offnet_list_incoming_numbers_test_value = True

call_id_list_recordings_test_value = "callId_example"

conference_id_list_recordings_test_value = "conferenceId_example"

date_created_list_recordings_test_value = "dateCreated_example"

queue_request_update_a_queue_test_value = QueueRequest(
        alias="alias_example",
        max_size=100,
)

application_request_update_an_application_test_value = ApplicationRequest(
            alias="alias_example",
            voice_url="voice_url_example",
            voice_fallback_url="voice_fallback_url_example",
            call_connect_url="call_connect_url_example",
            status_callback_url="status_callback_url_example",
            sms_url="sms_url_example",
            sms_fallback_url="sms_fallback_url_example",
)
make_call_request_make_a_call_test_value = MakeCallRequest(
    _from="_from_example",
    to="to_example",
    application_id="application_id_example",
    send_digits="send_digits_example",
    if_machine="if_machine_example",
    if_machine_url="if_machine_url_example",
    timeout=30,
    parent_call_id="parent_call_id_example",
    privacy_mode=True,
    call_connect_url="call_connect_url_example",
)

message_request_send_an_sms_message_test_value = MessageRequest(
        _from="_from_example",
        to="to_example",
        text="Example Text",
)

update_conference_request_update_a_conference_test_value = UpdateConferenceRequest(
        alias="alias_example",
        play_beep=PlayBeep.ALWAYS,
        status=UpdateConferenceRequestStatus.EMPTY,
)

update_call_request_update_a_live_call_test_value = UpdateCallRequest(
        status=UpdateCallRequestStatus.CANCELED,
)

update_conference_participant_request_update_a_participant_test_value = UpdateConferenceParticipantRequest(
        talk=True,
        listen=True,
)

account_request_update_an_account_test_value = AccountRequest(
        alias="alias_example",
        label="label_example",
)

incoming_number_request_update_an_incoming_number_test_value = IncomingNumberRequest(
        application_id="application_id_example",
        alias="alias_example",
)

if __name__ == '__main__':
    unittest.main()
