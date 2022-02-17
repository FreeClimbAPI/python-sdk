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



def lazy_import():
    from freeclimb.model.get_speech_all_of import GetSpeechAllOf
    from freeclimb.model.percl_command import PerclCommand
    globals()['GetSpeechAllOf'] = GetSpeechAllOf
    globals()['PerclCommand'] = PerclCommand


from freeclimb.model.percl_command import PerclCommand

class GetSpeech(PerclCommand):
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
        lazy_import()
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
        lazy_import()
        return {
            'action_url': (str,),  # noqa: E501
            'grammar_file': (str,),  # noqa: E501
            'grammar_type': (int,),  # noqa: E501
            'grammar_rule': (bool,),  # noqa: E501
            'play_beep': (str,),  # noqa: E501
            'prompts': ([PerclCommand],),  # noqa: E501
            'no_input_timeout_ms': (int,),  # noqa: E501
            'recognition_timeout_ms': (int,),  # noqa: E501
            'confidence_threshold': (float,),  # noqa: E501
            'sensitivity_level': (float,),  # noqa: E501
            'speech_complete_timeout_ms': (int,),  # noqa: E501
            'speech_incomplete_timeout_ms': (int,),  # noqa: E501
            'privacy_mode': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action_url': 'actionUrl',  # noqa: E501
        'grammar_file': 'grammarFile',  # noqa: E501
        'grammar_type': 'grammarType',  # noqa: E501
        'grammar_rule': 'grammarRule',  # noqa: E501
        'play_beep': 'playBeep',  # noqa: E501
        'prompts': 'prompts',  # noqa: E501
        'no_input_timeout_ms': 'noInputTimeoutMs',  # noqa: E501
        'recognition_timeout_ms': 'recognitionTimeoutMs',  # noqa: E501
        'confidence_threshold': 'confidenceThreshold',  # noqa: E501
        'sensitivity_level': 'sensitivityLevel',  # noqa: E501
        'speech_complete_timeout_ms': 'speechCompleteTimeoutMs',  # noqa: E501
        'speech_incomplete_timeout_ms': 'speechIncompleteTimeoutMs',  # noqa: E501
        'privacy_mode': 'privacyMode',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """GetSpeech - a model defined in OpenAPI

        Keyword Args:
            action_url (str): When the caller has finished speaking or the command has timed out, FreeClimb will make a POST request to this URL. A PerCL response is expected to continue handling the call.
            grammar_file (str): The grammar file to use for speech recognition. If grammarType is set to URL, this attribute is specified as a download URL.
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
            grammar_type (int): The grammar file type to use for speech recognition. A value of 'URL' indicates the grammarFile attribute specifies a URL that points to the grammar file. A value of `BUILTIN` indicates the grammarFile attribute specifies the name of one of the platform built-in grammar files.. [optional]  # noqa: E501
            grammar_rule (bool): The grammar rule within the specified grammar file to use for speech recognition. This attribute is optional if `grammarType` is `URL` and ignored if `grammarType` is `BUILTIN`.. [optional]  # noqa: E501
            play_beep (str): Indicates whether a beep should be played just before speech recognition is initiated so that the speaker can start to speak.. [optional]  # noqa: E501
            prompts ([PerclCommand]): The JSON array of PerCL commands to nest within the `GetSpeech` command. The `Say`, `Play`, and `Pause` commands can be used. The nested actions are executed while FreeClimb is waiting for input from the caller. This allows for playing menu options to the caller and to prompt for the expected input. These commands stop executing when the caller begins to input speech.. [optional]  # noqa: E501
            no_input_timeout_ms (int): When recognition is started and there is no speech detected for `noInputTimeoutMs` milliseconds, the recognizer will terminate the recognition operation.. [optional]  # noqa: E501
            recognition_timeout_ms (int): When playback of prompts ends and there is no match for `recognitionTimeoutMs` milliseconds, the recognizer will terminate the recognition operation.. [optional]  # noqa: E501
            confidence_threshold (float): When a recognition resource recognizes a spoken phrase, it associates a confidence level with that match. Parameter `confidenceThreshold` specifies what confidence level is considered a successful match. Values are between 0.0 and 1.0.. [optional]  # noqa: E501
            sensitivity_level (float): The speech recognizer supports a variable level of sound sensitivity. The sensitivityLevel attribute allows for filtering out background noise, so it is not mistaken for speech. Values are between 0.0 and 1.0 . [optional]  # noqa: E501
            speech_complete_timeout_ms (int): Parameter `speechCompleteTimeoutMs` specifies the length of silence required following user speech before the speech recognizer finalizes a result. This timeout applies when the recognizer currently has a complete match against an active grammar. Reasonable speech complete timeout values are typically in the range of 0.3 seconds to 1.0 seconds.. [optional]  # noqa: E501
            speech_incomplete_timeout_ms (int): Parameter `speechIncompleteTimeoutMs` specifies the length of silence following user speech after which a recognizer finalizes a result. This timeout applies when the speech prior to the silence is an incomplete match of all active grammars. Timeout `speechIncompleteTimeoutMs` is usually longer than `speechCompleteTimeoutMs` to allow users to pause mid-utterance.. [optional]  # noqa: E501
            privacy_mode (bool): Parameter privacyMode will not log the `text` as required by PCI compliance.. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """GetSpeech - a model defined in OpenAPI

        Keyword Args:
            action_url (str): When the caller has finished speaking or the command has timed out, FreeClimb will make a POST request to this URL. A PerCL response is expected to continue handling the call.
            grammar_file (str): The grammar file to use for speech recognition. If grammarType is set to URL, this attribute is specified as a download URL.
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
            grammar_type (int): The grammar file type to use for speech recognition. A value of 'URL' indicates the grammarFile attribute specifies a URL that points to the grammar file. A value of `BUILTIN` indicates the grammarFile attribute specifies the name of one of the platform built-in grammar files.. [optional]  # noqa: E501
            grammar_rule (bool): The grammar rule within the specified grammar file to use for speech recognition. This attribute is optional if `grammarType` is `URL` and ignored if `grammarType` is `BUILTIN`.. [optional]  # noqa: E501
            play_beep (str): Indicates whether a beep should be played just before speech recognition is initiated so that the speaker can start to speak.. [optional]  # noqa: E501
            prompts ([PerclCommand]): The JSON array of PerCL commands to nest within the `GetSpeech` command. The `Say`, `Play`, and `Pause` commands can be used. The nested actions are executed while FreeClimb is waiting for input from the caller. This allows for playing menu options to the caller and to prompt for the expected input. These commands stop executing when the caller begins to input speech.. [optional]  # noqa: E501
            no_input_timeout_ms (int): When recognition is started and there is no speech detected for `noInputTimeoutMs` milliseconds, the recognizer will terminate the recognition operation.. [optional]  # noqa: E501
            recognition_timeout_ms (int): When playback of prompts ends and there is no match for `recognitionTimeoutMs` milliseconds, the recognizer will terminate the recognition operation.. [optional]  # noqa: E501
            confidence_threshold (float): When a recognition resource recognizes a spoken phrase, it associates a confidence level with that match. Parameter `confidenceThreshold` specifies what confidence level is considered a successful match. Values are between 0.0 and 1.0.. [optional]  # noqa: E501
            sensitivity_level (float): The speech recognizer supports a variable level of sound sensitivity. The sensitivityLevel attribute allows for filtering out background noise, so it is not mistaken for speech. Values are between 0.0 and 1.0 . [optional]  # noqa: E501
            speech_complete_timeout_ms (int): Parameter `speechCompleteTimeoutMs` specifies the length of silence required following user speech before the speech recognizer finalizes a result. This timeout applies when the recognizer currently has a complete match against an active grammar. Reasonable speech complete timeout values are typically in the range of 0.3 seconds to 1.0 seconds.. [optional]  # noqa: E501
            speech_incomplete_timeout_ms (int): Parameter `speechIncompleteTimeoutMs` specifies the length of silence following user speech after which a recognizer finalizes a result. This timeout applies when the speech prior to the silence is an incomplete match of all active grammars. Timeout `speechIncompleteTimeoutMs` is usually longer than `speechCompleteTimeoutMs` to allow users to pause mid-utterance.. [optional]  # noqa: E501
            privacy_mode (bool): Parameter privacyMode will not log the `text` as required by PCI compliance.. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              GetSpeechAllOf,
              PerclCommand,
          ],
          'oneOf': [
          ],
        }

    def to_percl_dict(self):
        command = self.command_name()
        attributes = self.openapi_types
        attribute_map = {}
        for attribute in attributes:
            val = self.get(attribute)
            if val is None:
                continue
            if isinstance(val, PerclCommand):
                attribute_map[attribute] = val.to_percl_dict()
                continue
            if isinstance(val, list):
                attribute_map[attribute] = [item.to_percl_dict() if isinstance(item, PerclCommand) else item for item in val]
                continue
            attribute_map[attribute] = val 
        percl_dict = {
            command: attribute_map
        }
        return percl_dict