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


class WorkflowTransitionRequest(object):
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
        'bundles': 'list[int]',
        'directories': 'list[int]',
        'job': 'int',
        'root': 'int',
        'variables': 'dict(str, str)'
    }

    attribute_map = {
        'bundles': 'bundles',
        'directories': 'directories',
        'job': 'job',
        'root': 'root',
        'variables': 'variables'
    }

    def __init__(self, bundles=None, directories=None, job=None, root=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowTransitionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bundles = None
        self._directories = None
        self._job = None
        self._root = None
        self._variables = None
        self.discriminator = None

        if bundles is not None:
            self.bundles = bundles
        if directories is not None:
            self.directories = directories
        self.job = job
        self.root = root
        if variables is not None:
            self.variables = variables

    @property
    def bundles(self):
        """Gets the bundles of this WorkflowTransitionRequest.  # noqa: E501


        :return: The bundles of this WorkflowTransitionRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._bundles

    @bundles.setter
    def bundles(self, bundles):
        """Sets the bundles of this WorkflowTransitionRequest.


        :param bundles: The bundles of this WorkflowTransitionRequest.  # noqa: E501
        :type: list[int]
        """

        self._bundles = bundles

    @property
    def directories(self):
        """Gets the directories of this WorkflowTransitionRequest.  # noqa: E501


        :return: The directories of this WorkflowTransitionRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._directories

    @directories.setter
    def directories(self, directories):
        """Sets the directories of this WorkflowTransitionRequest.


        :param directories: The directories of this WorkflowTransitionRequest.  # noqa: E501
        :type: list[int]
        """

        self._directories = directories

    @property
    def job(self):
        """Gets the job of this WorkflowTransitionRequest.  # noqa: E501


        :return: The job of this WorkflowTransitionRequest.  # noqa: E501
        :rtype: int
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this WorkflowTransitionRequest.


        :param job: The job of this WorkflowTransitionRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and job is None:  # noqa: E501
            raise ValueError("Invalid value for `job`, must not be `None`")  # noqa: E501

        self._job = job

    @property
    def root(self):
        """Gets the root of this WorkflowTransitionRequest.  # noqa: E501


        :return: The root of this WorkflowTransitionRequest.  # noqa: E501
        :rtype: int
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this WorkflowTransitionRequest.


        :param root: The root of this WorkflowTransitionRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and root is None:  # noqa: E501
            raise ValueError("Invalid value for `root`, must not be `None`")  # noqa: E501

        self._root = root

    @property
    def variables(self):
        """Gets the variables of this WorkflowTransitionRequest.  # noqa: E501


        :return: The variables of this WorkflowTransitionRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this WorkflowTransitionRequest.


        :param variables: The variables of this WorkflowTransitionRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._variables = variables

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
        if not isinstance(other, WorkflowTransitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowTransitionRequest):
            return True

        return self.to_dict() != other.to_dict()
