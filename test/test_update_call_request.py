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
from freeclimb.model.update_call_request_status import UpdateCallRequestStatus
globals()['UpdateCallRequestStatus'] = UpdateCallRequestStatus

from freeclimb.model.update_call_request import UpdateCallRequest  # noqa: E501

class TestUpdateCallRequest(unittest.TestCase):
    """UpdateCallRequest unit test stubs"""

    def setUp(self):
        self.model = UpdateCallRequest(
            status="TEST_STRING"
        )
    
    def test_status(self):
        """Test UpdateCallRequest.status"""
        self.model.status = UpdateCallRequestStatus.CANCELED
        assert self.model.get("status") == UpdateCallRequestStatus.CANCELED
        self.model.status = UpdateCallRequestStatus.COMPLETED
        assert self.model.get("status") == UpdateCallRequestStatus.COMPLETED

if __name__ == '__main__':
    unittest.main()
