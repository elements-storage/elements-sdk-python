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
    from elements_sdk.model.backend import Backend
    from elements_sdk.model.fs_properties import FSProperties
    from elements_sdk.model.volume_status import VolumeStatus
    globals()['Backend'] = Backend
    globals()['FSProperties'] = FSProperties
    globals()['VolumeStatus'] = VolumeStatus


class Volume(ModelNormal):
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
        ('type',): {
            'GENERIC': "generic",
            'GENERIC-MOUNT': "generic-mount",
            'SNFS': "snfs",
            'BTRFS': "btrfs",
            'BCACHEFS': "bcachefs",
            'BEEGFS': "beegfs",
            'CLOUD': "cloud",
            'ONEFS': "onefs",
            'QUMULO': "qumulo",
        },
    }

    validations = {
        ('path',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('display_name',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('visual_tag',): {
            'max_length': 255,
        },
        ('snfs_name',): {
            'max_length': 255,
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
            'id': (int,),  # noqa: E501
            'path': (str,),  # noqa: E501
            'nodes': ([int],),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'visual_tag': (str, none_type,),  # noqa: E501
            'is_default': (bool,),  # noqa: E501
            'use_for_homes': (bool,),  # noqa: E501
            'use_for_workspaces': (bool,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'snm_enabled': (bool,),  # noqa: E501
            'snfs_name': (str, none_type,),  # noqa: E501
            'simulated_quotas': (bool,),  # noqa: E501
            'backend': (Backend,),  # noqa: E501
            'cloud_account': (int, none_type,),  # noqa: E501
            'qumulo_integration': (int, none_type,),  # noqa: E501
            'fs_properties': (FSProperties,),  # noqa: E501
            'status': (VolumeStatus,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'path': 'path',  # noqa: E501
        'nodes': 'nodes',  # noqa: E501
        'display_name': 'display_name',  # noqa: E501
        'visual_tag': 'visual_tag',  # noqa: E501
        'is_default': 'is_default',  # noqa: E501
        'use_for_homes': 'use_for_homes',  # noqa: E501
        'use_for_workspaces': 'use_for_workspaces',  # noqa: E501
        'type': 'type',  # noqa: E501
        'snm_enabled': 'snm_enabled',  # noqa: E501
        'snfs_name': 'snfs_name',  # noqa: E501
        'simulated_quotas': 'simulated_quotas',  # noqa: E501
        'backend': 'backend',  # noqa: E501
        'cloud_account': 'cloud_account',  # noqa: E501
        'qumulo_integration': 'qumulo_integration',  # noqa: E501
        'fs_properties': 'fs_properties',  # noqa: E501
        'status': 'status',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, path, nodes, display_name, visual_tag, is_default, use_for_homes, use_for_workspaces, type, snm_enabled, snfs_name, simulated_quotas, backend, cloud_account, qumulo_integration, *args, **xkwargs):  # noqa: E501
        """Volume - a model defined in OpenAPI

        Args:
            id (int):
            path (str):
            nodes ([int]):
            display_name (str):
            visual_tag (str, none_type):
            is_default (bool):
            use_for_homes (bool):
            use_for_workspaces (bool):
            type (str):
            snm_enabled (bool):
            snfs_name (str, none_type):
            simulated_quotas (bool):
            backend (Backend):
            cloud_account (int, none_type):
            qumulo_integration (int, none_type):

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
            fs_properties (FSProperties): [optional]  # noqa: E501
            status (VolumeStatus): [optional]  # noqa: E501
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
        self.path = path
        self.nodes = nodes
        self.display_name = display_name
        self.visual_tag = visual_tag
        self.is_default = is_default
        self.use_for_homes = use_for_homes
        self.use_for_workspaces = use_for_workspaces
        self.type = type
        self.snm_enabled = snm_enabled
        self.snfs_name = snfs_name
        self.simulated_quotas = simulated_quotas
        self.backend = backend
        self.cloud_account = cloud_account
        self.qumulo_integration = qumulo_integration
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
    def __init__(self, id, path, nodes, display_name, visual_tag, is_default, use_for_homes, use_for_workspaces, type, snm_enabled, snfs_name, simulated_quotas, backend, cloud_account, qumulo_integration, *args, **xkwargs):  # noqa: E501
        """Volume - a model defined in OpenAPI

        Args:
            id (int):
            path (str):
            nodes ([int]):
            display_name (str):
            visual_tag (str, none_type):
            is_default (bool):
            use_for_homes (bool):
            use_for_workspaces (bool):
            type (str):
            snm_enabled (bool):
            snfs_name (str, none_type):
            simulated_quotas (bool):
            backend (Backend):
            cloud_account (int, none_type):
            qumulo_integration (int, none_type):

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
            fs_properties (FSProperties): [optional]  # noqa: E501
            status (VolumeStatus): [optional]  # noqa: E501
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
        self.path = path
        self.nodes = nodes
        self.display_name = display_name
        self.visual_tag = visual_tag
        self.is_default = is_default
        self.use_for_homes = use_for_homes
        self.use_for_workspaces = use_for_workspaces
        self.type = type
        self.snm_enabled = snm_enabled
        self.snfs_name = snfs_name
        self.simulated_quotas = simulated_quotas
        self.backend = backend
        self.cloud_account = cloud_account
        self.qumulo_integration = qumulo_integration
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

