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


class LizardFSDisk(object):
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
        'node': 'StorageNodeMini',
        'host': 'str',
        'mountpoint': 'str',
        'to_delete': 'bool',
        'damaged': 'bool',
        'scanning': 'bool',
        'error_chunk': 'int',
        'error_timestamp': 'int',
        'size_total': 'int',
        'size_used': 'int',
        'size_free': 'int',
        'chunks': 'int'
    }

    attribute_map = {
        'node': 'node',
        'host': 'host',
        'mountpoint': 'mountpoint',
        'to_delete': 'to_delete',
        'damaged': 'damaged',
        'scanning': 'scanning',
        'error_chunk': 'error_chunk',
        'error_timestamp': 'error_timestamp',
        'size_total': 'size_total',
        'size_used': 'size_used',
        'size_free': 'size_free',
        'chunks': 'chunks'
    }

    def __init__(self, node=None, host=None, mountpoint=None, to_delete=None, damaged=None, scanning=None, error_chunk=None, error_timestamp=None, size_total=None, size_used=None, size_free=None, chunks=None, local_vars_configuration=None):  # noqa: E501
        """LizardFSDisk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._node = None
        self._host = None
        self._mountpoint = None
        self._to_delete = None
        self._damaged = None
        self._scanning = None
        self._error_chunk = None
        self._error_timestamp = None
        self._size_total = None
        self._size_used = None
        self._size_free = None
        self._chunks = None
        self.discriminator = None

        if node is not None:
            self.node = node
        self.host = host
        self.mountpoint = mountpoint
        self.to_delete = to_delete
        self.damaged = damaged
        self.scanning = scanning
        self.error_chunk = error_chunk
        self.error_timestamp = error_timestamp
        self.size_total = size_total
        self.size_used = size_used
        self.size_free = size_free
        self.chunks = chunks

    @property
    def node(self):
        """Gets the node of this LizardFSDisk.  # noqa: E501


        :return: The node of this LizardFSDisk.  # noqa: E501
        :rtype: StorageNodeMini
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this LizardFSDisk.


        :param node: The node of this LizardFSDisk.  # noqa: E501
        :type: StorageNodeMini
        """

        self._node = node

    @property
    def host(self):
        """Gets the host of this LizardFSDisk.  # noqa: E501


        :return: The host of this LizardFSDisk.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this LizardFSDisk.


        :param host: The host of this LizardFSDisk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                host is not None and len(host) < 1):
            raise ValueError("Invalid value for `host`, length must be greater than or equal to `1`")  # noqa: E501

        self._host = host

    @property
    def mountpoint(self):
        """Gets the mountpoint of this LizardFSDisk.  # noqa: E501


        :return: The mountpoint of this LizardFSDisk.  # noqa: E501
        :rtype: str
        """
        return self._mountpoint

    @mountpoint.setter
    def mountpoint(self, mountpoint):
        """Sets the mountpoint of this LizardFSDisk.


        :param mountpoint: The mountpoint of this LizardFSDisk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mountpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `mountpoint`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mountpoint is not None and len(mountpoint) < 1):
            raise ValueError("Invalid value for `mountpoint`, length must be greater than or equal to `1`")  # noqa: E501

        self._mountpoint = mountpoint

    @property
    def to_delete(self):
        """Gets the to_delete of this LizardFSDisk.  # noqa: E501


        :return: The to_delete of this LizardFSDisk.  # noqa: E501
        :rtype: bool
        """
        return self._to_delete

    @to_delete.setter
    def to_delete(self, to_delete):
        """Sets the to_delete of this LizardFSDisk.


        :param to_delete: The to_delete of this LizardFSDisk.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and to_delete is None:  # noqa: E501
            raise ValueError("Invalid value for `to_delete`, must not be `None`")  # noqa: E501

        self._to_delete = to_delete

    @property
    def damaged(self):
        """Gets the damaged of this LizardFSDisk.  # noqa: E501


        :return: The damaged of this LizardFSDisk.  # noqa: E501
        :rtype: bool
        """
        return self._damaged

    @damaged.setter
    def damaged(self, damaged):
        """Sets the damaged of this LizardFSDisk.


        :param damaged: The damaged of this LizardFSDisk.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and damaged is None:  # noqa: E501
            raise ValueError("Invalid value for `damaged`, must not be `None`")  # noqa: E501

        self._damaged = damaged

    @property
    def scanning(self):
        """Gets the scanning of this LizardFSDisk.  # noqa: E501


        :return: The scanning of this LizardFSDisk.  # noqa: E501
        :rtype: bool
        """
        return self._scanning

    @scanning.setter
    def scanning(self, scanning):
        """Sets the scanning of this LizardFSDisk.


        :param scanning: The scanning of this LizardFSDisk.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and scanning is None:  # noqa: E501
            raise ValueError("Invalid value for `scanning`, must not be `None`")  # noqa: E501

        self._scanning = scanning

    @property
    def error_chunk(self):
        """Gets the error_chunk of this LizardFSDisk.  # noqa: E501


        :return: The error_chunk of this LizardFSDisk.  # noqa: E501
        :rtype: int
        """
        return self._error_chunk

    @error_chunk.setter
    def error_chunk(self, error_chunk):
        """Sets the error_chunk of this LizardFSDisk.


        :param error_chunk: The error_chunk of this LizardFSDisk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and error_chunk is None:  # noqa: E501
            raise ValueError("Invalid value for `error_chunk`, must not be `None`")  # noqa: E501

        self._error_chunk = error_chunk

    @property
    def error_timestamp(self):
        """Gets the error_timestamp of this LizardFSDisk.  # noqa: E501


        :return: The error_timestamp of this LizardFSDisk.  # noqa: E501
        :rtype: int
        """
        return self._error_timestamp

    @error_timestamp.setter
    def error_timestamp(self, error_timestamp):
        """Sets the error_timestamp of this LizardFSDisk.


        :param error_timestamp: The error_timestamp of this LizardFSDisk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and error_timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `error_timestamp`, must not be `None`")  # noqa: E501

        self._error_timestamp = error_timestamp

    @property
    def size_total(self):
        """Gets the size_total of this LizardFSDisk.  # noqa: E501


        :return: The size_total of this LizardFSDisk.  # noqa: E501
        :rtype: int
        """
        return self._size_total

    @size_total.setter
    def size_total(self, size_total):
        """Sets the size_total of this LizardFSDisk.


        :param size_total: The size_total of this LizardFSDisk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size_total is None:  # noqa: E501
            raise ValueError("Invalid value for `size_total`, must not be `None`")  # noqa: E501

        self._size_total = size_total

    @property
    def size_used(self):
        """Gets the size_used of this LizardFSDisk.  # noqa: E501


        :return: The size_used of this LizardFSDisk.  # noqa: E501
        :rtype: int
        """
        return self._size_used

    @size_used.setter
    def size_used(self, size_used):
        """Sets the size_used of this LizardFSDisk.


        :param size_used: The size_used of this LizardFSDisk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size_used is None:  # noqa: E501
            raise ValueError("Invalid value for `size_used`, must not be `None`")  # noqa: E501

        self._size_used = size_used

    @property
    def size_free(self):
        """Gets the size_free of this LizardFSDisk.  # noqa: E501


        :return: The size_free of this LizardFSDisk.  # noqa: E501
        :rtype: int
        """
        return self._size_free

    @size_free.setter
    def size_free(self, size_free):
        """Sets the size_free of this LizardFSDisk.


        :param size_free: The size_free of this LizardFSDisk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size_free is None:  # noqa: E501
            raise ValueError("Invalid value for `size_free`, must not be `None`")  # noqa: E501

        self._size_free = size_free

    @property
    def chunks(self):
        """Gets the chunks of this LizardFSDisk.  # noqa: E501


        :return: The chunks of this LizardFSDisk.  # noqa: E501
        :rtype: int
        """
        return self._chunks

    @chunks.setter
    def chunks(self, chunks):
        """Sets the chunks of this LizardFSDisk.


        :param chunks: The chunks of this LizardFSDisk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and chunks is None:  # noqa: E501
            raise ValueError("Invalid value for `chunks`, must not be `None`")  # noqa: E501

        self._chunks = chunks

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
        if not isinstance(other, LizardFSDisk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LizardFSDisk):
            return True

        return self.to_dict() != other.to_dict()
