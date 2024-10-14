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
    from elements_sdk.model.production_mini import ProductionMini
    from elements_sdk.model.quota import Quota
    from elements_sdk.model.workspace_endpoint import WorkspaceEndpoint
    from elements_sdk.model.workspace_resolved_permission import WorkspaceResolvedPermission
    globals()['NFSPermission'] = NFSPermission
    globals()['ProductionMini'] = ProductionMini
    globals()['Quota'] = Quota
    globals()['WorkspaceEndpoint'] = WorkspaceEndpoint
    globals()['WorkspaceResolvedPermission'] = WorkspaceResolvedPermission


class Workspace(ModelNormal):
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
        ('volume_path',): {
            'min_length': 1,
        },
        ('path',): {
            'min_length': 1,
        },
        ('full_path',): {
            'min_length': 1,
        },
        ('directory',): {
            'min_length': 1,
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
            'production': (ProductionMini,),  # noqa: E501
            'volume': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'sharing_nfs_permissions': ([NFSPermission],),  # noqa: E501
            'current_share_name': (str,),  # noqa: E501
            'size_used': (int, none_type,),  # noqa: E501
            'size_total': (int, none_type,),  # noqa: E501
            'bookmarked': (bool, none_type,),  # noqa: E501
            'quota_size_hard': (int,),  # noqa: E501
            'quota_size_soft': (int,),  # noqa: E501
            'resolved_read_only': (bool, none_type,),  # noqa: E501
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
            'volume_path': (str, none_type,),  # noqa: E501
            'path': (str, none_type,),  # noqa: E501
            'full_path': (str, none_type,),  # noqa: E501
            'endpoints': ([WorkspaceEndpoint], none_type,),  # noqa: E501
            'quota': (Quota,),  # noqa: E501
            'resolved_permissions': ([WorkspaceResolvedPermission], none_type,),  # noqa: E501
            'directory': (str, none_type,),  # noqa: E501
            'last_login': (datetime, none_type,),  # noqa: E501
            'home_for': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'production': 'production',  # noqa: E501
        'volume': 'volume',  # noqa: E501
        'sharing_nfs_permissions': 'sharing_nfs_permissions',  # noqa: E501
        'current_share_name': 'current_share_name',  # noqa: E501
        'size_used': 'size_used',  # noqa: E501
        'size_total': 'size_total',  # noqa: E501
        'bookmarked': 'bookmarked',  # noqa: E501
        'quota_size_hard': 'quota_size_hard',  # noqa: E501
        'quota_size_soft': 'quota_size_soft',  # noqa: E501
        'resolved_read_only': 'resolved_read_only',  # noqa: E501
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
        'volume_path': 'volume_path',  # noqa: E501
        'path': 'path',  # noqa: E501
        'full_path': 'full_path',  # noqa: E501
        'endpoints': 'endpoints',  # noqa: E501
        'quota': 'quota',  # noqa: E501
        'resolved_permissions': 'resolved_permissions',  # noqa: E501
        'directory': 'directory',  # noqa: E501
        'last_login': 'last_login',  # noqa: E501
        'home_for': 'home_for',  # noqa: E501
    }

    read_only_vars = {
        'current_share_name',  # noqa: E501
        'size_used',  # noqa: E501
        'size_total',  # noqa: E501
        'bookmarked',  # noqa: E501
        'resolved_read_only',  # noqa: E501
        'volume_path',  # noqa: E501
        'path',  # noqa: E501
        'full_path',  # noqa: E501
        'endpoints',  # noqa: E501
        'resolved_permissions',  # noqa: E501
        'directory',  # noqa: E501
        'last_login',  # noqa: E501
        'home_for',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, production, volume, sharing_nfs_permissions, current_share_name, size_used, size_total, bookmarked, quota_size_hard, quota_size_soft, resolved_read_only, name, description, long_description, is_template, active, mac_protocol, win_protocol, win_drive, linux_protocol, linux_mountpoint, share_name, share_nfs, share_afp, sharing_hidden, sharing_require_login, sharing_read_only, sharing_allow_execute, enable_quota, affinity, emulate_avid, emulate_capture, emulate_preopen, emulate_ntfs_streams, emulate_recycle_bin, emulate_fruit, smb_extra_config, afp_extra_config, recycle_bin_exclude, is_external, external_mac_url, external_win_url, external_linux_url, allow_symlinks, rw_permission_priority, template, *args, **xkwargs):  # noqa: E501
        """Workspace - a model defined in OpenAPI

        Args:
            id (int):
            production (ProductionMini):
            volume (bool, date, datetime, dict, float, int, list, str, none_type):
            sharing_nfs_permissions ([NFSPermission]):
            current_share_name (str):
            size_used (int, none_type):
            size_total (int, none_type):
            bookmarked (bool, none_type):
            quota_size_hard (int):
            quota_size_soft (int):
            resolved_read_only (bool, none_type):
            name (str):
            description (str, none_type):
            long_description (str):
            is_template (bool):
            active (bool):
            mac_protocol (str):
            win_protocol (str):
            win_drive (str, none_type):
            linux_protocol (str):
            linux_mountpoint (str, none_type):
            share_name (str, none_type):
            share_nfs (bool):
            share_afp (bool):
            sharing_hidden (bool):
            sharing_require_login (bool):
            sharing_read_only (bool):
            sharing_allow_execute (bool):
            enable_quota (bool):
            affinity (str, none_type):
            emulate_avid (bool):
            emulate_capture (bool):
            emulate_preopen (bool):
            emulate_ntfs_streams (bool):
            emulate_recycle_bin (bool):
            emulate_fruit (bool):
            smb_extra_config (str):
            afp_extra_config (str):
            recycle_bin_exclude (str, none_type):
            is_external (bool):
            external_mac_url (str, none_type):
            external_win_url (str, none_type):
            external_linux_url (str, none_type):
            allow_symlinks (bool):
            rw_permission_priority (bool):
            template (int, none_type):

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
            volume_path (str, none_type): [optional]  # noqa: E501
            path (str, none_type): [optional]  # noqa: E501
            full_path (str, none_type): [optional]  # noqa: E501
            endpoints ([WorkspaceEndpoint], none_type): [optional]  # noqa: E501
            quota (Quota): [optional]  # noqa: E501
            resolved_permissions ([WorkspaceResolvedPermission], none_type): [optional]  # noqa: E501
            directory (str, none_type): [optional]  # noqa: E501
            last_login (datetime, none_type): [optional]  # noqa: E501
            home_for (int, none_type): [optional]  # noqa: E501
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
        self.production = production
        self.volume = volume
        self.sharing_nfs_permissions = sharing_nfs_permissions
        self.current_share_name = current_share_name
        self.size_used = size_used
        self.size_total = size_total
        self.bookmarked = bookmarked
        self.quota_size_hard = quota_size_hard
        self.quota_size_soft = quota_size_soft
        self.resolved_read_only = resolved_read_only
        self.name = name
        self.description = description
        self.long_description = long_description
        self.is_template = is_template
        self.active = active
        self.mac_protocol = mac_protocol
        self.win_protocol = win_protocol
        self.win_drive = win_drive
        self.linux_protocol = linux_protocol
        self.linux_mountpoint = linux_mountpoint
        self.share_name = share_name
        self.share_nfs = share_nfs
        self.share_afp = share_afp
        self.sharing_hidden = sharing_hidden
        self.sharing_require_login = sharing_require_login
        self.sharing_read_only = sharing_read_only
        self.sharing_allow_execute = sharing_allow_execute
        self.enable_quota = enable_quota
        self.affinity = affinity
        self.emulate_avid = emulate_avid
        self.emulate_capture = emulate_capture
        self.emulate_preopen = emulate_preopen
        self.emulate_ntfs_streams = emulate_ntfs_streams
        self.emulate_recycle_bin = emulate_recycle_bin
        self.emulate_fruit = emulate_fruit
        self.smb_extra_config = smb_extra_config
        self.afp_extra_config = afp_extra_config
        self.recycle_bin_exclude = recycle_bin_exclude
        self.is_external = is_external
        self.external_mac_url = external_mac_url
        self.external_win_url = external_win_url
        self.external_linux_url = external_linux_url
        self.allow_symlinks = allow_symlinks
        self.rw_permission_priority = rw_permission_priority
        self.template = template
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
    def __init__(self, id, production, volume, sharing_nfs_permissions, quota_size_hard, quota_size_soft, name, description, long_description, is_template, active, mac_protocol, win_protocol, win_drive, linux_protocol, linux_mountpoint, share_name, share_nfs, share_afp, sharing_hidden, sharing_require_login, sharing_read_only, sharing_allow_execute, enable_quota, affinity, emulate_avid, emulate_capture, emulate_preopen, emulate_ntfs_streams, emulate_recycle_bin, emulate_fruit, smb_extra_config, afp_extra_config, recycle_bin_exclude, is_external, external_mac_url, external_win_url, external_linux_url, allow_symlinks, rw_permission_priority, template, *args, **xkwargs):  # noqa: E501
        """Workspace - a model defined in OpenAPI

        Args:
            id (int):
            production (ProductionMini):
            volume (bool, date, datetime, dict, float, int, list, str, none_type):
            sharing_nfs_permissions ([NFSPermission]):
            quota_size_hard (int):
            quota_size_soft (int):
            name (str):
            description (str, none_type):
            long_description (str):
            is_template (bool):
            active (bool):
            mac_protocol (str):
            win_protocol (str):
            win_drive (str, none_type):
            linux_protocol (str):
            linux_mountpoint (str, none_type):
            share_name (str, none_type):
            share_nfs (bool):
            share_afp (bool):
            sharing_hidden (bool):
            sharing_require_login (bool):
            sharing_read_only (bool):
            sharing_allow_execute (bool):
            enable_quota (bool):
            affinity (str, none_type):
            emulate_avid (bool):
            emulate_capture (bool):
            emulate_preopen (bool):
            emulate_ntfs_streams (bool):
            emulate_recycle_bin (bool):
            emulate_fruit (bool):
            smb_extra_config (str):
            afp_extra_config (str):
            recycle_bin_exclude (str, none_type):
            is_external (bool):
            external_mac_url (str, none_type):
            external_win_url (str, none_type):
            external_linux_url (str, none_type):
            allow_symlinks (bool):
            rw_permission_priority (bool):
            template (int, none_type):

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
            volume_path (str, none_type): [optional]  # noqa: E501
            path (str, none_type): [optional]  # noqa: E501
            full_path (str, none_type): [optional]  # noqa: E501
            endpoints ([WorkspaceEndpoint], none_type): [optional]  # noqa: E501
            quota (Quota): [optional]  # noqa: E501
            resolved_permissions ([WorkspaceResolvedPermission], none_type): [optional]  # noqa: E501
            directory (str, none_type): [optional]  # noqa: E501
            last_login (datetime, none_type): [optional]  # noqa: E501
            home_for (int, none_type): [optional]  # noqa: E501
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
        self.production = production
        self.volume = volume
        self.sharing_nfs_permissions = sharing_nfs_permissions
        self.quota_size_hard = quota_size_hard
        self.quota_size_soft = quota_size_soft
        self.name = name
        self.description = description
        self.long_description = long_description
        self.is_template = is_template
        self.active = active
        self.mac_protocol = mac_protocol
        self.win_protocol = win_protocol
        self.win_drive = win_drive
        self.linux_protocol = linux_protocol
        self.linux_mountpoint = linux_mountpoint
        self.share_name = share_name
        self.share_nfs = share_nfs
        self.share_afp = share_afp
        self.sharing_hidden = sharing_hidden
        self.sharing_require_login = sharing_require_login
        self.sharing_read_only = sharing_read_only
        self.sharing_allow_execute = sharing_allow_execute
        self.enable_quota = enable_quota
        self.affinity = affinity
        self.emulate_avid = emulate_avid
        self.emulate_capture = emulate_capture
        self.emulate_preopen = emulate_preopen
        self.emulate_ntfs_streams = emulate_ntfs_streams
        self.emulate_recycle_bin = emulate_recycle_bin
        self.emulate_fruit = emulate_fruit
        self.smb_extra_config = smb_extra_config
        self.afp_extra_config = afp_extra_config
        self.recycle_bin_exclude = recycle_bin_exclude
        self.is_external = is_external
        self.external_mac_url = external_mac_url
        self.external_win_url = external_win_url
        self.external_linux_url = external_linux_url
        self.allow_symlinks = allow_symlinks
        self.rw_permission_priority = rw_permission_priority
        self.template = template
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

