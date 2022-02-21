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
    from elements_sdk.model.elements_user_mini_reference import ElementsUserMiniReference
    from elements_sdk.model.one_time_access_token_activity import OneTimeAccessTokenActivity
    from elements_sdk.model.one_time_access_token_shared_object import OneTimeAccessTokenSharedObject
    globals()['ElementsUserMini'] = ElementsUserMini
    globals()['ElementsUserMiniReference'] = ElementsUserMiniReference
    globals()['OneTimeAccessTokenActivity'] = OneTimeAccessTokenActivity
    globals()['OneTimeAccessTokenSharedObject'] = OneTimeAccessTokenSharedObject


class OneTimeAccessToken(ModelNormal):
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
        ('url',): {
            'max_length': 1023,
            'min_length': 1,
        },
        ('token',): {
            'max_length': 1023,
            'min_length': 1,
        },
        ('view_limit_left',): {
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
            'activity': ([OneTimeAccessTokenActivity],),  # noqa: E501
            'user': (ElementsUserMiniReference,),  # noqa: E501
            'created_by': (ElementsUserMini,),  # noqa: E501
            'shared_bundles': ([OneTimeAccessTokenSharedObject],),  # noqa: E501
            'shared_directories': ([OneTimeAccessTokenSharedObject],),  # noqa: E501
            'full_url': (str,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'token': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'is_easy_sharing_for_bundle': (int,),  # noqa: E501
            'is_easy_sharing_for_directory': (int,),  # noqa: E501
            'media_root_permissions': (str, none_type,),  # noqa: E501
            'view_limit_enabled': (bool,),  # noqa: E501
            'view_limit_left': (int,),  # noqa: E501
            'expires': (datetime, none_type,),  # noqa: E501
            'require_login': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'activity': 'activity',  # noqa: E501
        'user': 'user',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'shared_bundles': 'shared_bundles',  # noqa: E501
        'shared_directories': 'shared_directories',  # noqa: E501
        'full_url': 'full_url',  # noqa: E501
        'url': 'url',  # noqa: E501
        'token': 'token',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'is_easy_sharing_for_bundle': 'is_easy_sharing_for_bundle',  # noqa: E501
        'is_easy_sharing_for_directory': 'is_easy_sharing_for_directory',  # noqa: E501
        'media_root_permissions': 'media_root_permissions',  # noqa: E501
        'view_limit_enabled': 'view_limit_enabled',  # noqa: E501
        'view_limit_left': 'view_limit_left',  # noqa: E501
        'expires': 'expires',  # noqa: E501
        'require_login': 'require_login',  # noqa: E501
    }

    read_only_vars = {
        'activity',  # noqa: E501
        'shared_bundles',  # noqa: E501
        'shared_directories',  # noqa: E501
        'full_url',  # noqa: E501
        'created_at',  # noqa: E501
        'is_easy_sharing_for_bundle',  # noqa: E501
        'is_easy_sharing_for_directory',  # noqa: E501
        'media_root_permissions',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, activity, user, created_by, shared_bundles, shared_directories, full_url, url, token, created_at, is_easy_sharing_for_bundle, is_easy_sharing_for_directory, *args, **xkwargs):  # noqa: E501
        """OneTimeAccessToken - a model defined in OpenAPI

        Args:
            id (int):
            activity ([OneTimeAccessTokenActivity]):
            user (ElementsUserMiniReference):
            created_by (ElementsUserMini):
            shared_bundles ([OneTimeAccessTokenSharedObject]):
            shared_directories ([OneTimeAccessTokenSharedObject]):
            full_url (str):
            url (str):
            token (str):
            created_at (datetime):
            is_easy_sharing_for_bundle (int):
            is_easy_sharing_for_directory (int):

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
            media_root_permissions (str, none_type): [optional]  # noqa: E501
            view_limit_enabled (bool): [optional]  # noqa: E501
            view_limit_left (int): [optional]  # noqa: E501
            expires (datetime, none_type): [optional]  # noqa: E501
            require_login (bool): [optional]  # noqa: E501
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
        self.activity = activity
        self.user = user
        self.created_by = created_by
        self.shared_bundles = shared_bundles
        self.shared_directories = shared_directories
        self.full_url = full_url
        self.url = url
        self.token = token
        self.created_at = created_at
        self.is_easy_sharing_for_bundle = is_easy_sharing_for_bundle
        self.is_easy_sharing_for_directory = is_easy_sharing_for_directory
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
    def __init__(self, id, user, created_by, url, token, *args, **xkwargs):  # noqa: E501
        """OneTimeAccessToken - a model defined in OpenAPI

        Args:
            id (int):
            user (ElementsUserMiniReference):
            created_by (ElementsUserMini):
            url (str):
            token (str):
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
            media_root_permissions (str, none_type): [optional]  # noqa: E501
            view_limit_enabled (bool): [optional]  # noqa: E501
            view_limit_left (int): [optional]  # noqa: E501
            expires (datetime, none_type): [optional]  # noqa: E501
            require_login (bool): [optional]  # noqa: E501
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
        self.user = user
        self.created_by = created_by
        self.url = url
        self.token = token
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