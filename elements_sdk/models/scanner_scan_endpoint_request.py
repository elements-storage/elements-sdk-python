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


class ScannerScanEndpointRequest(object):
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
        'path': 'str',
        'recursive': 'bool',
        'notify': 'bool',
        'force_rescan': 'bool'
    }

    attribute_map = {
        'path': 'path',
        'recursive': 'recursive',
        'notify': 'notify',
        'force_rescan': 'force_rescan'
    }

    def __init__(self, path=None, recursive=None, notify=None, force_rescan=None, local_vars_configuration=None):  # noqa: E501
        """ScannerScanEndpointRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._recursive = None
        self._notify = None
        self._force_rescan = None
        self.discriminator = None

        self.path = path
        self.recursive = recursive
        self.notify = notify
        self.force_rescan = force_rescan

    @property
    def path(self):
        """Gets the path of this ScannerScanEndpointRequest.  # noqa: E501


        :return: The path of this ScannerScanEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ScannerScanEndpointRequest.


        :param path: The path of this ScannerScanEndpointRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) < 1):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

    @property
    def recursive(self):
        """Gets the recursive of this ScannerScanEndpointRequest.  # noqa: E501


        :return: The recursive of this ScannerScanEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._recursive

    @recursive.setter
    def recursive(self, recursive):
        """Sets the recursive of this ScannerScanEndpointRequest.


        :param recursive: The recursive of this ScannerScanEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._recursive = recursive

    @property
    def notify(self):
        """Gets the notify of this ScannerScanEndpointRequest.  # noqa: E501


        :return: The notify of this ScannerScanEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this ScannerScanEndpointRequest.


        :param notify: The notify of this ScannerScanEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._notify = notify

    @property
    def force_rescan(self):
        """Gets the force_rescan of this ScannerScanEndpointRequest.  # noqa: E501


        :return: The force_rescan of this ScannerScanEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._force_rescan

    @force_rescan.setter
    def force_rescan(self, force_rescan):
        """Sets the force_rescan of this ScannerScanEndpointRequest.


        :param force_rescan: The force_rescan of this ScannerScanEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._force_rescan = force_rescan

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
        if not isinstance(other, ScannerScanEndpointRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScannerScanEndpointRequest):
            return True

        return self.to_dict() != other.to_dict()
