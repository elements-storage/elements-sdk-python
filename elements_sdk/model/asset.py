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
    from elements_sdk.model.format_metadata import FormatMetadata
    from elements_sdk.model.media_file_bundle_mini import MediaFileBundleMini
    from elements_sdk.model.media_root_permission import MediaRootPermission
    from elements_sdk.model.proxy import Proxy
    globals()['ElementsUserMini'] = ElementsUserMini
    globals()['FormatMetadata'] = FormatMetadata
    globals()['MediaFileBundleMini'] = MediaFileBundleMini
    globals()['MediaRootPermission'] = MediaRootPermission
    globals()['Proxy'] = Proxy


class Asset(ModelNormal):
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
        ('display_name',): {
            'min_length': 1,
        },
        ('checksum',): {
            'min_length': 1,
        },
        ('type',): {
            'min_length': 1,
        },
        ('matched_scanner',): {
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
            'info': ({str: (str, none_type)},),  # noqa: E501
            'proxy_info': ({str: (str, none_type)},),  # noqa: E501
            'custom_fields': ({str: (str, none_type)},),  # noqa: E501
            'tags': ([int],),  # noqa: E501
            'backups': (str,),  # noqa: E501
            'proxies_generated': (bool,),  # noqa: E501
            'proxies_failed': (bool,),  # noqa: E501
            'bundles': ([MediaFileBundleMini],),  # noqa: E501
            'format': (FormatMetadata,),  # noqa: E501
            'sync_id': (str,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'has_files': (bool,),  # noqa: E501
            'has_backups': (bool,),  # noqa: E501
            'has_cloud_links': (bool,),  # noqa: E501
            'checksum': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'thumbnail_generated': (bool,),  # noqa: E501
            'matched_scanner': (str,),  # noqa: E501
            'workflow_state': (int,),  # noqa: E501
            'is_temporary': (bool,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'modified': (datetime,),  # noqa: E501
            'proxies': ([Proxy],),  # noqa: E501
            'default_proxy': (Proxy,),  # noqa: E501
            'resolved_permission': (MediaRootPermission,),  # noqa: E501
            'modified_by': (ElementsUserMini,),  # noqa: E501
            'rating': (int, none_type,),  # noqa: E501
            'set': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'info': 'info',  # noqa: E501
        'proxy_info': 'proxy_info',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'backups': 'backups',  # noqa: E501
        'proxies_generated': 'proxies_generated',  # noqa: E501
        'proxies_failed': 'proxies_failed',  # noqa: E501
        'bundles': 'bundles',  # noqa: E501
        'format': 'format',  # noqa: E501
        'sync_id': 'sync_id',  # noqa: E501
        'display_name': 'display_name',  # noqa: E501
        'has_files': 'has_files',  # noqa: E501
        'has_backups': 'has_backups',  # noqa: E501
        'has_cloud_links': 'has_cloud_links',  # noqa: E501
        'checksum': 'checksum',  # noqa: E501
        'type': 'type',  # noqa: E501
        'thumbnail_generated': 'thumbnail_generated',  # noqa: E501
        'matched_scanner': 'matched_scanner',  # noqa: E501
        'workflow_state': 'workflow_state',  # noqa: E501
        'is_temporary': 'is_temporary',  # noqa: E501
        'created': 'created',  # noqa: E501
        'modified': 'modified',  # noqa: E501
        'proxies': 'proxies',  # noqa: E501
        'default_proxy': 'default_proxy',  # noqa: E501
        'resolved_permission': 'resolved_permission',  # noqa: E501
        'modified_by': 'modified_by',  # noqa: E501
        'rating': 'rating',  # noqa: E501
        'set': 'set',  # noqa: E501
    }

    read_only_vars = {
        'info',  # noqa: E501
        'proxy_info',  # noqa: E501
        'backups',  # noqa: E501
        'proxies_generated',  # noqa: E501
        'proxies_failed',  # noqa: E501
        'bundles',  # noqa: E501
        'sync_id',  # noqa: E501
        'display_name',  # noqa: E501
        'has_files',  # noqa: E501
        'has_backups',  # noqa: E501
        'has_cloud_links',  # noqa: E501
        'checksum',  # noqa: E501
        'type',  # noqa: E501
        'thumbnail_generated',  # noqa: E501
        'matched_scanner',  # noqa: E501
        'workflow_state',  # noqa: E501
        'is_temporary',  # noqa: E501
        'created',  # noqa: E501
        'modified',  # noqa: E501
        'proxies',  # noqa: E501
        'rating',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, info, proxy_info, custom_fields, tags, backups, proxies_generated, proxies_failed, bundles, format, sync_id, display_name, has_files, has_backups, has_cloud_links, checksum, type, thumbnail_generated, matched_scanner, workflow_state, is_temporary, created, modified, *args, **xkwargs):  # noqa: E501
        """Asset - a model defined in OpenAPI

        Args:
            id (int):
            info ({str: (str, none_type)}):
            proxy_info ({str: (str, none_type)}):
            custom_fields ({str: (str, none_type)}):
            tags ([int]):
            backups (str):
            proxies_generated (bool):
            proxies_failed (bool):
            bundles ([MediaFileBundleMini]):
            format (FormatMetadata):
            sync_id (str):
            display_name (str):
            has_files (bool):
            has_backups (bool):
            has_cloud_links (bool):
            checksum (str):
            type (str):
            thumbnail_generated (bool):
            matched_scanner (str):
            workflow_state (int):
            is_temporary (bool):
            created (datetime):
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
            proxies ([Proxy]): [optional]  # noqa: E501
            default_proxy (Proxy): [optional]  # noqa: E501
            resolved_permission (MediaRootPermission): [optional]  # noqa: E501
            modified_by (ElementsUserMini): [optional]  # noqa: E501
            rating (int, none_type): [optional]  # noqa: E501
            set (int, none_type): [optional]  # noqa: E501
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
        self.info = info
        self.proxy_info = proxy_info
        self.custom_fields = custom_fields
        self.tags = tags
        self.backups = backups
        self.proxies_generated = proxies_generated
        self.proxies_failed = proxies_failed
        self.bundles = bundles
        self.format = format
        self.sync_id = sync_id
        self.display_name = display_name
        self.has_files = has_files
        self.has_backups = has_backups
        self.has_cloud_links = has_cloud_links
        self.checksum = checksum
        self.type = type
        self.thumbnail_generated = thumbnail_generated
        self.matched_scanner = matched_scanner
        self.workflow_state = workflow_state
        self.is_temporary = is_temporary
        self.created = created
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
    def __init__(self, id, custom_fields, tags, format, *args, **xkwargs):  # noqa: E501
        """Asset - a model defined in OpenAPI

        Args:
            id (int):
            custom_fields ({str: (str, none_type)}):
            tags ([int]):
            format (FormatMetadata):
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
            proxies ([Proxy]): [optional]  # noqa: E501
            default_proxy (Proxy): [optional]  # noqa: E501
            resolved_permission (MediaRootPermission): [optional]  # noqa: E501
            modified_by (ElementsUserMini): [optional]  # noqa: E501
            rating (int, none_type): [optional]  # noqa: E501
            set (int, none_type): [optional]  # noqa: E501
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
        self.custom_fields = custom_fields
        self.tags = tags
        self.format = format
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
