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
    OpenApiModel,
)
from freeclimb.exceptions import ApiAttributeError


def lazy_import():
    from freeclimb.model.message_result_all_of import MessageResultAllOf
    from freeclimb.model.message_status import MessageStatus
    from freeclimb.model.mutable_resource_model import MutableResourceModel

    globals()["MessageResultAllOf"] = MessageResultAllOf
    globals()["MessageStatus"] = MessageStatus
    globals()["MutableResourceModel"] = MutableResourceModel


class MessageResult(ModelComposed):
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

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

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
            "uri": (str,),  # noqa: E501
            "date_created": (str,),  # noqa: E501
            "date_updated": (str,),  # noqa: E501
            "revision": (int,),  # noqa: E501
            "account_id": (
                str,
                none_type,
            ),  # noqa: E501
            "message_id": (
                str,
                none_type,
            ),  # noqa: E501
            "status": (MessageStatus,),  # noqa: E501
            "_from": (
                str,
                none_type,
            ),  # noqa: E501
            "to": (
                str,
                none_type,
            ),  # noqa: E501
            "text": (
                str,
                none_type,
            ),  # noqa: E501
            "direction": (
                str,
                none_type,
            ),  # noqa: E501
            "notification_url": (
                str,
                none_type,
            ),  # noqa: E501
            "brand_id": (
                str,
                none_type,
            ),  # noqa: E501
            "campaign_id": (
                str,
                none_type,
            ),  # noqa: E501
            "segment_count": (
                float,
                none_type,
            ),  # noqa: E501
            "media_urls": (
                [str],
                none_type,
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "uri": "uri",  # noqa: E501
        "date_created": "dateCreated",  # noqa: E501
        "date_updated": "dateUpdated",  # noqa: E501
        "revision": "revision",  # noqa: E501
        "account_id": "accountId",  # noqa: E501
        "message_id": "messageId",  # noqa: E501
        "status": "status",  # noqa: E501
        "_from": "from",  # noqa: E501
        "to": "to",  # noqa: E501
        "text": "text",  # noqa: E501
        "direction": "direction",  # noqa: E501
        "notification_url": "notificationUrl",  # noqa: E501
        "brand_id": "brandId",  # noqa: E501
        "campaign_id": "campaignId",  # noqa: E501
        "segment_count": "segmentCount",  # noqa: E501
        "media_urls": "mediaUrls",  # noqa: E501
    }

    read_only_vars = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """MessageResult - a model defined in OpenAPI

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
            uri (str): The URI for this resource, relative to /apiserver.. [optional]  # noqa: E501
            date_created (str): The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).. [optional]  # noqa: E501
            date_updated (str): The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).. [optional]  # noqa: E501
            revision (int): Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.. [optional]  # noqa: E501
            account_id (str, none_type): String that uniquely identifies this account resource.. [optional]  # noqa: E501
            message_id (str, none_type): String that uniquely identifies this message resource. [optional]  # noqa: E501
            status (MessageStatus): [optional]  # noqa: E501
            _from (str, none_type): Phone number in E.164 format that sent the message.. [optional]  # noqa: E501
            to (str, none_type): Phone number in E.164 format that received the message.. [optional]  # noqa: E501
            text (str, none_type): Message contents. [optional]  # noqa: E501
            direction (str, none_type): Noting whether the message was inbound or outbound. [optional]  # noqa: E501
            notification_url (str, none_type): URL invoked when message sent. [optional]  # noqa: E501
            brand_id (str, none_type): The unique identifier for the brand associated with the message. [optional]  # noqa: E501
            campaign_id (str, none_type): The unique identifier for the campaign associated with the message. [optional]  # noqa: E501
            segment_count (float, none_type): The number of segments into which the message was split. [optional]  # noqa: E501
            media_urls ([str], none_type): an array of HTTP URLs which were attached this this message. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
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
            "_check_type": _check_type,
            "_path_to_item": _path_to_item,
            "_spec_property_naming": _spec_property_naming,
            "_configuration": _configuration,
            "_visited_composed_classes": self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if (
                var_name in discarded_args
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self._additional_properties_model_instances
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
            "_composed_instances",
            "_var_name_to_model_instances",
            "_additional_properties_model_instances",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """MessageResult - a model defined in OpenAPI

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
            uri (str): The URI for this resource, relative to /apiserver.. [optional]  # noqa: E501
            date_created (str): The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).. [optional]  # noqa: E501
            date_updated (str): The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).. [optional]  # noqa: E501
            revision (int): Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.. [optional]  # noqa: E501
            account_id (str, none_type): String that uniquely identifies this account resource.. [optional]  # noqa: E501
            message_id (str, none_type): String that uniquely identifies this message resource. [optional]  # noqa: E501
            status (MessageStatus): [optional]  # noqa: E501
            _from (str, none_type): Phone number in E.164 format that sent the message.. [optional]  # noqa: E501
            to (str, none_type): Phone number in E.164 format that received the message.. [optional]  # noqa: E501
            text (str, none_type): Message contents. [optional]  # noqa: E501
            direction (str, none_type): Noting whether the message was inbound or outbound. [optional]  # noqa: E501
            notification_url (str, none_type): URL invoked when message sent. [optional]  # noqa: E501
            brand_id (str, none_type): The unique identifier for the brand associated with the message. [optional]  # noqa: E501
            campaign_id (str, none_type): The unique identifier for the campaign associated with the message. [optional]  # noqa: E501
            segment_count (float, none_type): The number of segments into which the message was split. [optional]  # noqa: E501
            media_urls ([str], none_type): an array of HTTP URLs which were attached this this message. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
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
            "_check_type": _check_type,
            "_path_to_item": _path_to_item,
            "_spec_property_naming": _spec_property_naming,
            "_configuration": _configuration,
            "_visited_composed_classes": self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if (
                var_name in discarded_args
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self._additional_properties_model_instances
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )

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
            "anyOf": [],
            "allOf": [
                MessageResultAllOf,
                MutableResourceModel,
            ],
            "oneOf": [],
        }
