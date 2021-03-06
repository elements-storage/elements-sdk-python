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


class Comment(object):
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
        'assignee': 'ElementsUserMini',
        'user': 'ElementsUserMini',
        'drawing': 'dict(str, str)',
        'tags': 'list[Tag]',
        'full_asset': 'Asset',
        'sync_id': 'str',
        'date': 'datetime',
        'text': 'str',
        'time': 'float',
        'is_cloud': 'bool',
        'resolved': 'bool',
        'resolved_date': 'datetime',
        'asset': 'int',
        'root': 'int',
        'parent': 'int'
    }

    attribute_map = {
        'id': 'id',
        'assignee': 'assignee',
        'user': 'user',
        'drawing': 'drawing',
        'tags': 'tags',
        'full_asset': 'full_asset',
        'sync_id': 'sync_id',
        'date': 'date',
        'text': 'text',
        'time': 'time',
        'is_cloud': 'is_cloud',
        'resolved': 'resolved',
        'resolved_date': 'resolved_date',
        'asset': 'asset',
        'root': 'root',
        'parent': 'parent'
    }

    def __init__(self, id=None, assignee=None, user=None, drawing=None, tags=None, full_asset=None, sync_id=None, date=None, text=None, time=None, is_cloud=None, resolved=None, resolved_date=None, asset=None, root=None, parent=None, local_vars_configuration=None):  # noqa: E501
        """Comment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._assignee = None
        self._user = None
        self._drawing = None
        self._tags = None
        self._full_asset = None
        self._sync_id = None
        self._date = None
        self._text = None
        self._time = None
        self._is_cloud = None
        self._resolved = None
        self._resolved_date = None
        self._asset = None
        self._root = None
        self._parent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if assignee is not None:
            self.assignee = assignee
        if user is not None:
            self.user = user
        self.drawing = drawing
        if tags is not None:
            self.tags = tags
        if full_asset is not None:
            self.full_asset = full_asset
        if sync_id is not None:
            self.sync_id = sync_id
        if date is not None:
            self.date = date
        if text is not None:
            self.text = text
        self.time = time
        if is_cloud is not None:
            self.is_cloud = is_cloud
        if resolved is not None:
            self.resolved = resolved
        self.resolved_date = resolved_date
        self.asset = asset
        self.root = root
        self.parent = parent

    @property
    def id(self):
        """Gets the id of this Comment.  # noqa: E501


        :return: The id of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.


        :param id: The id of this Comment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def assignee(self):
        """Gets the assignee of this Comment.  # noqa: E501


        :return: The assignee of this Comment.  # noqa: E501
        :rtype: ElementsUserMini
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this Comment.


        :param assignee: The assignee of this Comment.  # noqa: E501
        :type: ElementsUserMini
        """

        self._assignee = assignee

    @property
    def user(self):
        """Gets the user of this Comment.  # noqa: E501


        :return: The user of this Comment.  # noqa: E501
        :rtype: ElementsUserMini
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Comment.


        :param user: The user of this Comment.  # noqa: E501
        :type: ElementsUserMini
        """

        self._user = user

    @property
    def drawing(self):
        """Gets the drawing of this Comment.  # noqa: E501


        :return: The drawing of this Comment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._drawing

    @drawing.setter
    def drawing(self, drawing):
        """Sets the drawing of this Comment.


        :param drawing: The drawing of this Comment.  # noqa: E501
        :type: dict(str, str)
        """

        self._drawing = drawing

    @property
    def tags(self):
        """Gets the tags of this Comment.  # noqa: E501


        :return: The tags of this Comment.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Comment.


        :param tags: The tags of this Comment.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def full_asset(self):
        """Gets the full_asset of this Comment.  # noqa: E501


        :return: The full_asset of this Comment.  # noqa: E501
        :rtype: Asset
        """
        return self._full_asset

    @full_asset.setter
    def full_asset(self, full_asset):
        """Sets the full_asset of this Comment.


        :param full_asset: The full_asset of this Comment.  # noqa: E501
        :type: Asset
        """

        self._full_asset = full_asset

    @property
    def sync_id(self):
        """Gets the sync_id of this Comment.  # noqa: E501


        :return: The sync_id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._sync_id

    @sync_id.setter
    def sync_id(self, sync_id):
        """Sets the sync_id of this Comment.


        :param sync_id: The sync_id of this Comment.  # noqa: E501
        :type: str
        """

        self._sync_id = sync_id

    @property
    def date(self):
        """Gets the date of this Comment.  # noqa: E501


        :return: The date of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Comment.


        :param date: The date of this Comment.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def text(self):
        """Gets the text of this Comment.  # noqa: E501


        :return: The text of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Comment.


        :param text: The text of this Comment.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def time(self):
        """Gets the time of this Comment.  # noqa: E501


        :return: The time of this Comment.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Comment.


        :param time: The time of this Comment.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def is_cloud(self):
        """Gets the is_cloud of this Comment.  # noqa: E501


        :return: The is_cloud of this Comment.  # noqa: E501
        :rtype: bool
        """
        return self._is_cloud

    @is_cloud.setter
    def is_cloud(self, is_cloud):
        """Sets the is_cloud of this Comment.


        :param is_cloud: The is_cloud of this Comment.  # noqa: E501
        :type: bool
        """

        self._is_cloud = is_cloud

    @property
    def resolved(self):
        """Gets the resolved of this Comment.  # noqa: E501


        :return: The resolved of this Comment.  # noqa: E501
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """Sets the resolved of this Comment.


        :param resolved: The resolved of this Comment.  # noqa: E501
        :type: bool
        """

        self._resolved = resolved

    @property
    def resolved_date(self):
        """Gets the resolved_date of this Comment.  # noqa: E501


        :return: The resolved_date of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._resolved_date

    @resolved_date.setter
    def resolved_date(self, resolved_date):
        """Sets the resolved_date of this Comment.


        :param resolved_date: The resolved_date of this Comment.  # noqa: E501
        :type: datetime
        """

        self._resolved_date = resolved_date

    @property
    def asset(self):
        """Gets the asset of this Comment.  # noqa: E501


        :return: The asset of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this Comment.


        :param asset: The asset of this Comment.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and asset is None:  # noqa: E501
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def root(self):
        """Gets the root of this Comment.  # noqa: E501


        :return: The root of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this Comment.


        :param root: The root of this Comment.  # noqa: E501
        :type: int
        """

        self._root = root

    @property
    def parent(self):
        """Gets the parent of this Comment.  # noqa: E501


        :return: The parent of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Comment.


        :param parent: The parent of this Comment.  # noqa: E501
        :type: int
        """

        self._parent = parent

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
        if not isinstance(other, Comment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Comment):
            return True

        return self.to_dict() != other.to_dict()
