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


class MarkerPartialUpdate(object):
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
        'title': 'str',
        'text': 'str',
        't_in': 'float',
        't_out': 'float',
        'asset': 'int'
    }

    attribute_map = {
        'title': 'title',
        'text': 'text',
        't_in': 't_in',
        't_out': 't_out',
        'asset': 'asset'
    }

    def __init__(self, title=None, text=None, t_in=None, t_out=None, asset=None, local_vars_configuration=None):  # noqa: E501
        """MarkerPartialUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._text = None
        self._t_in = None
        self._t_out = None
        self._asset = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if text is not None:
            self.text = text
        if t_in is not None:
            self.t_in = t_in
        if t_out is not None:
            self.t_out = t_out
        if asset is not None:
            self.asset = asset

    @property
    def title(self):
        """Gets the title of this MarkerPartialUpdate.  # noqa: E501


        :return: The title of this MarkerPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MarkerPartialUpdate.


        :param title: The title of this MarkerPartialUpdate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def text(self):
        """Gets the text of this MarkerPartialUpdate.  # noqa: E501


        :return: The text of this MarkerPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this MarkerPartialUpdate.


        :param text: The text of this MarkerPartialUpdate.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def t_in(self):
        """Gets the t_in of this MarkerPartialUpdate.  # noqa: E501


        :return: The t_in of this MarkerPartialUpdate.  # noqa: E501
        :rtype: float
        """
        return self._t_in

    @t_in.setter
    def t_in(self, t_in):
        """Sets the t_in of this MarkerPartialUpdate.


        :param t_in: The t_in of this MarkerPartialUpdate.  # noqa: E501
        :type: float
        """

        self._t_in = t_in

    @property
    def t_out(self):
        """Gets the t_out of this MarkerPartialUpdate.  # noqa: E501


        :return: The t_out of this MarkerPartialUpdate.  # noqa: E501
        :rtype: float
        """
        return self._t_out

    @t_out.setter
    def t_out(self, t_out):
        """Sets the t_out of this MarkerPartialUpdate.


        :param t_out: The t_out of this MarkerPartialUpdate.  # noqa: E501
        :type: float
        """

        self._t_out = t_out

    @property
    def asset(self):
        """Gets the asset of this MarkerPartialUpdate.  # noqa: E501


        :return: The asset of this MarkerPartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this MarkerPartialUpdate.


        :param asset: The asset of this MarkerPartialUpdate.  # noqa: E501
        :type: int
        """

        self._asset = asset

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
        if not isinstance(other, MarkerPartialUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarkerPartialUpdate):
            return True

        return self.to_dict() != other.to_dict()
