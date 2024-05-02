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
    from elements_sdk.model.elements_user_mini import ElementsUserMini
    from elements_sdk.model.media_file_exclusion_info import MediaFileExclusionInfo
    from elements_sdk.model.media_root_mini import MediaRootMini
    from elements_sdk.model.media_root_permission import MediaRootPermission
    from elements_sdk.model.volume_mini import VolumeMini
    globals()['ElementsUserMini'] = ElementsUserMini
    globals()['MediaFileExclusionInfo'] = MediaFileExclusionInfo
    globals()['MediaRootMini'] = MediaRootMini
    globals()['MediaRootPermission'] = MediaRootPermission
    globals()['VolumeMini'] = VolumeMini


class MediaFile(ModelNormal):
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
            'min_length': 1,
        },
        ('path',): {
            'min_length': 1,
        },
        ('pathhash',): {
            'min_length': 1,
        },
        ('ancestry',): {
            'min_length': 1,
        },
        ('is_excluded',): {
            'max_length': 1,
            'min_length': 1,
        },
        ('is_excluded_from_proxy_generation',): {
            'max_length': 1,
            'min_length': 1,
        },
        ('total_files',): {
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
            'id': (int,),  # noqa: E501
            'volume': (VolumeMini,),  # noqa: E501
            'effective_custom_fields': ({str: (str, none_type)}, none_type,),  # noqa: E501
            'full_path': (str,),  # noqa: E501
            'is_shared': (bool, none_type,),  # noqa: E501
            'is_hardlink': (bool,),  # noqa: E501
            'is_bookmarked': (bool, none_type,),  # noqa: E501
            'exclusion_info': (MediaFileExclusionInfo,),  # noqa: E501
            'child_count': (int, none_type,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'path': (str,),  # noqa: E501
            'pathhash': (str,),  # noqa: E501
            'ancestry': (str,),  # noqa: E501
            'is_dir': (bool,),  # noqa: E501
            'size': (int,),  # noqa: E501
            'mtime': (int,),  # noqa: E501
            'present': (bool,),  # noqa: E501
            'is_showroom': (bool,),  # noqa: E501
            'bundle_index': (int,),  # noqa: E501
            'modified': (datetime,),  # noqa: E501
            'info': ({str: (str, none_type)},),  # noqa: E501
            'custom_fields': ({str: (str, none_type)},),  # noqa: E501
            'resolved_permission': (MediaRootPermission,),  # noqa: E501
            'parent_file': ({str: (str, none_type)},),  # noqa: E501
            'root': (MediaRootMini,),  # noqa: E501
            'modified_by': (ElementsUserMini,),  # noqa: E501
            'is_excluded': (str, none_type,),  # noqa: E501
            'is_excluded_from_proxy_generation': (str, none_type,),  # noqa: E501
            'total_files': (int, none_type,),  # noqa: E501
            'needs_rescan': (bool,),  # noqa: E501
            'parent': (int, none_type,),  # noqa: E501
            'bundle': (int, none_type,),  # noqa: E501
            'bookmarked_by': ([int],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'volume': 'volume',  # noqa: E501
        'effective_custom_fields': 'effective_custom_fields',  # noqa: E501
        'full_path': 'full_path',  # noqa: E501
        'is_shared': 'is_shared',  # noqa: E501
        'is_hardlink': 'is_hardlink',  # noqa: E501
        'is_bookmarked': 'is_bookmarked',  # noqa: E501
        'exclusion_info': 'exclusion_info',  # noqa: E501
        'child_count': 'child_count',  # noqa: E501
        'name': 'name',  # noqa: E501
        'path': 'path',  # noqa: E501
        'pathhash': 'pathhash',  # noqa: E501
        'ancestry': 'ancestry',  # noqa: E501
        'is_dir': 'is_dir',  # noqa: E501
        'size': 'size',  # noqa: E501
        'mtime': 'mtime',  # noqa: E501
        'present': 'present',  # noqa: E501
        'is_showroom': 'is_showroom',  # noqa: E501
        'bundle_index': 'bundle_index',  # noqa: E501
        'modified': 'modified',  # noqa: E501
        'info': 'info',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'resolved_permission': 'resolved_permission',  # noqa: E501
        'parent_file': 'parent_file',  # noqa: E501
        'root': 'root',  # noqa: E501
        'modified_by': 'modified_by',  # noqa: E501
        'is_excluded': 'is_excluded',  # noqa: E501
        'is_excluded_from_proxy_generation': 'is_excluded_from_proxy_generation',  # noqa: E501
        'total_files': 'total_files',  # noqa: E501
        'needs_rescan': 'needs_rescan',  # noqa: E501
        'parent': 'parent',  # noqa: E501
        'bundle': 'bundle',  # noqa: E501
        'bookmarked_by': 'bookmarked_by',  # noqa: E501
    }

    read_only_vars = {
        'effective_custom_fields',  # noqa: E501
        'full_path',  # noqa: E501
        'is_shared',  # noqa: E501
        'is_hardlink',  # noqa: E501
        'is_bookmarked',  # noqa: E501
        'child_count',  # noqa: E501
        'name',  # noqa: E501
        'path',  # noqa: E501
        'pathhash',  # noqa: E501
        'ancestry',  # noqa: E501
        'is_dir',  # noqa: E501
        'size',  # noqa: E501
        'mtime',  # noqa: E501
        'present',  # noqa: E501
        'is_showroom',  # noqa: E501
        'bundle_index',  # noqa: E501
        'modified',  # noqa: E501
        'parent_file',  # noqa: E501
        'is_excluded',  # noqa: E501
        'is_excluded_from_proxy_generation',  # noqa: E501
        'parent',  # noqa: E501
        'bundle',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, volume, effective_custom_fields, full_path, is_shared, is_hardlink, is_bookmarked, exclusion_info, child_count, name, path, pathhash, ancestry, is_dir, size, mtime, present, is_showroom, bundle_index, modified, *args, **xkwargs):  # noqa: E501
        """MediaFile - a model defined in OpenAPI

        Args:
            id (int):
            volume (VolumeMini):
            effective_custom_fields ({str: (str, none_type)}, none_type):
            full_path (str):
            is_shared (bool, none_type):
            is_hardlink (bool):
            is_bookmarked (bool, none_type):
            exclusion_info (MediaFileExclusionInfo):
            child_count (int, none_type):
            name (str):
            path (str):
            pathhash (str):
            ancestry (str):
            is_dir (bool):
            size (int):
            mtime (int):
            present (bool):
            is_showroom (bool):
            bundle_index (int):
            modified (datetime):

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
            info ({str: (str, none_type)}): [optional]  # noqa: E501
            custom_fields ({str: (str, none_type)}): [optional]  # noqa: E501
            resolved_permission (MediaRootPermission): [optional]  # noqa: E501
            parent_file ({str: (str, none_type)}): [optional]  # noqa: E501
            root (MediaRootMini): [optional]  # noqa: E501
            modified_by (ElementsUserMini): [optional]  # noqa: E501
            is_excluded (str, none_type): [optional]  # noqa: E501
            is_excluded_from_proxy_generation (str, none_type): [optional]  # noqa: E501
            total_files (int, none_type): [optional]  # noqa: E501
            needs_rescan (bool): [optional]  # noqa: E501
            parent (int, none_type): [optional]  # noqa: E501
            bundle (int, none_type): [optional]  # noqa: E501
            bookmarked_by ([int]): [optional]  # noqa: E501
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
        self.volume = volume
        self.effective_custom_fields = effective_custom_fields
        self.full_path = full_path
        self.is_shared = is_shared
        self.is_hardlink = is_hardlink
        self.is_bookmarked = is_bookmarked
        self.exclusion_info = exclusion_info
        self.child_count = child_count
        self.name = name
        self.path = path
        self.pathhash = pathhash
        self.ancestry = ancestry
        self.is_dir = is_dir
        self.size = size
        self.mtime = mtime
        self.present = present
        self.is_showroom = is_showroom
        self.bundle_index = bundle_index
        self.modified = modified
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
    def __init__(self, id, volume, exclusion_info, *args, **xkwargs):  # noqa: E501
        """MediaFile - a model defined in OpenAPI

        Args:
            id (int):
            volume (VolumeMini):
            exclusion_info (MediaFileExclusionInfo):
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
            info ({str: (str, none_type)}): [optional]  # noqa: E501
            custom_fields ({str: (str, none_type)}): [optional]  # noqa: E501
            resolved_permission (MediaRootPermission): [optional]  # noqa: E501
            parent_file ({str: (str, none_type)}): [optional]  # noqa: E501
            root (MediaRootMini): [optional]  # noqa: E501
            modified_by (ElementsUserMini): [optional]  # noqa: E501
            is_excluded (str, none_type): [optional]  # noqa: E501
            is_excluded_from_proxy_generation (str, none_type): [optional]  # noqa: E501
            total_files (int, none_type): [optional]  # noqa: E501
            needs_rescan (bool): [optional]  # noqa: E501
            parent (int, none_type): [optional]  # noqa: E501
            bundle (int, none_type): [optional]  # noqa: E501
            bookmarked_by ([int]): [optional]  # noqa: E501
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
        self.volume = volume
        self.exclusion_info = exclusion_info
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

