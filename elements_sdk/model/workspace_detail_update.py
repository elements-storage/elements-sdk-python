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
    from elements_sdk.model.nfs_permission import NFSPermission
    from elements_sdk.model.production_reference import ProductionReference
    globals()['NFSPermission'] = NFSPermission
    globals()['ProductionReference'] = ProductionReference


class WorkspaceDetailUpdate(ModelNormal):
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
        ('mac_protocol',): {
            'SMB': "smb",
            'AFP': "afp",
            'NFS': "nfs",
            'OMFS': "omfs",
        },
        ('win_protocol',): {
            'DISK': "disk",
            'UNC': "unc",
        },
        ('win_drive',): {
            'None': None,
            'A': "a",
            'B': "b",
            'C': "c",
            'D': "d",
            'E': "e",
            'F': "f",
            'G': "g",
            'H': "h",
            'I': "i",
            'J': "j",
            'K': "k",
            'L': "l",
            'M': "m",
            'N': "n",
            'O': "o",
            'P': "p",
            'Q': "q",
            'R': "r",
            'S': "s",
            'T': "t",
            'U': "u",
            'V': "v",
            'W': "w",
            'X': "x",
            'Y': "y",
            'Z': "z",
        },
        ('linux_protocol',): {
            'SMB': "smb",
            'NFS': "nfs",
        },
    }

    validations = {
        ('quota_size_hard',): {
            'inclusive_maximum': 4611686018427388000,
            'inclusive_minimum': 0,
        },
        ('quota_size_soft',): {
            'inclusive_maximum': 4611686018427388000,
            'inclusive_minimum': 0,
        },
        ('name',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('description',): {
            'max_length': 255,
        },
        ('linux_mountpoint',): {
            'max_length': 255,
        },
        ('share_name',): {
            'max_length': 255,
        },
        ('affinity',): {
            'max_length': 255,
        },
        ('recycle_bin_exclude',): {
            'max_length': 1023,
        },
        ('external_mac_url',): {
            'max_length': 1023,
        },
        ('external_win_url',): {
            'max_length': 1023,
        },
        ('external_linux_url',): {
            'max_length': 1023,
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
            'production': (ProductionReference,),  # noqa: E501
            'volume': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'sharing_nfs_permissions': ([NFSPermission],),  # noqa: E501
            'quota_size_hard': (int,),  # noqa: E501
            'quota_size_soft': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'long_description': (str,),  # noqa: E501
            'is_template': (bool,),  # noqa: E501
            'active': (bool,),  # noqa: E501
            'mac_protocol': (str,),  # noqa: E501
            'win_protocol': (str,),  # noqa: E501
            'win_drive': (str, none_type,),  # noqa: E501
            'linux_protocol': (str,),  # noqa: E501
            'linux_mountpoint': (str, none_type,),  # noqa: E501
            'share_name': (str, none_type,),  # noqa: E501
            'share_nfs': (bool,),  # noqa: E501
            'share_afp': (bool,),  # noqa: E501
            'sharing_hidden': (bool,),  # noqa: E501
            'sharing_require_login': (bool,),  # noqa: E501
            'sharing_read_only': (bool,),  # noqa: E501
            'sharing_allow_execute': (bool,),  # noqa: E501
            'enable_quota': (bool,),  # noqa: E501
            'affinity': (str, none_type,),  # noqa: E501
            'emulate_avid': (bool,),  # noqa: E501
            'emulate_capture': (bool,),  # noqa: E501
            'emulate_preopen': (bool,),  # noqa: E501
            'emulate_ntfs_streams': (bool,),  # noqa: E501
            'emulate_recycle_bin': (bool,),  # noqa: E501
            'emulate_fruit': (bool,),  # noqa: E501
            'smb_extra_config': (str,),  # noqa: E501
            'afp_extra_config': (str,),  # noqa: E501
            'recycle_bin_exclude': (str, none_type,),  # noqa: E501
            'is_external': (bool,),  # noqa: E501
            'external_mac_url': (str, none_type,),  # noqa: E501
            'external_win_url': (str, none_type,),  # noqa: E501
            'external_linux_url': (str, none_type,),  # noqa: E501
            'allow_symlinks': (bool,),  # noqa: E501
            'rw_permission_priority': (bool,),  # noqa: E501
            'template': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'production': 'production',  # noqa: E501
        'volume': 'volume',  # noqa: E501
        'sharing_nfs_permissions': 'sharing_nfs_permissions',  # noqa: E501
        'quota_size_hard': 'quota_size_hard',  # noqa: E501
        'quota_size_soft': 'quota_size_soft',  # noqa: E501
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'long_description': 'long_description',  # noqa: E501
        'is_template': 'is_template',  # noqa: E501
        'active': 'active',  # noqa: E501
        'mac_protocol': 'mac_protocol',  # noqa: E501
        'win_protocol': 'win_protocol',  # noqa: E501
        'win_drive': 'win_drive',  # noqa: E501
        'linux_protocol': 'linux_protocol',  # noqa: E501
        'linux_mountpoint': 'linux_mountpoint',  # noqa: E501
        'share_name': 'share_name',  # noqa: E501
        'share_nfs': 'share_nfs',  # noqa: E501
        'share_afp': 'share_afp',  # noqa: E501
        'sharing_hidden': 'sharing_hidden',  # noqa: E501
        'sharing_require_login': 'sharing_require_login',  # noqa: E501
        'sharing_read_only': 'sharing_read_only',  # noqa: E501
        'sharing_allow_execute': 'sharing_allow_execute',  # noqa: E501
        'enable_quota': 'enable_quota',  # noqa: E501
        'affinity': 'affinity',  # noqa: E501
        'emulate_avid': 'emulate_avid',  # noqa: E501
        'emulate_capture': 'emulate_capture',  # noqa: E501
        'emulate_preopen': 'emulate_preopen',  # noqa: E501
        'emulate_ntfs_streams': 'emulate_ntfs_streams',  # noqa: E501
        'emulate_recycle_bin': 'emulate_recycle_bin',  # noqa: E501
        'emulate_fruit': 'emulate_fruit',  # noqa: E501
        'smb_extra_config': 'smb_extra_config',  # noqa: E501
        'afp_extra_config': 'afp_extra_config',  # noqa: E501
        'recycle_bin_exclude': 'recycle_bin_exclude',  # noqa: E501
        'is_external': 'is_external',  # noqa: E501
        'external_mac_url': 'external_mac_url',  # noqa: E501
        'external_win_url': 'external_win_url',  # noqa: E501
        'external_linux_url': 'external_linux_url',  # noqa: E501
        'allow_symlinks': 'allow_symlinks',  # noqa: E501
        'rw_permission_priority': 'rw_permission_priority',  # noqa: E501
        'template': 'template',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, production, *args, **xkwargs):  # noqa: E501
        """WorkspaceDetailUpdate - a model defined in OpenAPI

        Args:
            production (ProductionReference):

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
            volume (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            sharing_nfs_permissions ([NFSPermission]): [optional]  # noqa: E501
            quota_size_hard (int): [optional]  # noqa: E501
            quota_size_soft (int): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            long_description (str): [optional]  # noqa: E501
            is_template (bool): [optional]  # noqa: E501
            active (bool): [optional]  # noqa: E501
            mac_protocol (str): [optional]  # noqa: E501
            win_protocol (str): [optional]  # noqa: E501
            win_drive (str, none_type): [optional]  # noqa: E501
            linux_protocol (str): [optional]  # noqa: E501
            linux_mountpoint (str, none_type): [optional]  # noqa: E501
            share_name (str, none_type): [optional]  # noqa: E501
            share_nfs (bool): [optional]  # noqa: E501
            share_afp (bool): [optional]  # noqa: E501
            sharing_hidden (bool): [optional]  # noqa: E501
            sharing_require_login (bool): [optional]  # noqa: E501
            sharing_read_only (bool): [optional]  # noqa: E501
            sharing_allow_execute (bool): [optional]  # noqa: E501
            enable_quota (bool): [optional]  # noqa: E501
            affinity (str, none_type): [optional]  # noqa: E501
            emulate_avid (bool): [optional]  # noqa: E501
            emulate_capture (bool): [optional]  # noqa: E501
            emulate_preopen (bool): [optional]  # noqa: E501
            emulate_ntfs_streams (bool): [optional]  # noqa: E501
            emulate_recycle_bin (bool): [optional]  # noqa: E501
            emulate_fruit (bool): [optional]  # noqa: E501
            smb_extra_config (str): [optional]  # noqa: E501
            afp_extra_config (str): [optional]  # noqa: E501
            recycle_bin_exclude (str, none_type): [optional]  # noqa: E501
            is_external (bool): [optional]  # noqa: E501
            external_mac_url (str, none_type): [optional]  # noqa: E501
            external_win_url (str, none_type): [optional]  # noqa: E501
            external_linux_url (str, none_type): [optional]  # noqa: E501
            allow_symlinks (bool): [optional]  # noqa: E501
            rw_permission_priority (bool): [optional]  # noqa: E501
            template (int, none_type): [optional]  # noqa: E501
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


        self.production = production
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
    def __init__(self, production, *args, **xkwargs):  # noqa: E501
        """WorkspaceDetailUpdate - a model defined in OpenAPI

        Args:
            production (ProductionReference):

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
            volume (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            sharing_nfs_permissions ([NFSPermission]): [optional]  # noqa: E501
            quota_size_hard (int): [optional]  # noqa: E501
            quota_size_soft (int): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            long_description (str): [optional]  # noqa: E501
            is_template (bool): [optional]  # noqa: E501
            active (bool): [optional]  # noqa: E501
            mac_protocol (str): [optional]  # noqa: E501
            win_protocol (str): [optional]  # noqa: E501
            win_drive (str, none_type): [optional]  # noqa: E501
            linux_protocol (str): [optional]  # noqa: E501
            linux_mountpoint (str, none_type): [optional]  # noqa: E501
            share_name (str, none_type): [optional]  # noqa: E501
            share_nfs (bool): [optional]  # noqa: E501
            share_afp (bool): [optional]  # noqa: E501
            sharing_hidden (bool): [optional]  # noqa: E501
            sharing_require_login (bool): [optional]  # noqa: E501
            sharing_read_only (bool): [optional]  # noqa: E501
            sharing_allow_execute (bool): [optional]  # noqa: E501
            enable_quota (bool): [optional]  # noqa: E501
            affinity (str, none_type): [optional]  # noqa: E501
            emulate_avid (bool): [optional]  # noqa: E501
            emulate_capture (bool): [optional]  # noqa: E501
            emulate_preopen (bool): [optional]  # noqa: E501
            emulate_ntfs_streams (bool): [optional]  # noqa: E501
            emulate_recycle_bin (bool): [optional]  # noqa: E501
            emulate_fruit (bool): [optional]  # noqa: E501
            smb_extra_config (str): [optional]  # noqa: E501
            afp_extra_config (str): [optional]  # noqa: E501
            recycle_bin_exclude (str, none_type): [optional]  # noqa: E501
            is_external (bool): [optional]  # noqa: E501
            external_mac_url (str, none_type): [optional]  # noqa: E501
            external_win_url (str, none_type): [optional]  # noqa: E501
            external_linux_url (str, none_type): [optional]  # noqa: E501
            allow_symlinks (bool): [optional]  # noqa: E501
            rw_permission_priority (bool): [optional]  # noqa: E501
            template (int, none_type): [optional]  # noqa: E501
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


        self.production = production
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
