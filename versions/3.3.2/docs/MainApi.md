# elements_sdk.MainApi

All URIs are relative to *http://localhost*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_configuration**](MainApi.md#apply_configuration) | **POST** `/api/2/configuration/apply` | 
[**beep**](MainApi.md#beep) | **POST** `/api/2/system/beep` | 
[**check_chunk_uploaded**](MainApi.md#check_chunk_uploaded) | **GET** `/api/2/uploads/chunk` | 
[**check_internet_connectivity**](MainApi.md#check_internet_connectivity) | **POST** `/api/2/system/check-connectivity` | 
[**check_stor_next_license**](MainApi.md#check_stor_next_license) | **POST** `/api/2/stornext-license/check` | 
[**collect_diagnostics**](MainApi.md#collect_diagnostics) | **POST** `/api/2/system/collect-diagnostics` | 
[**create_archive**](MainApi.md#create_archive) | **POST** `/api/2/download-archive/create` | 
[**create_group**](MainApi.md#create_group) | **POST** `/api/2/groups` | 
[**create_home_workspace**](MainApi.md#create_home_workspace) | **POST** `/api/2/users/{id}/home` | 
[**create_ntp_server**](MainApi.md#create_ntp_server) | **POST** `/api/2/system/time/servers` | 
[**create_user**](MainApi.md#create_user) | **POST** `/api/2/users` | 
[**create_workstation**](MainApi.md#create_workstation) | **POST** `/api/2/workstations` | 
[**delete_download_archive**](MainApi.md#delete_download_archive) | **DELETE** `/api/2/download-archive/{id}` | 
[**delete_group**](MainApi.md#delete_group) | **DELETE** `/api/2/groups/{id}` | 
[**delete_home_workspace**](MainApi.md#delete_home_workspace) | **DELETE** `/api/2/users/{id}/home` | 
[**delete_ntp_server**](MainApi.md#delete_ntp_server) | **DELETE** `/api/2/system/time/servers/{id}` | 
[**delete_user**](MainApi.md#delete_user) | **DELETE** `/api/2/users/{id}` | 
[**delete_workstation**](MainApi.md#delete_workstation) | **DELETE** `/api/2/workstations/{id}` | 
[**disable_user_totp**](MainApi.md#disable_user_totp) | **DELETE** `/api/2/users/{id}/totp` | 
[**enable_user_totp**](MainApi.md#enable_user_totp) | **POST** `/api/2/users/{id}/totp` | 
[**finish_upload**](MainApi.md#finish_upload) | **POST** `/api/2/uploads/finish` | 
[**fix_ldap_group_memberships**](MainApi.md#fix_ldap_group_memberships) | **POST** `/api/2/ldap-servers/{id}/fix-memberships` | 
[**get_all_download_archives**](MainApi.md#get_all_download_archives) | **GET** `/api/2/download-archive` | 
[**get_all_downloads**](MainApi.md#get_all_downloads) | **GET** `/api/2/downloads` | 
[**get_all_groups**](MainApi.md#get_all_groups) | **GET** `/api/2/groups` | 
[**get_all_ldap_servers**](MainApi.md#get_all_ldap_servers) | **GET** `/api/2/ldap-servers` | 
[**get_all_ntp_servers**](MainApi.md#get_all_ntp_servers) | **GET** `/api/2/system/time/servers` | 
[**get_all_storage_nodes**](MainApi.md#get_all_storage_nodes) | **GET** `/api/2/nodes` | 
[**get_all_users**](MainApi.md#get_all_users) | **GET** `/api/2/users` | 
[**get_all_workstations**](MainApi.md#get_all_workstations) | **GET** `/api/2/workstations` | 
[**get_client_download_file**](MainApi.md#get_client_download_file) | **GET** `/api/2/downloads/clients/{file}` | 
[**get_client_downloads**](MainApi.md#get_client_downloads) | **GET** `/api/2/downloads/clients` | 
[**get_current_workstation**](MainApi.md#get_current_workstation) | **GET** `/api/2/workstations/current` | 
[**get_download**](MainApi.md#get_download) | **GET** `/api/2/downloads/{id}` | 
[**get_download_archive**](MainApi.md#get_download_archive) | **GET** `/api/2/download-archive/{id}` | 
[**get_download_archive_file**](MainApi.md#get_download_archive_file) | **GET** `/api/2/download-archive/{id}/download` | 
[**get_download_file**](MainApi.md#get_download_file) | **GET** `/api/2/downloads/{id}/download` | 
[**get_download_icon**](MainApi.md#get_download_icon) | **GET** `/api/2/downloads/{id}/icon` | 
[**get_group**](MainApi.md#get_group) | **GET** `/api/2/groups/{id}` | 
[**get_home_workspace**](MainApi.md#get_home_workspace) | **GET** `/api/2/users/{id}/home` | 
[**get_ipmi_configuration**](MainApi.md#get_ipmi_configuration) | **GET** `/api/2/nodes/{id}/ipmi` | 
[**get_ldap_server**](MainApi.md#get_ldap_server) | **GET** `/api/2/ldap-servers/{id}` | 
[**get_ldap_server_groups**](MainApi.md#get_ldap_server_groups) | **GET** `/api/2/ldap-servers/{id}/groups` | 
[**get_ldap_server_users**](MainApi.md#get_ldap_server_users) | **GET** `/api/2/ldap-servers/{id}/users` | 
[**get_license**](MainApi.md#get_license) | **GET** `/api/2/license` | 
[**get_local_time**](MainApi.md#get_local_time) | **GET** `/api/2/system/time` | 
[**get_log**](MainApi.md#get_log) | **GET** `/api/2/system/log/{path}` | 
[**get_node_ipmi_sensors**](MainApi.md#get_node_ipmi_sensors) | **GET** `/api/2/nodes/{id}/sensors` | 
[**get_node_stats**](MainApi.md#get_node_stats) | **GET** `/api/2/nodes/{id}/stats` | 
[**get_ntp_server**](MainApi.md#get_ntp_server) | **GET** `/api/2/system/time/servers/{id}` | 
[**get_parameters**](MainApi.md#get_parameters) | **GET** `/api/2/parameters` | 
[**get_profile**](MainApi.md#get_profile) | **GET** `/api/2/users/me` | 
[**get_release_notes**](MainApi.md#get_release_notes) | **GET** `/api/2/release-notes` | 
[**get_service_status**](MainApi.md#get_service_status) | **GET** `/api/2/nodes/{id}/services/{service}` | 
[**get_smtp_configuration**](MainApi.md#get_smtp_configuration) | **GET** `/api/2/system/smtp` | 
[**get_stor_next_license**](MainApi.md#get_stor_next_license) | **GET** `/api/2/stornext-license` | 
[**get_storage_node**](MainApi.md#get_storage_node) | **GET** `/api/2/nodes/{id}` | 
[**get_system_info**](MainApi.md#get_system_info) | **GET** `/api/2/system/info` | 
[**get_user**](MainApi.md#get_user) | **GET** `/api/2/users/{id}` | 
[**get_workstation**](MainApi.md#get_workstation) | **GET** `/api/2/workstations/{id}` | 
[**install_stor_next_license**](MainApi.md#install_stor_next_license) | **POST** `/api/2/stornext-license` | 
[**patch_current_workstation**](MainApi.md#patch_current_workstation) | **PATCH** `/api/2/workstations/current` | 
[**patch_download_archive**](MainApi.md#patch_download_archive) | **PATCH** `/api/2/download-archive/{id}` | 
[**patch_group**](MainApi.md#patch_group) | **PATCH** `/api/2/groups/{id}` | 
[**patch_ntp_server**](MainApi.md#patch_ntp_server) | **PATCH** `/api/2/system/time/servers/{id}` | 
[**patch_profile**](MainApi.md#patch_profile) | **PATCH** `/api/2/users/me` | 
[**patch_user**](MainApi.md#patch_user) | **PATCH** `/api/2/users/{id}` | 
[**patch_workstation**](MainApi.md#patch_workstation) | **PATCH** `/api/2/workstations/{id}` | 
[**preview_user**](MainApi.md#preview_user) | **POST** `/api/2/users/preview` | 
[**reboot**](MainApi.md#reboot) | **POST** `/api/2/system/reboot` | 
[**register_upload**](MainApi.md#register_upload) | **POST** `/api/2/uploads/register` | 
[**render_email_template_preview**](MainApi.md#render_email_template_preview) | **POST** `/api/2/system/smtp/preview` | 
[**reset_user_password**](MainApi.md#reset_user_password) | **POST** `/api/2/users/{id}/password/reset` | 
[**run_service_operation**](MainApi.md#run_service_operation) | **POST** `/api/2/nodes/{id}/services/{service}/{operation}` | 
[**set_ipmi_configuration**](MainApi.md#set_ipmi_configuration) | **PUT** `/api/2/nodes/{id}/ipmi` | 
[**set_local_time**](MainApi.md#set_local_time) | **POST** `/api/2/system/time` | 
[**set_my_password**](MainApi.md#set_my_password) | **POST** `/api/2/users/me/password` | 
[**set_user_password**](MainApi.md#set_user_password) | **POST** `/api/2/users/{id}/password` | 
[**shutdown**](MainApi.md#shutdown) | **POST** `/api/2/system/shutdown` | 
[**start_solr_reindex**](MainApi.md#start_solr_reindex) | **POST** `/api/2/system/solr/reindex` | 
[**start_support_session**](MainApi.md#start_support_session) | **POST** `/api/2/system/support-session/start` | 
[**start_system_backup**](MainApi.md#start_system_backup) | **POST** `/api/2/system/backup/start` | 
[**sync_ldap_group**](MainApi.md#sync_ldap_group) | **POST** `/api/2/groups/{id}/ldap-sync` | 
[**sync_ldap_users**](MainApi.md#sync_ldap_users) | **POST** `/api/2/ldap-servers/{id}/sync-users` | 
[**sync_time**](MainApi.md#sync_time) | **POST** `/api/2/system/time/sync` | 
[**sync_user_totp**](MainApi.md#sync_user_totp) | **PUT** `/api/2/users/{id}/totp` | 
[**test_smtp_configuration**](MainApi.md#test_smtp_configuration) | **POST** `/api/2/system/smtp/test` | 
[**update_current_workstation**](MainApi.md#update_current_workstation) | **PUT** `/api/2/workstations/current` | 
[**update_download_archive**](MainApi.md#update_download_archive) | **PUT** `/api/2/download-archive/{id}` | 
[**update_group**](MainApi.md#update_group) | **PUT** `/api/2/groups/{id}` | 
[**update_ntp_server**](MainApi.md#update_ntp_server) | **PUT** `/api/2/system/time/servers/{id}` | 
[**update_parameters**](MainApi.md#update_parameters) | **PUT** `/api/2/parameters` | 
[**update_profile**](MainApi.md#update_profile) | **PUT** `/api/2/users/me` | 
[**update_smtp_configuration**](MainApi.md#update_smtp_configuration) | **PUT** `/api/2/system/smtp` | 
[**update_user**](MainApi.md#update_user) | **PUT** `/api/2/users/{id}` | 
[**update_workstation**](MainApi.md#update_workstation) | **PUT** `/api/2/workstations/{id}` | 
[**upload_chunk**](MainApi.md#upload_chunk) | **POST** `/api/2/uploads/chunk` | 



***

# **apply_configuration**

    def apply_configuration() -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.apply_configuration()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->apply_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **beep**

    def beep() -> object 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.beep()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->beep: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **check_chunk_uploaded**

    def check_chunk_uploaded(upload_id=upload_id, chunk_number=chunk_number) -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    upload_id = 'upload_id_example' # str |  (optional)
chunk_number = 'chunk_number_example' # str |  (optional)

    try:
        api_response = api_instance.check_chunk_uploaded(upload_id=upload_id, chunk_number=chunk_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->check_chunk_uploaded: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | [optional] 
 **chunk_number** | **str**|  | [optional] 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **check_internet_connectivity**

    def check_internet_connectivity() -> CheckConnectivityEndpointResponse 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.check_internet_connectivity()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->check_internet_connectivity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**CheckConnectivityEndpointResponse**](CheckConnectivityEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **check_stor_next_license**

    def check_stor_next_license(data) -> list[StorNextLicenseCheckEndpointResponse] 



### Required permissions    * User account permission: `system:admin-access`   * License component: stornext_mdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.StornextLicense() # StornextLicense | 

    try:
        api_response = api_instance.check_stor_next_license(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->check_stor_next_license: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**StornextLicense**](StornextLicense.md)|  | 

### Return type

[**list[StorNextLicenseCheckEndpointResponse]**](StorNextLicenseCheckEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **collect_diagnostics**

    def collect_diagnostics() -> DownloadArchive 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.collect_diagnostics()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->collect_diagnostics: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_archive**

    def create_archive(data) -> DownloadArchive 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.CreateDownloadArchive() # CreateDownloadArchive | 

    try:
        api_response = api_instance.create_archive(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->create_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreateDownloadArchive**](CreateDownloadArchive.md)|  | 

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_group**

    def create_group(data) -> ElementsGroupDetail 



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.ElementsGroupDetail() # ElementsGroupDetail | 

    try:
        api_response = api_instance.create_group(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ElementsGroupDetail**](ElementsGroupDetail.md)|  | 

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_home_workspace**

    def create_home_workspace(id, data) -> Workspace 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
data = elements_sdk.CreateHomeWorkspaceRequest() # CreateHomeWorkspaceRequest | 

    try:
        api_response = api_instance.create_home_workspace(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->create_home_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **data** | [**CreateHomeWorkspaceRequest**](CreateHomeWorkspaceRequest.md)|  | 

### Return type

[**Workspace**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_ntp_server**

    def create_ntp_server(data) -> NTPServer 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.NTPServer() # NTPServer | 

    try:
        api_response = api_instance.create_ntp_server(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->create_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**NTPServer**](NTPServer.md)|  | 

### Return type

[**NTPServer**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_user**

    def create_user(data) -> ElementsUserDetail 



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.ElementsUserDetail() # ElementsUserDetail | 

    try:
        api_response = api_instance.create_user(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ElementsUserDetail**](ElementsUserDetail.md)|  | 

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_workstation**

    def create_workstation(data) -> Workstation 



### Required permissions    * Authenticated user   * Own workstation or User account permission: `workstations:view` (read) / `workstations:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.Workstation() # Workstation | 

    try:
        api_response = api_instance.create_workstation(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->create_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Workstation**](Workstation.md)|  | 

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_download_archive**

    def delete_download_archive(id) -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A UUID string identifying this download archive.

    try:
        api_response = api_instance.delete_download_archive(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->delete_download_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this download archive. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_group**

    def delete_group(id) -> object 



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Group.

    try:
        api_response = api_instance.delete_group(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_home_workspace**

    def delete_home_workspace(id) -> object 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.delete_home_workspace(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->delete_home_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_ntp_server**

    def delete_ntp_server(id) -> object 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this NTP Server.

    try:
        api_response = api_instance.delete_ntp_server(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->delete_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this NTP Server. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_user**

    def delete_user(id) -> object 



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.delete_user(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_workstation**

    def delete_workstation(id) -> object 



### Required permissions    * Authenticated user   * Own workstation or User account permission: `workstations:view` (read) / `workstations:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A unique value identifying this workstation.

    try:
        api_response = api_instance.delete_workstation(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->delete_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this workstation. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **disable_user_totp**

    def disable_user_totp(id) -> object 



### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.disable_user_totp(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->disable_user_totp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **enable_user_totp**

    def enable_user_totp(id, data) -> object 



### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
data = elements_sdk.EnableTOTPRequest() # EnableTOTPRequest | 

    try:
        api_response = api_instance.enable_user_totp(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->enable_user_totp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **data** | [**EnableTOTPRequest**](EnableTOTPRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **finish_upload**

    def finish_upload(data) -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.FinishUploadEndpointRequest() # FinishUploadEndpointRequest | 

    try:
        api_response = api_instance.finish_upload(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->finish_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FinishUploadEndpointRequest**](FinishUploadEndpointRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **fix_ldap_group_memberships**

    def fix_ldap_group_memberships(id) -> object 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Server.

    try:
        api_response = api_instance.fix_ldap_group_memberships(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->fix_ldap_group_memberships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_download_archives**

    def get_all_download_archives(ordering=ordering, limit=limit, offset=offset) -> list[DownloadArchive] 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_download_archives(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_all_download_archives: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[DownloadArchive]**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_downloads**

    def get_all_downloads(ordering=ordering, limit=limit, offset=offset) -> list[Download] 



### Required permissions    * User account permission: `downloads:view` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_downloads(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_all_downloads: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Download]**](Download.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_groups**

    def get_all_groups(ordering=ordering, limit=limit, offset=offset) -> list[ElementsGroup] 



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_groups(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_all_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[ElementsGroup]**](ElementsGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ldap_servers**

    def get_all_ldap_servers(ordering=ordering, limit=limit, offset=offset) -> list[LDAPServer] 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ldap_servers(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_all_ldap_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[LDAPServer]**](LDAPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ntp_servers**

    def get_all_ntp_servers(address=address, ordering=ordering, limit=limit, offset=offset) -> list[NTPServer] 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    address = 'address_example' # str | Filter the returned list by `address`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ntp_servers(address=address, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
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

[**list[NTPServer]**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_storage_nodes**

    def get_all_storage_nodes(type=type, backend=backend, ordering=ordering, limit=limit, offset=offset, include_status=include_status) -> list[StorageNode] 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    type = 'type_example' # str | Filter the returned list by `type`. (optional)
backend = 'backend_example' # str | Filter the returned list by `backend`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
include_status = True # bool |  (optional)

    try:
        api_response = api_instance.get_all_storage_nodes(type=type, backend=backend, ordering=ordering, limit=limit, offset=offset, include_status=include_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_all_storage_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter the returned list by &#x60;type&#x60;. | [optional] 
 **backend** | **str**| Filter the returned list by &#x60;backend&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **include_status** | **bool**|  | [optional] 

### Return type

[**list[StorageNode]**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_users**

    def get_all_users(username=username, home=home, ordering=ordering, limit=limit, offset=offset, include_allowed_fs_paths=include_allowed_fs_paths, include_client_sessions=include_client_sessions) -> list[ElementsUser] 



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    username = 'username_example' # str | Filter the returned list by `username`. (optional)
home = 'home_example' # str | Filter the returned list by `home`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
include_allowed_fs_paths = True # bool |  (optional)
include_client_sessions = True # bool |  (optional)

    try:
        api_response = api_instance.get_all_users(username=username, home=home, ordering=ordering, limit=limit, offset=offset, include_allowed_fs_paths=include_allowed_fs_paths, include_client_sessions=include_client_sessions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_all_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Filter the returned list by &#x60;username&#x60;. | [optional] 
 **home** | **str**| Filter the returned list by &#x60;home&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **include_allowed_fs_paths** | **bool**|  | [optional] 
 **include_client_sessions** | **bool**|  | [optional] 

### Return type

[**list[ElementsUser]**](ElementsUser.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_workstations**

    def get_all_workstations(ordering=ordering, limit=limit, offset=offset) -> list[Workstation] 



### Required permissions    * Authenticated user   * Own workstation or User account permission: `workstations:view` (read) / `workstations:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_workstations(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_all_workstations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Workstation]**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_client_download_file**

    def get_client_download_file(file) -> object 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    file = 'file_example' # str | 

    try:
        api_response = api_instance.get_client_download_file(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_client_download_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_client_downloads**

    def get_client_downloads() -> list[ClientsEndpointResponse] 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_client_downloads()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_client_downloads: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**list[ClientsEndpointResponse]**](ClientsEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_current_workstation**

    def get_current_workstation(ordering=ordering, limit=limit, offset=offset) -> Workstation 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_current_workstation(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
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


***

# **get_download**

    def get_download(id) -> Download 



### Required permissions    * User account permission: `downloads:view` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this download.

    try:
        api_response = api_instance.get_download(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this download. | 

### Return type

[**Download**](Download.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_download_archive**

    def get_download_archive(id) -> DownloadArchive 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A UUID string identifying this download archive.

    try:
        api_response = api_instance.get_download_archive(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_download_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this download archive. | 

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_download_archive_file**

    def get_download_archive_file(id) -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A UUID string identifying this download archive.

    try:
        api_response = api_instance.get_download_archive_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_download_archive_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this download archive. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_download_file**

    def get_download_file(id) -> object 



### Required permissions    * User account permission: `downloads:view` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this download.

    try:
        api_response = api_instance.get_download_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_download_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this download. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_download_icon**

    def get_download_icon(id) -> object 



### Required permissions    * User account permission: `downloads:view` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this download.

    try:
        api_response = api_instance.get_download_icon(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_download_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this download. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_group**

    def get_group(id) -> ElementsGroupDetail 



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Group.

    try:
        api_response = api_instance.get_group(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. | 

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_home_workspace**

    def get_home_workspace(id) -> Workspace 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.get_home_workspace(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_home_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

### Return type

[**Workspace**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ipmi_configuration**

    def get_ipmi_configuration(id) -> Ipmi 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Storage Node.

    try:
        api_response = api_instance.get_ipmi_configuration(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_ipmi_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. | 

### Return type

[**Ipmi**](Ipmi.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ldap_server**

    def get_ldap_server(id) -> LDAPServer 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Server.

    try:
        api_response = api_instance.get_ldap_server(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_ldap_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. | 

### Return type

[**LDAPServer**](LDAPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ldap_server_groups**

    def get_ldap_server_groups(id) -> LDAPServerGroups 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Server.

    try:
        api_response = api_instance.get_ldap_server_groups(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_ldap_server_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. | 

### Return type

[**LDAPServerGroups**](LDAPServerGroups.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ldap_server_users**

    def get_ldap_server_users(id) -> LDAPServerUsers 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Server.

    try:
        api_response = api_instance.get_ldap_server_users(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_ldap_server_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. | 

### Return type

[**LDAPServerUsers**](LDAPServerUsers.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_license**

    def get_license() -> License 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_license()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_license: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**License**](License.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_local_time**

    def get_local_time() -> TimeEndpointResponse 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_local_time()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_local_time: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**TimeEndpointResponse**](TimeEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_log**

    def get_log(path, offset=offset) -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    path = 'path_example' # str | 
offset = 56 # int |  (optional)

    try:
        api_response = api_instance.get_log(path, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **offset** | **int**|  | [optional] 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_node_ipmi_sensors**

    def get_node_ipmi_sensors(id) -> Sensors 



### Required permissions    * User account permission: `system:status:view` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Storage Node.

    try:
        api_response = api_instance.get_node_ipmi_sensors(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_node_ipmi_sensors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. | 

### Return type

[**Sensors**](Sensors.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_node_stats**

    def get_node_stats(id) -> Stats 



### Required permissions    * User account permission: `system:status:view` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Storage Node.

    try:
        api_response = api_instance.get_node_stats(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_node_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. | 

### Return type

[**Stats**](Stats.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ntp_server**

    def get_ntp_server(id) -> NTPServer 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this NTP Server.

    try:
        api_response = api_instance.get_ntp_server(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this NTP Server. | 

### Return type

[**NTPServer**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_parameters**

    def get_parameters(ordering=ordering, limit=limit, offset=offset) -> Parameters 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_parameters(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
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


***

# **get_profile**

    def get_profile(ordering=ordering, limit=limit, offset=offset) -> ElementsUserProfile 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_profile(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
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


***

# **get_release_notes**

    def get_release_notes() -> list[ReleaseNotesEndpointResponse] 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_release_notes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_release_notes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**list[ReleaseNotesEndpointResponse]**](ReleaseNotesEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_service_status**

    def get_service_status(id, service) -> ServiceStatus 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Storage Node.
service = 'service_example' # str | 

    try:
        api_response = api_instance.get_service_status(id, service)
        pprint(api_response)
    except ApiException as e:
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


***

# **get_smtp_configuration**

    def get_smtp_configuration() -> SMTPConfiguration 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_smtp_configuration()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_smtp_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**SMTPConfiguration**](SMTPConfiguration.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_stor_next_license**

    def get_stor_next_license() -> StorNextLicenseEndpointResponse 



### Required permissions    * User account permission: `system:admin-access`   * License component: stornext_mdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_stor_next_license()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_stor_next_license: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**StorNextLicenseEndpointResponse**](StorNextLicenseEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_storage_node**

    def get_storage_node(id, include_status=include_status) -> StorageNode 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Storage Node.
include_status = True # bool |  (optional)

    try:
        api_response = api_instance.get_storage_node(id, include_status=include_status)
        pprint(api_response)
    except ApiException as e:
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


***

# **get_system_info**

    def get_system_info() -> SystemInfoEndpointResponse 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_system_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_system_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**SystemInfoEndpointResponse**](SystemInfoEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_user**

    def get_user(id) -> ElementsUserDetail 



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.get_user(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_workstation**

    def get_workstation(id) -> Workstation 



### Required permissions    * Authenticated user   * Own workstation or User account permission: `workstations:view` (read) / `workstations:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A unique value identifying this workstation.

    try:
        api_response = api_instance.get_workstation(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this workstation. | 

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **install_stor_next_license**

    def install_stor_next_license(data) -> StorNextLicenseEndpointResponse 



### Required permissions    * User account permission: `system:admin-access`   * License component: stornext_mdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.StornextLicense() # StornextLicense | 

    try:
        api_response = api_instance.install_stor_next_license(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->install_stor_next_license: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**StornextLicense**](StornextLicense.md)|  | 

### Return type

[**StorNextLicenseEndpointResponse**](StorNextLicenseEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_current_workstation**

    def patch_current_workstation(data) -> Workstation 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.WorkstationPartialUpdate() # WorkstationPartialUpdate | 

    try:
        api_response = api_instance.patch_current_workstation(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->patch_current_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WorkstationPartialUpdate**](WorkstationPartialUpdate.md)|  | 

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_download_archive**

    def patch_download_archive(id, data) -> DownloadArchive 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A UUID string identifying this download archive.
data = elements_sdk.DownloadArchivePartialUpdate() # DownloadArchivePartialUpdate | 

    try:
        api_response = api_instance.patch_download_archive(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->patch_download_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this download archive. | 
 **data** | [**DownloadArchivePartialUpdate**](DownloadArchivePartialUpdate.md)|  | 

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_group**

    def patch_group(id, data) -> ElementsGroupDetail 



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Group.
data = elements_sdk.ElementsGroupDetailPartialUpdate() # ElementsGroupDetailPartialUpdate | 

    try:
        api_response = api_instance.patch_group(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->patch_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. | 
 **data** | [**ElementsGroupDetailPartialUpdate**](ElementsGroupDetailPartialUpdate.md)|  | 

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_ntp_server**

    def patch_ntp_server(id, data) -> NTPServer 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this NTP Server.
data = elements_sdk.NTPServerPartialUpdate() # NTPServerPartialUpdate | 

    try:
        api_response = api_instance.patch_ntp_server(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->patch_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this NTP Server. | 
 **data** | [**NTPServerPartialUpdate**](NTPServerPartialUpdate.md)|  | 

### Return type

[**NTPServer**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_profile**

    def patch_profile(data) -> ElementsUserProfile 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.ElementsUserProfilePartialUpdate() # ElementsUserProfilePartialUpdate | 

    try:
        api_response = api_instance.patch_profile(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->patch_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ElementsUserProfilePartialUpdate**](ElementsUserProfilePartialUpdate.md)|  | 

### Return type

[**ElementsUserProfile**](ElementsUserProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_user**

    def patch_user(id, data) -> ElementsUserDetail 



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
data = elements_sdk.ElementsUserDetailPartialUpdate() # ElementsUserDetailPartialUpdate | 

    try:
        api_response = api_instance.patch_user(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->patch_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **data** | [**ElementsUserDetailPartialUpdate**](ElementsUserDetailPartialUpdate.md)|  | 

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_workstation**

    def patch_workstation(id, data) -> Workstation 



### Required permissions    * Authenticated user   * Own workstation or User account permission: `workstations:view` (read) / `workstations:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A unique value identifying this workstation.
data = elements_sdk.WorkstationPartialUpdate() # WorkstationPartialUpdate | 

    try:
        api_response = api_instance.patch_workstation(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->patch_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this workstation. | 
 **data** | [**WorkstationPartialUpdate**](WorkstationPartialUpdate.md)|  | 

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **preview_user**

    def preview_user(data) -> UserPreviewResponse 



### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.UserPreviewRequest() # UserPreviewRequest | 

    try:
        api_response = api_instance.preview_user(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->preview_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserPreviewRequest**](UserPreviewRequest.md)|  | 

### Return type

[**UserPreviewResponse**](UserPreviewResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **reboot**

    def reboot() -> object 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.reboot()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->reboot: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **register_upload**

    def register_upload(data) -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.RegisterUploadEndpointRequest() # RegisterUploadEndpointRequest | 

    try:
        api_response = api_instance.register_upload(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->register_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RegisterUploadEndpointRequest**](RegisterUploadEndpointRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **render_email_template_preview**

    def render_email_template_preview(data) -> object 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.EmailPreview() # EmailPreview | 

    try:
        api_response = api_instance.render_email_template_preview(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->render_email_template_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**EmailPreview**](EmailPreview.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **reset_user_password**

    def reset_user_password(id, data) -> object 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
data = None # object | 

    try:
        api_response = api_instance.reset_user_password(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->reset_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **data** | **object**|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **run_service_operation**

    def run_service_operation(id, operation, service) -> object 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Storage Node.
operation = 'operation_example' # str | 
service = 'service_example' # str | 

    try:
        api_response = api_instance.run_service_operation(id, operation, service)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->run_service_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. | 
 **operation** | **str**|  | 
 **service** | **str**|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **set_ipmi_configuration**

    def set_ipmi_configuration(id, data) -> Ipmi 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Storage Node.
data = elements_sdk.Ipmi() # Ipmi | 

    try:
        api_response = api_instance.set_ipmi_configuration(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->set_ipmi_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. | 
 **data** | [**Ipmi**](Ipmi.md)|  | 

### Return type

[**Ipmi**](Ipmi.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **set_local_time**

    def set_local_time(data) -> TimeEndpointResponse 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.TimeEndpointRequest() # TimeEndpointRequest | 

    try:
        api_response = api_instance.set_local_time(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->set_local_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TimeEndpointRequest**](TimeEndpointRequest.md)|  | 

### Return type

[**TimeEndpointResponse**](TimeEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **set_my_password**

    def set_my_password(data) -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.ChangeOwnPasswordRequest() # ChangeOwnPasswordRequest | 

    try:
        api_response = api_instance.set_my_password(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->set_my_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ChangeOwnPasswordRequest**](ChangeOwnPasswordRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **set_user_password**

    def set_user_password(id, data) -> object 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
data = elements_sdk.ChangePasswordRequest() # ChangePasswordRequest | 

    try:
        api_response = api_instance.set_user_password(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->set_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **data** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **shutdown**

    def shutdown() -> object 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.shutdown()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->shutdown: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_solr_reindex**

    def start_solr_reindex() -> SolrReindexEndpointResponse 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.start_solr_reindex()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->start_solr_reindex: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**SolrReindexEndpointResponse**](SolrReindexEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_support_session**

    def start_support_session() -> TaskInfo 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.start_support_session()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->start_support_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_system_backup**

    def start_system_backup(data) -> TaskInfo 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.Path() # Path | 

    try:
        api_response = api_instance.start_system_backup(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->start_system_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Path**](Path.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **sync_ldap_group**

    def sync_ldap_group(id) -> object 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Group.

    try:
        api_response = api_instance.sync_ldap_group(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->sync_ldap_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **sync_ldap_users**

    def sync_ldap_users(id) -> object 



### Required permissions    * User account permission: `users:manage` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Server.

    try:
        api_response = api_instance.sync_ldap_users(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->sync_ldap_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Server. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **sync_time**

    def sync_time(data) -> TimeSyncEndpointResponse 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.TimeSyncEndpointRequest() # TimeSyncEndpointRequest | 

    try:
        api_response = api_instance.sync_time(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->sync_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TimeSyncEndpointRequest**](TimeSyncEndpointRequest.md)|  | 

### Return type

[**TimeSyncEndpointResponse**](TimeSyncEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **sync_user_totp**

    def sync_user_totp(id, data) -> SyncTOTP 



### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
data = elements_sdk.SyncTOTPRequest() # SyncTOTPRequest | 

    try:
        api_response = api_instance.sync_user_totp(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->sync_user_totp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **data** | [**SyncTOTPRequest**](SyncTOTPRequest.md)|  | 

### Return type

[**SyncTOTP**](SyncTOTP.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **test_smtp_configuration**

    def test_smtp_configuration(data) -> object 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.TestSMTP() # TestSMTP | 

    try:
        api_response = api_instance.test_smtp_configuration(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->test_smtp_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TestSMTP**](TestSMTP.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_current_workstation**

    def update_current_workstation(data) -> Workstation 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.Workstation() # Workstation | 

    try:
        api_response = api_instance.update_current_workstation(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_current_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Workstation**](Workstation.md)|  | 

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_download_archive**

    def update_download_archive(id, data) -> DownloadArchive 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A UUID string identifying this download archive.
data = elements_sdk.DownloadArchive() # DownloadArchive | 

    try:
        api_response = api_instance.update_download_archive(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_download_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this download archive. | 
 **data** | [**DownloadArchive**](DownloadArchive.md)|  | 

### Return type

[**DownloadArchive**](DownloadArchive.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_group**

    def update_group(id, data) -> ElementsGroupDetail 



### Required permissions    * User account permission: `users:view` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Group.
data = elements_sdk.ElementsGroupDetail() # ElementsGroupDetail | 

    try:
        api_response = api_instance.update_group(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Group. | 
 **data** | [**ElementsGroupDetail**](ElementsGroupDetail.md)|  | 

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_ntp_server**

    def update_ntp_server(id, data) -> NTPServer 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this NTP Server.
data = elements_sdk.NTPServer() # NTPServer | 

    try:
        api_response = api_instance.update_ntp_server(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_ntp_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this NTP Server. | 
 **data** | [**NTPServer**](NTPServer.md)|  | 

### Return type

[**NTPServer**](NTPServer.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_parameters**

    def update_parameters(data) -> Parameters 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.Parameters() # Parameters | 

    try:
        api_response = api_instance.update_parameters(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Parameters**](Parameters.md)|  | 

### Return type

[**Parameters**](Parameters.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_profile**

    def update_profile(data) -> ElementsUserProfile 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.ElementsUserProfile() # ElementsUserProfile | 

    try:
        api_response = api_instance.update_profile(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ElementsUserProfile**](ElementsUserProfile.md)|  | 

### Return type

[**ElementsUserProfile**](ElementsUserProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_smtp_configuration**

    def update_smtp_configuration(data) -> SMTPConfiguration 



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.SMTPConfiguration() # SMTPConfiguration | 

    try:
        api_response = api_instance.update_smtp_configuration(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_smtp_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SMTPConfiguration**](SMTPConfiguration.md)|  | 

### Return type

[**SMTPConfiguration**](SMTPConfiguration.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_user**

    def update_user(id, data) -> ElementsUserDetail 



### Required permissions    * User account permission: `None` (read) / `users:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
data = elements_sdk.ElementsUserDetail() # ElementsUserDetail | 

    try:
        api_response = api_instance.update_user(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **data** | [**ElementsUserDetail**](ElementsUserDetail.md)|  | 

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_workstation**

    def update_workstation(id, data) -> Workstation 



### Required permissions    * Authenticated user   * Own workstation or User account permission: `workstations:view` (read) / `workstations:manage` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A unique value identifying this workstation.
data = elements_sdk.Workstation() # Workstation | 

    try:
        api_response = api_instance.update_workstation(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->update_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this workstation. | 
 **data** | [**Workstation**](Workstation.md)|  | 

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **upload_chunk**

    def upload_chunk(data) -> object 



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.UploadChunkEndpointRequest() # UploadChunkEndpointRequest | 

    try:
        api_response = api_instance.upload_chunk(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->upload_chunk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UploadChunkEndpointRequest**](UploadChunkEndpointRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

