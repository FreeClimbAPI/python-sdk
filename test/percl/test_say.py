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
from freeclimb.percl.say import Say  # noqa: E501
from freeclimb.rest import ApiException


class TestSay(unittest.TestCase):
    """Say unit test stubs"""
    text='Test message'

    def setUp(self):
        self.say = Say(text=self.text)

    def tearDown(self):
        pass

    def testSay(self):
        """Test Say"""
        # construct object with mandatory attributes with example values
        # percl = freeclimb.percl.Say()  # noqa: E501
        self.assertTrue(isinstance(self.say, Say))
        self.assertEqual(self.text, self.say.get('Say').get('text'))
        self.assertTrue(hasattr(self.say, 'language'))
        self.assertTrue(hasattr(self.say, 'conference_id'))
        self.assertTrue(hasattr(self.say, 'loop'))
        self.assertTrue(hasattr(self.say, 'enforcePCI'))

    def testAddLanguage(self):
        """Add Language to conference"""
        language_code = 'ru-RU'
        self.say.language = language_code
        self.assertEqual(self.say.language, language_code)

if __name__ == '__main__':
    unittest.main()
