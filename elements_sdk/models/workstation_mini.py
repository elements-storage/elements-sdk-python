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


class WorkstationMini(object):
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
        'id': 'str',
        'display_name': 'str',
        'hostname': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'hostname': 'hostname'
    }

    def __init__(self, id=None, display_name=None, hostname=None, local_vars_configuration=None):  # noqa: E501
        """WorkstationMini - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._hostname = None
        self.discriminator = None

        self.id = id
        if display_name is not None:
            self.display_name = display_name
        self.hostname = hostname

    @property
    def id(self):
        """Gets the id of this WorkstationMini.  # noqa: E501


        :return: The id of this WorkstationMini.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkstationMini.


        :param id: The id of this WorkstationMini.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this WorkstationMini.  # noqa: E501


        :return: The display_name of this WorkstationMini.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this WorkstationMini.


        :param display_name: The display_name of this WorkstationMini.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def hostname(self):
        """Gets the hostname of this WorkstationMini.  # noqa: E501


        :return: The hostname of this WorkstationMini.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this WorkstationMini.


        :param hostname: The hostname of this WorkstationMini.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) < 1):
            raise ValueError("Invalid value for `hostname`, length must be greater than or equal to `1`")  # noqa: E501

        self._hostname = hostname

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
        if not isinstance(other, WorkstationMini):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkstationMini):
            return True

        return self.to_dict() != other.to_dict()
