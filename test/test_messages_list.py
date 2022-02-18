"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import freeclimb
from freeclimb.model.message_result import MessageResult
from freeclimb.model.messages_list_all_of import MessagesListAllOf
from freeclimb.model.pagination_model import PaginationModel
globals()['MessageResult'] = MessageResult
globals()['MessagesListAllOf'] = MessagesListAllOf
globals()['PaginationModel'] = PaginationModel

from freeclimb.model.messages_list import MessagesList  # noqa: E501

class TestMessagesList(unittest.TestCase):
    """MessagesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMessagesList(self):
        """Test MessagesList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MessagesList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
