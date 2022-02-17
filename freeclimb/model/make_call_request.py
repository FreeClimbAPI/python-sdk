"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from freeclimb.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from freeclimb.exceptions import ApiAttributeError




class MakeCallRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            '_from': (str,),  # noqa: E501
            'to': (str,),  # noqa: E501
            'application_id': (str,),  # noqa: E501
            'send_digits': (str,),  # noqa: E501
            'if_machine': (str,),  # noqa: E501
            'if_machine_url': (str,),  # noqa: E501
            'timeout': (int,),  # noqa: E501
            'parent_call_id': (str,),  # noqa: E501
            'privacy_mode': (bool,),  # noqa: E501
            'call_connect_url': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        '_from': 'from',  # noqa: E501
        'to': 'to',  # noqa: E501
        'application_id': 'applicationId',  # noqa: E501
        'send_digits': 'sendDigits',  # noqa: E501
        'if_machine': 'ifMachine',  # noqa: E501
        'if_machine_url': 'ifMachineUrl',  # noqa: E501
        'timeout': 'timeout',  # noqa: E501
        'parent_call_id': 'parentCallId',  # noqa: E501
        'privacy_mode': 'privacyMode',  # noqa: E501
        'call_connect_url': 'callConnectUrl',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, _from, to, *args, **kwargs):  # noqa: E501
        """MakeCallRequest - a model defined in OpenAPI

        Args:
            _from (str): Phone number to use as the caller ID. This can be: (a) The To or From number provided in FreeClimb's initial request to your app or (b) Any incoming phone number you have purchased from FreeClimb.
            to (str): Phone number to place the Call to.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            application_id (str): Required if no `parentCallId` or `callConnectUrl` has been provided. ID of the application FreeClimb should use to handle this phone call. FreeClimb will use the `callConnectUrl` and `statusCallbackUrl` set on the application unless the `callConnectUrl` attribute is also provided with the request. In this case, the URL specified in that `callConnectUrl` attribute will be used as a replacement of the `callConnectUrl` originally assigned in the application. If the `callConnectUrl` is not set as either an attribute of the request or as part of the specified application, an error will be provided. The application’s voiceUrl parameter is not used for outbound calls.. [optional]  # noqa: E501
            send_digits (str): String of digits to dial after connecting to the number. It can include digits `0-9`, `*`, and `#`, and allows embedding a pause between the output of individual digits. The default pause is 500 milliseconds. So, a string such as *1234#* will be played in 2 seconds because of the 4 standard pauses implied within the string. A custom pause is specified by including a positive integer wrapped in curly braces: {n}. For more information, see **sendDigits examples** below.. [optional]  # noqa: E501
            if_machine (str): Specifies how FreeClimb should handle this Call if an answering machine answers it.. [optional]  # noqa: E501
            if_machine_url (str): This attribute specifies a URL to which FreeClimb will make a POST request when an answering machine or a fax machine is detected. This URL is required if the ifMachine flag is set to redirect. When ifMachine is set to hangup, ifMachineUrl must not be included in the request. For more information, see **ifMachineUrl example** below.. [optional]  # noqa: E501
            timeout (int): Number of seconds that FreeClimb should allow the phone to ring before assuming there is no answer. Default is 30 seconds. Maximum allowed ring-time is determined by the target phone's provider. Note that most providers limit ring-time to 120 seconds.. [optional]  # noqa: E501
            parent_call_id (str): Required if no `applicationId` or `callConnectUrl` has been provided. The ID of the parent Call in the case that this new Call is meant to be treated as a child of an existing Call. This attribute should be included when possible to reduce latency when adding child calls to Conferences containing the parent Call. A call can only be used as a parent once the call is in progress or as an inbound call that is still ringing. An outbound call is considered to be in progress once the `outdialConnect` or `outdialApiConnect` webhook is invoked. An inbound call is ringing when the inbound webhook is invoked. If a `callConnectUrl` attribute is also included with the `parentCallId` in the request, this URL will be used as a replacement of the `callConnectUrl` originally assigned in the parent call.. [optional]  # noqa: E501
            privacy_mode (bool): Activate privacy mode in order to obscure log data that can potentially expose private information.. [optional]  # noqa: E501
            call_connect_url (str): The URL that FreeClimb should use to handle this phone call. If an applicationId or parentCallId have already been provided, this callConnectUrl attribute will be used as a replacement of the callConnectUrl originally assigned in the application or parent call.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self._from = _from
        self.to = to
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, _from, to, *args, **kwargs):  # noqa: E501
        """MakeCallRequest - a model defined in OpenAPI

        Args:
            _from (str): Phone number to use as the caller ID. This can be: (a) The To or From number provided in FreeClimb's initial request to your app or (b) Any incoming phone number you have purchased from FreeClimb.
            to (str): Phone number to place the Call to.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            application_id (str): Required if no `parentCallId` or `callConnectUrl` has been provided. ID of the application FreeClimb should use to handle this phone call. FreeClimb will use the `callConnectUrl` and `statusCallbackUrl` set on the application unless the `callConnectUrl` attribute is also provided with the request. In this case, the URL specified in that `callConnectUrl` attribute will be used as a replacement of the `callConnectUrl` originally assigned in the application. If the `callConnectUrl` is not set as either an attribute of the request or as part of the specified application, an error will be provided. The application’s voiceUrl parameter is not used for outbound calls.. [optional]  # noqa: E501
            send_digits (str): String of digits to dial after connecting to the number. It can include digits `0-9`, `*`, and `#`, and allows embedding a pause between the output of individual digits. The default pause is 500 milliseconds. So, a string such as *1234#* will be played in 2 seconds because of the 4 standard pauses implied within the string. A custom pause is specified by including a positive integer wrapped in curly braces: {n}. For more information, see **sendDigits examples** below.. [optional]  # noqa: E501
            if_machine (str): Specifies how FreeClimb should handle this Call if an answering machine answers it.. [optional]  # noqa: E501
            if_machine_url (str): This attribute specifies a URL to which FreeClimb will make a POST request when an answering machine or a fax machine is detected. This URL is required if the ifMachine flag is set to redirect. When ifMachine is set to hangup, ifMachineUrl must not be included in the request. For more information, see **ifMachineUrl example** below.. [optional]  # noqa: E501
            timeout (int): Number of seconds that FreeClimb should allow the phone to ring before assuming there is no answer. Default is 30 seconds. Maximum allowed ring-time is determined by the target phone's provider. Note that most providers limit ring-time to 120 seconds.. [optional]  # noqa: E501
            parent_call_id (str): Required if no `applicationId` or `callConnectUrl` has been provided. The ID of the parent Call in the case that this new Call is meant to be treated as a child of an existing Call. This attribute should be included when possible to reduce latency when adding child calls to Conferences containing the parent Call. A call can only be used as a parent once the call is in progress or as an inbound call that is still ringing. An outbound call is considered to be in progress once the `outdialConnect` or `outdialApiConnect` webhook is invoked. An inbound call is ringing when the inbound webhook is invoked. If a `callConnectUrl` attribute is also included with the `parentCallId` in the request, this URL will be used as a replacement of the `callConnectUrl` originally assigned in the parent call.. [optional]  # noqa: E501
            privacy_mode (bool): Activate privacy mode in order to obscure log data that can potentially expose private information.. [optional]  # noqa: E501
            call_connect_url (str): The URL that FreeClimb should use to handle this phone call. If an applicationId or parentCallId have already been provided, this callConnectUrl attribute will be used as a replacement of the callConnectUrl originally assigned in the application or parent call.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self._from = _from
        self.to = to
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

