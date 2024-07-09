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



class ParametersUpdate(ModelNormal):
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
        ('https_redirect',): {
            'None': None,
            'DOMAIN': "domain",
            'ON': "on",
        },
        ('language',): {
            'EN': "en",
            'FR': "fr",
            'DE': "de",
            'IT': "it",
            'PT': "pt",
            'ES': "es",
            'DA': "da",
            'XX': "xx",
        },
        ('media_default_custom_field_type',): {
            'FILE': "file",
            'ASSET': "asset",
        },
        ('media_default_delete_behaviour',): {
            'DISK': "disk",
            'DATABASE': "database",
            'COMPLETELY': "completely",
        },
        ('media_shuttle_left_behaviour',): {
            'SLOWDOWN': "slowdown",
            'STOP': "stop",
        },
        ('otp_policy',): {
            'ADMIN-ONLY': "admin-only",
            'SELF-SERVICE-SETUP-ONLY': "self-service-setup-only",
            'SELF-SERVICE-ALL': "self-service-all",
        },
    }

    validations = {
        ('external_url',): {
            'max_length': 128,
        },
        ('ltfs_library_address',): {
            'max_length': 255,
        },
        ('media_max_link_views',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('users_default_permissions',): {
            'max_length': 255,
        },
        ('workspaces_path',): {
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
            'analytics': (bool,),  # noqa: E501
            'branding_css': (str,),  # noqa: E501
            'branding_logo': (str,),  # noqa: E501
            'email_logo_url': (str, none_type,),  # noqa: E501
            'client_offer_file_search': (bool,),  # noqa: E501
            'external_url': (str, none_type,),  # noqa: E501
            'file_manager_recycle_bin': (bool,),  # noqa: E501
            'https_redirect': (str, none_type,),  # noqa: E501
            'language': (str,),  # noqa: E501
            'ltfs_default_restore_to_original_location': (bool,),  # noqa: E501
            'ltfs_default_search_directories': (bool,),  # noqa: E501
            'ltfs_library_address': (str, none_type,),  # noqa: E501
            'mail_styling': ({str: (str, none_type)},),  # noqa: E501
            'media_allow_anonymous_links': (bool,),  # noqa: E501
            'media_auto_play': (bool,),  # noqa: E501
            'media_auto_proxy': (bool,),  # noqa: E501
            'media_auto_scan': (bool,),  # noqa: E501
            'media_auto_transport': (bool,),  # noqa: E501
            'media_background_auto_pause': (bool,),  # noqa: E501
            'media_default_custom_field_type': (str,),  # noqa: E501
            'media_default_delete_behaviour': (str,),  # noqa: E501
            'media_detect_versions': (bool,),  # noqa: E501
            'media_force_show_deleted': (bool, none_type,),  # noqa: E501
            'media_keep_selection_when_browsing': (bool,),  # noqa: E501
            'media_recycle_bin': (bool,),  # noqa: E501
            'media_require_link_password': (bool,),  # noqa: E501
            'media_max_link_views': (int, none_type,),  # noqa: E501
            'media_shuttle_left_behaviour': (str,),  # noqa: E501
            'ntp_offer_sync': (bool,),  # noqa: E501
            'otp_policy': (str,),  # noqa: E501
            'password_login': (bool,),  # noqa: E501
            'session_key_restrict_to_ip': (bool,),  # noqa: E501
            'tasks_run_scheduled': (bool,),  # noqa: E501
            'users_default_permissions': (str,),  # noqa: E501
            'user_notification_settings': (bool,),  # noqa: E501
            'workspaces_path': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'analytics': 'analytics',  # noqa: E501
        'branding_css': 'branding_css',  # noqa: E501
        'branding_logo': 'branding_logo',  # noqa: E501
        'email_logo_url': 'email_logo_url',  # noqa: E501
        'client_offer_file_search': 'client_offer_file_search',  # noqa: E501
        'external_url': 'external_url',  # noqa: E501
        'file_manager_recycle_bin': 'file_manager_recycle_bin',  # noqa: E501
        'https_redirect': 'https_redirect',  # noqa: E501
        'language': 'language',  # noqa: E501
        'ltfs_default_restore_to_original_location': 'ltfs_default_restore_to_original_location',  # noqa: E501
        'ltfs_default_search_directories': 'ltfs_default_search_directories',  # noqa: E501
        'ltfs_library_address': 'ltfs_library_address',  # noqa: E501
        'mail_styling': 'mail_styling',  # noqa: E501
        'media_allow_anonymous_links': 'media_allow_anonymous_links',  # noqa: E501
        'media_auto_play': 'media_auto_play',  # noqa: E501
        'media_auto_proxy': 'media_auto_proxy',  # noqa: E501
        'media_auto_scan': 'media_auto_scan',  # noqa: E501
        'media_auto_transport': 'media_auto_transport',  # noqa: E501
        'media_background_auto_pause': 'media_background_auto_pause',  # noqa: E501
        'media_default_custom_field_type': 'media_default_custom_field_type',  # noqa: E501
        'media_default_delete_behaviour': 'media_default_delete_behaviour',  # noqa: E501
        'media_detect_versions': 'media_detect_versions',  # noqa: E501
        'media_force_show_deleted': 'media_force_show_deleted',  # noqa: E501
        'media_keep_selection_when_browsing': 'media_keep_selection_when_browsing',  # noqa: E501
        'media_recycle_bin': 'media_recycle_bin',  # noqa: E501
        'media_require_link_password': 'media_require_link_password',  # noqa: E501
        'media_max_link_views': 'media_max_link_views',  # noqa: E501
        'media_shuttle_left_behaviour': 'media_shuttle_left_behaviour',  # noqa: E501
        'ntp_offer_sync': 'ntp_offer_sync',  # noqa: E501
        'otp_policy': 'otp_policy',  # noqa: E501
        'password_login': 'password_login',  # noqa: E501
        'session_key_restrict_to_ip': 'session_key_restrict_to_ip',  # noqa: E501
        'tasks_run_scheduled': 'tasks_run_scheduled',  # noqa: E501
        'users_default_permissions': 'users_default_permissions',  # noqa: E501
        'user_notification_settings': 'user_notification_settings',  # noqa: E501
        'workspaces_path': 'workspaces_path',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **xkwargs):  # noqa: E501
        """ParametersUpdate - a model defined in OpenAPI

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
            analytics (bool): [optional]  # noqa: E501
            branding_css (str): [optional]  # noqa: E501
            branding_logo (str): [optional]  # noqa: E501
            email_logo_url (str, none_type): [optional]  # noqa: E501
            client_offer_file_search (bool): [optional]  # noqa: E501
            external_url (str, none_type): http://host/. [optional]  # noqa: E501
            file_manager_recycle_bin (bool): Recycle bins are usually either in Workspace/Share or Volume folder. [optional]  # noqa: E501
            https_redirect (str, none_type): [optional]  # noqa: E501
            language (str): [optional]  # noqa: E501
            ltfs_default_restore_to_original_location (bool): [optional]  # noqa: E501
            ltfs_default_search_directories (bool): [optional]  # noqa: E501
            ltfs_library_address (str, none_type): [optional]  # noqa: E501
            mail_styling ({str: (str, none_type)}): [optional]  # noqa: E501
            media_allow_anonymous_links (bool): [optional]  # noqa: E501
            media_auto_play (bool): [optional]  # noqa: E501
            media_auto_proxy (bool): [optional]  # noqa: E501
            media_auto_scan (bool): [optional]  # noqa: E501
            media_auto_transport (bool): [optional]  # noqa: E501
            media_background_auto_pause (bool): [optional]  # noqa: E501
            media_default_custom_field_type (str): [optional]  # noqa: E501
            media_default_delete_behaviour (str): [optional]  # noqa: E501
            media_detect_versions (bool): [optional]  # noqa: E501
            media_force_show_deleted (bool, none_type): [optional]  # noqa: E501
            media_keep_selection_when_browsing (bool): [optional]  # noqa: E501
            media_recycle_bin (bool): Recycle bin is usually in the .recycle-bin folder in the volume root. [optional]  # noqa: E501
            media_require_link_password (bool): [optional]  # noqa: E501
            media_max_link_views (int, none_type): [optional]  # noqa: E501
            media_shuttle_left_behaviour (str): [optional]  # noqa: E501
            ntp_offer_sync (bool): [optional]  # noqa: E501
            otp_policy (str): [optional]  # noqa: E501
            password_login (bool): [optional]  # noqa: E501
            session_key_restrict_to_ip (bool): [optional]  # noqa: E501
            tasks_run_scheduled (bool): [optional]  # noqa: E501
            users_default_permissions (str): Copy this value from an existing user. [optional]  # noqa: E501
            user_notification_settings (bool): [optional]  # noqa: E501
            workspaces_path (str): [optional]  # noqa: E501
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
        """ParametersUpdate - a model defined in OpenAPI

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
            analytics (bool): [optional]  # noqa: E501
            branding_css (str): [optional]  # noqa: E501
            branding_logo (str): [optional]  # noqa: E501
            email_logo_url (str, none_type): [optional]  # noqa: E501
            client_offer_file_search (bool): [optional]  # noqa: E501
            external_url (str, none_type): http://host/. [optional]  # noqa: E501
            file_manager_recycle_bin (bool): Recycle bins are usually either in Workspace/Share or Volume folder. [optional]  # noqa: E501
            https_redirect (str, none_type): [optional]  # noqa: E501
            language (str): [optional]  # noqa: E501
            ltfs_default_restore_to_original_location (bool): [optional]  # noqa: E501
            ltfs_default_search_directories (bool): [optional]  # noqa: E501
            ltfs_library_address (str, none_type): [optional]  # noqa: E501
            mail_styling ({str: (str, none_type)}): [optional]  # noqa: E501
            media_allow_anonymous_links (bool): [optional]  # noqa: E501
            media_auto_play (bool): [optional]  # noqa: E501
            media_auto_proxy (bool): [optional]  # noqa: E501
            media_auto_scan (bool): [optional]  # noqa: E501
            media_auto_transport (bool): [optional]  # noqa: E501
            media_background_auto_pause (bool): [optional]  # noqa: E501
            media_default_custom_field_type (str): [optional]  # noqa: E501
            media_default_delete_behaviour (str): [optional]  # noqa: E501
            media_detect_versions (bool): [optional]  # noqa: E501
            media_force_show_deleted (bool, none_type): [optional]  # noqa: E501
            media_keep_selection_when_browsing (bool): [optional]  # noqa: E501
            media_recycle_bin (bool): Recycle bin is usually in the .recycle-bin folder in the volume root. [optional]  # noqa: E501
            media_require_link_password (bool): [optional]  # noqa: E501
            media_max_link_views (int, none_type): [optional]  # noqa: E501
            media_shuttle_left_behaviour (str): [optional]  # noqa: E501
            ntp_offer_sync (bool): [optional]  # noqa: E501
            otp_policy (str): [optional]  # noqa: E501
            password_login (bool): [optional]  # noqa: E501
            session_key_restrict_to_ip (bool): [optional]  # noqa: E501
            tasks_run_scheduled (bool): [optional]  # noqa: E501
            users_default_permissions (str): Copy this value from an existing user. [optional]  # noqa: E501
            user_notification_settings (bool): [optional]  # noqa: E501
            workspaces_path (str): [optional]  # noqa: E501
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

