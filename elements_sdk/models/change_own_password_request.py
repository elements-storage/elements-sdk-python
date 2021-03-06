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


class ChangeOwnPasswordRequest(object):
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
        'current_password': 'str',
        'current_otp': 'str',
        'password': 'str'
    }

    attribute_map = {
        'current_password': 'current_password',
        'current_otp': 'current_otp',
        'password': 'password'
    }

    def __init__(self, current_password=None, current_otp=None, password=None, local_vars_configuration=None):  # noqa: E501
        """ChangeOwnPasswordRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_password = None
        self._current_otp = None
        self._password = None
        self.discriminator = None

        self.current_password = current_password
        self.current_otp = current_otp
        self.password = password

    @property
    def current_password(self):
        """Gets the current_password of this ChangeOwnPasswordRequest.  # noqa: E501


        :return: The current_password of this ChangeOwnPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._current_password

    @current_password.setter
    def current_password(self, current_password):
        """Sets the current_password of this ChangeOwnPasswordRequest.


        :param current_password: The current_password of this ChangeOwnPasswordRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and current_password is None:  # noqa: E501
            raise ValueError("Invalid value for `current_password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                current_password is not None and len(current_password) < 1):
            raise ValueError("Invalid value for `current_password`, length must be greater than or equal to `1`")  # noqa: E501

        self._current_password = current_password

    @property
    def current_otp(self):
        """Gets the current_otp of this ChangeOwnPasswordRequest.  # noqa: E501


        :return: The current_otp of this ChangeOwnPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._current_otp

    @current_otp.setter
    def current_otp(self, current_otp):
        """Sets the current_otp of this ChangeOwnPasswordRequest.


        :param current_otp: The current_otp of this ChangeOwnPasswordRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                current_otp is not None and len(current_otp) < 1):
            raise ValueError("Invalid value for `current_otp`, length must be greater than or equal to `1`")  # noqa: E501

        self._current_otp = current_otp

    @property
    def password(self):
        """Gets the password of this ChangeOwnPasswordRequest.  # noqa: E501


        :return: The password of this ChangeOwnPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ChangeOwnPasswordRequest.


        :param password: The password of this ChangeOwnPasswordRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 1):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

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
        if not isinstance(other, ChangeOwnPasswordRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeOwnPasswordRequest):
            return True

        return self.to_dict() != other.to_dict()
