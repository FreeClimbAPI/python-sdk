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


class OutDial(object):
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
        'call_connect_url': 'str',
        'calling_number': 'float',
        'destination': 'float',
        'if_machine': 'str',
        'if_machine_url': 'str',
        'send_digits': 'str',
        'status_callback_url': 'str',
        'timeout': 'int',
        'privacy_mode': 'bool'
    }

    attribute_map = {
        'action_url': 'actionUrl',
        'call_connect_url': 'callConnectUrl',
        'calling_number': 'callingNumber',
        'destination': 'destination',
        'if_machine': 'ifMachine',
        'if_machine_url': 'ifMachineUrl',
        'send_digits': 'sendDigits',
        'status_callback_url': 'statusCallbackUrl',
        'timeout': 'timeout',
        'privacy_mode': 'privacyMode'
    }

    def __init__(self, action_url=None, call_connect_url=None, calling_number=None, destination=None, if_machine=None, if_machine_url=None, send_digits=None, status_callback_url=None, timeout=None, privacy_mode=None, local_vars_configuration=None):  # noqa: E501
        """OutDial - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action_url = None
        self._call_connect_url = None
        self._calling_number = None
        self._destination = None
        self._if_machine = None
        self._if_machine_url = None
        self._send_digits = None
        self._status_callback_url = None
        self._timeout = None
        self._privacy_mode = None
        self.discriminator = None

        self.action_url = action_url
        self.call_connect_url = call_connect_url
        self.calling_number = calling_number
        self.destination = destination
        if if_machine is not None:
            self.if_machine = if_machine
        if if_machine_url is not None:
            self.if_machine_url = if_machine_url
        if send_digits is not None:
            self.send_digits = send_digits
        if status_callback_url is not None:
            self.status_callback_url = status_callback_url
        if timeout is not None:
            self.timeout = timeout
        if privacy_mode is not None:
            self.privacy_mode = privacy_mode

    @property
    def action_url(self):
        """Gets the action_url of this OutDial.  # noqa: E501

        URL to which FreeClimb sends an HTTP POST request.   # noqa: E501

        :return: The action_url of this OutDial.  # noqa: E501
        :rtype: str
        """
        return self._action_url

    @action_url.setter
    def action_url(self, action_url):
        """Sets the action_url of this OutDial.

        URL to which FreeClimb sends an HTTP POST request.   # noqa: E501

        :param action_url: The action_url of this OutDial.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action_url is None:  # noqa: E501
            raise ValueError("Invalid value for `action_url`, must not be `None`")  # noqa: E501

        self._action_url = action_url

    @property
    def call_connect_url(self):
        """Gets the call_connect_url of this OutDial.  # noqa: E501

        URL to which FreeClimb makes an HTTP POST request informing the result of the OutDial.  # noqa: E501

        :return: The call_connect_url of this OutDial.  # noqa: E501
        :rtype: str
        """
        return self._call_connect_url

    @call_connect_url.setter
    def call_connect_url(self, call_connect_url):
        """Sets the call_connect_url of this OutDial.

        URL to which FreeClimb makes an HTTP POST request informing the result of the OutDial.  # noqa: E501

        :param call_connect_url: The call_connect_url of this OutDial.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and call_connect_url is None:  # noqa: E501
            raise ValueError("Invalid value for `call_connect_url`, must not be `None`")  # noqa: E501

        self._call_connect_url = call_connect_url

    @property
    def calling_number(self):
        """Gets the calling_number of this OutDial.  # noqa: E501

        he caller ID to show to the called party when FreeClimb calls. This can be one of the following: The To or From number provided in the first Webhook to your webserver. Any phone number you have purchased from FreeClimb.  # noqa: E501

        :return: The calling_number of this OutDial.  # noqa: E501
        :rtype: float
        """
        return self._calling_number

    @calling_number.setter
    def calling_number(self, calling_number):
        """Sets the calling_number of this OutDial.

        he caller ID to show to the called party when FreeClimb calls. This can be one of the following: The To or From number provided in the first Webhook to your webserver. Any phone number you have purchased from FreeClimb.  # noqa: E501

        :param calling_number: The calling_number of this OutDial.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and calling_number is None:  # noqa: E501
            raise ValueError("Invalid value for `calling_number`, must not be `None`")  # noqa: E501

        self._calling_number = calling_number

    @property
    def destination(self):
        """Gets the destination of this OutDial.  # noqa: E501

        E.164 representation of the phone number to Call.   # noqa: E501

        :return: The destination of this OutDial.  # noqa: E501
        :rtype: float
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this OutDial.

        E.164 representation of the phone number to Call.   # noqa: E501

        :param destination: The destination of this OutDial.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and destination is None:  # noqa: E501
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def if_machine(self):
        """Gets the if_machine of this OutDial.  # noqa: E501

        Specifies how FreeClimb should handle this OutDial if an answering machine answers the Call. Valid values: `redirect` invokes the ifMachineUrl for instructions. `hangup` hangs up the Call. The ifMachineUrl will not be invoked.  # noqa: E501

        :return: The if_machine of this OutDial.  # noqa: E501
        :rtype: str
        """
        return self._if_machine

    @if_machine.setter
    def if_machine(self, if_machine):
        """Sets the if_machine of this OutDial.

        Specifies how FreeClimb should handle this OutDial if an answering machine answers the Call. Valid values: `redirect` invokes the ifMachineUrl for instructions. `hangup` hangs up the Call. The ifMachineUrl will not be invoked.  # noqa: E501

        :param if_machine: The if_machine of this OutDial.  # noqa: E501
        :type: str
        """

        self._if_machine = if_machine

    @property
    def if_machine_url(self):
        """Gets the if_machine_url of this OutDial.  # noqa: E501

        When the `ifMachine` flag is set to `redirect`, this attribute specifies a URL to which FreeClimb makes a POST request when an answering machine or a fax machine is detected. This URL is required if the `ifMachine` flag is set to `redirect`. Otherwise, it should not be included.  # noqa: E501

        :return: The if_machine_url of this OutDial.  # noqa: E501
        :rtype: str
        """
        return self._if_machine_url

    @if_machine_url.setter
    def if_machine_url(self, if_machine_url):
        """Sets the if_machine_url of this OutDial.

        When the `ifMachine` flag is set to `redirect`, this attribute specifies a URL to which FreeClimb makes a POST request when an answering machine or a fax machine is detected. This URL is required if the `ifMachine` flag is set to `redirect`. Otherwise, it should not be included.  # noqa: E501

        :param if_machine_url: The if_machine_url of this OutDial.  # noqa: E501
        :type: str
        """

        self._if_machine_url = if_machine_url

    @property
    def send_digits(self):
        """Gets the send_digits of this OutDial.  # noqa: E501

        DTMF tones to play to the outdialed Call. This is typically used to dial a number and then dial an extension.  # noqa: E501

        :return: The send_digits of this OutDial.  # noqa: E501
        :rtype: str
        """
        return self._send_digits

    @send_digits.setter
    def send_digits(self, send_digits):
        """Sets the send_digits of this OutDial.

        DTMF tones to play to the outdialed Call. This is typically used to dial a number and then dial an extension.  # noqa: E501

        :param send_digits: The send_digits of this OutDial.  # noqa: E501
        :type: str
        """

        self._send_digits = send_digits

    @property
    def status_callback_url(self):
        """Gets the status_callback_url of this OutDial.  # noqa: E501

        When the outdialed Call leg terminates, FreeClimb sends a `callStatus` Webhook to the `statusCallbackUrl`. This is a notification only; any PerCL command returned is ignored.  # noqa: E501

        :return: The status_callback_url of this OutDial.  # noqa: E501
        :rtype: str
        """
        return self._status_callback_url

    @status_callback_url.setter
    def status_callback_url(self, status_callback_url):
        """Sets the status_callback_url of this OutDial.

        When the outdialed Call leg terminates, FreeClimb sends a `callStatus` Webhook to the `statusCallbackUrl`. This is a notification only; any PerCL command returned is ignored.  # noqa: E501

        :param status_callback_url: The status_callback_url of this OutDial.  # noqa: E501
        :type: str
        """

        self._status_callback_url = status_callback_url

    @property
    def timeout(self):
        """Gets the timeout of this OutDial.  # noqa: E501

        Maximum time in seconds the `OutDial` command waits for the called party to answer the Call. When a timeout occurs, FreeClimb invokes the `callConnectUrl` Webhook to report that the out-dialed Call has ended with a status of `noAnswer`.  # noqa: E501

        :return: The timeout of this OutDial.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this OutDial.

        Maximum time in seconds the `OutDial` command waits for the called party to answer the Call. When a timeout occurs, FreeClimb invokes the `callConnectUrl` Webhook to report that the out-dialed Call has ended with a status of `noAnswer`.  # noqa: E501

        :param timeout: The timeout of this OutDial.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def privacy_mode(self):
        """Gets the privacy_mode of this OutDial.  # noqa: E501

        Parameter `privacyMode` will not log the `text` as required by PCI compliance.  # noqa: E501

        :return: The privacy_mode of this OutDial.  # noqa: E501
        :rtype: bool
        """
        return self._privacy_mode

    @privacy_mode.setter
    def privacy_mode(self, privacy_mode):
        """Sets the privacy_mode of this OutDial.

        Parameter `privacyMode` will not log the `text` as required by PCI compliance.  # noqa: E501

        :param privacy_mode: The privacy_mode of this OutDial.  # noqa: E501
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
        if not isinstance(other, OutDial):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutDial):
            return True

        return self.to_dict() != other.to_dict()

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
