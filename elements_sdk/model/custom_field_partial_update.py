"""
    ELEMENTS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from elements_sdk.model_utils import (  # noqa: F401
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
from elements_sdk.exceptions import ApiAttributeError



class CustomFieldPartialUpdate(ModelNormal):
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
        ('validation',): {
            'None': None,
            'NUMBER_OF_DIGITS': "number_of_digits",
            'REGEX': "regex",
            'RANGE': "range",
            'REQUIRE_TRUE': "require_true",
        },
    }

    validations = {
        ('name',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('order',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('type',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('regex',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('range_min',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('range_max',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('number_of_digits',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('metadata_prefill',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('help_text',): {
            'max_length': 255,
        },
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
            'labels': ([{str: (str, none_type)}],),  # noqa: E501
            'options': ([str, none_type],),  # noqa: E501
            'name': (str,),  # noqa: E501
            'order': (int,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'use_for_uploads': (bool,),  # noqa: E501
            'require_to_upload': (bool,),  # noqa: E501
            'non_user_editable': (bool,),  # noqa: E501
            'validation': (str, none_type,),  # noqa: E501
            'regex': (str, none_type,),  # noqa: E501
            'range_min': (int, none_type,),  # noqa: E501
            'range_max': (int, none_type,),  # noqa: E501
            'number_of_digits': (int, none_type,),  # noqa: E501
            'metadata_prefill': (str, none_type,),  # noqa: E501
            'highlight_expiration': (bool,),  # noqa: E501
            'multiple_response': (bool,),  # noqa: E501
            'help_text': (str, none_type,),  # noqa: E501
            'users_from_group': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'labels': 'labels',  # noqa: E501
        'options': 'options',  # noqa: E501
        'name': 'name',  # noqa: E501
        'order': 'order',  # noqa: E501
        'type': 'type',  # noqa: E501
        'use_for_uploads': 'use_for_uploads',  # noqa: E501
        'require_to_upload': 'require_to_upload',  # noqa: E501
        'non_user_editable': 'non_user_editable',  # noqa: E501
        'validation': 'validation',  # noqa: E501
        'regex': 'regex',  # noqa: E501
        'range_min': 'range_min',  # noqa: E501
        'range_max': 'range_max',  # noqa: E501
        'number_of_digits': 'number_of_digits',  # noqa: E501
        'metadata_prefill': 'metadata_prefill',  # noqa: E501
        'highlight_expiration': 'highlight_expiration',  # noqa: E501
        'multiple_response': 'multiple_response',  # noqa: E501
        'help_text': 'help_text',  # noqa: E501
        'users_from_group': 'users_from_group',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **xkwargs):  # noqa: E501
        """CustomFieldPartialUpdate - a model defined in OpenAPI

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
            labels ([{str: (str, none_type)}]): [optional]  # noqa: E501
            options ([str, none_type]): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            order (int): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            use_for_uploads (bool): [optional]  # noqa: E501
            require_to_upload (bool): [optional]  # noqa: E501
            non_user_editable (bool): [optional]  # noqa: E501
            validation (str, none_type): [optional]  # noqa: E501
            regex (str, none_type): [optional]  # noqa: E501
            range_min (int, none_type): [optional]  # noqa: E501
            range_max (int, none_type): [optional]  # noqa: E501
            number_of_digits (int, none_type): [optional]  # noqa: E501
            metadata_prefill (str, none_type): [optional]  # noqa: E501
            highlight_expiration (bool): [optional]  # noqa: E501
            multiple_response (bool): [optional]  # noqa: E501
            help_text (str, none_type): [optional]  # noqa: E501
            users_from_group (int, none_type): [optional]  # noqa: E501
        """

        _check_type = xkwargs.pop('_check_type', True)
        _spec_property_naming = xkwargs.pop('_spec_property_naming', False)
        _path_to_item = xkwargs.pop('_path_to_item', ())
        _configuration = xkwargs.pop('_configuration', None)
        _visited_composed_classes = xkwargs.pop('_visited_composed_classes', ())

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


        for var_name, var_value in xkwargs.items():
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
    def __init__(self, *args, **xkwargs):  # noqa: E501
        """CustomFieldPartialUpdate - a model defined in OpenAPI

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
            labels ([{str: (str, none_type)}]): [optional]  # noqa: E501
            options ([str, none_type]): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            order (int): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            use_for_uploads (bool): [optional]  # noqa: E501
            require_to_upload (bool): [optional]  # noqa: E501
            non_user_editable (bool): [optional]  # noqa: E501
            validation (str, none_type): [optional]  # noqa: E501
            regex (str, none_type): [optional]  # noqa: E501
            range_min (int, none_type): [optional]  # noqa: E501
            range_max (int, none_type): [optional]  # noqa: E501
            number_of_digits (int, none_type): [optional]  # noqa: E501
            metadata_prefill (str, none_type): [optional]  # noqa: E501
            highlight_expiration (bool): [optional]  # noqa: E501
            multiple_response (bool): [optional]  # noqa: E501
            help_text (str, none_type): [optional]  # noqa: E501
            users_from_group (int, none_type): [optional]  # noqa: E501
        """

        _check_type = xkwargs.pop('_check_type', True)
        _spec_property_naming = xkwargs.pop('_spec_property_naming', False)
        _path_to_item = xkwargs.pop('_path_to_item', ())
        _configuration = xkwargs.pop('_configuration', None)
        _visited_composed_classes = xkwargs.pop('_visited_composed_classes', ())

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


        for var_name, var_value in xkwargs.items():
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

