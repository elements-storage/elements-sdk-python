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


class CustomField(object):
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
        'id': 'int',
        'labels': 'list[str]',
        'options': 'list[str]',
        'name': 'str',
        'order': 'int',
        'type': 'str',
        'use_for_uploads': 'bool',
        'require_to_upload': 'bool',
        'non_user_editable': 'bool',
        'validation': 'str',
        'regex': 'str',
        'range_min': 'int',
        'range_max': 'int',
        'number_of_digits': 'int',
        'metadata_prefill': 'str',
        'highlight_expiration': 'bool',
        'multiple_response': 'bool',
        'help_text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'labels': 'labels',
        'options': 'options',
        'name': 'name',
        'order': 'order',
        'type': 'type',
        'use_for_uploads': 'use_for_uploads',
        'require_to_upload': 'require_to_upload',
        'non_user_editable': 'non_user_editable',
        'validation': 'validation',
        'regex': 'regex',
        'range_min': 'range_min',
        'range_max': 'range_max',
        'number_of_digits': 'number_of_digits',
        'metadata_prefill': 'metadata_prefill',
        'highlight_expiration': 'highlight_expiration',
        'multiple_response': 'multiple_response',
        'help_text': 'help_text'
    }

    def __init__(self, id=None, labels=None, options=None, name=None, order=None, type=None, use_for_uploads=None, require_to_upload=None, non_user_editable=None, validation=None, regex=None, range_min=None, range_max=None, number_of_digits=None, metadata_prefill=None, highlight_expiration=None, multiple_response=None, help_text=None, local_vars_configuration=None):  # noqa: E501
        """CustomField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._labels = None
        self._options = None
        self._name = None
        self._order = None
        self._type = None
        self._use_for_uploads = None
        self._require_to_upload = None
        self._non_user_editable = None
        self._validation = None
        self._regex = None
        self._range_min = None
        self._range_max = None
        self._number_of_digits = None
        self._metadata_prefill = None
        self._highlight_expiration = None
        self._multiple_response = None
        self._help_text = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if labels is not None:
            self.labels = labels
        self.options = options
        self.name = name
        if order is not None:
            self.order = order
        self.type = type
        if use_for_uploads is not None:
            self.use_for_uploads = use_for_uploads
        if require_to_upload is not None:
            self.require_to_upload = require_to_upload
        if non_user_editable is not None:
            self.non_user_editable = non_user_editable
        self.validation = validation
        self.regex = regex
        self.range_min = range_min
        self.range_max = range_max
        self.number_of_digits = number_of_digits
        self.metadata_prefill = metadata_prefill
        if highlight_expiration is not None:
            self.highlight_expiration = highlight_expiration
        if multiple_response is not None:
            self.multiple_response = multiple_response
        self.help_text = help_text

    @property
    def id(self):
        """Gets the id of this CustomField.  # noqa: E501


        :return: The id of this CustomField.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomField.


        :param id: The id of this CustomField.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this CustomField.  # noqa: E501


        :return: The labels of this CustomField.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CustomField.


        :param labels: The labels of this CustomField.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def options(self):
        """Gets the options of this CustomField.  # noqa: E501


        :return: The options of this CustomField.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CustomField.


        :param options: The options of this CustomField.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def name(self):
        """Gets the name of this CustomField.  # noqa: E501


        :return: The name of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomField.


        :param name: The name of this CustomField.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def order(self):
        """Gets the order of this CustomField.  # noqa: E501


        :return: The order of this CustomField.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CustomField.


        :param order: The order of this CustomField.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def type(self):
        """Gets the type of this CustomField.  # noqa: E501


        :return: The type of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomField.


        :param type: The type of this CustomField.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 255):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def use_for_uploads(self):
        """Gets the use_for_uploads of this CustomField.  # noqa: E501


        :return: The use_for_uploads of this CustomField.  # noqa: E501
        :rtype: bool
        """
        return self._use_for_uploads

    @use_for_uploads.setter
    def use_for_uploads(self, use_for_uploads):
        """Sets the use_for_uploads of this CustomField.


        :param use_for_uploads: The use_for_uploads of this CustomField.  # noqa: E501
        :type: bool
        """

        self._use_for_uploads = use_for_uploads

    @property
    def require_to_upload(self):
        """Gets the require_to_upload of this CustomField.  # noqa: E501


        :return: The require_to_upload of this CustomField.  # noqa: E501
        :rtype: bool
        """
        return self._require_to_upload

    @require_to_upload.setter
    def require_to_upload(self, require_to_upload):
        """Sets the require_to_upload of this CustomField.


        :param require_to_upload: The require_to_upload of this CustomField.  # noqa: E501
        :type: bool
        """

        self._require_to_upload = require_to_upload

    @property
    def non_user_editable(self):
        """Gets the non_user_editable of this CustomField.  # noqa: E501


        :return: The non_user_editable of this CustomField.  # noqa: E501
        :rtype: bool
        """
        return self._non_user_editable

    @non_user_editable.setter
    def non_user_editable(self, non_user_editable):
        """Sets the non_user_editable of this CustomField.


        :param non_user_editable: The non_user_editable of this CustomField.  # noqa: E501
        :type: bool
        """

        self._non_user_editable = non_user_editable

    @property
    def validation(self):
        """Gets the validation of this CustomField.  # noqa: E501


        :return: The validation of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this CustomField.


        :param validation: The validation of this CustomField.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"number_of_digits", "regex", "range"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and validation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `validation` ({0}), must be one of {1}"  # noqa: E501
                .format(validation, allowed_values)
            )

        self._validation = validation

    @property
    def regex(self):
        """Gets the regex of this CustomField.  # noqa: E501


        :return: The regex of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this CustomField.


        :param regex: The regex of this CustomField.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                regex is not None and len(regex) > 255):
            raise ValueError("Invalid value for `regex`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                regex is not None and len(regex) < 1):
            raise ValueError("Invalid value for `regex`, length must be greater than or equal to `1`")  # noqa: E501

        self._regex = regex

    @property
    def range_min(self):
        """Gets the range_min of this CustomField.  # noqa: E501


        :return: The range_min of this CustomField.  # noqa: E501
        :rtype: int
        """
        return self._range_min

    @range_min.setter
    def range_min(self, range_min):
        """Sets the range_min of this CustomField.


        :param range_min: The range_min of this CustomField.  # noqa: E501
        :type: int
        """

        self._range_min = range_min

    @property
    def range_max(self):
        """Gets the range_max of this CustomField.  # noqa: E501


        :return: The range_max of this CustomField.  # noqa: E501
        :rtype: int
        """
        return self._range_max

    @range_max.setter
    def range_max(self, range_max):
        """Sets the range_max of this CustomField.


        :param range_max: The range_max of this CustomField.  # noqa: E501
        :type: int
        """

        self._range_max = range_max

    @property
    def number_of_digits(self):
        """Gets the number_of_digits of this CustomField.  # noqa: E501


        :return: The number_of_digits of this CustomField.  # noqa: E501
        :rtype: int
        """
        return self._number_of_digits

    @number_of_digits.setter
    def number_of_digits(self, number_of_digits):
        """Sets the number_of_digits of this CustomField.


        :param number_of_digits: The number_of_digits of this CustomField.  # noqa: E501
        :type: int
        """

        self._number_of_digits = number_of_digits

    @property
    def metadata_prefill(self):
        """Gets the metadata_prefill of this CustomField.  # noqa: E501


        :return: The metadata_prefill of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._metadata_prefill

    @metadata_prefill.setter
    def metadata_prefill(self, metadata_prefill):
        """Sets the metadata_prefill of this CustomField.


        :param metadata_prefill: The metadata_prefill of this CustomField.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                metadata_prefill is not None and len(metadata_prefill) > 255):
            raise ValueError("Invalid value for `metadata_prefill`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metadata_prefill is not None and len(metadata_prefill) < 1):
            raise ValueError("Invalid value for `metadata_prefill`, length must be greater than or equal to `1`")  # noqa: E501

        self._metadata_prefill = metadata_prefill

    @property
    def highlight_expiration(self):
        """Gets the highlight_expiration of this CustomField.  # noqa: E501


        :return: The highlight_expiration of this CustomField.  # noqa: E501
        :rtype: bool
        """
        return self._highlight_expiration

    @highlight_expiration.setter
    def highlight_expiration(self, highlight_expiration):
        """Sets the highlight_expiration of this CustomField.


        :param highlight_expiration: The highlight_expiration of this CustomField.  # noqa: E501
        :type: bool
        """

        self._highlight_expiration = highlight_expiration

    @property
    def multiple_response(self):
        """Gets the multiple_response of this CustomField.  # noqa: E501


        :return: The multiple_response of this CustomField.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_response

    @multiple_response.setter
    def multiple_response(self, multiple_response):
        """Sets the multiple_response of this CustomField.


        :param multiple_response: The multiple_response of this CustomField.  # noqa: E501
        :type: bool
        """

        self._multiple_response = multiple_response

    @property
    def help_text(self):
        """Gets the help_text of this CustomField.  # noqa: E501


        :return: The help_text of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """Sets the help_text of this CustomField.


        :param help_text: The help_text of this CustomField.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                help_text is not None and len(help_text) > 255):
            raise ValueError("Invalid value for `help_text`, length must be less than or equal to `255`")  # noqa: E501

        self._help_text = help_text

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
        if not isinstance(other, CustomField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomField):
            return True

        return self.to_dict() != other.to_dict()
