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
from freeclimb.models.add_to_conference import AddToConference


class TestAddToConference(unittest.TestCase):
    """AddToConference unit test stubs"""

    def setUp(self):
        self.model = AddToConference(
            conference_id="",
        )

    def test_allow_call_control(self):
        """Test AddToConference.allow_call_control"""
        self.model.allow_call_control = False
        assert self.model.allow_call_control == False

    def test_call_control_sequence(self):
        """Test AddToConference.call_control_sequence"""
        self.model.call_control_sequence = "TEST_STRING"
        assert self.model.call_control_sequence == "TEST_STRING"

    def test_call_control_url(self):
        """Test AddToConference.call_control_url"""
        self.model.call_control_url = "TEST_STRING"
        assert self.model.call_control_url == "TEST_STRING"

    def test_conference_id(self):
        """Test AddToConference.conference_id"""
        self.model.conference_id = "TEST_STRING"
        assert self.model.conference_id == "TEST_STRING"

    def test_leave_conference_url(self):
        """Test AddToConference.leave_conference_url"""
        self.model.leave_conference_url = "TEST_STRING"
        assert self.model.leave_conference_url == "TEST_STRING"

    def test_listen(self):
        """Test AddToConference.listen"""
        self.model.listen = False
        assert self.model.listen == False

    def test_notification_url(self):
        """Test AddToConference.notification_url"""
        self.model.notification_url = "TEST_STRING"
        assert self.model.notification_url == "TEST_STRING"

    def test_start_conf_on_enter(self):
        """Test AddToConference.start_conf_on_enter"""
        self.model.start_conf_on_enter = False
        assert self.model.start_conf_on_enter == False

    def test_talk(self):
        """Test AddToConference.talk"""
        self.model.talk = False
        assert self.model.talk == False

    def test_dtmf_pass_through(self):
        """Test AddToConference.dtmf_pass_through"""
        self.model.dtmf_pass_through = False
        assert self.model.dtmf_pass_through == False


if __name__ == "__main__":
    unittest.main()
