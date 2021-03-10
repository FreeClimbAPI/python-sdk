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


class MakeCallRequest(object):
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
        '_from': 'str',
        'to': 'str',
        'application_id': 'str',
        'send_digits': 'str',
        'if_machine': 'str',
        'if_machine_url': 'str',
        'timeout': 'int',
        'parent_call_id': 'str',
        'privacy_mode': 'bool',
        'call_connect_url': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'application_id': 'applicationId',
        'send_digits': 'sendDigits',
        'if_machine': 'ifMachine',
        'if_machine_url': 'ifMachineUrl',
        'timeout': 'timeout',
        'parent_call_id': 'parentCallId',
        'privacy_mode': 'privacyMode',
        'call_connect_url': 'callConnectUrl'
    }

    def __init__(self, _from=None, to=None, application_id=None, send_digits=None, if_machine=None, if_machine_url=None, timeout=None, parent_call_id=None, privacy_mode=None, call_connect_url=None, local_vars_configuration=None):  # noqa: E501
        """MakeCallRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__from = None
        self._to = None
        self._application_id = None
        self._send_digits = None
        self._if_machine = None
        self._if_machine_url = None
        self._timeout = None
        self._parent_call_id = None
        self._privacy_mode = None
        self._call_connect_url = None
        self.discriminator = None

        self._from = _from
        self.to = to
        if application_id is not None:
            self.application_id = application_id
        if send_digits is not None:
            self.send_digits = send_digits
        if if_machine is not None:
            self.if_machine = if_machine
        if if_machine_url is not None:
            self.if_machine_url = if_machine_url
        if timeout is not None:
            self.timeout = timeout
        if parent_call_id is not None:
            self.parent_call_id = parent_call_id
        if privacy_mode is not None:
            self.privacy_mode = privacy_mode
        if call_connect_url is not None:
            self.call_connect_url = call_connect_url

    @property
    def _from(self):
        """Gets the _from of this MakeCallRequest.  # noqa: E501

        Phone number to use as the caller ID. This can be: (a) The To or From number provided in FreeClimb's initial request to your app or (b) Any incoming phone number you have purchased from FreeClimb.  # noqa: E501

        :return: The _from of this MakeCallRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this MakeCallRequest.

        Phone number to use as the caller ID. This can be: (a) The To or From number provided in FreeClimb's initial request to your app or (b) Any incoming phone number you have purchased from FreeClimb.  # noqa: E501

        :param _from: The _from of this MakeCallRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this MakeCallRequest.  # noqa: E501

        Phone number to place the Call to.  # noqa: E501

        :return: The to of this MakeCallRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this MakeCallRequest.

        Phone number to place the Call to.  # noqa: E501

        :param to: The to of this MakeCallRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def application_id(self):
        """Gets the application_id of this MakeCallRequest.  # noqa: E501

        Required if no `parentCallId` or `callConnectUrl` has been provided. ID of the application FreeClimb should use to handle this phone call. FreeClimb will use the `callConnectUrl` and `statusCallbackUrl` set on the application unless the `callConnectUrl` attribute is also provided with the request. In this case, the URL specified in that `callConnectUrl` attribute will be used as a replacement of the `callConnectUrl` originally assigned in the application. If the `callConnectUrl` is not set as either an attribute of the request or as part of the specified application, an error will be provided. The application’s voiceUrl parameter is not used for outbound calls.  # noqa: E501

        :return: The application_id of this MakeCallRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this MakeCallRequest.

        Required if no `parentCallId` or `callConnectUrl` has been provided. ID of the application FreeClimb should use to handle this phone call. FreeClimb will use the `callConnectUrl` and `statusCallbackUrl` set on the application unless the `callConnectUrl` attribute is also provided with the request. In this case, the URL specified in that `callConnectUrl` attribute will be used as a replacement of the `callConnectUrl` originally assigned in the application. If the `callConnectUrl` is not set as either an attribute of the request or as part of the specified application, an error will be provided. The application’s voiceUrl parameter is not used for outbound calls.  # noqa: E501

        :param application_id: The application_id of this MakeCallRequest.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def send_digits(self):
        """Gets the send_digits of this MakeCallRequest.  # noqa: E501

        String of digits to dial after connecting to the number. It can include digits `0-9`, `*`, and `#`, and allows embedding a pause between the output of individual digits. The default pause is 500 milliseconds. So, a string such as *1234#* will be played in 2 seconds because of the 4 standard pauses implied within the string. A custom pause is specified by including a positive integer wrapped in curly braces: {n}. For more information, see **sendDigits examples** below.  # noqa: E501

        :return: The send_digits of this MakeCallRequest.  # noqa: E501
        :rtype: str
        """
        return self._send_digits

    @send_digits.setter
    def send_digits(self, send_digits):
        """Sets the send_digits of this MakeCallRequest.

        String of digits to dial after connecting to the number. It can include digits `0-9`, `*`, and `#`, and allows embedding a pause between the output of individual digits. The default pause is 500 milliseconds. So, a string such as *1234#* will be played in 2 seconds because of the 4 standard pauses implied within the string. A custom pause is specified by including a positive integer wrapped in curly braces: {n}. For more information, see **sendDigits examples** below.  # noqa: E501

        :param send_digits: The send_digits of this MakeCallRequest.  # noqa: E501
        :type: str
        """

        self._send_digits = send_digits

    @property
    def if_machine(self):
        """Gets the if_machine of this MakeCallRequest.  # noqa: E501

        Specifies how FreeClimb should handle this Call if an answering machine answers it.  # noqa: E501

        :return: The if_machine of this MakeCallRequest.  # noqa: E501
        :rtype: str
        """
        return self._if_machine

    @if_machine.setter
    def if_machine(self, if_machine):
        """Sets the if_machine of this MakeCallRequest.

        Specifies how FreeClimb should handle this Call if an answering machine answers it.  # noqa: E501

        :param if_machine: The if_machine of this MakeCallRequest.  # noqa: E501
        :type: str
        """

        self._if_machine = if_machine

    @property
    def if_machine_url(self):
        """Gets the if_machine_url of this MakeCallRequest.  # noqa: E501

        This attribute specifies a URL to which FreeClimb will make a POST request when an answering machine or a fax machine is detected. This URL is required if the ifMachine flag is set to redirect. When ifMachine is set to hangup, ifMachineUrl must not be included in the request. For more information, see **ifMachineUrl example** below.  # noqa: E501

        :return: The if_machine_url of this MakeCallRequest.  # noqa: E501
        :rtype: str
        """
        return self._if_machine_url

    @if_machine_url.setter
    def if_machine_url(self, if_machine_url):
        """Sets the if_machine_url of this MakeCallRequest.

        This attribute specifies a URL to which FreeClimb will make a POST request when an answering machine or a fax machine is detected. This URL is required if the ifMachine flag is set to redirect. When ifMachine is set to hangup, ifMachineUrl must not be included in the request. For more information, see **ifMachineUrl example** below.  # noqa: E501

        :param if_machine_url: The if_machine_url of this MakeCallRequest.  # noqa: E501
        :type: str
        """

        self._if_machine_url = if_machine_url

    @property
    def timeout(self):
        """Gets the timeout of this MakeCallRequest.  # noqa: E501

        Number of seconds that FreeClimb should allow the phone to ring before assuming there is no answer. Default is 30 seconds. Maximum allowed ring-time is determined by the target phone's provider. Note that most providers limit ring-time to 120 seconds.  # noqa: E501

        :return: The timeout of this MakeCallRequest.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this MakeCallRequest.

        Number of seconds that FreeClimb should allow the phone to ring before assuming there is no answer. Default is 30 seconds. Maximum allowed ring-time is determined by the target phone's provider. Note that most providers limit ring-time to 120 seconds.  # noqa: E501

        :param timeout: The timeout of this MakeCallRequest.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def parent_call_id(self):
        """Gets the parent_call_id of this MakeCallRequest.  # noqa: E501

        Required if no `applicationId` or `callConnectUrl` has been provided. The ID of the parent Call in the case that this new Call is meant to be treated as a child of an existing Call. This attribute should be included when possible to reduce latency when adding child calls to Conferences containing the parent Call. A call can only be used as a parent once the call is in progress or as an inbound call that is still ringing. An outbound call is considered to be in progress once the `outdialConnect` or `outdialApiConnect` webhook is invoked. An inbound call is ringing when the inbound webhook is invoked. If a `callConnectUrl` attribute is also included with the `parentCallId` in the request, this URL will be used as a replacement of the `callConnectUrl` originally assigned in the parent call.  # noqa: E501

        :return: The parent_call_id of this MakeCallRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_call_id

    @parent_call_id.setter
    def parent_call_id(self, parent_call_id):
        """Sets the parent_call_id of this MakeCallRequest.

        Required if no `applicationId` or `callConnectUrl` has been provided. The ID of the parent Call in the case that this new Call is meant to be treated as a child of an existing Call. This attribute should be included when possible to reduce latency when adding child calls to Conferences containing the parent Call. A call can only be used as a parent once the call is in progress or as an inbound call that is still ringing. An outbound call is considered to be in progress once the `outdialConnect` or `outdialApiConnect` webhook is invoked. An inbound call is ringing when the inbound webhook is invoked. If a `callConnectUrl` attribute is also included with the `parentCallId` in the request, this URL will be used as a replacement of the `callConnectUrl` originally assigned in the parent call.  # noqa: E501

        :param parent_call_id: The parent_call_id of this MakeCallRequest.  # noqa: E501
        :type: str
        """

        self._parent_call_id = parent_call_id

    @property
    def privacy_mode(self):
        """Gets the privacy_mode of this MakeCallRequest.  # noqa: E501

        Activate privacy mode in order to obscure log data that can potentially expose private information.  # noqa: E501

        :return: The privacy_mode of this MakeCallRequest.  # noqa: E501
        :rtype: bool
        """
        return self._privacy_mode

    @privacy_mode.setter
    def privacy_mode(self, privacy_mode):
        """Sets the privacy_mode of this MakeCallRequest.

        Activate privacy mode in order to obscure log data that can potentially expose private information.  # noqa: E501

        :param privacy_mode: The privacy_mode of this MakeCallRequest.  # noqa: E501
        :type: bool
        """

        self._privacy_mode = privacy_mode

    @property
    def call_connect_url(self):
        """Gets the call_connect_url of this MakeCallRequest.  # noqa: E501

        The URL that FreeClimb should use to handle this phone call. If an applicationId or parentCallId have already been provided, this callConnectUrl attribute will be used as a replacement of the callConnectUrl originally assigned in the application or parent call.  # noqa: E501

        :return: The call_connect_url of this MakeCallRequest.  # noqa: E501
        :rtype: str
        """
        return self._call_connect_url

    @call_connect_url.setter
    def call_connect_url(self, call_connect_url):
        """Sets the call_connect_url of this MakeCallRequest.

        The URL that FreeClimb should use to handle this phone call. If an applicationId or parentCallId have already been provided, this callConnectUrl attribute will be used as a replacement of the callConnectUrl originally assigned in the application or parent call.  # noqa: E501

        :param call_connect_url: The call_connect_url of this MakeCallRequest.  # noqa: E501
        :type: str
        """

        self._call_connect_url = call_connect_url

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
        if not isinstance(other, MakeCallRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MakeCallRequest):
            return True

        return self.to_dict() != other.to_dict()

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
