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


class Workstation(object):
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
        'display_name': 'str',
        'rdc_allow_users': 'list[ElementsUserReference]',
        'rdc_allow_groups': 'list[ElementsGroupReference]',
        'report': 'dict(str, str)',
        'client_sessions': 'list[ClientSession]',
        'name': 'str',
        'hostname': 'str',
        'rdc_last_used': 'datetime',
        'rdc_disable_upnp': 'bool',
        'rdc_client_port': 'int',
        'rdc_host_port': 'int'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'rdc_allow_users': 'rdc_allow_users',
        'rdc_allow_groups': 'rdc_allow_groups',
        'report': 'report',
        'client_sessions': 'client_sessions',
        'name': 'name',
        'hostname': 'hostname',
        'rdc_last_used': 'rdc_last_used',
        'rdc_disable_upnp': 'rdc_disable_upnp',
        'rdc_client_port': 'rdc_client_port',
        'rdc_host_port': 'rdc_host_port'
    }

    def __init__(self, id=None, display_name=None, rdc_allow_users=None, rdc_allow_groups=None, report=None, client_sessions=None, name=None, hostname=None, rdc_last_used=None, rdc_disable_upnp=None, rdc_client_port=None, rdc_host_port=None, local_vars_configuration=None):  # noqa: E501
        """Workstation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._rdc_allow_users = None
        self._rdc_allow_groups = None
        self._report = None
        self._client_sessions = None
        self._name = None
        self._hostname = None
        self._rdc_last_used = None
        self._rdc_disable_upnp = None
        self._rdc_client_port = None
        self._rdc_host_port = None
        self.discriminator = None

        self.id = id
        if display_name is not None:
            self.display_name = display_name
        if rdc_allow_users is not None:
            self.rdc_allow_users = rdc_allow_users
        if rdc_allow_groups is not None:
            self.rdc_allow_groups = rdc_allow_groups
        if report is not None:
            self.report = report
        if client_sessions is not None:
            self.client_sessions = client_sessions
        self.name = name
        self.hostname = hostname
        self.rdc_last_used = rdc_last_used
        if rdc_disable_upnp is not None:
            self.rdc_disable_upnp = rdc_disable_upnp
        self.rdc_client_port = rdc_client_port
        self.rdc_host_port = rdc_host_port

    @property
    def id(self):
        """Gets the id of this Workstation.  # noqa: E501


        :return: The id of this Workstation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Workstation.


        :param id: The id of this Workstation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this Workstation.  # noqa: E501


        :return: The display_name of this Workstation.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Workstation.


        :param display_name: The display_name of this Workstation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def rdc_allow_users(self):
        """Gets the rdc_allow_users of this Workstation.  # noqa: E501


        :return: The rdc_allow_users of this Workstation.  # noqa: E501
        :rtype: list[ElementsUserReference]
        """
        return self._rdc_allow_users

    @rdc_allow_users.setter
    def rdc_allow_users(self, rdc_allow_users):
        """Sets the rdc_allow_users of this Workstation.


        :param rdc_allow_users: The rdc_allow_users of this Workstation.  # noqa: E501
        :type: list[ElementsUserReference]
        """

        self._rdc_allow_users = rdc_allow_users

    @property
    def rdc_allow_groups(self):
        """Gets the rdc_allow_groups of this Workstation.  # noqa: E501


        :return: The rdc_allow_groups of this Workstation.  # noqa: E501
        :rtype: list[ElementsGroupReference]
        """
        return self._rdc_allow_groups

    @rdc_allow_groups.setter
    def rdc_allow_groups(self, rdc_allow_groups):
        """Sets the rdc_allow_groups of this Workstation.


        :param rdc_allow_groups: The rdc_allow_groups of this Workstation.  # noqa: E501
        :type: list[ElementsGroupReference]
        """

        self._rdc_allow_groups = rdc_allow_groups

    @property
    def report(self):
        """Gets the report of this Workstation.  # noqa: E501


        :return: The report of this Workstation.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this Workstation.


        :param report: The report of this Workstation.  # noqa: E501
        :type: dict(str, str)
        """

        self._report = report

    @property
    def client_sessions(self):
        """Gets the client_sessions of this Workstation.  # noqa: E501


        :return: The client_sessions of this Workstation.  # noqa: E501
        :rtype: list[ClientSession]
        """
        return self._client_sessions

    @client_sessions.setter
    def client_sessions(self, client_sessions):
        """Sets the client_sessions of this Workstation.


        :param client_sessions: The client_sessions of this Workstation.  # noqa: E501
        :type: list[ClientSession]
        """

        self._client_sessions = client_sessions

    @property
    def name(self):
        """Gets the name of this Workstation.  # noqa: E501


        :return: The name of this Workstation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workstation.


        :param name: The name of this Workstation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def hostname(self):
        """Gets the hostname of this Workstation.  # noqa: E501


        :return: The hostname of this Workstation.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Workstation.


        :param hostname: The hostname of this Workstation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) < 1):
            raise ValueError("Invalid value for `hostname`, length must be greater than or equal to `1`")  # noqa: E501

        self._hostname = hostname

    @property
    def rdc_last_used(self):
        """Gets the rdc_last_used of this Workstation.  # noqa: E501


        :return: The rdc_last_used of this Workstation.  # noqa: E501
        :rtype: datetime
        """
        return self._rdc_last_used

    @rdc_last_used.setter
    def rdc_last_used(self, rdc_last_used):
        """Sets the rdc_last_used of this Workstation.


        :param rdc_last_used: The rdc_last_used of this Workstation.  # noqa: E501
        :type: datetime
        """

        self._rdc_last_used = rdc_last_used

    @property
    def rdc_disable_upnp(self):
        """Gets the rdc_disable_upnp of this Workstation.  # noqa: E501


        :return: The rdc_disable_upnp of this Workstation.  # noqa: E501
        :rtype: bool
        """
        return self._rdc_disable_upnp

    @rdc_disable_upnp.setter
    def rdc_disable_upnp(self, rdc_disable_upnp):
        """Sets the rdc_disable_upnp of this Workstation.


        :param rdc_disable_upnp: The rdc_disable_upnp of this Workstation.  # noqa: E501
        :type: bool
        """

        self._rdc_disable_upnp = rdc_disable_upnp

    @property
    def rdc_client_port(self):
        """Gets the rdc_client_port of this Workstation.  # noqa: E501


        :return: The rdc_client_port of this Workstation.  # noqa: E501
        :rtype: int
        """
        return self._rdc_client_port

    @rdc_client_port.setter
    def rdc_client_port(self, rdc_client_port):
        """Sets the rdc_client_port of this Workstation.


        :param rdc_client_port: The rdc_client_port of this Workstation.  # noqa: E501
        :type: int
        """

        self._rdc_client_port = rdc_client_port

    @property
    def rdc_host_port(self):
        """Gets the rdc_host_port of this Workstation.  # noqa: E501


        :return: The rdc_host_port of this Workstation.  # noqa: E501
        :rtype: int
        """
        return self._rdc_host_port

    @rdc_host_port.setter
    def rdc_host_port(self, rdc_host_port):
        """Sets the rdc_host_port of this Workstation.


        :param rdc_host_port: The rdc_host_port of this Workstation.  # noqa: E501
        :type: int
        """

        self._rdc_host_port = rdc_host_port

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
        if not isinstance(other, Workstation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Workstation):
            return True

        return self.to_dict() != other.to_dict()
