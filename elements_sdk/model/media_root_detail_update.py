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


def lazy_import():
    from elements_sdk.model.custom_field_reference import CustomFieldReference
    from elements_sdk.model.job_reference import JobReference
    from elements_sdk.model.volume_reference import VolumeReference
    globals()['CustomFieldReference'] = CustomFieldReference
    globals()['JobReference'] = JobReference
    globals()['VolumeReference'] = VolumeReference


class MediaRootDetailUpdate(ModelNormal):
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
        ('name',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('path',): {
            'max_length': 255,
        },
        ('view_mode',): {
            'max_length': 63,
            'min_length': 1,
        },
        ('view_style',): {
            'max_length': 63,
            'min_length': 1,
        },
        ('view_default_tab',): {
            'max_length': 63,
            'min_length': 1,
        },
        ('cover',): {
            'max_length': 255,
        },
        ('name_field',): {
            'max_length': 255,
        },
        ('share_link_duration',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
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
            'volume': (VolumeReference,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'custom_fields': ([CustomFieldReference],),  # noqa: E501
            'workflow': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'jobs': ([JobReference],),  # noqa: E501
            'path': (str,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'needs_rescan': (bool,),  # noqa: E501
            'view_mode': (str,),  # noqa: E501
            'view_style': (str,),  # noqa: E501
            'view_default_tab': (str,),  # noqa: E501
            'show_tags': (bool,),  # noqa: E501
            'show_comments': (bool,),  # noqa: E501
            'show_locations': (bool,),  # noqa: E501
            'show_custom_fields': (bool,),  # noqa: E501
            'show_ratings': (bool,),  # noqa: E501
            'show_subclips': (bool,),  # noqa: E501
            'show_subtitles': (bool,),  # noqa: E501
            'show_markers': (bool,),  # noqa: E501
            'show_history': (bool,),  # noqa: E501
            'show_ai_metadata': (bool,),  # noqa: E501
            'prefetch_thumbnail_strips': (bool,),  # noqa: E501
            'cover': (str, none_type,),  # noqa: E501
            'name_field': (str, none_type,),  # noqa: E501
            'share_comments': (bool,),  # noqa: E501
            'share_link_duration': (int,),  # noqa: E501
            'disable_framestacks': (bool,),  # noqa: E501
            'default_proxy_profile': (int, none_type,),  # noqa: E501
            'cloud_proxy_profile': (int, none_type,),  # noqa: E501
            'proxy_profiles': ([int],),  # noqa: E501
            'tags': ([int],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'volume': 'volume',  # noqa: E501
        'name': 'name',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'workflow': 'workflow',  # noqa: E501
        'jobs': 'jobs',  # noqa: E501
        'path': 'path',  # noqa: E501
        'description': 'description',  # noqa: E501
        'needs_rescan': 'needs_rescan',  # noqa: E501
        'view_mode': 'view_mode',  # noqa: E501
        'view_style': 'view_style',  # noqa: E501
        'view_default_tab': 'view_default_tab',  # noqa: E501
        'show_tags': 'show_tags',  # noqa: E501
        'show_comments': 'show_comments',  # noqa: E501
        'show_locations': 'show_locations',  # noqa: E501
        'show_custom_fields': 'show_custom_fields',  # noqa: E501
        'show_ratings': 'show_ratings',  # noqa: E501
        'show_subclips': 'show_subclips',  # noqa: E501
        'show_subtitles': 'show_subtitles',  # noqa: E501
        'show_markers': 'show_markers',  # noqa: E501
        'show_history': 'show_history',  # noqa: E501
        'show_ai_metadata': 'show_ai_metadata',  # noqa: E501
        'prefetch_thumbnail_strips': 'prefetch_thumbnail_strips',  # noqa: E501
        'cover': 'cover',  # noqa: E501
        'name_field': 'name_field',  # noqa: E501
        'share_comments': 'share_comments',  # noqa: E501
        'share_link_duration': 'share_link_duration',  # noqa: E501
        'disable_framestacks': 'disable_framestacks',  # noqa: E501
        'default_proxy_profile': 'default_proxy_profile',  # noqa: E501
        'cloud_proxy_profile': 'cloud_proxy_profile',  # noqa: E501
        'proxy_profiles': 'proxy_profiles',  # noqa: E501
        'tags': 'tags',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, volume, name, *args, **xkwargs):  # noqa: E501
        """MediaRootDetailUpdate - a model defined in OpenAPI

        Args:
            volume (VolumeReference):
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
            custom_fields ([CustomFieldReference]): [optional]  # noqa: E501
            workflow (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            jobs ([JobReference]): [optional]  # noqa: E501
            path (str): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            needs_rescan (bool): [optional]  # noqa: E501
            view_mode (str): [optional]  # noqa: E501
            view_style (str): [optional]  # noqa: E501
            view_default_tab (str): [optional]  # noqa: E501
            show_tags (bool): [optional]  # noqa: E501
            show_comments (bool): [optional]  # noqa: E501
            show_locations (bool): [optional]  # noqa: E501
            show_custom_fields (bool): [optional]  # noqa: E501
            show_ratings (bool): [optional]  # noqa: E501
            show_subclips (bool): [optional]  # noqa: E501
            show_subtitles (bool): [optional]  # noqa: E501
            show_markers (bool): [optional]  # noqa: E501
            show_history (bool): [optional]  # noqa: E501
            show_ai_metadata (bool): [optional]  # noqa: E501
            prefetch_thumbnail_strips (bool): [optional]  # noqa: E501
            cover (str, none_type): [optional]  # noqa: E501
            name_field (str, none_type): [optional]  # noqa: E501
            share_comments (bool): [optional]  # noqa: E501
            share_link_duration (int): [optional]  # noqa: E501
            disable_framestacks (bool): [optional]  # noqa: E501
            default_proxy_profile (int, none_type): [optional]  # noqa: E501
            cloud_proxy_profile (int, none_type): [optional]  # noqa: E501
            proxy_profiles ([int]): [optional]  # noqa: E501
            tags ([int]): [optional]  # noqa: E501
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


        self.volume = volume
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
    def __init__(self, volume, name, *args, **xkwargs):  # noqa: E501
        """MediaRootDetailUpdate - a model defined in OpenAPI

        Args:
            volume (VolumeReference):
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
            custom_fields ([CustomFieldReference]): [optional]  # noqa: E501
            workflow (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            jobs ([JobReference]): [optional]  # noqa: E501
            path (str): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            needs_rescan (bool): [optional]  # noqa: E501
            view_mode (str): [optional]  # noqa: E501
            view_style (str): [optional]  # noqa: E501
            view_default_tab (str): [optional]  # noqa: E501
            show_tags (bool): [optional]  # noqa: E501
            show_comments (bool): [optional]  # noqa: E501
            show_locations (bool): [optional]  # noqa: E501
            show_custom_fields (bool): [optional]  # noqa: E501
            show_ratings (bool): [optional]  # noqa: E501
            show_subclips (bool): [optional]  # noqa: E501
            show_subtitles (bool): [optional]  # noqa: E501
            show_markers (bool): [optional]  # noqa: E501
            show_history (bool): [optional]  # noqa: E501
            show_ai_metadata (bool): [optional]  # noqa: E501
            prefetch_thumbnail_strips (bool): [optional]  # noqa: E501
            cover (str, none_type): [optional]  # noqa: E501
            name_field (str, none_type): [optional]  # noqa: E501
            share_comments (bool): [optional]  # noqa: E501
            share_link_duration (int): [optional]  # noqa: E501
            disable_framestacks (bool): [optional]  # noqa: E501
            default_proxy_profile (int, none_type): [optional]  # noqa: E501
            cloud_proxy_profile (int, none_type): [optional]  # noqa: E501
            proxy_profiles ([int]): [optional]  # noqa: E501
            tags ([int]): [optional]  # noqa: E501
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


        self.volume = volume
        self.name = name
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

