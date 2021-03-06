# coding: utf-8

"""
    ELEMENTS API

    The version of the OpenAPI document: 2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from elements_sdk.configuration import Configuration


class OneTimeAccessToken(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'activity': 'list[OneTimeAccessTokenActivity]',
        'user': 'ElementsUserMini',
        'created_by': 'ElementsUserMini',
        'media_root_permissions': 'str',
        'shared_bundles': 'list[OneTimeAccessTokenSharedObject]',
        'shared_directories': 'list[OneTimeAccessTokenSharedObject]',
        'full_url': 'str',
        'url': 'str',
        'token': 'str',
        'view_limit_enabled': 'bool',
        'view_limit_left': 'int',
        'expires': 'datetime',
        'require_login': 'bool',
        'is_easy_sharing_for_bundle': 'int',
        'is_easy_sharing_for_directory': 'int'
    }

    attribute_map = {
        'id': 'id',
        'activity': 'activity',
        'user': 'user',
        'created_by': 'created_by',
        'media_root_permissions': 'media_root_permissions',
        'shared_bundles': 'shared_bundles',
        'shared_directories': 'shared_directories',
        'full_url': 'full_url',
        'url': 'url',
        'token': 'token',
        'view_limit_enabled': 'view_limit_enabled',
        'view_limit_left': 'view_limit_left',
        'expires': 'expires',
        'require_login': 'require_login',
        'is_easy_sharing_for_bundle': 'is_easy_sharing_for_bundle',
        'is_easy_sharing_for_directory': 'is_easy_sharing_for_directory'
    }

    def __init__(self, id=None, activity=None, user=None, created_by=None, media_root_permissions=None, shared_bundles=None, shared_directories=None, full_url=None, url=None, token=None, view_limit_enabled=None, view_limit_left=None, expires=None, require_login=None, is_easy_sharing_for_bundle=None, is_easy_sharing_for_directory=None, local_vars_configuration=None):  # noqa: E501
        """OneTimeAccessToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._activity = None
        self._user = None
        self._created_by = None
        self._media_root_permissions = None
        self._shared_bundles = None
        self._shared_directories = None
        self._full_url = None
        self._url = None
        self._token = None
        self._view_limit_enabled = None
        self._view_limit_left = None
        self._expires = None
        self._require_login = None
        self._is_easy_sharing_for_bundle = None
        self._is_easy_sharing_for_directory = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if activity is not None:
            self.activity = activity
        self.user = user
        if created_by is not None:
            self.created_by = created_by
        if media_root_permissions is not None:
            self.media_root_permissions = media_root_permissions
        if shared_bundles is not None:
            self.shared_bundles = shared_bundles
        if shared_directories is not None:
            self.shared_directories = shared_directories
        if full_url is not None:
            self.full_url = full_url
        self.url = url
        self.token = token
        if view_limit_enabled is not None:
            self.view_limit_enabled = view_limit_enabled
        if view_limit_left is not None:
            self.view_limit_left = view_limit_left
        self.expires = expires
        if require_login is not None:
            self.require_login = require_login
        if is_easy_sharing_for_bundle is not None:
            self.is_easy_sharing_for_bundle = is_easy_sharing_for_bundle
        if is_easy_sharing_for_directory is not None:
            self.is_easy_sharing_for_directory = is_easy_sharing_for_directory

    @property
    def id(self):
        """Gets the id of this OneTimeAccessToken.  # noqa: E501


        :return: The id of this OneTimeAccessToken.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OneTimeAccessToken.


        :param id: The id of this OneTimeAccessToken.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def activity(self):
        """Gets the activity of this OneTimeAccessToken.  # noqa: E501


        :return: The activity of this OneTimeAccessToken.  # noqa: E501
        :rtype: list[OneTimeAccessTokenActivity]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this OneTimeAccessToken.


        :param activity: The activity of this OneTimeAccessToken.  # noqa: E501
        :type: list[OneTimeAccessTokenActivity]
        """

        self._activity = activity

    @property
    def user(self):
        """Gets the user of this OneTimeAccessToken.  # noqa: E501


        :return: The user of this OneTimeAccessToken.  # noqa: E501
        :rtype: ElementsUserMini
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OneTimeAccessToken.


        :param user: The user of this OneTimeAccessToken.  # noqa: E501
        :type: ElementsUserMini
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def created_by(self):
        """Gets the created_by of this OneTimeAccessToken.  # noqa: E501


        :return: The created_by of this OneTimeAccessToken.  # noqa: E501
        :rtype: ElementsUserMini
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OneTimeAccessToken.


        :param created_by: The created_by of this OneTimeAccessToken.  # noqa: E501
        :type: ElementsUserMini
        """

        self._created_by = created_by

    @property
    def media_root_permissions(self):
        """Gets the media_root_permissions of this OneTimeAccessToken.  # noqa: E501


        :return: The media_root_permissions of this OneTimeAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._media_root_permissions

    @media_root_permissions.setter
    def media_root_permissions(self, media_root_permissions):
        """Sets the media_root_permissions of this OneTimeAccessToken.


        :param media_root_permissions: The media_root_permissions of this OneTimeAccessToken.  # noqa: E501
        :type: str
        """

        self._media_root_permissions = media_root_permissions

    @property
    def shared_bundles(self):
        """Gets the shared_bundles of this OneTimeAccessToken.  # noqa: E501


        :return: The shared_bundles of this OneTimeAccessToken.  # noqa: E501
        :rtype: list[OneTimeAccessTokenSharedObject]
        """
        return self._shared_bundles

    @shared_bundles.setter
    def shared_bundles(self, shared_bundles):
        """Sets the shared_bundles of this OneTimeAccessToken.


        :param shared_bundles: The shared_bundles of this OneTimeAccessToken.  # noqa: E501
        :type: list[OneTimeAccessTokenSharedObject]
        """

        self._shared_bundles = shared_bundles

    @property
    def shared_directories(self):
        """Gets the shared_directories of this OneTimeAccessToken.  # noqa: E501


        :return: The shared_directories of this OneTimeAccessToken.  # noqa: E501
        :rtype: list[OneTimeAccessTokenSharedObject]
        """
        return self._shared_directories

    @shared_directories.setter
    def shared_directories(self, shared_directories):
        """Sets the shared_directories of this OneTimeAccessToken.


        :param shared_directories: The shared_directories of this OneTimeAccessToken.  # noqa: E501
        :type: list[OneTimeAccessTokenSharedObject]
        """

        self._shared_directories = shared_directories

    @property
    def full_url(self):
        """Gets the full_url of this OneTimeAccessToken.  # noqa: E501


        :return: The full_url of this OneTimeAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._full_url

    @full_url.setter
    def full_url(self, full_url):
        """Sets the full_url of this OneTimeAccessToken.


        :param full_url: The full_url of this OneTimeAccessToken.  # noqa: E501
        :type: str
        """

        self._full_url = full_url

    @property
    def url(self):
        """Gets the url of this OneTimeAccessToken.  # noqa: E501


        :return: The url of this OneTimeAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OneTimeAccessToken.


        :param url: The url of this OneTimeAccessToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) > 1023):
            raise ValueError("Invalid value for `url`, length must be less than or equal to `1023`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 1):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

    @property
    def token(self):
        """Gets the token of this OneTimeAccessToken.  # noqa: E501


        :return: The token of this OneTimeAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this OneTimeAccessToken.


        :param token: The token of this OneTimeAccessToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token is not None and len(token) > 1023):
            raise ValueError("Invalid value for `token`, length must be less than or equal to `1023`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token is not None and len(token) < 1):
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `1`")  # noqa: E501

        self._token = token

    @property
    def view_limit_enabled(self):
        """Gets the view_limit_enabled of this OneTimeAccessToken.  # noqa: E501


        :return: The view_limit_enabled of this OneTimeAccessToken.  # noqa: E501
        :rtype: bool
        """
        return self._view_limit_enabled

    @view_limit_enabled.setter
    def view_limit_enabled(self, view_limit_enabled):
        """Sets the view_limit_enabled of this OneTimeAccessToken.


        :param view_limit_enabled: The view_limit_enabled of this OneTimeAccessToken.  # noqa: E501
        :type: bool
        """

        self._view_limit_enabled = view_limit_enabled

    @property
    def view_limit_left(self):
        """Gets the view_limit_left of this OneTimeAccessToken.  # noqa: E501


        :return: The view_limit_left of this OneTimeAccessToken.  # noqa: E501
        :rtype: int
        """
        return self._view_limit_left

    @view_limit_left.setter
    def view_limit_left(self, view_limit_left):
        """Sets the view_limit_left of this OneTimeAccessToken.


        :param view_limit_left: The view_limit_left of this OneTimeAccessToken.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                view_limit_left is not None and view_limit_left > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `view_limit_left`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                view_limit_left is not None and view_limit_left < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `view_limit_left`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._view_limit_left = view_limit_left

    @property
    def expires(self):
        """Gets the expires of this OneTimeAccessToken.  # noqa: E501


        :return: The expires of this OneTimeAccessToken.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this OneTimeAccessToken.


        :param expires: The expires of this OneTimeAccessToken.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

    @property
    def require_login(self):
        """Gets the require_login of this OneTimeAccessToken.  # noqa: E501


        :return: The require_login of this OneTimeAccessToken.  # noqa: E501
        :rtype: bool
        """
        return self._require_login

    @require_login.setter
    def require_login(self, require_login):
        """Sets the require_login of this OneTimeAccessToken.


        :param require_login: The require_login of this OneTimeAccessToken.  # noqa: E501
        :type: bool
        """

        self._require_login = require_login

    @property
    def is_easy_sharing_for_bundle(self):
        """Gets the is_easy_sharing_for_bundle of this OneTimeAccessToken.  # noqa: E501


        :return: The is_easy_sharing_for_bundle of this OneTimeAccessToken.  # noqa: E501
        :rtype: int
        """
        return self._is_easy_sharing_for_bundle

    @is_easy_sharing_for_bundle.setter
    def is_easy_sharing_for_bundle(self, is_easy_sharing_for_bundle):
        """Sets the is_easy_sharing_for_bundle of this OneTimeAccessToken.


        :param is_easy_sharing_for_bundle: The is_easy_sharing_for_bundle of this OneTimeAccessToken.  # noqa: E501
        :type: int
        """

        self._is_easy_sharing_for_bundle = is_easy_sharing_for_bundle

    @property
    def is_easy_sharing_for_directory(self):
        """Gets the is_easy_sharing_for_directory of this OneTimeAccessToken.  # noqa: E501


        :return: The is_easy_sharing_for_directory of this OneTimeAccessToken.  # noqa: E501
        :rtype: int
        """
        return self._is_easy_sharing_for_directory

    @is_easy_sharing_for_directory.setter
    def is_easy_sharing_for_directory(self, is_easy_sharing_for_directory):
        """Sets the is_easy_sharing_for_directory of this OneTimeAccessToken.


        :param is_easy_sharing_for_directory: The is_easy_sharing_for_directory of this OneTimeAccessToken.  # noqa: E501
        :type: int
        """

        self._is_easy_sharing_for_directory = is_easy_sharing_for_directory

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OneTimeAccessToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneTimeAccessToken):
            return True

        return self.to_dict() != other.to_dict()
