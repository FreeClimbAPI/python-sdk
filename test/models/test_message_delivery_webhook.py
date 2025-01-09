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
from freeclimb.models.message_delivery_webhook import MessageDeliveryWebhook


class TestMessageDeliveryWebhook(unittest.TestCase):
    """MessageDeliveryWebhook unit test stubs"""

    def setUp(self):
        self.model = MessageDeliveryWebhook()

    def test_request_type(self):
        """Test MessageDeliveryWebhook.request_type"""

    def test_account_id(self):
        """Test MessageDeliveryWebhook.account_id"""
        self.model.account_id = "TEST_STRING"
        assert self.model.account_id == "TEST_STRING"

    def test_var_from(self):
        """Test MessageDeliveryWebhook.var_from"""
        self.model.var_from = "TEST_STRING"
        assert self.model.var_from == "TEST_STRING"

    def test_to(self):
        """Test MessageDeliveryWebhook.to"""
        self.model.to = "TEST_STRING"
        assert self.model.to == "TEST_STRING"

    def test_text(self):
        """Test MessageDeliveryWebhook.text"""
        self.model.text = "TEST_STRING"
        assert self.model.text == "TEST_STRING"

    def test_direction(self):
        """Test MessageDeliveryWebhook.direction"""
        self.model.direction = "TEST_STRING"
        assert self.model.direction == "TEST_STRING"

    def test_application_id(self):
        """Test MessageDeliveryWebhook.application_id"""
        self.model.application_id = "TEST_STRING"
        assert self.model.application_id == "TEST_STRING"

    def test_status(self):
        """Test MessageDeliveryWebhook.status"""
        self.model.status = "TEST_STRING"
        assert self.model.status == "TEST_STRING"

    def test_phone_number_id(self):
        """Test MessageDeliveryWebhook.phone_number_id"""
        self.model.phone_number_id = "TEST_STRING"
        assert self.model.phone_number_id == "TEST_STRING"

    def test_uri(self):
        """Test MessageDeliveryWebhook.uri"""
        self.model.uri = "TEST_STRING"
        assert self.model.uri == "TEST_STRING"

    def test_deserialize(self):
        payload = '{ "requestType": "messageDelivery" }'
        assert isinstance(
            MessageDeliveryWebhook.deserialize(payload), MessageDeliveryWebhook
        )


if __name__ == "__main__":
    unittest.main()
