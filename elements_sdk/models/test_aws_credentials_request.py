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


class TestAWSCredentialsRequest(object):
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
        'access_key_id': 'str',
        'secret_access_key': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'secret_access_key': 'secret_access_key'
    }

    def __init__(self, access_key_id=None, secret_access_key=None, local_vars_configuration=None):  # noqa: E501
        """TestAWSCredentialsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key_id = None
        self._secret_access_key = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    @property
    def access_key_id(self):
        """Gets the access_key_id of this TestAWSCredentialsRequest.  # noqa: E501


        :return: The access_key_id of this TestAWSCredentialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this TestAWSCredentialsRequest.


        :param access_key_id: The access_key_id of this TestAWSCredentialsRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `access_key_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                access_key_id is not None and len(access_key_id) < 1):
            raise ValueError("Invalid value for `access_key_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this TestAWSCredentialsRequest.  # noqa: E501


        :return: The secret_access_key of this TestAWSCredentialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this TestAWSCredentialsRequest.


        :param secret_access_key: The secret_access_key of this TestAWSCredentialsRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secret_access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `secret_access_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                secret_access_key is not None and len(secret_access_key) < 1):
            raise ValueError("Invalid value for `secret_access_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._secret_access_key = secret_access_key

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
        if not isinstance(other, TestAWSCredentialsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestAWSCredentialsRequest):
            return True

        return self.to_dict() != other.to_dict()
