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


class Parameters(object):
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
        'analytics': 'bool',
        'branding_css': 'str',
        'branding_logo': 'str',
        'external_url': 'str',
        'file_manager_recycle_bin': 'bool',
        'https_redirect': 'str',
        'language': 'str',
        'ltfs_default_restore_to_original_location': 'bool',
        'ltfs_default_search_directories': 'bool',
        'ltfs_library_address': 'str',
        'mail_styling': 'dict(str, str)',
        'media_auto_play': 'bool',
        'media_auto_proxy': 'bool',
        'media_auto_scan': 'bool',
        'media_auto_transport': 'bool',
        'media_auto_veritone_upload': 'bool',
        'media_default_custom_field_type': 'str',
        'media_default_delete_behaviour': 'str',
        'media_force_show_deleted': 'bool',
        'media_keep_selection_when_browsing': 'bool',
        'media_recycle_bin': 'bool',
        'ntp_offer_sync': 'bool',
        'otp_policy': 'str',
        'tasks_run_scheduled': 'bool',
        'users_default_permissions': 'str',
        'workspaces_folder_template_path': 'str',
        'workspaces_path': 'str'
    }

    attribute_map = {
        'analytics': 'analytics',
        'branding_css': 'branding_css',
        'branding_logo': 'branding_logo',
        'external_url': 'external_url',
        'file_manager_recycle_bin': 'file_manager_recycle_bin',
        'https_redirect': 'https_redirect',
        'language': 'language',
        'ltfs_default_restore_to_original_location': 'ltfs_default_restore_to_original_location',
        'ltfs_default_search_directories': 'ltfs_default_search_directories',
        'ltfs_library_address': 'ltfs_library_address',
        'mail_styling': 'mail_styling',
        'media_auto_play': 'media_auto_play',
        'media_auto_proxy': 'media_auto_proxy',
        'media_auto_scan': 'media_auto_scan',
        'media_auto_transport': 'media_auto_transport',
        'media_auto_veritone_upload': 'media_auto_veritone_upload',
        'media_default_custom_field_type': 'media_default_custom_field_type',
        'media_default_delete_behaviour': 'media_default_delete_behaviour',
        'media_force_show_deleted': 'media_force_show_deleted',
        'media_keep_selection_when_browsing': 'media_keep_selection_when_browsing',
        'media_recycle_bin': 'media_recycle_bin',
        'ntp_offer_sync': 'ntp_offer_sync',
        'otp_policy': 'otp_policy',
        'tasks_run_scheduled': 'tasks_run_scheduled',
        'users_default_permissions': 'users_default_permissions',
        'workspaces_folder_template_path': 'workspaces_folder_template_path',
        'workspaces_path': 'workspaces_path'
    }

    def __init__(self, analytics=None, branding_css=None, branding_logo=None, external_url=None, file_manager_recycle_bin=None, https_redirect=None, language=None, ltfs_default_restore_to_original_location=None, ltfs_default_search_directories=None, ltfs_library_address=None, mail_styling=None, media_auto_play=None, media_auto_proxy=None, media_auto_scan=None, media_auto_transport=None, media_auto_veritone_upload=None, media_default_custom_field_type=None, media_default_delete_behaviour=None, media_force_show_deleted=None, media_keep_selection_when_browsing=None, media_recycle_bin=None, ntp_offer_sync=None, otp_policy=None, tasks_run_scheduled=None, users_default_permissions=None, workspaces_folder_template_path=None, workspaces_path=None, local_vars_configuration=None):  # noqa: E501
        """Parameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._analytics = None
        self._branding_css = None
        self._branding_logo = None
        self._external_url = None
        self._file_manager_recycle_bin = None
        self._https_redirect = None
        self._language = None
        self._ltfs_default_restore_to_original_location = None
        self._ltfs_default_search_directories = None
        self._ltfs_library_address = None
        self._mail_styling = None
        self._media_auto_play = None
        self._media_auto_proxy = None
        self._media_auto_scan = None
        self._media_auto_transport = None
        self._media_auto_veritone_upload = None
        self._media_default_custom_field_type = None
        self._media_default_delete_behaviour = None
        self._media_force_show_deleted = None
        self._media_keep_selection_when_browsing = None
        self._media_recycle_bin = None
        self._ntp_offer_sync = None
        self._otp_policy = None
        self._tasks_run_scheduled = None
        self._users_default_permissions = None
        self._workspaces_folder_template_path = None
        self._workspaces_path = None
        self.discriminator = None

        if analytics is not None:
            self.analytics = analytics
        if branding_css is not None:
            self.branding_css = branding_css
        if branding_logo is not None:
            self.branding_logo = branding_logo
        self.external_url = external_url
        if file_manager_recycle_bin is not None:
            self.file_manager_recycle_bin = file_manager_recycle_bin
        self.https_redirect = https_redirect
        if language is not None:
            self.language = language
        if ltfs_default_restore_to_original_location is not None:
            self.ltfs_default_restore_to_original_location = ltfs_default_restore_to_original_location
        if ltfs_default_search_directories is not None:
            self.ltfs_default_search_directories = ltfs_default_search_directories
        self.ltfs_library_address = ltfs_library_address
        if mail_styling is not None:
            self.mail_styling = mail_styling
        if media_auto_play is not None:
            self.media_auto_play = media_auto_play
        if media_auto_proxy is not None:
            self.media_auto_proxy = media_auto_proxy
        if media_auto_scan is not None:
            self.media_auto_scan = media_auto_scan
        if media_auto_transport is not None:
            self.media_auto_transport = media_auto_transport
        if media_auto_veritone_upload is not None:
            self.media_auto_veritone_upload = media_auto_veritone_upload
        if media_default_custom_field_type is not None:
            self.media_default_custom_field_type = media_default_custom_field_type
        if media_default_delete_behaviour is not None:
            self.media_default_delete_behaviour = media_default_delete_behaviour
        self.media_force_show_deleted = media_force_show_deleted
        if media_keep_selection_when_browsing is not None:
            self.media_keep_selection_when_browsing = media_keep_selection_when_browsing
        if media_recycle_bin is not None:
            self.media_recycle_bin = media_recycle_bin
        if ntp_offer_sync is not None:
            self.ntp_offer_sync = ntp_offer_sync
        if otp_policy is not None:
            self.otp_policy = otp_policy
        if tasks_run_scheduled is not None:
            self.tasks_run_scheduled = tasks_run_scheduled
        if users_default_permissions is not None:
            self.users_default_permissions = users_default_permissions
        if workspaces_folder_template_path is not None:
            self.workspaces_folder_template_path = workspaces_folder_template_path
        if workspaces_path is not None:
            self.workspaces_path = workspaces_path

    @property
    def analytics(self):
        """Gets the analytics of this Parameters.  # noqa: E501


        :return: The analytics of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._analytics

    @analytics.setter
    def analytics(self, analytics):
        """Sets the analytics of this Parameters.


        :param analytics: The analytics of this Parameters.  # noqa: E501
        :type: bool
        """

        self._analytics = analytics

    @property
    def branding_css(self):
        """Gets the branding_css of this Parameters.  # noqa: E501


        :return: The branding_css of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._branding_css

    @branding_css.setter
    def branding_css(self, branding_css):
        """Sets the branding_css of this Parameters.


        :param branding_css: The branding_css of this Parameters.  # noqa: E501
        :type: str
        """

        self._branding_css = branding_css

    @property
    def branding_logo(self):
        """Gets the branding_logo of this Parameters.  # noqa: E501


        :return: The branding_logo of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._branding_logo

    @branding_logo.setter
    def branding_logo(self, branding_logo):
        """Sets the branding_logo of this Parameters.


        :param branding_logo: The branding_logo of this Parameters.  # noqa: E501
        :type: str
        """

        self._branding_logo = branding_logo

    @property
    def external_url(self):
        """Gets the external_url of this Parameters.  # noqa: E501

        http://host/  # noqa: E501

        :return: The external_url of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """Sets the external_url of this Parameters.

        http://host/  # noqa: E501

        :param external_url: The external_url of this Parameters.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_url is not None and len(external_url) > 1023):
            raise ValueError("Invalid value for `external_url`, length must be less than or equal to `1023`")  # noqa: E501

        self._external_url = external_url

    @property
    def file_manager_recycle_bin(self):
        """Gets the file_manager_recycle_bin of this Parameters.  # noqa: E501

        Recycle bins are usually either in Workspace/Share or Volume folder  # noqa: E501

        :return: The file_manager_recycle_bin of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._file_manager_recycle_bin

    @file_manager_recycle_bin.setter
    def file_manager_recycle_bin(self, file_manager_recycle_bin):
        """Sets the file_manager_recycle_bin of this Parameters.

        Recycle bins are usually either in Workspace/Share or Volume folder  # noqa: E501

        :param file_manager_recycle_bin: The file_manager_recycle_bin of this Parameters.  # noqa: E501
        :type: bool
        """

        self._file_manager_recycle_bin = file_manager_recycle_bin

    @property
    def https_redirect(self):
        """Gets the https_redirect of this Parameters.  # noqa: E501


        :return: The https_redirect of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._https_redirect

    @https_redirect.setter
    def https_redirect(self, https_redirect):
        """Sets the https_redirect of this Parameters.


        :param https_redirect: The https_redirect of this Parameters.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"domain", "on"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and https_redirect not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `https_redirect` ({0}), must be one of {1}"  # noqa: E501
                .format(https_redirect, allowed_values)
            )

        self._https_redirect = https_redirect

    @property
    def language(self):
        """Gets the language of this Parameters.  # noqa: E501


        :return: The language of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Parameters.


        :param language: The language of this Parameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["en", "fr", "de", "ru"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def ltfs_default_restore_to_original_location(self):
        """Gets the ltfs_default_restore_to_original_location of this Parameters.  # noqa: E501


        :return: The ltfs_default_restore_to_original_location of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._ltfs_default_restore_to_original_location

    @ltfs_default_restore_to_original_location.setter
    def ltfs_default_restore_to_original_location(self, ltfs_default_restore_to_original_location):
        """Sets the ltfs_default_restore_to_original_location of this Parameters.


        :param ltfs_default_restore_to_original_location: The ltfs_default_restore_to_original_location of this Parameters.  # noqa: E501
        :type: bool
        """

        self._ltfs_default_restore_to_original_location = ltfs_default_restore_to_original_location

    @property
    def ltfs_default_search_directories(self):
        """Gets the ltfs_default_search_directories of this Parameters.  # noqa: E501


        :return: The ltfs_default_search_directories of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._ltfs_default_search_directories

    @ltfs_default_search_directories.setter
    def ltfs_default_search_directories(self, ltfs_default_search_directories):
        """Sets the ltfs_default_search_directories of this Parameters.


        :param ltfs_default_search_directories: The ltfs_default_search_directories of this Parameters.  # noqa: E501
        :type: bool
        """

        self._ltfs_default_search_directories = ltfs_default_search_directories

    @property
    def ltfs_library_address(self):
        """Gets the ltfs_library_address of this Parameters.  # noqa: E501


        :return: The ltfs_library_address of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._ltfs_library_address

    @ltfs_library_address.setter
    def ltfs_library_address(self, ltfs_library_address):
        """Sets the ltfs_library_address of this Parameters.


        :param ltfs_library_address: The ltfs_library_address of this Parameters.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ltfs_library_address is not None and len(ltfs_library_address) > 255):
            raise ValueError("Invalid value for `ltfs_library_address`, length must be less than or equal to `255`")  # noqa: E501

        self._ltfs_library_address = ltfs_library_address

    @property
    def mail_styling(self):
        """Gets the mail_styling of this Parameters.  # noqa: E501


        :return: The mail_styling of this Parameters.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._mail_styling

    @mail_styling.setter
    def mail_styling(self, mail_styling):
        """Sets the mail_styling of this Parameters.


        :param mail_styling: The mail_styling of this Parameters.  # noqa: E501
        :type: dict(str, str)
        """

        self._mail_styling = mail_styling

    @property
    def media_auto_play(self):
        """Gets the media_auto_play of this Parameters.  # noqa: E501


        :return: The media_auto_play of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._media_auto_play

    @media_auto_play.setter
    def media_auto_play(self, media_auto_play):
        """Sets the media_auto_play of this Parameters.


        :param media_auto_play: The media_auto_play of this Parameters.  # noqa: E501
        :type: bool
        """

        self._media_auto_play = media_auto_play

    @property
    def media_auto_proxy(self):
        """Gets the media_auto_proxy of this Parameters.  # noqa: E501


        :return: The media_auto_proxy of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._media_auto_proxy

    @media_auto_proxy.setter
    def media_auto_proxy(self, media_auto_proxy):
        """Sets the media_auto_proxy of this Parameters.


        :param media_auto_proxy: The media_auto_proxy of this Parameters.  # noqa: E501
        :type: bool
        """

        self._media_auto_proxy = media_auto_proxy

    @property
    def media_auto_scan(self):
        """Gets the media_auto_scan of this Parameters.  # noqa: E501


        :return: The media_auto_scan of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._media_auto_scan

    @media_auto_scan.setter
    def media_auto_scan(self, media_auto_scan):
        """Sets the media_auto_scan of this Parameters.


        :param media_auto_scan: The media_auto_scan of this Parameters.  # noqa: E501
        :type: bool
        """

        self._media_auto_scan = media_auto_scan

    @property
    def media_auto_transport(self):
        """Gets the media_auto_transport of this Parameters.  # noqa: E501


        :return: The media_auto_transport of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._media_auto_transport

    @media_auto_transport.setter
    def media_auto_transport(self, media_auto_transport):
        """Sets the media_auto_transport of this Parameters.


        :param media_auto_transport: The media_auto_transport of this Parameters.  # noqa: E501
        :type: bool
        """

        self._media_auto_transport = media_auto_transport

    @property
    def media_auto_veritone_upload(self):
        """Gets the media_auto_veritone_upload of this Parameters.  # noqa: E501


        :return: The media_auto_veritone_upload of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._media_auto_veritone_upload

    @media_auto_veritone_upload.setter
    def media_auto_veritone_upload(self, media_auto_veritone_upload):
        """Sets the media_auto_veritone_upload of this Parameters.


        :param media_auto_veritone_upload: The media_auto_veritone_upload of this Parameters.  # noqa: E501
        :type: bool
        """

        self._media_auto_veritone_upload = media_auto_veritone_upload

    @property
    def media_default_custom_field_type(self):
        """Gets the media_default_custom_field_type of this Parameters.  # noqa: E501


        :return: The media_default_custom_field_type of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._media_default_custom_field_type

    @media_default_custom_field_type.setter
    def media_default_custom_field_type(self, media_default_custom_field_type):
        """Sets the media_default_custom_field_type of this Parameters.


        :param media_default_custom_field_type: The media_default_custom_field_type of this Parameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["file", "asset"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and media_default_custom_field_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `media_default_custom_field_type` ({0}), must be one of {1}"  # noqa: E501
                .format(media_default_custom_field_type, allowed_values)
            )

        self._media_default_custom_field_type = media_default_custom_field_type

    @property
    def media_default_delete_behaviour(self):
        """Gets the media_default_delete_behaviour of this Parameters.  # noqa: E501


        :return: The media_default_delete_behaviour of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._media_default_delete_behaviour

    @media_default_delete_behaviour.setter
    def media_default_delete_behaviour(self, media_default_delete_behaviour):
        """Sets the media_default_delete_behaviour of this Parameters.


        :param media_default_delete_behaviour: The media_default_delete_behaviour of this Parameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["disk", "database", "completely"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and media_default_delete_behaviour not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `media_default_delete_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(media_default_delete_behaviour, allowed_values)
            )

        self._media_default_delete_behaviour = media_default_delete_behaviour

    @property
    def media_force_show_deleted(self):
        """Gets the media_force_show_deleted of this Parameters.  # noqa: E501


        :return: The media_force_show_deleted of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._media_force_show_deleted

    @media_force_show_deleted.setter
    def media_force_show_deleted(self, media_force_show_deleted):
        """Sets the media_force_show_deleted of this Parameters.


        :param media_force_show_deleted: The media_force_show_deleted of this Parameters.  # noqa: E501
        :type: bool
        """

        self._media_force_show_deleted = media_force_show_deleted

    @property
    def media_keep_selection_when_browsing(self):
        """Gets the media_keep_selection_when_browsing of this Parameters.  # noqa: E501


        :return: The media_keep_selection_when_browsing of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._media_keep_selection_when_browsing

    @media_keep_selection_when_browsing.setter
    def media_keep_selection_when_browsing(self, media_keep_selection_when_browsing):
        """Sets the media_keep_selection_when_browsing of this Parameters.


        :param media_keep_selection_when_browsing: The media_keep_selection_when_browsing of this Parameters.  # noqa: E501
        :type: bool
        """

        self._media_keep_selection_when_browsing = media_keep_selection_when_browsing

    @property
    def media_recycle_bin(self):
        """Gets the media_recycle_bin of this Parameters.  # noqa: E501

        Recycle bin is usually in the .recycle-bin folder in the volume root  # noqa: E501

        :return: The media_recycle_bin of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._media_recycle_bin

    @media_recycle_bin.setter
    def media_recycle_bin(self, media_recycle_bin):
        """Sets the media_recycle_bin of this Parameters.

        Recycle bin is usually in the .recycle-bin folder in the volume root  # noqa: E501

        :param media_recycle_bin: The media_recycle_bin of this Parameters.  # noqa: E501
        :type: bool
        """

        self._media_recycle_bin = media_recycle_bin

    @property
    def ntp_offer_sync(self):
        """Gets the ntp_offer_sync of this Parameters.  # noqa: E501


        :return: The ntp_offer_sync of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._ntp_offer_sync

    @ntp_offer_sync.setter
    def ntp_offer_sync(self, ntp_offer_sync):
        """Sets the ntp_offer_sync of this Parameters.


        :param ntp_offer_sync: The ntp_offer_sync of this Parameters.  # noqa: E501
        :type: bool
        """

        self._ntp_offer_sync = ntp_offer_sync

    @property
    def otp_policy(self):
        """Gets the otp_policy of this Parameters.  # noqa: E501


        :return: The otp_policy of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._otp_policy

    @otp_policy.setter
    def otp_policy(self, otp_policy):
        """Sets the otp_policy of this Parameters.


        :param otp_policy: The otp_policy of this Parameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["admin-only", "self-service-setup-only", "self-service-all"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and otp_policy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `otp_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(otp_policy, allowed_values)
            )

        self._otp_policy = otp_policy

    @property
    def tasks_run_scheduled(self):
        """Gets the tasks_run_scheduled of this Parameters.  # noqa: E501


        :return: The tasks_run_scheduled of this Parameters.  # noqa: E501
        :rtype: bool
        """
        return self._tasks_run_scheduled

    @tasks_run_scheduled.setter
    def tasks_run_scheduled(self, tasks_run_scheduled):
        """Sets the tasks_run_scheduled of this Parameters.


        :param tasks_run_scheduled: The tasks_run_scheduled of this Parameters.  # noqa: E501
        :type: bool
        """

        self._tasks_run_scheduled = tasks_run_scheduled

    @property
    def users_default_permissions(self):
        """Gets the users_default_permissions of this Parameters.  # noqa: E501

        Copy this value from an existing user  # noqa: E501

        :return: The users_default_permissions of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._users_default_permissions

    @users_default_permissions.setter
    def users_default_permissions(self, users_default_permissions):
        """Sets the users_default_permissions of this Parameters.

        Copy this value from an existing user  # noqa: E501

        :param users_default_permissions: The users_default_permissions of this Parameters.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                users_default_permissions is not None and len(users_default_permissions) > 255):
            raise ValueError("Invalid value for `users_default_permissions`, length must be less than or equal to `255`")  # noqa: E501

        self._users_default_permissions = users_default_permissions

    @property
    def workspaces_folder_template_path(self):
        """Gets the workspaces_folder_template_path of this Parameters.  # noqa: E501


        :return: The workspaces_folder_template_path of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._workspaces_folder_template_path

    @workspaces_folder_template_path.setter
    def workspaces_folder_template_path(self, workspaces_folder_template_path):
        """Sets the workspaces_folder_template_path of this Parameters.


        :param workspaces_folder_template_path: The workspaces_folder_template_path of this Parameters.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                workspaces_folder_template_path is not None and len(workspaces_folder_template_path) > 255):
            raise ValueError("Invalid value for `workspaces_folder_template_path`, length must be less than or equal to `255`")  # noqa: E501

        self._workspaces_folder_template_path = workspaces_folder_template_path

    @property
    def workspaces_path(self):
        """Gets the workspaces_path of this Parameters.  # noqa: E501


        :return: The workspaces_path of this Parameters.  # noqa: E501
        :rtype: str
        """
        return self._workspaces_path

    @workspaces_path.setter
    def workspaces_path(self, workspaces_path):
        """Sets the workspaces_path of this Parameters.


        :param workspaces_path: The workspaces_path of this Parameters.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                workspaces_path is not None and len(workspaces_path) > 255):
            raise ValueError("Invalid value for `workspaces_path`, length must be less than or equal to `255`")  # noqa: E501

        self._workspaces_path = workspaces_path

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
        if not isinstance(other, Parameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Parameters):
            return True

        return self.to_dict() != other.to_dict()
