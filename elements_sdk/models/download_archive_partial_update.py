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


class DownloadArchivePartialUpdate(object):
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
        'task_info': 'TaskInfo',
        'name': 'str',
        'path': 'str',
        'progress_unit': 'int',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'task_info': 'task_info',
        'name': 'name',
        'path': 'path',
        'progress_unit': 'progress_unit',
        'user': 'user'
    }

    def __init__(self, id=None, task_info=None, name=None, path=None, progress_unit=None, user=None, local_vars_configuration=None):  # noqa: E501
        """DownloadArchivePartialUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._task_info = None
        self._name = None
        self._path = None
        self._progress_unit = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_info is not None:
            self.task_info = task_info
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if progress_unit is not None:
            self.progress_unit = progress_unit
        self.user = user

    @property
    def id(self):
        """Gets the id of this DownloadArchivePartialUpdate.  # noqa: E501


        :return: The id of this DownloadArchivePartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DownloadArchivePartialUpdate.


        :param id: The id of this DownloadArchivePartialUpdate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def task_info(self):
        """Gets the task_info of this DownloadArchivePartialUpdate.  # noqa: E501


        :return: The task_info of this DownloadArchivePartialUpdate.  # noqa: E501
        :rtype: TaskInfo
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        """Sets the task_info of this DownloadArchivePartialUpdate.


        :param task_info: The task_info of this DownloadArchivePartialUpdate.  # noqa: E501
        :type: TaskInfo
        """

        self._task_info = task_info

    @property
    def name(self):
        """Gets the name of this DownloadArchivePartialUpdate.  # noqa: E501


        :return: The name of this DownloadArchivePartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DownloadArchivePartialUpdate.


        :param name: The name of this DownloadArchivePartialUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this DownloadArchivePartialUpdate.  # noqa: E501


        :return: The path of this DownloadArchivePartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DownloadArchivePartialUpdate.


        :param path: The path of this DownloadArchivePartialUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) > 255):
            raise ValueError("Invalid value for `path`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) < 1):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

    @property
    def progress_unit(self):
        """Gets the progress_unit of this DownloadArchivePartialUpdate.  # noqa: E501


        :return: The progress_unit of this DownloadArchivePartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._progress_unit

    @progress_unit.setter
    def progress_unit(self, progress_unit):
        """Sets the progress_unit of this DownloadArchivePartialUpdate.


        :param progress_unit: The progress_unit of this DownloadArchivePartialUpdate.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and progress_unit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `progress_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(progress_unit, allowed_values)
            )

        self._progress_unit = progress_unit

    @property
    def user(self):
        """Gets the user of this DownloadArchivePartialUpdate.  # noqa: E501


        :return: The user of this DownloadArchivePartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DownloadArchivePartialUpdate.


        :param user: The user of this DownloadArchivePartialUpdate.  # noqa: E501
        :type: int
        """

        self._user = user

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
        if not isinstance(other, DownloadArchivePartialUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DownloadArchivePartialUpdate):
            return True

        return self.to_dict() != other.to_dict()
