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


class VolumeSNFSStatus(object):
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
        'stripe_groups': 'list[SNFSStripeGroup]'
    }

    attribute_map = {
        'stripe_groups': 'stripe_groups'
    }

    def __init__(self, stripe_groups=None, local_vars_configuration=None):  # noqa: E501
        """VolumeSNFSStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stripe_groups = None
        self.discriminator = None

        self.stripe_groups = stripe_groups

    @property
    def stripe_groups(self):
        """Gets the stripe_groups of this VolumeSNFSStatus.  # noqa: E501


        :return: The stripe_groups of this VolumeSNFSStatus.  # noqa: E501
        :rtype: list[SNFSStripeGroup]
        """
        return self._stripe_groups

    @stripe_groups.setter
    def stripe_groups(self, stripe_groups):
        """Sets the stripe_groups of this VolumeSNFSStatus.


        :param stripe_groups: The stripe_groups of this VolumeSNFSStatus.  # noqa: E501
        :type: list[SNFSStripeGroup]
        """
        if self.local_vars_configuration.client_side_validation and stripe_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_groups`, must not be `None`")  # noqa: E501

        self._stripe_groups = stripe_groups

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
        if not isinstance(other, VolumeSNFSStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeSNFSStatus):
            return True

        return self.to_dict() != other.to_dict()
