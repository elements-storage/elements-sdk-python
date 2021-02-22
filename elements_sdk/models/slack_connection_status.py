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


class SlackConnectionStatus(object):
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
        'ok': 'bool',
        'team': 'str',
        'user': 'str',
        'url': 'str'
    }

    attribute_map = {
        'ok': 'ok',
        'team': 'team',
        'user': 'user',
        'url': 'url'
    }

    def __init__(self, ok=None, team=None, user=None, url=None, local_vars_configuration=None):  # noqa: E501
        """SlackConnectionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ok = None
        self._team = None
        self._user = None
        self._url = None
        self.discriminator = None

        self.ok = ok
        self.team = team
        self.user = user
        self.url = url

    @property
    def ok(self):
        """Gets the ok of this SlackConnectionStatus.  # noqa: E501


        :return: The ok of this SlackConnectionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._ok

    @ok.setter
    def ok(self, ok):
        """Sets the ok of this SlackConnectionStatus.


        :param ok: The ok of this SlackConnectionStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and ok is None:  # noqa: E501
            raise ValueError("Invalid value for `ok`, must not be `None`")  # noqa: E501

        self._ok = ok

    @property
    def team(self):
        """Gets the team of this SlackConnectionStatus.  # noqa: E501


        :return: The team of this SlackConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this SlackConnectionStatus.


        :param team: The team of this SlackConnectionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and team is None:  # noqa: E501
            raise ValueError("Invalid value for `team`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                team is not None and len(team) < 1):
            raise ValueError("Invalid value for `team`, length must be greater than or equal to `1`")  # noqa: E501

        self._team = team

    @property
    def user(self):
        """Gets the user of this SlackConnectionStatus.  # noqa: E501


        :return: The user of this SlackConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SlackConnectionStatus.


        :param user: The user of this SlackConnectionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user is not None and len(user) < 1):
            raise ValueError("Invalid value for `user`, length must be greater than or equal to `1`")  # noqa: E501

        self._user = user

    @property
    def url(self):
        """Gets the url of this SlackConnectionStatus.  # noqa: E501


        :return: The url of this SlackConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SlackConnectionStatus.


        :param url: The url of this SlackConnectionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 1):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, SlackConnectionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlackConnectionStatus):
            return True

        return self.to_dict() != other.to_dict()
