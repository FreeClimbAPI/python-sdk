# coding: utf-8

"""
    FreeClimb API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import freeclimb
from freeclimb.models.conference_participant_list import ConferenceParticipantList  # noqa: E501
from freeclimb.rest import ApiException


class TestConferenceParticipantList(unittest.TestCase):
    """ConferenceParticipantList unit test stubs"""

    def setUp(self):
        self.conference_participant_list = ConferenceParticipantList()

    def tearDown(self):
        pass

    def testConferenceParticipantList(self):
        """Test ConferenceParticipantList"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.conference_participant_list.ConferenceParticipantList()  # noqa: E501
        self.assertTrue(isinstance(self.conference_participant_list, ConferenceParticipantList))


if __name__ == '__main__':
    unittest.main()
