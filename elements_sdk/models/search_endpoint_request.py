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


class SearchEndpointRequest(object):
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
        'query': 'str',
        'exclude': 'str',
        'offset': 'int',
        'limit': 'int',
        'dirs_only': 'bool',
        'names_only': 'bool',
        'tapes': 'bool'
    }

    attribute_map = {
        'query': 'query',
        'exclude': 'exclude',
        'offset': 'offset',
        'limit': 'limit',
        'dirs_only': 'dirs_only',
        'names_only': 'names_only',
        'tapes': 'tapes'
    }

    def __init__(self, query=None, exclude=None, offset=None, limit=None, dirs_only=None, names_only=None, tapes=None, local_vars_configuration=None):  # noqa: E501
        """SearchEndpointRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._exclude = None
        self._offset = None
        self._limit = None
        self._dirs_only = None
        self._names_only = None
        self._tapes = None
        self.discriminator = None

        self.query = query
        if exclude is not None:
            self.exclude = exclude
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if dirs_only is not None:
            self.dirs_only = dirs_only
        if names_only is not None:
            self.names_only = names_only
        if tapes is not None:
            self.tapes = tapes

    @property
    def query(self):
        """Gets the query of this SearchEndpointRequest.  # noqa: E501


        :return: The query of this SearchEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchEndpointRequest.


        :param query: The query of this SearchEndpointRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and query is None:  # noqa: E501
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def exclude(self):
        """Gets the exclude of this SearchEndpointRequest.  # noqa: E501


        :return: The exclude of this SearchEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this SearchEndpointRequest.


        :param exclude: The exclude of this SearchEndpointRequest.  # noqa: E501
        :type: str
        """

        self._exclude = exclude

    @property
    def offset(self):
        """Gets the offset of this SearchEndpointRequest.  # noqa: E501


        :return: The offset of this SearchEndpointRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchEndpointRequest.


        :param offset: The offset of this SearchEndpointRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchEndpointRequest.  # noqa: E501


        :return: The limit of this SearchEndpointRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchEndpointRequest.


        :param limit: The limit of this SearchEndpointRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def dirs_only(self):
        """Gets the dirs_only of this SearchEndpointRequest.  # noqa: E501


        :return: The dirs_only of this SearchEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dirs_only

    @dirs_only.setter
    def dirs_only(self, dirs_only):
        """Sets the dirs_only of this SearchEndpointRequest.


        :param dirs_only: The dirs_only of this SearchEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._dirs_only = dirs_only

    @property
    def names_only(self):
        """Gets the names_only of this SearchEndpointRequest.  # noqa: E501


        :return: The names_only of this SearchEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._names_only

    @names_only.setter
    def names_only(self, names_only):
        """Sets the names_only of this SearchEndpointRequest.


        :param names_only: The names_only of this SearchEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._names_only = names_only

    @property
    def tapes(self):
        """Gets the tapes of this SearchEndpointRequest.  # noqa: E501


        :return: The tapes of this SearchEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._tapes

    @tapes.setter
    def tapes(self, tapes):
        """Sets the tapes of this SearchEndpointRequest.


        :param tapes: The tapes of this SearchEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._tapes = tapes

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
        if not isinstance(other, SearchEndpointRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchEndpointRequest):
            return True

        return self.to_dict() != other.to_dict()