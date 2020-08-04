# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from freeclimb.configuration import Configuration


class CreateConferenceRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'alias': 'str',
        'play_beep': 'str',
        'record': 'bool',
        'wait_url': 'str',
        'status_callback_url': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'play_beep': 'playBeep',
        'record': 'record',
        'wait_url': 'waitUrl',
        'status_callback_url': 'statusCallbackUrl'
    }

    def __init__(self, alias=None, play_beep='always', record=None, wait_url=None, status_callback_url=None, local_vars_configuration=None):  # noqa: E501
        """CreateConferenceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alias = None
        self._play_beep = None
        self._record = None
        self._wait_url = None
        self._status_callback_url = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if play_beep is not None:
            self.play_beep = play_beep
        if record is not None:
            self.record = record
        if wait_url is not None:
            self.wait_url = wait_url
        if status_callback_url is not None:
            self.status_callback_url = status_callback_url

    @property
    def alias(self):
        """Gets the alias of this CreateConferenceRequest.  # noqa: E501

        A description for this Conference. Maximum 64 characters.  # noqa: E501

        :return: The alias of this CreateConferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CreateConferenceRequest.

        A description for this Conference. Maximum 64 characters.  # noqa: E501

        :param alias: The alias of this CreateConferenceRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def play_beep(self):
        """Gets the play_beep of this CreateConferenceRequest.  # noqa: E501

        Controls when a beep is played. Valid values: `always`, `never`, `entryOnly`, `exitOnly`.  # noqa: E501

        :return: The play_beep of this CreateConferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._play_beep

    @play_beep.setter
    def play_beep(self, play_beep):
        """Sets the play_beep of this CreateConferenceRequest.

        Controls when a beep is played. Valid values: `always`, `never`, `entryOnly`, `exitOnly`.  # noqa: E501

        :param play_beep: The play_beep of this CreateConferenceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["always", "never", "entryOnly", "exitOnly"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and play_beep not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `play_beep` ({0}), must be one of {1}"  # noqa: E501
                .format(play_beep, allowed_values)
            )

        self._play_beep = play_beep

    @property
    def record(self):
        """Gets the record of this CreateConferenceRequest.  # noqa: E501

        Setting to `true` records the entire Conference.  # noqa: E501

        :return: The record of this CreateConferenceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this CreateConferenceRequest.

        Setting to `true` records the entire Conference.  # noqa: E501

        :param record: The record of this CreateConferenceRequest.  # noqa: E501
        :type: bool
        """

        self._record = record

    @property
    def wait_url(self):
        """Gets the wait_url of this CreateConferenceRequest.  # noqa: E501

        If specified, a URL for the audio file that provides custom hold music for the Conference when it is in the populated state. Otherwise, FreeClimb uses a system default audio file. This is always fetched using HTTP GET and is fetched just once &mdash; when the Conference is created.  # noqa: E501

        :return: The wait_url of this CreateConferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._wait_url

    @wait_url.setter
    def wait_url(self, wait_url):
        """Sets the wait_url of this CreateConferenceRequest.

        If specified, a URL for the audio file that provides custom hold music for the Conference when it is in the populated state. Otherwise, FreeClimb uses a system default audio file. This is always fetched using HTTP GET and is fetched just once &mdash; when the Conference is created.  # noqa: E501

        :param wait_url: The wait_url of this CreateConferenceRequest.  # noqa: E501
        :type: str
        """

        self._wait_url = wait_url

    @property
    def status_callback_url(self):
        """Gets the status_callback_url of this CreateConferenceRequest.  # noqa: E501

        This URL is invoked when the status of the Conference changes. For more information, see **statusCallbackUrl** (below).  # noqa: E501

        :return: The status_callback_url of this CreateConferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._status_callback_url

    @status_callback_url.setter
    def status_callback_url(self, status_callback_url):
        """Sets the status_callback_url of this CreateConferenceRequest.

        This URL is invoked when the status of the Conference changes. For more information, see **statusCallbackUrl** (below).  # noqa: E501

        :param status_callback_url: The status_callback_url of this CreateConferenceRequest.  # noqa: E501
        :type: str
        """

        self._status_callback_url = status_callback_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateConferenceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateConferenceRequest):
            return True

        return self.to_dict() != other.to_dict()
