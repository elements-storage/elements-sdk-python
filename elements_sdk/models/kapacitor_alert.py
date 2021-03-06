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


class KapacitorAlert(object):
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
        'level': 'str',
        'message': 'str',
        'details': 'str',
        'data': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'level': 'level',
        'message': 'message',
        'details': 'details',
        'data': 'data'
    }

    def __init__(self, id=None, level=None, message=None, details=None, data=None, local_vars_configuration=None):  # noqa: E501
        """KapacitorAlert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._level = None
        self._message = None
        self._details = None
        self._data = None
        self.discriminator = None

        self.id = id
        self.level = level
        self.message = message
        self.details = details
        self.data = data

    @property
    def id(self):
        """Gets the id of this KapacitorAlert.  # noqa: E501


        :return: The id of this KapacitorAlert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KapacitorAlert.


        :param id: The id of this KapacitorAlert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def level(self):
        """Gets the level of this KapacitorAlert.  # noqa: E501


        :return: The level of this KapacitorAlert.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this KapacitorAlert.


        :param level: The level of this KapacitorAlert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and level is None:  # noqa: E501
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                level is not None and len(level) < 1):
            raise ValueError("Invalid value for `level`, length must be greater than or equal to `1`")  # noqa: E501

        self._level = level

    @property
    def message(self):
        """Gets the message of this KapacitorAlert.  # noqa: E501


        :return: The message of this KapacitorAlert.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this KapacitorAlert.


        :param message: The message of this KapacitorAlert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) < 1):
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501

        self._message = message

    @property
    def details(self):
        """Gets the details of this KapacitorAlert.  # noqa: E501


        :return: The details of this KapacitorAlert.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this KapacitorAlert.


        :param details: The details of this KapacitorAlert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and details is None:  # noqa: E501
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                details is not None and len(details) < 1):
            raise ValueError("Invalid value for `details`, length must be greater than or equal to `1`")  # noqa: E501

        self._details = details

    @property
    def data(self):
        """Gets the data of this KapacitorAlert.  # noqa: E501


        :return: The data of this KapacitorAlert.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this KapacitorAlert.


        :param data: The data of this KapacitorAlert.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, KapacitorAlert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KapacitorAlert):
            return True

        return self.to_dict() != other.to_dict()
