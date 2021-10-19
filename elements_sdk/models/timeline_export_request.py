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


class TimelineExportRequest(object):
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
        'project': 'object',
        'sequence': 'str',
        'format': 'str'
    }

    attribute_map = {
        'project': 'project',
        'sequence': 'sequence',
        'format': 'format'
    }

    def __init__(self, project=None, sequence=None, format=None, local_vars_configuration=None):  # noqa: E501
        """TimelineExportRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project = None
        self._sequence = None
        self._format = None
        self.discriminator = None

        self.project = project
        self.sequence = sequence
        self.format = format

    @property
    def project(self):
        """Gets the project of this TimelineExportRequest.  # noqa: E501


        :return: The project of this TimelineExportRequest.  # noqa: E501
        :rtype: object
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TimelineExportRequest.


        :param project: The project of this TimelineExportRequest.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def sequence(self):
        """Gets the sequence of this TimelineExportRequest.  # noqa: E501


        :return: The sequence of this TimelineExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this TimelineExportRequest.


        :param sequence: The sequence of this TimelineExportRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sequence is None:  # noqa: E501
            raise ValueError("Invalid value for `sequence`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sequence is not None and len(sequence) < 1):
            raise ValueError("Invalid value for `sequence`, length must be greater than or equal to `1`")  # noqa: E501

        self._sequence = sequence

    @property
    def format(self):
        """Gets the format of this TimelineExportRequest.  # noqa: E501


        :return: The format of this TimelineExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this TimelineExportRequest.


        :param format: The format of this TimelineExportRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and format is None:  # noqa: E501
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                format is not None and len(format) < 1):
            raise ValueError("Invalid value for `format`, length must be greater than or equal to `1`")  # noqa: E501

        self._format = format

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
        if not isinstance(other, TimelineExportRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimelineExportRequest):
            return True

        return self.to_dict() != other.to_dict()
