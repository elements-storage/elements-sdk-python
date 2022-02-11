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



class ProxyProfile(ModelNormal):
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
        ('proxy_generator',): {
            'FFMPEG': "ffmpeg",
            'HOTFOLDER': "hotfolder",
            'TRANSKODER': "transkoder",
            'VANTAGE': "vantage",
            'NOOP': "noop",
        },
        ('rate_control',): {
            'CRF': "CRF",
            'CBR': "CBR",
            'VBR': "VBR",
        },
        ('watermark_position',): {
            'TL': "TL",
            'TR': "TR",
            'BR': "BR",
            'BL': "BL",
            'C': "C",
        },
        ('timecode_position',): {
            'TL': "TL",
            'TR': "TR",
            'BR': "BR",
            'BL': "BL",
            'C': "C",
        },
    }

    validations = {
        ('name',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('resolution',): {
            'max_length': 1023,
        },
        ('crf',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('bitrate',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('audio_bitrate',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('variants_limit',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('watermark_image',): {
            'max_length': 1023,
        },
        ('hotfolder_copy_to',): {
            'max_length': 1023,
        },
        ('hotfolder_read_from',): {
            'max_length': 1023,
        },
        ('hotfolder_queue_timeout',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('hotfolder_encode_timeout',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('vantage_workflow_id',): {
            'max_length': 63,
        },
        ('external_transcoder_staging_path',): {
            'max_length': 1023,
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
            'id': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'proxy_generator': (str,),  # noqa: E501
            'resolution': (str, none_type,),  # noqa: E501
            'rate_control': (str,),  # noqa: E501
            'crf': (int, none_type,),  # noqa: E501
            'bitrate': (int, none_type,),  # noqa: E501
            'audio_bitrate': (int,),  # noqa: E501
            'variants_limit': (int,),  # noqa: E501
            'enable_dense_filmstrip': (bool,),  # noqa: E501
            'enable_watermark': (bool,),  # noqa: E501
            'watermark_image': (str, none_type,),  # noqa: E501
            'watermark_position': (str,),  # noqa: E501
            'watermark_opacity': (float,),  # noqa: E501
            'watermark_size': (float,),  # noqa: E501
            'enable_timecode': (bool,),  # noqa: E501
            'timecode_position': (str,),  # noqa: E501
            'timecode_opacity': (float,),  # noqa: E501
            'timecode_size': (float,),  # noqa: E501
            'lut': (str, none_type,),  # noqa: E501
            'hotfolder_copy_to': (str, none_type,),  # noqa: E501
            'hotfolder_read_from': (str, none_type,),  # noqa: E501
            'hotfolder_queue_timeout': (int,),  # noqa: E501
            'hotfolder_encode_timeout': (int,),  # noqa: E501
            'vantage_workflow_id': (str, none_type,),  # noqa: E501
            'external_transcoder_staging_path': (str, none_type,),  # noqa: E501
            'external_transcoder': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'proxy_generator': 'proxy_generator',  # noqa: E501
        'resolution': 'resolution',  # noqa: E501
        'rate_control': 'rate_control',  # noqa: E501
        'crf': 'crf',  # noqa: E501
        'bitrate': 'bitrate',  # noqa: E501
        'audio_bitrate': 'audio_bitrate',  # noqa: E501
        'variants_limit': 'variants_limit',  # noqa: E501
        'enable_dense_filmstrip': 'enable_dense_filmstrip',  # noqa: E501
        'enable_watermark': 'enable_watermark',  # noqa: E501
        'watermark_image': 'watermark_image',  # noqa: E501
        'watermark_position': 'watermark_position',  # noqa: E501
        'watermark_opacity': 'watermark_opacity',  # noqa: E501
        'watermark_size': 'watermark_size',  # noqa: E501
        'enable_timecode': 'enable_timecode',  # noqa: E501
        'timecode_position': 'timecode_position',  # noqa: E501
        'timecode_opacity': 'timecode_opacity',  # noqa: E501
        'timecode_size': 'timecode_size',  # noqa: E501
        'lut': 'lut',  # noqa: E501
        'hotfolder_copy_to': 'hotfolder_copy_to',  # noqa: E501
        'hotfolder_read_from': 'hotfolder_read_from',  # noqa: E501
        'hotfolder_queue_timeout': 'hotfolder_queue_timeout',  # noqa: E501
        'hotfolder_encode_timeout': 'hotfolder_encode_timeout',  # noqa: E501
        'vantage_workflow_id': 'vantage_workflow_id',  # noqa: E501
        'external_transcoder_staging_path': 'external_transcoder_staging_path',  # noqa: E501
        'external_transcoder': 'external_transcoder',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, name, *args, **xkwargs):  # noqa: E501
        """ProxyProfile - a model defined in OpenAPI

        Args:
            id (int):
            name (str):

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
            proxy_generator (str): [optional]  # noqa: E501
            resolution (str, none_type): [optional]  # noqa: E501
            rate_control (str): [optional]  # noqa: E501
            crf (int, none_type): [optional]  # noqa: E501
            bitrate (int, none_type): [optional]  # noqa: E501
            audio_bitrate (int): [optional]  # noqa: E501
            variants_limit (int): [optional]  # noqa: E501
            enable_dense_filmstrip (bool): [optional]  # noqa: E501
            enable_watermark (bool): [optional]  # noqa: E501
            watermark_image (str, none_type): [optional]  # noqa: E501
            watermark_position (str): [optional]  # noqa: E501
            watermark_opacity (float): [optional]  # noqa: E501
            watermark_size (float): [optional]  # noqa: E501
            enable_timecode (bool): [optional]  # noqa: E501
            timecode_position (str): [optional]  # noqa: E501
            timecode_opacity (float): [optional]  # noqa: E501
            timecode_size (float): [optional]  # noqa: E501
            lut (str, none_type): [optional]  # noqa: E501
            hotfolder_copy_to (str, none_type): [optional]  # noqa: E501
            hotfolder_read_from (str, none_type): [optional]  # noqa: E501
            hotfolder_queue_timeout (int): [optional]  # noqa: E501
            hotfolder_encode_timeout (int): [optional]  # noqa: E501
            vantage_workflow_id (str, none_type): [optional]  # noqa: E501
            external_transcoder_staging_path (str, none_type): [optional]  # noqa: E501
            external_transcoder (int, none_type): [optional]  # noqa: E501
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


        self.id = id
        self.name = name
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
    def __init__(self, id, name, *args, **xkwargs):  # noqa: E501
        """ProxyProfile - a model defined in OpenAPI

        Args:
            id (int):
            name (str):

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
            proxy_generator (str): [optional]  # noqa: E501
            resolution (str, none_type): [optional]  # noqa: E501
            rate_control (str): [optional]  # noqa: E501
            crf (int, none_type): [optional]  # noqa: E501
            bitrate (int, none_type): [optional]  # noqa: E501
            audio_bitrate (int): [optional]  # noqa: E501
            variants_limit (int): [optional]  # noqa: E501
            enable_dense_filmstrip (bool): [optional]  # noqa: E501
            enable_watermark (bool): [optional]  # noqa: E501
            watermark_image (str, none_type): [optional]  # noqa: E501
            watermark_position (str): [optional]  # noqa: E501
            watermark_opacity (float): [optional]  # noqa: E501
            watermark_size (float): [optional]  # noqa: E501
            enable_timecode (bool): [optional]  # noqa: E501
            timecode_position (str): [optional]  # noqa: E501
            timecode_opacity (float): [optional]  # noqa: E501
            timecode_size (float): [optional]  # noqa: E501
            lut (str, none_type): [optional]  # noqa: E501
            hotfolder_copy_to (str, none_type): [optional]  # noqa: E501
            hotfolder_read_from (str, none_type): [optional]  # noqa: E501
            hotfolder_queue_timeout (int): [optional]  # noqa: E501
            hotfolder_encode_timeout (int): [optional]  # noqa: E501
            vantage_workflow_id (str, none_type): [optional]  # noqa: E501
            external_transcoder_staging_path (str, none_type): [optional]  # noqa: E501
            external_transcoder (int, none_type): [optional]  # noqa: E501
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


        self.id = id
        self.name = name
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
