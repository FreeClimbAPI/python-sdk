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


class GetDigitsAllOf(object):
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
        'action_url': 'str',
        'digit_timeout_ms': 'int',
        'finish_on_key': 'str',
        'flush_buffer': 'bool',
        'initial_timeout_ms': 'str',
        'max_digits': 'int',
        'min_digits': 'int',
        'prompts': 'list[PerclCommand]',
        'privacy_mode': 'bool'
    }

    attribute_map = {
        'action_url': 'actionUrl',
        'digit_timeout_ms': 'digitTimeoutMs',
        'finish_on_key': 'finishOnKey',
        'flush_buffer': 'flushBuffer',
        'initial_timeout_ms': 'initialTimeoutMs',
        'max_digits': 'maxDigits',
        'min_digits': 'minDigits',
        'prompts': 'prompts',
        'privacy_mode': 'privacyMode'
    }

    def __init__(self, action_url=None, digit_timeout_ms=None, finish_on_key=None, flush_buffer=None, initial_timeout_ms=None, max_digits=None, min_digits=None, prompts=None, privacy_mode=None, local_vars_configuration=None):  # noqa: E501
        """GetDigitsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action_url = None
        self._digit_timeout_ms = None
        self._finish_on_key = None
        self._flush_buffer = None
        self._initial_timeout_ms = None
        self._max_digits = None
        self._min_digits = None
        self._prompts = None
        self._privacy_mode = None
        self.discriminator = None

        self.action_url = action_url
        if digit_timeout_ms is not None:
            self.digit_timeout_ms = digit_timeout_ms
        if finish_on_key is not None:
            self.finish_on_key = finish_on_key
        if flush_buffer is not None:
            self.flush_buffer = flush_buffer
        if initial_timeout_ms is not None:
            self.initial_timeout_ms = initial_timeout_ms
        if max_digits is not None:
            self.max_digits = max_digits
        if min_digits is not None:
            self.min_digits = min_digits
        if prompts is not None:
            self.prompts = prompts
        if privacy_mode is not None:
            self.privacy_mode = privacy_mode

    @property
    def action_url(self):
        """Gets the action_url of this GetDigitsAllOf.  # noqa: E501

        When the Caller has finished entering digits, FreeClimb will make an HTTP POST request to this URL. A PerCL response is expected to continue handling the Call. Make sure to keep “http://“ in the URL.  # noqa: E501

        :return: The action_url of this GetDigitsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._action_url

    @action_url.setter
    def action_url(self, action_url):
        """Sets the action_url of this GetDigitsAllOf.

        When the Caller has finished entering digits, FreeClimb will make an HTTP POST request to this URL. A PerCL response is expected to continue handling the Call. Make sure to keep “http://“ in the URL.  # noqa: E501

        :param action_url: The action_url of this GetDigitsAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action_url is None:  # noqa: E501
            raise ValueError("Invalid value for `action_url`, must not be `None`")  # noqa: E501

        self._action_url = action_url

    @property
    def digit_timeout_ms(self):
        """Gets the digit_timeout_ms of this GetDigitsAllOf.  # noqa: E501

         Maximum time in milliseconds that FreeClimb will wait for the Caller to press any digit after the last digit entered, before making a determination that a `timeout` has occurred and moving on to make the request to the actionUrl to submit the results of the `GetDigits` command. This timeout interval begins and resets after each digit entered.  # noqa: E501

        :return: The digit_timeout_ms of this GetDigitsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._digit_timeout_ms

    @digit_timeout_ms.setter
    def digit_timeout_ms(self, digit_timeout_ms):
        """Sets the digit_timeout_ms of this GetDigitsAllOf.

         Maximum time in milliseconds that FreeClimb will wait for the Caller to press any digit after the last digit entered, before making a determination that a `timeout` has occurred and moving on to make the request to the actionUrl to submit the results of the `GetDigits` command. This timeout interval begins and resets after each digit entered.  # noqa: E501

        :param digit_timeout_ms: The digit_timeout_ms of this GetDigitsAllOf.  # noqa: E501
        :type: int
        """

        self._digit_timeout_ms = digit_timeout_ms

    @property
    def finish_on_key(self):
        """Gets the finish_on_key of this GetDigitsAllOf.  # noqa: E501

        Digit that causes the input sequence to be deemed complete. This attribute defers to the `timeout` attribute – so, if a `timeout` occurs, then the command terminates regardless of the value of `finishOnKey`.  # noqa: E501

        :return: The finish_on_key of this GetDigitsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._finish_on_key

    @finish_on_key.setter
    def finish_on_key(self, finish_on_key):
        """Sets the finish_on_key of this GetDigitsAllOf.

        Digit that causes the input sequence to be deemed complete. This attribute defers to the `timeout` attribute – so, if a `timeout` occurs, then the command terminates regardless of the value of `finishOnKey`.  # noqa: E501

        :param finish_on_key: The finish_on_key of this GetDigitsAllOf.  # noqa: E501
        :type: str
        """

        self._finish_on_key = finish_on_key

    @property
    def flush_buffer(self):
        """Gets the flush_buffer of this GetDigitsAllOf.  # noqa: E501

        If set to true, the FreeClimb platform starts with an empty DTMF buffer to store the digits entered by the caller. If set to false, FreeClimb will append the user inputs to the end of the existing digits buffer and will return digits from the start of the digits buffer.  # noqa: E501

        :return: The flush_buffer of this GetDigitsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._flush_buffer

    @flush_buffer.setter
    def flush_buffer(self, flush_buffer):
        """Sets the flush_buffer of this GetDigitsAllOf.

        If set to true, the FreeClimb platform starts with an empty DTMF buffer to store the digits entered by the caller. If set to false, FreeClimb will append the user inputs to the end of the existing digits buffer and will return digits from the start of the digits buffer.  # noqa: E501

        :param flush_buffer: The flush_buffer of this GetDigitsAllOf.  # noqa: E501
        :type: bool
        """

        self._flush_buffer = flush_buffer

    @property
    def initial_timeout_ms(self):
        """Gets the initial_timeout_ms of this GetDigitsAllOf.  # noqa: E501

        Maximum time in milliseconds that FreeClimb will wait for the Caller to press the first digit before making a determination that a `timeout` has occurred and moving on to make the request to the `actionUrl` to submit the results of the `GetDigits` command. This timeout interval begins when all nested commands have been fully executed.  # noqa: E501

        :return: The initial_timeout_ms of this GetDigitsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._initial_timeout_ms

    @initial_timeout_ms.setter
    def initial_timeout_ms(self, initial_timeout_ms):
        """Sets the initial_timeout_ms of this GetDigitsAllOf.

        Maximum time in milliseconds that FreeClimb will wait for the Caller to press the first digit before making a determination that a `timeout` has occurred and moving on to make the request to the `actionUrl` to submit the results of the `GetDigits` command. This timeout interval begins when all nested commands have been fully executed.  # noqa: E501

        :param initial_timeout_ms: The initial_timeout_ms of this GetDigitsAllOf.  # noqa: E501
        :type: str
        """

        self._initial_timeout_ms = initial_timeout_ms

    @property
    def max_digits(self):
        """Gets the max_digits of this GetDigitsAllOf.  # noqa: E501

        Maximum number of digits expected in the input. If the terminating digit is not entered and the caller has entered the maximum number of digits allowed, the `GetDigits` command terminates regardless of the value of `finishOnKey`.  # noqa: E501

        :return: The max_digits of this GetDigitsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._max_digits

    @max_digits.setter
    def max_digits(self, max_digits):
        """Sets the max_digits of this GetDigitsAllOf.

        Maximum number of digits expected in the input. If the terminating digit is not entered and the caller has entered the maximum number of digits allowed, the `GetDigits` command terminates regardless of the value of `finishOnKey`.  # noqa: E501

        :param max_digits: The max_digits of this GetDigitsAllOf.  # noqa: E501
        :type: int
        """

        self._max_digits = max_digits

    @property
    def min_digits(self):
        """Gets the min_digits of this GetDigitsAllOf.  # noqa: E501

        Minimum number of digits expected in the input. If specified, FreeClimb will return the collected digits only if the Caller has entered at least that many digits.  # noqa: E501

        :return: The min_digits of this GetDigitsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._min_digits

    @min_digits.setter
    def min_digits(self, min_digits):
        """Sets the min_digits of this GetDigitsAllOf.

        Minimum number of digits expected in the input. If specified, FreeClimb will return the collected digits only if the Caller has entered at least that many digits.  # noqa: E501

        :param min_digits: The min_digits of this GetDigitsAllOf.  # noqa: E501
        :type: int
        """

        self._min_digits = min_digits

    @property
    def prompts(self):
        """Gets the prompts of this GetDigitsAllOf.  # noqa: E501

        JSON array of PerCL commands to nest within the `GetDigits` command. The `Say`, `Play`, and `Pause` commands can be used. The nested actions are executed while FreeClimb is waiting for input from the Caller.  # noqa: E501

        :return: The prompts of this GetDigitsAllOf.  # noqa: E501
        :rtype: list[PerclCommand]
        """
        return self._prompts

    @prompts.setter
    def prompts(self, prompts):
        """Sets the prompts of this GetDigitsAllOf.

        JSON array of PerCL commands to nest within the `GetDigits` command. The `Say`, `Play`, and `Pause` commands can be used. The nested actions are executed while FreeClimb is waiting for input from the Caller.  # noqa: E501

        :param prompts: The prompts of this GetDigitsAllOf.  # noqa: E501
        :type: list[PerclCommand]
        """

        self._prompts = prompts

    @property
    def privacy_mode(self):
        """Gets the privacy_mode of this GetDigitsAllOf.  # noqa: E501

        Parameter `privacyMode` will not log the `text` as required by PCI compliance.  # noqa: E501

        :return: The privacy_mode of this GetDigitsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._privacy_mode

    @privacy_mode.setter
    def privacy_mode(self, privacy_mode):
        """Sets the privacy_mode of this GetDigitsAllOf.

        Parameter `privacyMode` will not log the `text` as required by PCI compliance.  # noqa: E501

        :param privacy_mode: The privacy_mode of this GetDigitsAllOf.  # noqa: E501
        :type: bool
        """

        self._privacy_mode = privacy_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.to_camel_case(attr)
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
            elif value is None:
                continue
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
        if not isinstance(other, GetDigitsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDigitsAllOf):
            return True

        return self.to_dict() != other.to_dict()

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
