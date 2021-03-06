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


class Stats(object):
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
        'cpu': 'list[CPUStat]',
        'ram': 'list[RAMStat]',
        'net': 'dict(str, list[NetStat])',
        'io': 'list[IOStat]'
    }

    attribute_map = {
        'cpu': 'cpu',
        'ram': 'ram',
        'net': 'net',
        'io': 'io'
    }

    def __init__(self, cpu=None, ram=None, net=None, io=None, local_vars_configuration=None):  # noqa: E501
        """Stats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu = None
        self._ram = None
        self._net = None
        self._io = None
        self.discriminator = None

        self.cpu = cpu
        self.ram = ram
        self.net = net
        self.io = io

    @property
    def cpu(self):
        """Gets the cpu of this Stats.  # noqa: E501


        :return: The cpu of this Stats.  # noqa: E501
        :rtype: list[CPUStat]
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this Stats.


        :param cpu: The cpu of this Stats.  # noqa: E501
        :type: list[CPUStat]
        """
        if self.local_vars_configuration.client_side_validation and cpu is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def ram(self):
        """Gets the ram of this Stats.  # noqa: E501


        :return: The ram of this Stats.  # noqa: E501
        :rtype: list[RAMStat]
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this Stats.


        :param ram: The ram of this Stats.  # noqa: E501
        :type: list[RAMStat]
        """
        if self.local_vars_configuration.client_side_validation and ram is None:  # noqa: E501
            raise ValueError("Invalid value for `ram`, must not be `None`")  # noqa: E501

        self._ram = ram

    @property
    def net(self):
        """Gets the net of this Stats.  # noqa: E501


        :return: The net of this Stats.  # noqa: E501
        :rtype: dict(str, list[NetStat])
        """
        return self._net

    @net.setter
    def net(self, net):
        """Sets the net of this Stats.


        :param net: The net of this Stats.  # noqa: E501
        :type: dict(str, list[NetStat])
        """
        if self.local_vars_configuration.client_side_validation and net is None:  # noqa: E501
            raise ValueError("Invalid value for `net`, must not be `None`")  # noqa: E501

        self._net = net

    @property
    def io(self):
        """Gets the io of this Stats.  # noqa: E501


        :return: The io of this Stats.  # noqa: E501
        :rtype: list[IOStat]
        """
        return self._io

    @io.setter
    def io(self, io):
        """Sets the io of this Stats.


        :param io: The io of this Stats.  # noqa: E501
        :type: list[IOStat]
        """
        if self.local_vars_configuration.client_side_validation and io is None:  # noqa: E501
            raise ValueError("Invalid value for `io`, must not be `None`")  # noqa: E501

        self._io = io

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
        if not isinstance(other, Stats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Stats):
            return True

        return self.to_dict() != other.to_dict()
