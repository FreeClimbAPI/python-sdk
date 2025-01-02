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

from freeclimb.model.add_to_conference_all_of import AddToConferenceAllOf  # noqa: E501


class TestAddToConferenceAllOf(unittest.TestCase):
    """AddToConferenceAllOf unit test stubs"""

    def setUp(self):
        self.model = AddToConferenceAllOf(
            conference_id="",
        )

    def test_allow_call_control(self):
        """Test AddToConferenceAllOf.allow_call_control"""
        self.model.allow_call_control = False
        assert self.model.get("allow_call_control") == False

    def test_call_control_sequence(self):
        """Test AddToConferenceAllOf.call_control_sequence"""
        self.model.call_control_sequence = "TEST_STRING"
        assert self.model.get("call_control_sequence") == "TEST_STRING"

    def test_call_control_url(self):
        """Test AddToConferenceAllOf.call_control_url"""
        self.model.call_control_url = "TEST_STRING"
        assert self.model.get("call_control_url") == "TEST_STRING"

    def test_conference_id(self):
        """Test AddToConferenceAllOf.conference_id"""
        self.model.conference_id = "TEST_STRING"
        assert self.model.get("conference_id") == "TEST_STRING"

    def test_leave_conference_url(self):
        """Test AddToConferenceAllOf.leave_conference_url"""
        self.model.leave_conference_url = "TEST_STRING"
        assert self.model.get("leave_conference_url") == "TEST_STRING"

    def test_listen(self):
        """Test AddToConferenceAllOf.listen"""
        self.model.listen = False
        assert self.model.get("listen") == False

    def test_notification_url(self):
        """Test AddToConferenceAllOf.notification_url"""
        self.model.notification_url = "TEST_STRING"
        assert self.model.get("notification_url") == "TEST_STRING"

    def test_start_conf_on_enter(self):
        """Test AddToConferenceAllOf.start_conf_on_enter"""
        self.model.start_conf_on_enter = False
        assert self.model.get("start_conf_on_enter") == False

    def test_talk(self):
        """Test AddToConferenceAllOf.talk"""
        self.model.talk = False
        assert self.model.get("talk") == False


if __name__ == "__main__":
    unittest.main()
