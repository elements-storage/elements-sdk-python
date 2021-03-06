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


class MemberPreview(object):
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
        'avatar': 'str',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'avatar': 'avatar',
        'email': 'email'
    }

    def __init__(self, id=None, avatar=None, email=None, local_vars_configuration=None):  # noqa: E501
        """MemberPreview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._avatar = None
        self._email = None
        self.discriminator = None

        self.id = id
        if avatar is not None:
            self.avatar = avatar
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this MemberPreview.  # noqa: E501


        :return: The id of this MemberPreview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MemberPreview.


        :param id: The id of this MemberPreview.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def avatar(self):
        """Gets the avatar of this MemberPreview.  # noqa: E501


        :return: The avatar of this MemberPreview.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this MemberPreview.


        :param avatar: The avatar of this MemberPreview.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                avatar is not None and len(avatar) < 1):
            raise ValueError("Invalid value for `avatar`, length must be greater than or equal to `1`")  # noqa: E501

        self._avatar = avatar

    @property
    def email(self):
        """Gets the email of this MemberPreview.  # noqa: E501


        :return: The email of this MemberPreview.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MemberPreview.


        :param email: The email of this MemberPreview.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

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
        if not isinstance(other, MemberPreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MemberPreview):
            return True

        return self.to_dict() != other.to_dict()
