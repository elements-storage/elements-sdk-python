# elements_sdk.MainApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_all_notifications**](MainApi.md#acknowledge_all_notifications) | **POST** `/api/2/notifications/acknowledge-all` | 
[**apply_configuration**](MainApi.md#apply_configuration) | **POST** `/api/2/configuration/apply` | 
[**beep**](MainApi.md#beep) | **POST** `/api/2/system/beep` | 
[**check_certificate**](MainApi.md#check_certificate) | **POST** `/api/2/system/certificate/check` | 
[**check_chunk_uploaded**](MainApi.md#check_chunk_uploaded) | **GET** `/api/2/uploads/chunk` | 
[**check_internet_connectivity**](MainApi.md#check_internet_connectivity) | **POST** `/api/2/system/check-connectivity` | 
[**check_stor_next_license**](MainApi.md#check_stor_next_license) | **POST** `/api/2/stornext-license/check` | 
[**collect_diagnostics**](MainApi.md#collect_diagnostics) | **POST** `/api/2/system/collect-diagnostics` | 
[**count_unread_notifications**](MainApi.md#count_unread_notifications) | **GET** `/api/2/notifications/count-unread` | 
[**create_archive**](MainApi.md#create_archive) | **POST** `/api/2/download-archive/create` | 
[**create_certificate_signing_request**](MainApi.md#create_certificate_signing_request) | **POST** `/api/2/system/certificate/csr` | 
[**create_cloud_account**](MainApi.md#create_cloud_account) | **POST** `/api/2/cloud/accounts` | 
[**create_filesystem_permission**](MainApi.md#create_filesystem_permission) | **POST** `/api/2/filesystem-permissions` | 
[**create_group**](MainApi.md#create_group) | **POST** `/api/2/groups` | 
[**create_home_workspace**](MainApi.md#create_home_workspace) | **POST** `/api/2/users/{id}/home` | 
[**create_ldap_server**](MainApi.md#create_ldap_server) | **POST** `/api/2/ldap-servers` | 
[**create_notification_setting**](MainApi.md#create_notification_setting) | **POST** `/api/2/notification-settings` | 
[**create_ntp_server**](MainApi.md#create_ntp_server) | **POST** `/api/2/system/time/servers` | 
[**create_storage_node**](MainApi.md#create_storage_node) | **POST** `/api/2/nodes` | 
[**create_user**](MainApi.md#create_user) | **POST** `/api/2/users` | 
[**create_workstation**](MainApi.md#create_workstation) | **POST** `/api/2/workstations` | 
[**delete_all_notifications**](MainApi.md#delete_all_notifications) | **DELETE** `/api/2/notifications/all` | 
[**delete_certificate_signing_request**](MainApi.md#delete_certificate_signing_request) | **DELETE** `/api/2/system/certificate/csr` | 
[**delete_cloud_account**](MainApi.md#delete_cloud_account) | **DELETE** `/api/2/cloud/accounts/{id}` | 
[**delete_disabled_users**](MainApi.md#delete_disabled_users) | **POST** `/api/2/users/delete-disabled` | 
[**delete_download_archive**](MainApi.md#delete_download_archive) | **DELETE** `/api/2/download-archive/{id}` | 
[**delete_filesystem_permission**](MainApi.md#delete_filesystem_permission) | **DELETE** `/api/2/filesystem-permissions/{id}` | 
[**delete_group**](MainApi.md#delete_group) | **DELETE** `/api/2/groups/{id}` | 
[**delete_home_workspace**](MainApi.md#delete_home_workspace) | **DELETE** `/api/2/users/{id}/home` | 
[**delete_ldap_server**](MainApi.md#delete_ldap_server) | **DELETE** `/api/2/ldap-servers/{id}` | 
[**delete_my_avatar**](MainApi.md#delete_my_avatar) | **DELETE** `/api/2/users/me/avatar` | 
[**delete_notification**](MainApi.md#delete_notification) | **DELETE** `/api/2/notifications/{id}` | 
[**delete_notification_setting**](MainApi.md#delete_notification_setting) | **DELETE** `/api/2/notification-settings/{id}` | 
[**delete_ntp_server**](MainApi.md#delete_ntp_server) | **DELETE** `/api/2/system/time/servers/{id}` | 
[**delete_smtp_configuration**](MainApi.md#delete_smtp_configuration) | **DELETE** `/api/2/system/smtp` | 
[**delete_storage_node**](MainApi.md#delete_storage_node) | **DELETE** `/api/2/nodes/{id}` | 
[**delete_user**](MainApi.md#delete_user) | **DELETE** `/api/2/users/{id}` | 
[**delete_user_avatar**](MainApi.md#delete_user_avatar) | **DELETE** `/api/2/users/{id}/avatar` | 
[**delete_workstation**](MainApi.md#delete_workstation) | **DELETE** `/api/2/workstations/{id}` | 
[**disable_user_totp**](MainApi.md#disable_user_totp) | **DELETE** `/api/2/users/{id}/totp` | 
[**enable_user_totp**](MainApi.md#enable_user_totp) | **POST** `/api/2/users/{id}/totp` | 
[**finish_upload**](MainApi.md#finish_upload) | **POST** `/api/2/uploads/finish` | 
[**fix_ldap_group_memberships**](MainApi.md#fix_ldap_group_memberships) | **POST** `/api/2/ldap-servers/{id}/fix-memberships` | 
[**get_all_client_sessions**](MainApi.md#get_all_client_sessions) | **GET** `/api/2/client-sessions` | 
[**get_all_cloud_accounts**](MainApi.md#get_all_cloud_accounts) | **GET** `/api/2/cloud/accounts` | 
[**get_all_download_archives**](MainApi.md#get_all_download_archives) | **GET** `/api/2/download-archive` | 
[**get_all_downloads**](MainApi.md#get_all_downloads) | **GET** `/api/2/downloads` | 
[**get_all_filesystem_permissions**](MainApi.md#get_all_filesystem_permissions) | **GET** `/api/2/filesystem-permissions` | 
[**get_all_groups**](MainApi.md#get_all_groups) | **GET** `/api/2/groups` | 
[**get_all_interfaces**](MainApi.md#get_all_interfaces) | **GET** `/api/2/interfaces` | 
[**get_all_ldap_servers**](MainApi.md#get_all_ldap_servers) | **GET** `/api/2/ldap-servers` | 
[**get_all_notification_receipts**](MainApi.md#get_all_notification_receipts) | **GET** `/api/2/notification-receipts` | 
[**get_all_notification_settings**](MainApi.md#get_all_notification_settings) | **GET** `/api/2/notification-settings` | 
[**get_all_notifications**](MainApi.md#get_all_notifications) | **GET** `/api/2/notifications` | 
[**get_all_ntp_servers**](MainApi.md#get_all_ntp_servers) | **GET** `/api/2/system/time/servers` | 
[**get_all_storage_nodes**](MainApi.md#get_all_storage_nodes) | **GET** `/api/2/nodes` | 
[**get_all_users**](MainApi.md#get_all_users) | **GET** `/api/2/users` | 
[**get_all_workstations**](MainApi.md#get_all_workstations) | **GET** `/api/2/workstations` | 
[**get_certificate_configuration**](MainApi.md#get_certificate_configuration) | **GET** `/api/2/system/certificate` | 
[**get_certificate_signing_request**](MainApi.md#get_certificate_signing_request) | **GET** `/api/2/system/certificate/csr` | 
[**get_client_download_file**](MainApi.md#get_client_download_file) | **GET** `/api/2/downloads/clients/{file}` | 
[**get_client_downloads**](MainApi.md#get_client_downloads) | **GET** `/api/2/downloads/clients` | 
[**get_client_session**](MainApi.md#get_client_session) | **GET** `/api/2/client-sessions/{id}` | 
[**get_cloud_account**](MainApi.md#get_cloud_account) | **GET** `/api/2/cloud/accounts/{id}` | 
[**get_cloud_account_costs**](MainApi.md#get_cloud_account_costs) | **GET** `/api/2/cloud/accounts/{id}/costs` | 
[**get_cloud_account_storage_roots**](MainApi.md#get_cloud_account_storage_roots) | **GET** `/api/2/cloud/accounts/{id}/storage-roots` | 
[**get_cloud_account_volume_sizes**](MainApi.md#get_cloud_account_volume_sizes) | **GET** `/api/2/cloud/accounts/{id}/volume-sizes` | 
[**get_current_node**](MainApi.md#get_current_node) | **GET** `/api/2/nodes/current` | 
[**get_current_workstation**](MainApi.md#get_current_workstation) | **GET** `/api/2/workstations/current` | 
[**get_download**](MainApi.md#get_download) | **GET** `/api/2/downloads/{id}` | 
[**get_download_archive**](MainApi.md#get_download_archive) | **GET** `/api/2/download-archive/{id}` | 
[**get_download_archive_file**](MainApi.md#get_download_archive_file) | **GET** `/api/2/download-archive/{id}/download` | 
[**get_download_file**](MainApi.md#get_download_file) | **GET** `/api/2/downloads/{id}/download` | 
[**get_download_icon**](MainApi.md#get_download_icon) | **GET** `/api/2/downloads/{id}/icon` | 
[**get_filesystem_permission**](MainApi.md#get_filesystem_permission) | **GET** `/api/2/filesystem-permissions/{id}` | 
[**get_group**](MainApi.md#get_group) | **GET** `/api/2/groups/{id}` | 
[**get_home_workspace**](MainApi.md#get_home_workspace) | **GET** `/api/2/users/{id}/home` | 
[**get_interface**](MainApi.md#get_interface) | **GET** `/api/2/interfaces/{id}` | 
[**get_ipmi_configuration**](MainApi.md#get_ipmi_configuration) | **GET** `/api/2/nodes/{id}/ipmi` | 
[**get_ldap_server**](MainApi.md#get_ldap_server) | **GET** `/api/2/ldap-servers/{id}` | 
[**get_ldap_server_groups**](MainApi.md#get_ldap_server_groups) | **GET** `/api/2/ldap-servers/{id}/groups` | 
[**get_ldap_server_users**](MainApi.md#get_ldap_server_users) | **GET** `/api/2/ldap-servers/{id}/users` | 
[**get_license**](MainApi.md#get_license) | **GET** `/api/2/license` | 
[**get_license_components**](MainApi.md#get_license_components) | **GET** `/api/2/license/components` | 
[**get_log**](MainApi.md#get_log) | **GET** `/api/2/system/log/{path}` | 
[**get_my_avatar**](MainApi.md#get_my_avatar) | **GET** `/api/2/users/me/avatar` | 
[**get_node_ipmi_sensors**](MainApi.md#get_node_ipmi_sensors) | **GET** `/api/2/nodes/{id}/sensors` | 
[**get_node_raid_status**](MainApi.md#get_node_raid_status) | **GET** `/api/2/nodes/{id}/raid/status` | 
[**get_node_stats**](MainApi.md#get_node_stats) | **GET** `/api/2/nodes/{id}/stats` | 
[**get_node_time**](MainApi.md#get_node_time) | **GET** `/api/2/nodes/{id}/time` | 
[**get_notification**](MainApi.md#get_notification) | **GET** `/api/2/notifications/{id}` | 
[**get_notification_receipt**](MainApi.md#get_notification_receipt) | **GET** `/api/2/notification-receipts/{id}` | 
[**get_notification_setting**](MainApi.md#get_notification_setting) | **GET** `/api/2/notification-settings/{id}` | 
[**get_ntp_server**](MainApi.md#get_ntp_server) | **GET** `/api/2/system/time/servers/{id}` | 
[**get_parameters**](MainApi.md#get_parameters) | **GET** `/api/2/parameters` | 
[**get_password_policy**](MainApi.md#get_password_policy) | **GET** `/api/2/system/password-policy` | 
[**get_profile**](MainApi.md#get_profile) | **GET** `/api/2/users/me` | 
[**get_release_notes**](MainApi.md#get_release_notes) | **GET** `/api/2/release-notes` | 
[**get_service_status**](MainApi.md#get_service_status) | **GET** `/api/2/nodes/{id}/services/{service}` | 
[**get_smtp_configuration**](MainApi.md#get_smtp_configuration) | **GET** `/api/2/system/smtp` | 
[**get_stor_next_license**](MainApi.md#get_stor_next_license) | **GET** `/api/2/stornext-license` | 
[**get_storage_node**](MainApi.md#get_storage_node) | **GET** `/api/2/nodes/{id}` | 
[**get_system_info**](MainApi.md#get_system_info) | **GET** `/api/2/system/info` | 
[**get_user**](MainApi.md#get_user) | **GET** `/api/2/users/{id}` | 
[**get_user_avatar**](MainApi.md#get_user_avatar) | **GET** `/api/2/users/{id}/avatar` | 
[**get_workstation**](MainApi.md#get_workstation) | **GET** `/api/2/workstations/{id}` | 
[**install_stor_next_license**](MainApi.md#install_stor_next_license) | **POST** `/api/2/stornext-license` | 
[**patch_certificate_configuration**](MainApi.md#patch_certificate_configuration) | **PATCH** `/api/2/system/certificate` | 
[**patch_cloud_account**](MainApi.md#patch_cloud_account) | **PATCH** `/api/2/cloud/accounts/{id}` | 
[**patch_current_workstation**](MainApi.md#patch_current_workstation) | **PATCH** `/api/2/workstations/current` | 
[**patch_download_archive**](MainApi.md#patch_download_archive) | **PATCH** `/api/2/download-archive/{id}` | 
[**patch_filesystem_permission**](MainApi.md#patch_filesystem_permission) | **PATCH** `/api/2/filesystem-permissions/{id}` | 
[**patch_group**](MainApi.md#patch_group) | **PATCH** `/api/2/groups/{id}` | 
[**patch_interface**](MainApi.md#patch_interface) | **PATCH** `/api/2/interfaces/{id}` | 
[**patch_ldap_server**](MainApi.md#patch_ldap_server) | **PATCH** `/api/2/ldap-servers/{id}` | 
[**patch_notification**](MainApi.md#patch_notification) | **PATCH** `/api/2/notifications/{id}` | 
[**patch_notification_receipt**](MainApi.md#patch_notification_receipt) | **PATCH** `/api/2/notification-receipts/{id}` | 
[**patch_notification_setting**](MainApi.md#patch_notification_setting) | **PATCH** `/api/2/notification-settings/{id}` | 
[**patch_ntp_server**](MainApi.md#patch_ntp_server) | **PATCH** `/api/2/system/time/servers/{id}` | 
[**patch_profile**](MainApi.md#patch_profile) | **PATCH** `/api/2/users/me` | 
[**patch_storage_node**](MainApi.md#patch_storage_node) | **PATCH** `/api/2/nodes/{id}` | 
[**patch_user**](MainApi.md#patch_user) | **PATCH** `/api/2/users/{id}` | 
[**patch_workstation**](MainApi.md#patch_workstation) | **PATCH** `/api/2/workstations/{id}` | 
[**probe_ldap_config**](MainApi.md#probe_ldap_config) | **POST** `/api/2/ldap-servers/probe` | 
[**reboot**](MainApi.md#reboot) | **POST** `/api/2/system/reboot` | 
[**register_upload**](MainApi.md#register_upload) | **POST** `/api/2/uploads/register` | 
[**register_upload_metadata**](MainApi.md#register_upload_metadata) | **POST** `/api/2/uploads/metadata` | 
[**render_email_template_preview**](MainApi.md#render_email_template_preview) | **POST** `/api/2/system/smtp/preview` | 
[**rescan_interfaces**](MainApi.md#rescan_interfaces) | **POST** `/api/2/nodes/{id}/rescan-interfaces` | 
[**reset_user_password**](MainApi.md#reset_user_password) | **POST** `/api/2/users/{id}/password/reset` | 
[**restart_web_ui**](MainApi.md#restart_web_ui) | **POST** `/api/2/system/restart-webui` | 
[**run_service_operation**](MainApi.md#run_service_operation) | **POST** `/api/2/nodes/{id}/services/{service}/{operation}` | 
[**set_ipmi_configuration**](MainApi.md#set_ipmi_configuration) | **PUT** `/api/2/nodes/{id}/ipmi` | 
[**set_my_password**](MainApi.md#set_my_password) | **POST** `/api/2/users/me/password` | 
[**set_node_time**](MainApi.md#set_node_time) | **PUT** `/api/2/nodes/{id}/time` | 
[**set_user_password**](MainApi.md#set_user_password) | **POST** `/api/2/users/{id}/password` | 
[**shutdown**](MainApi.md#shutdown) | **POST** `/api/2/system/shutdown` | 
[**silence_node_raid_alarm**](MainApi.md#silence_node_raid_alarm) | **POST** `/api/2/nodes/{id}/raid/silence-alarm` | 
[**start_solr_reindex**](MainApi.md#start_solr_reindex) | **POST** `/api/2/system/solr/reindex` | 
[**start_support_session**](MainApi.md#start_support_session) | **POST** `/api/2/system/support-session/start` | 
[**start_system_backup**](MainApi.md#start_system_backup) | **POST** `/api/2/system/backup/start` | 
[**sync_ldap_group**](MainApi.md#sync_ldap_group) | **POST** `/api/2/groups/{id}/ldap-sync` | 
[**sync_ldap_users**](MainApi.md#sync_ldap_users) | **POST** `/api/2/ldap-servers/{id}/sync-users` | 
[**sync_time**](MainApi.md#sync_time) | **POST** `/api/2/system/time/sync` | 
[**sync_user_totp**](MainApi.md#sync_user_totp) | **PUT** `/api/2/users/{id}/totp` | 
[**test_cloud_account_credentials**](MainApi.md#test_cloud_account_credentials) | **POST** `/api/2/cloud/accounts/test-credentials` | 
[**test_smtp_configuration**](MainApi.md#test_smtp_configuration) | **POST** `/api/2/system/smtp/test` | 
[**update_certificate_configuration**](MainApi.md#update_certificate_configuration) | **PUT** `/api/2/system/certificate` | 
[**update_cloud_account**](MainApi.md#update_cloud_account) | **PUT** `/api/2/cloud/accounts/{id}` | 
[**update_current_workstation**](MainApi.md#update_current_workstation) | **PUT** `/api/2/workstations/current` | 
[**update_download_archive**](MainApi.md#update_download_archive) | **PUT** `/api/2/download-archive/{id}` | 
[**update_filesystem_permission**](MainApi.md#update_filesystem_permission) | **PUT** `/api/2/filesystem-permissions/{id}` | 
[**update_group**](MainApi.md#update_group) | **PUT** `/api/2/groups/{id}` | 
[**update_interface**](MainApi.md#update_interface) | **PUT** `/api/2/interfaces/{id}` | 
[**update_ldap_server**](MainApi.md#update_ldap_server) | **PUT** `/api/2/ldap-servers/{id}` | 
[**update_my_avatar**](MainApi.md#update_my_avatar) | **POST** `/api/2/users/me/avatar` | 
[**update_notification**](MainApi.md#update_notification) | **PUT** `/api/2/notifications/{id}` | 
[**update_notification_receipt**](MainApi.md#update_notification_receipt) | **PUT** `/api/2/notification-receipts/{id}` | 
[**update_notification_setting**](MainApi.md#update_notification_setting) | **PUT** `/api/2/notification-settings/{id}` | 
[**update_ntp_server**](MainApi.md#update_ntp_server) | **PUT** `/api/2/system/time/servers/{id}` | 
[**update_parameters**](MainApi.md#update_parameters) | **PUT** `/api/2/parameters` | 
[**update_password_policy**](MainApi.md#update_password_policy) | **PUT** `/api/2/system/password-policy` | 
[**update_profile**](MainApi.md#update_profile) | **PUT** `/api/2/users/me` | 
[**update_smtp_configuration**](MainApi.md#update_smtp_configuration) | **PUT** `/api/2/system/smtp` | 
[**update_storage_node**](MainApi.md#update_storage_node) | **PUT** `/api/2/nodes/{id}` | 
[**update_user**](MainApi.md#update_user) | **PUT** `/api/2/users/{id}` | 
[**update_user_avatar**](MainApi.md#update_user_avatar) | **POST** `/api/2/users/{id}/avatar` | 
[**update_workstation**](MainApi.md#update_workstation) | **PUT** `/api/2/workstations/{id}` | 
[**upload_chunk**](MainApi.md#upload_chunk) | **POST** `/api/2/uploads/chunk` | 


# **acknowledge_all_notifications**
    def acknowledge_all_notifications()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.acknowledge_all_notifications()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->acknowledge_all_notifications: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **apply_configuration**
    def TaskInfo apply_configuration()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.task_info import TaskInfo
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.apply_configuration()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->apply_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **beep**
    def beep()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.beep()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->beep: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **check_certificate**
    def Certificate check_certificate(check_certificate_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.check_certificate_request import CheckCertificateRequest
from elements_sdk.model.certificate import Certificate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    check_certificate_request = CheckCertificateRequest(
        certificate="certificate_example",
        key="key_example",
    ) # CheckCertificateRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.check_certificate(check_certificate_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->check_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_certificate_request** | [**CheckCertificateRequest**](CheckCertificateRequest.md)|  |

### Return type

[**Certificate**](Certificate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **check_chunk_uploaded**
    def check_chunk_uploaded()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    upload_id = "upload_id_example" # str |  (optional)
    chunk_number = "chunk_number_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.check_chunk_uploaded(upload_id=upload_id, chunk_number=chunk_number)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->check_chunk_uploaded: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | [optional]
 **chunk_number** | **str**|  | [optional]

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **check_internet_connectivity**
    def CheckConnectivityEndpointResponse check_internet_connectivity()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.check_connectivity_endpoint_response import CheckConnectivityEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.check_internet_connectivity()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->check_internet_connectivity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CheckConnectivityEndpointResponse**](CheckConnectivityEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **check_stor_next_license**
    def [StorNextLicenseCheckEndpointResponse] check_stor_next_license(stornext_license)



### Required permissions    * User account permission: `system:admin-access`   * License component: stornext_mdc 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.stor_next_license_check_endpoint_response import StorNextLicenseCheckEndpointResponse
from elements_sdk.model.stornext_license import StornextLicense
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    stornext_license = StornextLicense(
        license="license_example",
    ) # StornextLicense | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.check_stor_next_license(stornext_license)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->check_stor_next_license: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stornext_license** | [**StornextLicense**](StornextLicense.md)|  |

### Return type

[**[StorNextLicenseCheckEndpointResponse]**](StorNextLicenseCheckEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **collect_diagnostics**
    def DownloadArchive collect_diagnostics()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.download_archive import DownloadArchive
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.collect_diagnostics()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->collect_diagnostics: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **count_unread_notifications**
    def UnreadCount count_unread_notifications()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.unread_count import UnreadCount
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    cursor = "cursor_example" # str | The pagination cursor value. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.count_unread_notifications(ordering=ordering, cursor=cursor)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->count_unread_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]

### Return type

[**UnreadCount**](UnreadCount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_archive**
    def DownloadArchive create_archive(create_download_archive)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.create_download_archive import CreateDownloadArchive
from elements_sdk.model.download_archive import DownloadArchive
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    create_download_archive = CreateDownloadArchive(
        paths=[
            "paths_example",
        ],
        file_ids=[
            1,
        ],
        bundle_ids=[
            1,
        ],
        proxy=True,
        for_root=1,
    ) # CreateDownloadArchive | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_archive(create_download_archive)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_download_archive** | [**CreateDownloadArchive**](CreateDownloadArchive.md)|  |

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_certificate_signing_request**
    def TaskInfo create_certificate_signing_request(certificate_signing_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.certificate_signing_request import CertificateSigningRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    certificate_signing_request = CertificateSigningRequest(
        country="country_example",
        state="state_example",
        locality="locality_example",
        organization="organization_example",
        organizational_unit="organizational_unit_example",
        common_name="common_name_example",
        email="email_example",
    ) # CertificateSigningRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_certificate_signing_request(certificate_signing_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_certificate_signing_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_signing_request** | [**CertificateSigningRequest**](CertificateSigningRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_cloud_account**
    def CloudAccount create_cloud_account(cloud_account_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.cloud_account_update import CloudAccountUpdate
from elements_sdk.model.cloud_account import CloudAccount
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    cloud_account_update = CloudAccountUpdate(
        name="name_example",
        provider="azure",
        access_id="access_id_example",
        secret="secret_example",
        tenant="tenant_example",
        subscription="subscription_example",
        endpoint="endpoint_example",
        mount_credentials_management="share",
    ) # CloudAccountUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cloud_account(cloud_account_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_cloud_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account_update** | [**CloudAccountUpdate**](CloudAccountUpdate.md)|  |

### Return type

[**CloudAccount**](CloudAccount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_filesystem_permission**
    def FilesystemPermission create_filesystem_permission(filesystem_permission_update)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.filesystem_permission_update import FilesystemPermissionUpdate
from elements_sdk.model.filesystem_permission import FilesystemPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    filesystem_permission_update = FilesystemPermissionUpdate(
        path="path_example",
        read_only=True,
        user=1,
        group=1,
    ) # FilesystemPermissionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_filesystem_permission(filesystem_permission_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_filesystem_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filesystem_permission_update** | [**FilesystemPermissionUpdate**](FilesystemPermissionUpdate.md)|  |

### Return type

[**FilesystemPermission**](FilesystemPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_group**
    def ElementsGroupDetail create_group(elements_group_detail_update)



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_group_detail_update import ElementsGroupDetailUpdate
from elements_sdk.model.elements_group_detail import ElementsGroupDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    elements_group_detail_update = ElementsGroupDetailUpdate(
        permissions=[
            "permissions_example",
        ],
        members=[
            ElementsUserReference(
                id=1,
            ),
        ],
        ldap=None,
        name="name_example",
        ldap_dn="ldap_dn_example",
        ldap_guid="ldap_guid_example",
        unix_groupname="unix_groupname_example",
        gid=-2147483648,
    ) # ElementsGroupDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_group(elements_group_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elements_group_detail_update** | [**ElementsGroupDetailUpdate**](ElementsGroupDetailUpdate.md)|  |

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_home_workspace**
    def Workspace create_home_workspace(id, create_home_workspace_request)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workspace import Workspace
from elements_sdk.model.create_home_workspace_request import CreateHomeWorkspaceRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.
    create_home_workspace_request = CreateHomeWorkspaceRequest(
        volume=1,
    ) # CreateHomeWorkspaceRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_home_workspace(id, create_home_workspace_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_home_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |
 **create_home_workspace_request** | [**CreateHomeWorkspaceRequest**](CreateHomeWorkspaceRequest.md)|  |

### Return type

[**Workspace**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ldap_server**
    def LDAPServerDetail create_ldap_server(ldap_server_detail_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ldap_server_detail_update import LDAPServerDetailUpdate
from elements_sdk.model.ldap_server_detail import LDAPServerDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ldap_server_detail_update = LDAPServerDetailUpdate(
        type=0,
        name="name_example",
        host="host_example",
        tls="ssl",
        username="username_example",
        password="password_example",
        domain="domain_example",
        search_filter="search_filter_example",
        group_search_filter="group_search_filter_example",
        nt_domain="nt_domain_example",
        nt_domain_mapping="nt_domain_mapping_example",
        root="root_example",
        users_root="users_root_example",
        groups_root="groups_root_example",
        use_wbinfo=True,
        username_format="sAMAccountName",
    ) # LDAPServerDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ldap_server(ldap_server_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_ldap_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_server_detail_update** | [**LDAPServerDetailUpdate**](LDAPServerDetailUpdate.md)|  |

### Return type

[**LDAPServerDetail**](LDAPServerDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_notification_setting**
    def NotificationSetting create_notification_setting(notification_setting_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_setting_update import NotificationSettingUpdate
from elements_sdk.model.notification_setting import NotificationSetting
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    notification_setting_update = NotificationSettingUpdate(
        topic="topic_example",
        type="type_example",
        user=1,
    ) # NotificationSettingUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_notification_setting(notification_setting_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_notification_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_setting_update** | [**NotificationSettingUpdate**](NotificationSettingUpdate.md)|  |

### Return type

[**NotificationSetting**](NotificationSetting.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ntp_server**
    def NTPServer create_ntp_server(ntp_server_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ntp_server_update import NTPServerUpdate
from elements_sdk.model.ntp_server import NTPServer
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ntp_server_update = NTPServerUpdate(
        address="address_example",
        options="options_example",
    ) # NTPServerUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ntp_server(ntp_server_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_server_update** | [**NTPServerUpdate**](NTPServerUpdate.md)|  |

### Return type

[**NTPServer**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_storage_node**
    def StorageNode create_storage_node(create_storage_node_request)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.create_storage_node_request import CreateStorageNodeRequest
from elements_sdk.model.storage_node import StorageNode
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    create_storage_node_request = CreateStorageNodeRequest(
        name="name_example",
        backend="backend_example",
    ) # CreateStorageNodeRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_storage_node(create_storage_node_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_storage_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_storage_node_request** | [**CreateStorageNodeRequest**](CreateStorageNodeRequest.md)|  |

### Return type

[**StorageNode**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_user**
    def ElementsUserDetail create_user(elements_user_detail_update)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_user_detail import ElementsUserDetail
from elements_sdk.model.elements_user_detail_update import ElementsUserDetailUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    elements_user_detail_update = ElementsUserDetailUpdate(
        allow_changing_password=True,
        allow_wan_login=True,
        avatar="avatar_example",
        default_page="default_page_example",
        email="email_example",
        expiry=dateutil_parser('1970-01-01T00:00:00.00Z'),
        fm_bookmarks=[
            "fm_bookmarks_example",
        ],
        full_name="full_name_example",
        gid=-2147483648,
        home=1,
        is_external=True,
        is_cloud=True,
        is_enabled=True,
        language="en",
        ldap=None,
        ldap_dn="ldap_dn_example",
        password_change_required=True,
        permissions=[
            "permissions_example",
        ],
        shaper_ceiling=0,
        shaper_rate=0,
        uid=-2147483648,
        unix_username="unix_username_example",
        username="username_example",
        groups=[
            1,
        ],
    ) # ElementsUserDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_user(elements_user_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elements_user_detail_update** | [**ElementsUserDetailUpdate**](ElementsUserDetailUpdate.md)|  |

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_workstation**
    def Workstation create_workstation(workstation_update)



### Required permissions    * Authenticated user   * Own workstation or <class 'elements.api.permissions.UserPermission.<locals>.Permission'> 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workstation_update import WorkstationUpdate
from elements_sdk.model.workstation import Workstation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    workstation_update = WorkstationUpdate(
        report={
            "key": "key_example",
        },
        name="name_example",
        hostname="hostname_example",
        last_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # WorkstationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_workstation(workstation_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->create_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstation_update** | [**WorkstationUpdate**](WorkstationUpdate.md)|  |

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_all_notifications**
    def delete_all_notifications()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.delete_all_notifications()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_all_notifications: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_certificate_signing_request**
    def delete_certificate_signing_request()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.delete_certificate_signing_request()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_certificate_signing_request: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_cloud_account**
    def delete_cloud_account(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_cloud_account(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_cloud_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_disabled_users**
    def delete_disabled_users(delete_disabled_users_request)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.delete_disabled_users_request import DeleteDisabledUsersRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    delete_disabled_users_request = DeleteDisabledUsersRequest(
        delete_workspace_content=False,
        delete_media_root=False,
    ) # DeleteDisabledUsersRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_disabled_users(delete_disabled_users_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_disabled_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_disabled_users_request** | [**DeleteDisabledUsersRequest**](DeleteDisabledUsersRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_download_archive**
    def delete_download_archive(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this download archive.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_download_archive(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_download_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this download archive. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_filesystem_permission**
    def delete_filesystem_permission(id)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this filesystem permission.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_filesystem_permission(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_filesystem_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filesystem permission. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_group**
    def delete_group(id)



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Group.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_group(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_home_workspace**
    def delete_home_workspace(id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_home_workspace(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_home_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ldap_server**
    def delete_ldap_server(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this LDAP Server.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ldap_server(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_ldap_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_my_avatar**
    def delete_my_avatar()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.delete_my_avatar()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_my_avatar: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_notification**
    def delete_notification(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this Notification.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_notification(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Notification. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_notification_setting**
    def delete_notification_setting(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this notification setting.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_notification_setting(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_notification_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification setting. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ntp_server**
    def delete_ntp_server(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this NTP Server.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ntp_server(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this NTP Server. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_smtp_configuration**
    def delete_smtp_configuration()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.delete_smtp_configuration()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_smtp_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_storage_node**
    def delete_storage_node(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_storage_node(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_storage_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_user**
    def delete_user(id)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_user(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_user_avatar**
    def delete_user_avatar(id)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_user_avatar(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_user_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_workstation**
    def delete_workstation(id)



### Required permissions    * Authenticated user   * Own workstation or <class 'elements.api.permissions.UserPermission.<locals>.Permission'> 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A unique value identifying this workstation.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_workstation(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->delete_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this workstation. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **disable_user_totp**
    def disable_user_totp(id)



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.

    # example passing only required values which don't have defaults set
    try:
        api_instance.disable_user_totp(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->disable_user_totp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **enable_user_totp**
    def enable_user_totp(id, enable_totp_request)



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.enable_totp_request import EnableTOTPRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.
    enable_totp_request = EnableTOTPRequest(
        key="key_example",
        otp="otp_example",
    ) # EnableTOTPRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.enable_user_totp(id, enable_totp_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->enable_user_totp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |
 **enable_totp_request** | [**EnableTOTPRequest**](EnableTOTPRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **finish_upload**
    def TaskInfo finish_upload(finish_upload_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.finish_upload_endpoint_request import FinishUploadEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    finish_upload_endpoint_request = FinishUploadEndpointRequest(
        upload_id="upload_id_example",
    ) # FinishUploadEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.finish_upload(finish_upload_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->finish_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finish_upload_endpoint_request** | [**FinishUploadEndpointRequest**](FinishUploadEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **fix_ldap_group_memberships**
    def fix_ldap_group_memberships(id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this LDAP Server.

    # example passing only required values which don't have defaults set
    try:
        api_instance.fix_ldap_group_memberships(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->fix_ldap_group_memberships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_client_sessions**
    def [ClientSession] get_all_client_sessions()



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.client_session import ClientSession
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    user = 1 # int | Filter the returned list by `user`. (optional)
    mounted_workspaces__mount_node = 1 # int | Filter the returned list by `mounted_workspaces__mount_node`. (optional)
    workstation = "workstation_example" # str | Filter the returned list by `workstation`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_client_sessions(user=user, mounted_workspaces__mount_node=mounted_workspaces__mount_node, workstation=workstation, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_client_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **mounted_workspaces__mount_node** | **int**| Filter the returned list by &#x60;mounted_workspaces__mount_node&#x60;. | [optional]
 **workstation** | **str**| Filter the returned list by &#x60;workstation&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[ClientSession]**](ClientSession.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_cloud_accounts**
    def [CloudAccount] get_all_cloud_accounts()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.cloud_account import CloudAccount
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    provider = "azure" # str | Filter the returned list by `provider`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_cloud_accounts(name=name, provider=provider, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_cloud_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **provider** | **str**| Filter the returned list by &#x60;provider&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[CloudAccount]**](CloudAccount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_download_archives**
    def [DownloadArchive] get_all_download_archives()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.download_archive import DownloadArchive
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_download_archives(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_download_archives: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[DownloadArchive]**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_downloads**
    def [Download] get_all_downloads()



### Required permissions    * User account permission: `downloads:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.download import Download
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_downloads(name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_downloads: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Download]**](Download.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_filesystem_permissions**
    def [FilesystemPermission] get_all_filesystem_permissions()



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.filesystem_permission import FilesystemPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    user = 1 # int | Filter the returned list by `user`. (optional)
    group = 1 # int | Filter the returned list by `group`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    for_user = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_filesystem_permissions(user=user, group=group, ordering=ordering, limit=limit, offset=offset, for_user=for_user)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_filesystem_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **group** | **int**| Filter the returned list by &#x60;group&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **for_user** | **int**|  | [optional]

### Return type

[**[FilesystemPermission]**](FilesystemPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_groups**
    def [ElementsGroup] get_all_groups()



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_group import ElementsGroup
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_groups(name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[ElementsGroup]**](ElementsGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_interfaces**
    def [Interface] get_all_interfaces()



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.interface import Interface
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    node_id = 1 # int | Filter the returned list by `node_id`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_interfaces(node_id=node_id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_interfaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**| Filter the returned list by &#x60;node_id&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Interface]**](Interface.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ldap_servers**
    def [LDAPServer] get_all_ldap_servers()



### Required permissions    * User account permission: `users:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ldap_server import LDAPServer
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ldap_servers(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_ldap_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[LDAPServer]**](LDAPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_notification_receipts**
    def [NotificationReceipt] get_all_notification_receipts()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_receipt import NotificationReceipt
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_notification_receipts(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_notification_receipts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[NotificationReceipt]**](NotificationReceipt.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_notification_settings**
    def [NotificationSetting] get_all_notification_settings()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_setting import NotificationSetting
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    topic = "topic_example" # str | Filter the returned list by `topic`. (optional)
    type = "type_example" # str | Filter the returned list by `type`. (optional)
    user = 1 # int | Filter the returned list by `user`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    system_defaults = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_notification_settings(topic=topic, type=type, user=user, ordering=ordering, limit=limit, offset=offset, system_defaults=system_defaults)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_notification_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**| Filter the returned list by &#x60;topic&#x60;. | [optional]
 **type** | **str**| Filter the returned list by &#x60;type&#x60;. | [optional]
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **system_defaults** | **bool**|  | [optional]

### Return type

[**[NotificationSetting]**](NotificationSetting.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_notifications**
    def [Notification] get_all_notifications()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification import Notification
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    cursor = "cursor_example" # str | The pagination cursor value. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_notifications(ordering=ordering, cursor=cursor)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]

### Return type

[**[Notification]**](Notification.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ntp_servers**
    def [NTPServer] get_all_ntp_servers()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ntp_server import NTPServer
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    address = "address_example" # str | Filter the returned list by `address`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ntp_servers(address=address, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_ntp_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Filter the returned list by &#x60;address&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[NTPServer]**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_storage_nodes**
    def [StorageNode] get_all_storage_nodes()



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.storage_node import StorageNode
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    type = "1" # str | Filter the returned list by `type`. (optional)
    backend = "elements" # str | Filter the returned list by `backend`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    address = "address_example" # str | Filter the returned list by `address`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    include_status = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_storage_nodes(type=type, backend=backend, name=name, address=address, ordering=ordering, limit=limit, offset=offset, include_status=include_status)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_storage_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter the returned list by &#x60;type&#x60;. | [optional]
 **backend** | **str**| Filter the returned list by &#x60;backend&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **address** | **str**| Filter the returned list by &#x60;address&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **include_status** | **bool**|  | [optional]

### Return type

[**[StorageNode]**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_users**
    def [ElementsUser] get_all_users()



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_user import ElementsUser
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    username = "username_example" # str | Filter the returned list by `username`. (optional)
    home = "home_example" # str | Filter the returned list by `home`. (optional)
    full_name = "full_name_example" # str | Filter the returned list by `full_name`. (optional)
    groups = "groups_example" # str | Filter the returned list by `groups`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    include_allowed_fs_paths = True # bool |  (optional)
    include_effective_permissions = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_users(username=username, home=home, full_name=full_name, groups=groups, ordering=ordering, limit=limit, offset=offset, include_allowed_fs_paths=include_allowed_fs_paths, include_effective_permissions=include_effective_permissions)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Filter the returned list by &#x60;username&#x60;. | [optional]
 **home** | **str**| Filter the returned list by &#x60;home&#x60;. | [optional]
 **full_name** | **str**| Filter the returned list by &#x60;full_name&#x60;. | [optional]
 **groups** | **str**| Filter the returned list by &#x60;groups&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **include_allowed_fs_paths** | **bool**|  | [optional]
 **include_effective_permissions** | **bool**|  | [optional]

### Return type

[**[ElementsUser]**](ElementsUser.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_workstations**
    def [Workstation] get_all_workstations()



### Required permissions    * Authenticated user   * Own workstation or <class 'elements.api.permissions.UserPermission.<locals>.Permission'> 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workstation import Workstation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    hostname = "hostname_example" # str | Filter the returned list by `hostname`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_workstations(hostname=hostname, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_all_workstations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| Filter the returned list by &#x60;hostname&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Workstation]**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_certificate_configuration**
    def Certificate get_certificate_configuration()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.certificate import Certificate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_certificate_configuration()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_certificate_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Certificate**](Certificate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_certificate_signing_request**
    def CSRFile get_certificate_signing_request()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.csr_file import CSRFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_certificate_signing_request()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_certificate_signing_request: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CSRFile**](CSRFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_client_download_file**
    def get_client_download_file(file)



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    file = "file_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_client_download_file(file)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_client_download_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_client_downloads**
    def [ClientsEndpointResponse] get_client_downloads()



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.clients_endpoint_response import ClientsEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_client_downloads()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_client_downloads: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ClientsEndpointResponse]**](ClientsEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_client_session**
    def ClientSession get_client_session(id)



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.client_session import ClientSession
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this client session.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_client_session(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_client_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this client session. |

### Return type

[**ClientSession**](ClientSession.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_cloud_account**
    def CloudAccount get_cloud_account(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.cloud_account import CloudAccount
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_account(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_cloud_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |

### Return type

[**CloudAccount**](CloudAccount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_cloud_account_costs**
    def GetCloudAccountCostsResponse get_cloud_account_costs(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.get_cloud_account_costs_response import GetCloudAccountCostsResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_account_costs(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_cloud_account_costs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |

### Return type

[**GetCloudAccountCostsResponse**](GetCloudAccountCostsResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_cloud_account_storage_roots**
    def [StorageRoot] get_cloud_account_storage_roots(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.storage_root import StorageRoot
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_account_storage_roots(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_cloud_account_storage_roots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |

### Return type

[**[StorageRoot]**](StorageRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_cloud_account_volume_sizes**
    def GetCloudAccountVolumeSizesResponse get_cloud_account_volume_sizes(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.get_cloud_account_volume_sizes_response import GetCloudAccountVolumeSizesResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_account_volume_sizes(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_cloud_account_volume_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |

### Return type

[**GetCloudAccountVolumeSizesResponse**](GetCloudAccountVolumeSizesResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_current_node**
    def StorageNode get_current_node()



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.storage_node import StorageNode
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    type = "1" # str | Filter the returned list by `type`. (optional)
    backend = "elements" # str | Filter the returned list by `backend`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    address = "address_example" # str | Filter the returned list by `address`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_current_node(type=type, backend=backend, name=name, address=address, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_current_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter the returned list by &#x60;type&#x60;. | [optional]
 **backend** | **str**| Filter the returned list by &#x60;backend&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **address** | **str**| Filter the returned list by &#x60;address&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**StorageNode**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_current_workstation**
    def Workstation get_current_workstation()



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workstation import Workstation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_current_workstation(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_current_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_download**
    def Download get_download(id)



### Required permissions    * User account permission: `downloads:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.download import Download
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this download.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_download(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this download. |

### Return type

[**Download**](Download.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_download_archive**
    def DownloadArchive get_download_archive(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.download_archive import DownloadArchive
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this download archive.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_download_archive(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_download_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this download archive. |

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_download_archive_file**
    def get_download_archive_file(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this download archive.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_download_archive_file(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_download_archive_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this download archive. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_download_file**
    def get_download_file(id)



### Required permissions    * User account permission: `downloads:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this download.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_download_file(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_download_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this download. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_download_icon**
    def get_download_icon(id)



### Required permissions    * User account permission: `downloads:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this download.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_download_icon(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_download_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this download. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_filesystem_permission**
    def FilesystemPermission get_filesystem_permission(id)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.filesystem_permission import FilesystemPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this filesystem permission.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_filesystem_permission(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_filesystem_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filesystem permission. |

### Return type

[**FilesystemPermission**](FilesystemPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_group**
    def ElementsGroupDetail get_group(id)



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_group_detail import ElementsGroupDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Group.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_group(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. |

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_home_workspace**
    def Workspace get_home_workspace(id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workspace import Workspace
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_home_workspace(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_home_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |

### Return type

[**Workspace**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_interface**
    def Interface get_interface(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.interface import Interface
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this interface.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_interface(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. |

### Return type

[**Interface**](Interface.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ipmi_configuration**
    def Ipmi get_ipmi_configuration(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ipmi import Ipmi
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ipmi_configuration(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_ipmi_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |

### Return type

[**Ipmi**](Ipmi.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ldap_server**
    def LDAPServerDetail get_ldap_server(id)



### Required permissions    * User account permission: `users:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ldap_server_detail import LDAPServerDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this LDAP Server.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ldap_server(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_ldap_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. |

### Return type

[**LDAPServerDetail**](LDAPServerDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ldap_server_groups**
    def LDAPServerGroups get_ldap_server_groups(id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ldap_server_groups import LDAPServerGroups
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this LDAP Server.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ldap_server_groups(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_ldap_server_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. |

### Return type

[**LDAPServerGroups**](LDAPServerGroups.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ldap_server_users**
    def LDAPServerUsers get_ldap_server_users(id)



### Required permissions    * User account permission: `users:manage`   * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ldap_server_users import LDAPServerUsers
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this LDAP Server.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ldap_server_users(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_ldap_server_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. |

### Return type

[**LDAPServerUsers**](LDAPServerUsers.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_license**
    def License get_license()



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.license import License
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_license()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_license: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**License**](License.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_license_components**
    def [LicenseComponentsEndpointResponse] get_license_components()



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.license_components_endpoint_response import LicenseComponentsEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_license_components()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_license_components: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[LicenseComponentsEndpointResponse]**](LicenseComponentsEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_log**
    def TaskLogV2 get_log(path)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.task_log_v2 import TaskLogV2
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    path = "path_example" # str | 
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_log(path)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_log(path, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **offset** | **int**|  | [optional]

### Return type

[**TaskLogV2**](TaskLogV2.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_my_avatar**
    def get_my_avatar()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_my_avatar(ordering=ordering, limit=limit, offset=offset)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_my_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_node_ipmi_sensors**
    def Sensors get_node_ipmi_sensors(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.sensors import Sensors
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_node_ipmi_sensors(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_node_ipmi_sensors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |

### Return type

[**Sensors**](Sensors.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_node_raid_status**
    def RAIDStatus get_node_raid_status(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.raid_status import RAIDStatus
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_node_raid_status(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_node_raid_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |

### Return type

[**RAIDStatus**](RAIDStatus.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_node_stats**
    def Stats get_node_stats(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.stats import Stats
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_node_stats(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_node_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |

### Return type

[**Stats**](Stats.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_node_time**
    def TimeResponse get_node_time(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.time_response import TimeResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_node_time(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_node_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |

### Return type

[**TimeResponse**](TimeResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_notification**
    def Notification get_notification(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification import Notification
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this Notification.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_notification(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Notification. |

### Return type

[**Notification**](Notification.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_notification_receipt**
    def NotificationReceipt get_notification_receipt(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_receipt import NotificationReceipt
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this notification receipt.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_notification_receipt(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_notification_receipt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification receipt. |

### Return type

[**NotificationReceipt**](NotificationReceipt.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_notification_setting**
    def NotificationSetting get_notification_setting(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_setting import NotificationSetting
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this notification setting.
    system_defaults = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_notification_setting(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_notification_setting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_notification_setting(id, system_defaults=system_defaults)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_notification_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification setting. |
 **system_defaults** | **bool**|  | [optional]

### Return type

[**NotificationSetting**](NotificationSetting.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ntp_server**
    def NTPServer get_ntp_server(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ntp_server import NTPServer
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this NTP Server.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ntp_server(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this NTP Server. |

### Return type

[**NTPServer**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_parameters**
    def Parameters get_parameters()



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.parameters import Parameters
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_parameters(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**Parameters**](Parameters.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_password_policy**
    def PasswordPolicy get_password_policy()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.password_policy import PasswordPolicy
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_password_policy()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_password_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_profile**
    def ElementsUserProfile get_profile()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_user_profile import ElementsUserProfile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_profile(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**ElementsUserProfile**](ElementsUserProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_release_notes**
    def [ReleaseNotesEndpointResponse] get_release_notes()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.release_notes_endpoint_response import ReleaseNotesEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_release_notes()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_release_notes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ReleaseNotesEndpointResponse]**](ReleaseNotesEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_service_status**
    def ServiceStatus get_service_status(id, service)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.service_status import ServiceStatus
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.
    service = "service_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_service_status(id, service)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_service_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |
 **service** | **str**|  |

### Return type

[**ServiceStatus**](ServiceStatus.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_smtp_configuration**
    def SMTPConfiguration get_smtp_configuration()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.smtp_configuration import SMTPConfiguration
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_smtp_configuration()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_smtp_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SMTPConfiguration**](SMTPConfiguration.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_stor_next_license**
    def StorNextLicenseEndpointResponse get_stor_next_license()



### Required permissions    * User account permission: `system:admin-access`   * License component: stornext_mdc 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.stor_next_license_endpoint_response import StorNextLicenseEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stor_next_license()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_stor_next_license: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**StorNextLicenseEndpointResponse**](StorNextLicenseEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_storage_node**
    def StorageNode get_storage_node(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.storage_node import StorageNode
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.
    include_status = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_storage_node(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_storage_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_storage_node(id, include_status=include_status)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_storage_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |
 **include_status** | **bool**|  | [optional]

### Return type

[**StorageNode**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_system_info**
    def SystemInfoEndpointResponse get_system_info()



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.system_info_endpoint_response import SystemInfoEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_system_info()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_system_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfoEndpointResponse**](SystemInfoEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_user**
    def ElementsUserDetail get_user(id)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_user_detail import ElementsUserDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.
    include_allowed_fs_paths = True # bool |  (optional)
    include_effective_permissions = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user(id, include_allowed_fs_paths=include_allowed_fs_paths, include_effective_permissions=include_effective_permissions)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |
 **include_allowed_fs_paths** | **bool**|  | [optional]
 **include_effective_permissions** | **bool**|  | [optional]

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_user_avatar**
    def get_user_avatar(id)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_user_avatar(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_user_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_workstation**
    def Workstation get_workstation(id)



### Required permissions    * Authenticated user   * Own workstation or <class 'elements.api.permissions.UserPermission.<locals>.Permission'> 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workstation import Workstation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A unique value identifying this workstation.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_workstation(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->get_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this workstation. |

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **install_stor_next_license**
    def StorNextLicenseEndpointResponse install_stor_next_license(stornext_license)



### Required permissions    * User account permission: `system:admin-access`   * License component: stornext_mdc 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.stor_next_license_endpoint_response import StorNextLicenseEndpointResponse
from elements_sdk.model.stornext_license import StornextLicense
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    stornext_license = StornextLicense(
        license="license_example",
    ) # StornextLicense | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.install_stor_next_license(stornext_license)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->install_stor_next_license: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stornext_license** | [**StornextLicense**](StornextLicense.md)|  |

### Return type

[**StorNextLicenseEndpointResponse**](StorNextLicenseEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_certificate_configuration**
    def Certificate patch_certificate_configuration(certificate_partial_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.certificate_partial_update import CertificatePartialUpdate
from elements_sdk.model.certificate import Certificate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    certificate_partial_update = CertificatePartialUpdate(
        certificate="certificate_example",
        key="key_example",
    ) # CertificatePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_certificate_configuration(certificate_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_certificate_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_partial_update** | [**CertificatePartialUpdate**](CertificatePartialUpdate.md)|  |

### Return type

[**Certificate**](Certificate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_cloud_account**
    def CloudAccount patch_cloud_account(id, cloud_account_partial_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.cloud_account import CloudAccount
from elements_sdk.model.cloud_account_partial_update import CloudAccountPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.
    cloud_account_partial_update = CloudAccountPartialUpdate(
        name="name_example",
        provider="azure",
        access_id="access_id_example",
        secret="secret_example",
        tenant="tenant_example",
        subscription="subscription_example",
        endpoint="endpoint_example",
        mount_credentials_management="share",
    ) # CloudAccountPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_cloud_account(id, cloud_account_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_cloud_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |
 **cloud_account_partial_update** | [**CloudAccountPartialUpdate**](CloudAccountPartialUpdate.md)|  |

### Return type

[**CloudAccount**](CloudAccount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_current_workstation**
    def Workstation patch_current_workstation(workstation_partial_update)



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workstation import Workstation
from elements_sdk.model.workstation_partial_update import WorkstationPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    workstation_partial_update = WorkstationPartialUpdate(
        report={
            "key": "key_example",
        },
        name="name_example",
        hostname="hostname_example",
        last_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # WorkstationPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_current_workstation(workstation_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_current_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstation_partial_update** | [**WorkstationPartialUpdate**](WorkstationPartialUpdate.md)|  |

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_download_archive**
    def DownloadArchive patch_download_archive(id, download_archive_partial_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.download_archive_partial_update import DownloadArchivePartialUpdate
from elements_sdk.model.download_archive import DownloadArchive
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this download archive.
    download_archive_partial_update = DownloadArchivePartialUpdate(
        task_info=TaskInfo(
            id="id_example",
            subtask=None,
            worker=None,
            user=None,
            workstation=None,
            progress=TaskProgress(
                message="message_example",
                current=1,
                max=3.14,
                bar=True,
            ),
            name="name_example",
            task_name="task_name_example",
            is_private=True,
            worker_name="worker_name_example",
            queue="queue_example",
            state=0,
            state_text="state_text_example",
            job_instance="job_instance_example",
            is_running=True,
            is_finished=True,
            exception="exception_example",
            traceback="traceback_example",
            related_bundle_id=-2147483648,
            related_proxy_id=-2147483648,
            schedule=1,
        ),
        name="name_example",
        path="path_example",
        progress_unit=0,
        user=1,
    ) # DownloadArchivePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_download_archive(id, download_archive_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_download_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this download archive. |
 **download_archive_partial_update** | [**DownloadArchivePartialUpdate**](DownloadArchivePartialUpdate.md)|  |

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_filesystem_permission**
    def FilesystemPermission patch_filesystem_permission(id, filesystem_permission_partial_update)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.filesystem_permission_partial_update import FilesystemPermissionPartialUpdate
from elements_sdk.model.filesystem_permission import FilesystemPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this filesystem permission.
    filesystem_permission_partial_update = FilesystemPermissionPartialUpdate(
        path="path_example",
        read_only=True,
        user=1,
        group=1,
    ) # FilesystemPermissionPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_filesystem_permission(id, filesystem_permission_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_filesystem_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filesystem permission. |
 **filesystem_permission_partial_update** | [**FilesystemPermissionPartialUpdate**](FilesystemPermissionPartialUpdate.md)|  |

### Return type

[**FilesystemPermission**](FilesystemPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_group**
    def ElementsGroupDetail patch_group(id, elements_group_detail_partial_update)



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_group_detail_partial_update import ElementsGroupDetailPartialUpdate
from elements_sdk.model.elements_group_detail import ElementsGroupDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Group.
    elements_group_detail_partial_update = ElementsGroupDetailPartialUpdate(
        permissions=[
            "permissions_example",
        ],
        members=[
            ElementsUserReference(
                id=1,
            ),
        ],
        ldap=None,
        name="name_example",
        ldap_dn="ldap_dn_example",
        ldap_guid="ldap_guid_example",
        unix_groupname="unix_groupname_example",
        gid=-2147483648,
    ) # ElementsGroupDetailPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_group(id, elements_group_detail_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. |
 **elements_group_detail_partial_update** | [**ElementsGroupDetailPartialUpdate**](ElementsGroupDetailPartialUpdate.md)|  |

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_interface**
    def Interface patch_interface(id, interface_partial_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.interface import Interface
from elements_sdk.model.interface_partial_update import InterfacePartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this interface.
    interface_partial_update = InterfacePartialUpdate(
        device="device_example",
        speed=-9223372036854775000,
        mac="mac_example",
        mtu=-2147483648,
        use_for_mounts=True,
        priority=-2147483648,
        port="port_example",
    ) # InterfacePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_interface(id, interface_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. |
 **interface_partial_update** | [**InterfacePartialUpdate**](InterfacePartialUpdate.md)|  |

### Return type

[**Interface**](Interface.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_ldap_server**
    def LDAPServerDetail patch_ldap_server(id, ldap_server_detail_partial_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ldap_server_detail import LDAPServerDetail
from elements_sdk.model.ldap_server_detail_partial_update import LDAPServerDetailPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this LDAP Server.
    ldap_server_detail_partial_update = LDAPServerDetailPartialUpdate(
        type=0,
        name="name_example",
        host="host_example",
        tls="ssl",
        username="username_example",
        password="password_example",
        domain="domain_example",
        search_filter="search_filter_example",
        group_search_filter="group_search_filter_example",
        nt_domain="nt_domain_example",
        nt_domain_mapping="nt_domain_mapping_example",
        root="root_example",
        users_root="users_root_example",
        groups_root="groups_root_example",
        use_wbinfo=True,
        username_format="sAMAccountName",
    ) # LDAPServerDetailPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_ldap_server(id, ldap_server_detail_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_ldap_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. |
 **ldap_server_detail_partial_update** | [**LDAPServerDetailPartialUpdate**](LDAPServerDetailPartialUpdate.md)|  |

### Return type

[**LDAPServerDetail**](LDAPServerDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_notification**
    def Notification patch_notification(id, notification_partial_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_partial_update import NotificationPartialUpdate
from elements_sdk.model.notification import Notification
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this Notification.
    notification_partial_update = NotificationPartialUpdate(
        receipts=[
            None,
        ],
        kwargs={
            "key": "key_example",
        },
    ) # NotificationPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_notification(id, notification_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Notification. |
 **notification_partial_update** | [**NotificationPartialUpdate**](NotificationPartialUpdate.md)|  |

### Return type

[**Notification**](Notification.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_notification_receipt**
    def NotificationReceipt patch_notification_receipt(id, notification_receipt_partial_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_receipt import NotificationReceipt
from elements_sdk.model.notification_receipt_partial_update import NotificationReceiptPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this notification receipt.
    notification_receipt_partial_update = NotificationReceiptPartialUpdate(
        user=None,
        notify_type="notify_type_example",
        failed=True,
        acknowledged=True,
        removed=True,
        notification="notification_example",
    ) # NotificationReceiptPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_notification_receipt(id, notification_receipt_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_notification_receipt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification receipt. |
 **notification_receipt_partial_update** | [**NotificationReceiptPartialUpdate**](NotificationReceiptPartialUpdate.md)|  |

### Return type

[**NotificationReceipt**](NotificationReceipt.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_notification_setting**
    def NotificationSetting patch_notification_setting(id, notification_setting_partial_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_setting_partial_update import NotificationSettingPartialUpdate
from elements_sdk.model.notification_setting import NotificationSetting
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this notification setting.
    notification_setting_partial_update = NotificationSettingPartialUpdate(
        topic="topic_example",
        type="type_example",
        user=1,
    ) # NotificationSettingPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_notification_setting(id, notification_setting_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_notification_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification setting. |
 **notification_setting_partial_update** | [**NotificationSettingPartialUpdate**](NotificationSettingPartialUpdate.md)|  |

### Return type

[**NotificationSetting**](NotificationSetting.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_ntp_server**
    def NTPServer patch_ntp_server(id, ntp_server_partial_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ntp_server_partial_update import NTPServerPartialUpdate
from elements_sdk.model.ntp_server import NTPServer
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this NTP Server.
    ntp_server_partial_update = NTPServerPartialUpdate(
        address="address_example",
        options="options_example",
    ) # NTPServerPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_ntp_server(id, ntp_server_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this NTP Server. |
 **ntp_server_partial_update** | [**NTPServerPartialUpdate**](NTPServerPartialUpdate.md)|  |

### Return type

[**NTPServer**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_profile**
    def ElementsUserProfile patch_profile(elements_user_profile_partial_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_user_profile_partial_update import ElementsUserProfilePartialUpdate
from elements_sdk.model.elements_user_profile import ElementsUserProfile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    elements_user_profile_partial_update = ElementsUserProfilePartialUpdate(
        avatar="avatar_example",
        default_page="default_page_example",
        full_name="full_name_example",
        language="en",
        fm_bookmarks=[
            "fm_bookmarks_example",
        ],
    ) # ElementsUserProfilePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_profile(elements_user_profile_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elements_user_profile_partial_update** | [**ElementsUserProfilePartialUpdate**](ElementsUserProfilePartialUpdate.md)|  |

### Return type

[**ElementsUserProfile**](ElementsUserProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_storage_node**
    def StorageNode patch_storage_node(id, storage_node_partial_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.storage_node_partial_update import StorageNodePartialUpdate
from elements_sdk.model.storage_node import StorageNode
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.
    storage_node_partial_update = StorageNodePartialUpdate(
        backend=Backend(
            name="name_example",
            properties=BackendProperties(
                supports_sharing_rw_permissions_priority=True,
                supports_sharing_afp=True,
                supports_sharing_smb_require_logon=True,
                supports_sharing_smb_recycle_bin=True,
                supports_sharing_smb_xattrs=True,
                supports_sharing_smb_symlinks=True,
                supports_sharing_smb_custom_options=True,
                supports_sharing_smb_allow_execute=True,
                supports_sharing_smb_locking_options=True,
                supports_sharing_smb_hidden=True,
                supports_sharing_veto=True,
                supports_sharing_nfs_permissions=True,
            ),
        ),
        task_queues=[
            "media",
        ],
        unique_id="unique_id_example",
        name="name_example",
        address="address_example",
        ipmi=1,
        ipmi_address="ipmi_address_example",
        ipmi_username="ipmi_username_example",
        ipmi_password="ipmi_password_example",
        proxy_queue=True,
        email_queue=True,
        apply_configuration_queue=True,
        solr_indexer_enabled=True,
        discovery_enabled=True,
        discovery_address_override="discovery_address_override_example",
        ntp_enabled=True,
        type=1,
        allow_root_login=True,
        permission_mask="permission_mask_example",
        address_override="address_override_example",
        auto_scan_interfaces=True,
        onefs_host="onefs_host_example",
        onefs_username="onefs_username_example",
        onefs_password="onefs_password_example",
        onefs_zone="onefs_zone_example",
        volume_queues=[
            1,
        ],
    ) # StorageNodePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_storage_node(id, storage_node_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_storage_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |
 **storage_node_partial_update** | [**StorageNodePartialUpdate**](StorageNodePartialUpdate.md)|  |

### Return type

[**StorageNode**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_user**
    def ElementsUserDetail patch_user(id, elements_user_detail_partial_update)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_user_detail import ElementsUserDetail
from elements_sdk.model.elements_user_detail_partial_update import ElementsUserDetailPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.
    elements_user_detail_partial_update = ElementsUserDetailPartialUpdate(
        allow_changing_password=True,
        allow_wan_login=True,
        avatar="avatar_example",
        default_page="default_page_example",
        email="email_example",
        expiry=dateutil_parser('1970-01-01T00:00:00.00Z'),
        fm_bookmarks=[
            "fm_bookmarks_example",
        ],
        full_name="full_name_example",
        gid=-2147483648,
        home=1,
        is_external=True,
        is_cloud=True,
        is_enabled=True,
        language="en",
        ldap=None,
        ldap_dn="ldap_dn_example",
        password_change_required=True,
        permissions=[
            "permissions_example",
        ],
        shaper_ceiling=0,
        shaper_rate=0,
        uid=-2147483648,
        unix_username="unix_username_example",
        username="username_example",
        groups=[
            1,
        ],
    ) # ElementsUserDetailPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_user(id, elements_user_detail_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |
 **elements_user_detail_partial_update** | [**ElementsUserDetailPartialUpdate**](ElementsUserDetailPartialUpdate.md)|  |

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_workstation**
    def Workstation patch_workstation(id, workstation_partial_update)



### Required permissions    * Authenticated user   * Own workstation or <class 'elements.api.permissions.UserPermission.<locals>.Permission'> 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workstation import Workstation
from elements_sdk.model.workstation_partial_update import WorkstationPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A unique value identifying this workstation.
    workstation_partial_update = WorkstationPartialUpdate(
        report={
            "key": "key_example",
        },
        name="name_example",
        hostname="hostname_example",
        last_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # WorkstationPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_workstation(id, workstation_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->patch_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this workstation. |
 **workstation_partial_update** | [**WorkstationPartialUpdate**](WorkstationPartialUpdate.md)|  |

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **probe_ldap_config**
    def LDAPProbeResponse probe_ldap_config(ldap_probe_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ldap_probe_response import LDAPProbeResponse
from elements_sdk.model.ldap_probe_request import LDAPProbeRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    ldap_probe_request = LDAPProbeRequest(
        host="host_example",
        username="username_example",
        password="password_example",
    ) # LDAPProbeRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.probe_ldap_config(ldap_probe_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->probe_ldap_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_probe_request** | [**LDAPProbeRequest**](LDAPProbeRequest.md)|  |

### Return type

[**LDAPProbeResponse**](LDAPProbeResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **reboot**
    def reboot()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.reboot()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->reboot: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **register_upload**
    def register_upload(register_upload_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.register_upload_endpoint_request import RegisterUploadEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    register_upload_endpoint_request = RegisterUploadEndpointRequest(
        upload_id="upload_id_example",
        path="path_example",
    ) # RegisterUploadEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.register_upload(register_upload_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->register_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_upload_endpoint_request** | [**RegisterUploadEndpointRequest**](RegisterUploadEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **register_upload_metadata**
    def register_upload_metadata(register_upload_metadata_endpoint_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.register_upload_metadata_endpoint_request import RegisterUploadMetadataEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    register_upload_metadata_endpoint_request = RegisterUploadMetadataEndpointRequest(
        items=[
            MetadataItem(
                custom_fields={
                    "key": "key_example",
                },
                tags=[
                    {
                        "key": "key_example",
                    },
                ],
                path="path_example",
            ),
        ],
    ) # RegisterUploadMetadataEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.register_upload_metadata(register_upload_metadata_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->register_upload_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_upload_metadata_endpoint_request** | [**RegisterUploadMetadataEndpointRequest**](RegisterUploadMetadataEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **render_email_template_preview**
    def EmailPreviewResponse render_email_template_preview(email_preview_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.email_preview_response import EmailPreviewResponse
from elements_sdk.model.email_preview_request import EmailPreviewRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    email_preview_request = EmailPreviewRequest(
        styling=EmailStyling(
            background="background_example",
            backdrop="backdrop_example",
            primary="primary_example",
        ),
        logo_url="logo_url_example",
    ) # EmailPreviewRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.render_email_template_preview(email_preview_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->render_email_template_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_preview_request** | [**EmailPreviewRequest**](EmailPreviewRequest.md)|  |

### Return type

[**EmailPreviewResponse**](EmailPreviewResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **rescan_interfaces**
    def rescan_interfaces(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.

    # example passing only required values which don't have defaults set
    try:
        api_instance.rescan_interfaces(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->rescan_interfaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **reset_user_password**
    def reset_user_password(id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.

    # example passing only required values which don't have defaults set
    try:
        api_instance.reset_user_password(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->reset_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **restart_web_ui**
    def restart_web_ui()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.restart_web_ui()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->restart_web_ui: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **run_service_operation**
    def run_service_operation(id, service, operation)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.
    service = "service_example" # str | 
    operation = "operation_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.run_service_operation(id, service, operation)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->run_service_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |
 **service** | **str**|  |
 **operation** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **set_ipmi_configuration**
    def Ipmi set_ipmi_configuration(id, ipmi)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ipmi import Ipmi
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.
    ipmi = Ipmi(
        ip="ip_example",
        netmask="netmask_example",
        gateway="gateway_example",
    ) # Ipmi | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_ipmi_configuration(id, ipmi)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->set_ipmi_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |
 **ipmi** | [**Ipmi**](Ipmi.md)|  |

### Return type

[**Ipmi**](Ipmi.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **set_my_password**
    def set_my_password(change_own_password_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.change_own_password_request import ChangeOwnPasswordRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    change_own_password_request = ChangeOwnPasswordRequest(
        password="password_example",
        current_password="current_password_example",
        current_otp="current_otp_example",
    ) # ChangeOwnPasswordRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_my_password(change_own_password_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->set_my_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_own_password_request** | [**ChangeOwnPasswordRequest**](ChangeOwnPasswordRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **set_node_time**
    def TimeResponse set_node_time(id, set_time_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.time_response import TimeResponse
from elements_sdk.model.set_time_request import SetTimeRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.
    set_time_request = SetTimeRequest(
        timezone=Timezone(
            value="value_example",
        ),
        local_hours=1,
        local_minutes=1,
        local_seconds=1,
        local_day=1,
        local_month=1,
        local_year=1,
    ) # SetTimeRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_node_time(id, set_time_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->set_node_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |
 **set_time_request** | [**SetTimeRequest**](SetTimeRequest.md)|  |

### Return type

[**TimeResponse**](TimeResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **set_user_password**
    def set_user_password(id, change_password_request)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.change_password_request import ChangePasswordRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.
    change_password_request = ChangePasswordRequest(
        password="password_example",
    ) # ChangePasswordRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_user_password(id, change_password_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->set_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **shutdown**
    def shutdown()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.shutdown()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->shutdown: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **silence_node_raid_alarm**
    def silence_node_raid_alarm(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.

    # example passing only required values which don't have defaults set
    try:
        api_instance.silence_node_raid_alarm(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->silence_node_raid_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_solr_reindex**
    def SolrReindexEndpointResponse start_solr_reindex()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.solr_reindex_endpoint_response import SolrReindexEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.start_solr_reindex()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->start_solr_reindex: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SolrReindexEndpointResponse**](SolrReindexEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_support_session**
    def TaskInfo start_support_session()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.task_info import TaskInfo
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.start_support_session()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->start_support_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_system_backup**
    def TaskInfo start_system_backup(path)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.path import Path
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    path = Path(
        path="path_example",
    ) # Path | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.start_system_backup(path)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->start_system_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**Path**](Path.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sync_ldap_group**
    def sync_ldap_group(id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Group.

    # example passing only required values which don't have defaults set
    try:
        api_instance.sync_ldap_group(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->sync_ldap_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sync_ldap_users**
    def sync_ldap_users(id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this LDAP Server.

    # example passing only required values which don't have defaults set
    try:
        api_instance.sync_ldap_users(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->sync_ldap_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sync_time**
    def sync_time()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.sync_time()
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->sync_time: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sync_user_totp**
    def SyncTOTP sync_user_totp(id, sync_totp_request)



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.sync_totp import SyncTOTP
from elements_sdk.model.sync_totp_request import SyncTOTPRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.
    sync_totp_request = SyncTOTPRequest(
        otp="otp_example",
    ) # SyncTOTPRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sync_user_totp(id, sync_totp_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->sync_user_totp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |
 **sync_totp_request** | [**SyncTOTPRequest**](SyncTOTPRequest.md)|  |

### Return type

[**SyncTOTP**](SyncTOTP.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **test_cloud_account_credentials**
    def TestCloudAccountCredentialsResponse test_cloud_account_credentials(test_cloud_account_credentials_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.test_cloud_account_credentials_response import TestCloudAccountCredentialsResponse
from elements_sdk.model.test_cloud_account_credentials_request import TestCloudAccountCredentialsRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    test_cloud_account_credentials_request = TestCloudAccountCredentialsRequest(
        name="name_example",
        provider="azure",
        access_id="access_id_example",
        secret="secret_example",
        tenant="tenant_example",
        subscription="subscription_example",
        endpoint="endpoint_example",
        mount_credentials_management="share",
    ) # TestCloudAccountCredentialsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.test_cloud_account_credentials(test_cloud_account_credentials_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->test_cloud_account_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_cloud_account_credentials_request** | [**TestCloudAccountCredentialsRequest**](TestCloudAccountCredentialsRequest.md)|  |

### Return type

[**TestCloudAccountCredentialsResponse**](TestCloudAccountCredentialsResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **test_smtp_configuration**
    def test_smtp_configuration(test_smtp)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.test_smtp import TestSMTP
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    test_smtp = TestSMTP(
        email="email_example",
    ) # TestSMTP | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.test_smtp_configuration(test_smtp)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->test_smtp_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_smtp** | [**TestSMTP**](TestSMTP.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_certificate_configuration**
    def Certificate update_certificate_configuration(check_certificate_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.check_certificate_request import CheckCertificateRequest
from elements_sdk.model.certificate import Certificate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    check_certificate_request = CheckCertificateRequest(
        certificate="certificate_example",
        key="key_example",
    ) # CheckCertificateRequest | 
    force = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_certificate_configuration(check_certificate_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_certificate_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_certificate_configuration(check_certificate_request, force=force)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_certificate_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_certificate_request** | [**CheckCertificateRequest**](CheckCertificateRequest.md)|  |
 **force** | **bool**|  | [optional]

### Return type

[**Certificate**](Certificate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_cloud_account**
    def CloudAccount update_cloud_account(id, cloud_account_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.cloud_account_update import CloudAccountUpdate
from elements_sdk.model.cloud_account import CloudAccount
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.
    cloud_account_update = CloudAccountUpdate(
        name="name_example",
        provider="azure",
        access_id="access_id_example",
        secret="secret_example",
        tenant="tenant_example",
        subscription="subscription_example",
        endpoint="endpoint_example",
        mount_credentials_management="share",
    ) # CloudAccountUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_cloud_account(id, cloud_account_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_cloud_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |
 **cloud_account_update** | [**CloudAccountUpdate**](CloudAccountUpdate.md)|  |

### Return type

[**CloudAccount**](CloudAccount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_current_workstation**
    def Workstation update_current_workstation(workstation_update)



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workstation_update import WorkstationUpdate
from elements_sdk.model.workstation import Workstation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    workstation_update = WorkstationUpdate(
        report={
            "key": "key_example",
        },
        name="name_example",
        hostname="hostname_example",
        last_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # WorkstationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_current_workstation(workstation_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_current_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstation_update** | [**WorkstationUpdate**](WorkstationUpdate.md)|  |

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_download_archive**
    def DownloadArchive update_download_archive(id, download_archive_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.download_archive_update import DownloadArchiveUpdate
from elements_sdk.model.download_archive import DownloadArchive
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this download archive.
    download_archive_update = DownloadArchiveUpdate(
        task_info=TaskInfo(
            id="id_example",
            subtask=None,
            worker=None,
            user=None,
            workstation=None,
            progress=TaskProgress(
                message="message_example",
                current=1,
                max=3.14,
                bar=True,
            ),
            name="name_example",
            task_name="task_name_example",
            is_private=True,
            worker_name="worker_name_example",
            queue="queue_example",
            state=0,
            state_text="state_text_example",
            job_instance="job_instance_example",
            is_running=True,
            is_finished=True,
            exception="exception_example",
            traceback="traceback_example",
            related_bundle_id=-2147483648,
            related_proxy_id=-2147483648,
            schedule=1,
        ),
        name="name_example",
        path="path_example",
        progress_unit=0,
        user=1,
    ) # DownloadArchiveUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_download_archive(id, download_archive_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_download_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this download archive. |
 **download_archive_update** | [**DownloadArchiveUpdate**](DownloadArchiveUpdate.md)|  |

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_filesystem_permission**
    def FilesystemPermission update_filesystem_permission(id, filesystem_permission_update)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.filesystem_permission_update import FilesystemPermissionUpdate
from elements_sdk.model.filesystem_permission import FilesystemPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this filesystem permission.
    filesystem_permission_update = FilesystemPermissionUpdate(
        path="path_example",
        read_only=True,
        user=1,
        group=1,
    ) # FilesystemPermissionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_filesystem_permission(id, filesystem_permission_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_filesystem_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filesystem permission. |
 **filesystem_permission_update** | [**FilesystemPermissionUpdate**](FilesystemPermissionUpdate.md)|  |

### Return type

[**FilesystemPermission**](FilesystemPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_group**
    def ElementsGroupDetail update_group(id, elements_group_detail_update)



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_group_detail_update import ElementsGroupDetailUpdate
from elements_sdk.model.elements_group_detail import ElementsGroupDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Group.
    elements_group_detail_update = ElementsGroupDetailUpdate(
        permissions=[
            "permissions_example",
        ],
        members=[
            ElementsUserReference(
                id=1,
            ),
        ],
        ldap=None,
        name="name_example",
        ldap_dn="ldap_dn_example",
        ldap_guid="ldap_guid_example",
        unix_groupname="unix_groupname_example",
        gid=-2147483648,
    ) # ElementsGroupDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_group(id, elements_group_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. |
 **elements_group_detail_update** | [**ElementsGroupDetailUpdate**](ElementsGroupDetailUpdate.md)|  |

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_interface**
    def Interface update_interface(id, interface_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.interface import Interface
from elements_sdk.model.interface_update import InterfaceUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this interface.
    interface_update = InterfaceUpdate(
        device="device_example",
        speed=-9223372036854775000,
        mac="mac_example",
        mtu=-2147483648,
        use_for_mounts=True,
        priority=-2147483648,
        port="port_example",
    ) # InterfaceUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_interface(id, interface_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. |
 **interface_update** | [**InterfaceUpdate**](InterfaceUpdate.md)|  |

### Return type

[**Interface**](Interface.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_ldap_server**
    def LDAPServerDetail update_ldap_server(id, ldap_server_detail_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ldap_server_detail_update import LDAPServerDetailUpdate
from elements_sdk.model.ldap_server_detail import LDAPServerDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this LDAP Server.
    ldap_server_detail_update = LDAPServerDetailUpdate(
        type=0,
        name="name_example",
        host="host_example",
        tls="ssl",
        username="username_example",
        password="password_example",
        domain="domain_example",
        search_filter="search_filter_example",
        group_search_filter="group_search_filter_example",
        nt_domain="nt_domain_example",
        nt_domain_mapping="nt_domain_mapping_example",
        root="root_example",
        users_root="users_root_example",
        groups_root="groups_root_example",
        use_wbinfo=True,
        username_format="sAMAccountName",
    ) # LDAPServerDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_ldap_server(id, ldap_server_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_ldap_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. |
 **ldap_server_detail_update** | [**LDAPServerDetailUpdate**](LDAPServerDetailUpdate.md)|  |

### Return type

[**LDAPServerDetail**](LDAPServerDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_my_avatar**
    def update_my_avatar(image_upload_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.image_upload_request import ImageUploadRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    image_upload_request = ImageUploadRequest(
        data="data_example",
    ) # ImageUploadRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_my_avatar(image_upload_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_my_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_upload_request** | [**ImageUploadRequest**](ImageUploadRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_notification**
    def Notification update_notification(id, notification_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_update import NotificationUpdate
from elements_sdk.model.notification import Notification
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A UUID string identifying this Notification.
    notification_update = NotificationUpdate(
        receipts=[
            None,
        ],
        kwargs={
            "key": "key_example",
        },
    ) # NotificationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_notification(id, notification_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Notification. |
 **notification_update** | [**NotificationUpdate**](NotificationUpdate.md)|  |

### Return type

[**Notification**](Notification.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_notification_receipt**
    def NotificationReceipt update_notification_receipt(id, notification_receipt_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_receipt_update import NotificationReceiptUpdate
from elements_sdk.model.notification_receipt import NotificationReceipt
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this notification receipt.
    notification_receipt_update = NotificationReceiptUpdate(
        user=None,
        notify_type="notify_type_example",
        failed=True,
        acknowledged=True,
        removed=True,
        notification="notification_example",
    ) # NotificationReceiptUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_notification_receipt(id, notification_receipt_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_notification_receipt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification receipt. |
 **notification_receipt_update** | [**NotificationReceiptUpdate**](NotificationReceiptUpdate.md)|  |

### Return type

[**NotificationReceipt**](NotificationReceipt.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_notification_setting**
    def NotificationSetting update_notification_setting(id, notification_setting_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.notification_setting_update import NotificationSettingUpdate
from elements_sdk.model.notification_setting import NotificationSetting
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this notification setting.
    notification_setting_update = NotificationSettingUpdate(
        topic="topic_example",
        type="type_example",
        user=1,
    ) # NotificationSettingUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_notification_setting(id, notification_setting_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_notification_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification setting. |
 **notification_setting_update** | [**NotificationSettingUpdate**](NotificationSettingUpdate.md)|  |

### Return type

[**NotificationSetting**](NotificationSetting.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_ntp_server**
    def NTPServer update_ntp_server(id, ntp_server_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.ntp_server_update import NTPServerUpdate
from elements_sdk.model.ntp_server import NTPServer
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this NTP Server.
    ntp_server_update = NTPServerUpdate(
        address="address_example",
        options="options_example",
    ) # NTPServerUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_ntp_server(id, ntp_server_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this NTP Server. |
 **ntp_server_update** | [**NTPServerUpdate**](NTPServerUpdate.md)|  |

### Return type

[**NTPServer**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_parameters**
    def Parameters update_parameters(parameters_update)



### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.parameters import Parameters
from elements_sdk.model.parameters_update import ParametersUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    parameters_update = ParametersUpdate(
        analytics=True,
        branding_css="branding_css_example",
        branding_logo="branding_logo_example",
        email_logo_url="email_logo_url_example",
        client_offer_file_search=True,
        external_url="external_url_example",
        file_manager_recycle_bin=True,
        https_redirect="domain",
        language="en",
        ltfs_default_restore_to_original_location=True,
        ltfs_default_search_directories=True,
        ltfs_library_address="ltfs_library_address_example",
        mail_styling=EmailStyling(
            background="background_example",
            backdrop="backdrop_example",
            primary="primary_example",
        ),
        media_allow_anonymous_links=True,
        media_allow_changing_archived=True,
        media_auto_play=True,
        media_auto_proxy=True,
        media_auto_scan=True,
        media_auto_transport=True,
        media_background_auto_pause=True,
        media_default_custom_field_type="file",
        media_default_delete_behaviour="disk",
        media_detect_versions=True,
        media_force_show_deleted=True,
        media_keep_selection_when_browsing=True,
        media_recycle_bin=True,
        media_require_link_password=True,
        media_max_link_views=-2147483648,
        media_shuttle_left_behaviour="slowdown",
        ntp_enable=True,
        ntp_offer_sync=True,
        otp_policy="admin-only",
        password_login=True,
        session_key_restrict_to_ip=True,
        tasks_run_scheduled=True,
        update_in_progress=True,
        users_default_permissions="users_default_permissions_example",
        user_notification_settings=True,
        workspaces_path="workspaces_path_example",
    ) # ParametersUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_parameters(parameters_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters_update** | [**ParametersUpdate**](ParametersUpdate.md)|  |

### Return type

[**Parameters**](Parameters.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_password_policy**
    def PasswordPolicy update_password_policy(password_policy_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.password_policy import PasswordPolicy
from elements_sdk.model.password_policy_update import PasswordPolicyUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    password_policy_update = PasswordPolicyUpdate(
        rules=[
            PasswordPolicyRule(
                group_name="group_name_example",
                group_regex="group_regex_example",
                min_count=1,
            ),
        ],
        min_length=1,
        min_entropy_bits=1,
        regex="regex_example",
        no_pwned=True,
    ) # PasswordPolicyUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_password_policy(password_policy_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_password_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_policy_update** | [**PasswordPolicyUpdate**](PasswordPolicyUpdate.md)|  |

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_profile**
    def ElementsUserProfile update_profile(elements_user_profile_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_user_profile_update import ElementsUserProfileUpdate
from elements_sdk.model.elements_user_profile import ElementsUserProfile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    elements_user_profile_update = ElementsUserProfileUpdate(
        avatar="avatar_example",
        default_page="default_page_example",
        full_name="full_name_example",
        language="en",
        fm_bookmarks=[
            "fm_bookmarks_example",
        ],
    ) # ElementsUserProfileUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_profile(elements_user_profile_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elements_user_profile_update** | [**ElementsUserProfileUpdate**](ElementsUserProfileUpdate.md)|  |

### Return type

[**ElementsUserProfile**](ElementsUserProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_smtp_configuration**
    def SMTPConfiguration update_smtp_configuration(smtp_configuration_update)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.smtp_configuration import SMTPConfiguration
from elements_sdk.model.smtp_configuration_update import SMTPConfigurationUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    smtp_configuration_update = SMTPConfigurationUpdate(
        from_address="from_address_example",
        server="server_example",
        port=1,
        tls="tls_example",
        username="username_example",
        password="password_example",
    ) # SMTPConfigurationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_smtp_configuration(smtp_configuration_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_smtp_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smtp_configuration_update** | [**SMTPConfigurationUpdate**](SMTPConfigurationUpdate.md)|  |

### Return type

[**SMTPConfiguration**](SMTPConfiguration.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_storage_node**
    def StorageNode update_storage_node(id, storage_node_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.storage_node_update import StorageNodeUpdate
from elements_sdk.model.storage_node import StorageNode
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this Storage Node.
    storage_node_update = StorageNodeUpdate(
        backend=Backend(
            name="name_example",
            properties=BackendProperties(
                supports_sharing_rw_permissions_priority=True,
                supports_sharing_afp=True,
                supports_sharing_smb_require_logon=True,
                supports_sharing_smb_recycle_bin=True,
                supports_sharing_smb_xattrs=True,
                supports_sharing_smb_symlinks=True,
                supports_sharing_smb_custom_options=True,
                supports_sharing_smb_allow_execute=True,
                supports_sharing_smb_locking_options=True,
                supports_sharing_smb_hidden=True,
                supports_sharing_veto=True,
                supports_sharing_nfs_permissions=True,
            ),
        ),
        task_queues=[
            "media",
        ],
        unique_id="unique_id_example",
        name="name_example",
        address="address_example",
        ipmi=1,
        ipmi_address="ipmi_address_example",
        ipmi_username="ipmi_username_example",
        ipmi_password="ipmi_password_example",
        proxy_queue=True,
        email_queue=True,
        apply_configuration_queue=True,
        solr_indexer_enabled=True,
        discovery_enabled=True,
        discovery_address_override="discovery_address_override_example",
        ntp_enabled=True,
        type=1,
        allow_root_login=True,
        permission_mask="permission_mask_example",
        address_override="address_override_example",
        auto_scan_interfaces=True,
        onefs_host="onefs_host_example",
        onefs_username="onefs_username_example",
        onefs_password="onefs_password_example",
        onefs_zone="onefs_zone_example",
        volume_queues=[
            1,
        ],
    ) # StorageNodeUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_storage_node(id, storage_node_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_storage_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. |
 **storage_node_update** | [**StorageNodeUpdate**](StorageNodeUpdate.md)|  |

### Return type

[**StorageNode**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_user**
    def ElementsUserDetail update_user(id, elements_user_detail_update)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.elements_user_detail import ElementsUserDetail
from elements_sdk.model.elements_user_detail_update import ElementsUserDetailUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.
    elements_user_detail_update = ElementsUserDetailUpdate(
        allow_changing_password=True,
        allow_wan_login=True,
        avatar="avatar_example",
        default_page="default_page_example",
        email="email_example",
        expiry=dateutil_parser('1970-01-01T00:00:00.00Z'),
        fm_bookmarks=[
            "fm_bookmarks_example",
        ],
        full_name="full_name_example",
        gid=-2147483648,
        home=1,
        is_external=True,
        is_cloud=True,
        is_enabled=True,
        language="en",
        ldap=None,
        ldap_dn="ldap_dn_example",
        password_change_required=True,
        permissions=[
            "permissions_example",
        ],
        shaper_ceiling=0,
        shaper_rate=0,
        uid=-2147483648,
        unix_username="unix_username_example",
        username="username_example",
        groups=[
            1,
        ],
    ) # ElementsUserDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_user(id, elements_user_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |
 **elements_user_detail_update** | [**ElementsUserDetailUpdate**](ElementsUserDetailUpdate.md)|  |

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_user_avatar**
    def update_user_avatar(id, image_upload_request)



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.image_upload_request import ImageUploadRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = 1 # int | A unique integer value identifying this User.
    image_upload_request = ImageUploadRequest(
        data="data_example",
    ) # ImageUploadRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_user_avatar(id, image_upload_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_user_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. |
 **image_upload_request** | [**ImageUploadRequest**](ImageUploadRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_workstation**
    def Workstation update_workstation(id, workstation_update)



### Required permissions    * Authenticated user   * Own workstation or <class 'elements.api.permissions.UserPermission.<locals>.Permission'> 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.workstation_update import WorkstationUpdate
from elements_sdk.model.workstation import Workstation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    id = "id_example" # str | A unique value identifying this workstation.
    workstation_update = WorkstationUpdate(
        report={
            "key": "key_example",
        },
        name="name_example",
        hostname="hostname_example",
        last_seen=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # WorkstationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_workstation(id, workstation_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->update_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this workstation. |
 **workstation_update** | [**WorkstationUpdate**](WorkstationUpdate.md)|  |

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **upload_chunk**
    def upload_chunk(upload_chunk_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import main_api
from elements_sdk.model.upload_chunk_endpoint_request import UploadChunkEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = main_api.MainApi(api_client)
    upload_chunk_endpoint_request = UploadChunkEndpointRequest(
        upload_id="upload_id_example",
        chunk_number=1,
        total_chunks=1,
    ) # UploadChunkEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.upload_chunk(upload_chunk_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MainApi->upload_chunk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_chunk_endpoint_request** | [**UploadChunkEndpointRequest**](UploadChunkEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

