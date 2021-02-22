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


class TestAWSCredentialsResponse(object):
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
        'arn': 'str',
        'account': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'ok': 'ok',
        'arn': 'arn',
        'account': 'account',
        'user_id': 'user_id'
    }

    def __init__(self, ok=None, arn=None, account=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """TestAWSCredentialsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ok = None
        self._arn = None
        self._account = None
        self._user_id = None
        self.discriminator = None

        self.ok = ok
        if arn is not None:
            self.arn = arn
        if account is not None:
            self.account = account
        if user_id is not None:
            self.user_id = user_id

    @property
    def ok(self):
        """Gets the ok of this TestAWSCredentialsResponse.  # noqa: E501


        :return: The ok of this TestAWSCredentialsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._ok

    @ok.setter
    def ok(self, ok):
        """Sets the ok of this TestAWSCredentialsResponse.


        :param ok: The ok of this TestAWSCredentialsResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and ok is None:  # noqa: E501
            raise ValueError("Invalid value for `ok`, must not be `None`")  # noqa: E501

        self._ok = ok

    @property
    def arn(self):
        """Gets the arn of this TestAWSCredentialsResponse.  # noqa: E501


        :return: The arn of this TestAWSCredentialsResponse.  # noqa: E501
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, arn):
        """Sets the arn of this TestAWSCredentialsResponse.


        :param arn: The arn of this TestAWSCredentialsResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                arn is not None and len(arn) < 1):
            raise ValueError("Invalid value for `arn`, length must be greater than or equal to `1`")  # noqa: E501

        self._arn = arn

    @property
    def account(self):
        """Gets the account of this TestAWSCredentialsResponse.  # noqa: E501


        :return: The account of this TestAWSCredentialsResponse.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this TestAWSCredentialsResponse.


        :param account: The account of this TestAWSCredentialsResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                account is not None and len(account) < 1):
            raise ValueError("Invalid value for `account`, length must be greater than or equal to `1`")  # noqa: E501

        self._account = account

    @property
    def user_id(self):
        """Gets the user_id of this TestAWSCredentialsResponse.  # noqa: E501


        :return: The user_id of this TestAWSCredentialsResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TestAWSCredentialsResponse.


        :param user_id: The user_id of this TestAWSCredentialsResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) < 1):
            raise ValueError("Invalid value for `user_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_id = user_id

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
        if not isinstance(other, TestAWSCredentialsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestAWSCredentialsResponse):
            return True

        return self.to_dict() != other.to_dict()
