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


class Quota(object):
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
        'current': 'int',
        'soft': 'int',
        'hard': 'int'
    }

    attribute_map = {
        'current': 'current',
        'soft': 'soft',
        'hard': 'hard'
    }

    def __init__(self, current=None, soft=None, hard=None, local_vars_configuration=None):  # noqa: E501
        """Quota - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current = None
        self._soft = None
        self._hard = None
        self.discriminator = None

        self.current = current
        self.soft = soft
        self.hard = hard

    @property
    def current(self):
        """Gets the current of this Quota.  # noqa: E501


        :return: The current of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this Quota.


        :param current: The current of this Quota.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and current is None:  # noqa: E501
            raise ValueError("Invalid value for `current`, must not be `None`")  # noqa: E501

        self._current = current

    @property
    def soft(self):
        """Gets the soft of this Quota.  # noqa: E501


        :return: The soft of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._soft

    @soft.setter
    def soft(self, soft):
        """Sets the soft of this Quota.


        :param soft: The soft of this Quota.  # noqa: E501
        :type: int
        """

        self._soft = soft

    @property
    def hard(self):
        """Gets the hard of this Quota.  # noqa: E501


        :return: The hard of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._hard

    @hard.setter
    def hard(self, hard):
        """Sets the hard of this Quota.


        :param hard: The hard of this Quota.  # noqa: E501
        :type: int
        """

        self._hard = hard

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
        if not isinstance(other, Quota):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Quota):
            return True

        return self.to_dict() != other.to_dict()
