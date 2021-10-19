# elements_sdk.StorageApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_workspace_affinity**](StorageApi.md#apply_workspace_affinity) | **POST** `/api/2/workspaces/{id}/apply-affinity` | 
[**bookmark_workspace**](StorageApi.md#bookmark_workspace) | **POST** `/api/2/workspaces/{id}/bookmark` | 
[**calculate_directory_size**](StorageApi.md#calculate_directory_size) | **POST** `/api/2/filesystem/calculate-directory-size` | 
[**check_in_into_workspace**](StorageApi.md#check_in_into_workspace) | **POST** `/api/2/workspaces/{id}/check-in` | 
[**check_out_of_workspace**](StorageApi.md#check_out_of_workspace) | **POST** `/api/2/workspaces/{id}/check-out` | 
[**copy_files**](StorageApi.md#copy_files) | **POST** `/api/2/filesystem/copy` | 
[**create_file**](StorageApi.md#create_file) | **POST** `/api/2/files` | 
[**create_path_quota**](StorageApi.md#create_path_quota) | **POST** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
[**create_production**](StorageApi.md#create_production) | **POST** `/api/2/productions` | 
[**create_share**](StorageApi.md#create_share) | **POST** `/api/2/shares` | 
[**create_snapshot**](StorageApi.md#create_snapshot) | **POST** `/api/2/snapshots` | 
[**create_template_folder**](StorageApi.md#create_template_folder) | **POST** `/api/2/private/create-template-folder` | 
[**create_workspace**](StorageApi.md#create_workspace) | **POST** `/api/2/workspaces` | 
[**create_workspace_permission**](StorageApi.md#create_workspace_permission) | **POST** `/api/2/workspace-permissions` | 
[**delete_file**](StorageApi.md#delete_file) | **DELETE** `/api/2/files/{path}` | 
[**delete_files**](StorageApi.md#delete_files) | **POST** `/api/2/filesystem/delete` | 
[**delete_path_quota**](StorageApi.md#delete_path_quota) | **DELETE** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
[**delete_production**](StorageApi.md#delete_production) | **DELETE** `/api/2/productions/{id}` | 
[**delete_share**](StorageApi.md#delete_share) | **DELETE** `/api/2/shares/{id}` | 
[**delete_snapshot**](StorageApi.md#delete_snapshot) | **DELETE** `/api/2/snapshots/{id}` | 
[**delete_workspace**](StorageApi.md#delete_workspace) | **DELETE** `/api/2/workspaces/{id}` | 
[**delete_workspace_permission**](StorageApi.md#delete_workspace_permission) | **DELETE** `/api/2/workspace-permissions/{id}` | 
[**get_all_deleted_workspaces**](StorageApi.md#get_all_deleted_workspaces) | **GET** `/api/2/workspaces/deleted` | 
[**get_all_productions**](StorageApi.md#get_all_productions) | **GET** `/api/2/productions` | 
[**get_all_shares**](StorageApi.md#get_all_shares) | **GET** `/api/2/shares` | 
[**get_all_snapshots**](StorageApi.md#get_all_snapshots) | **GET** `/api/2/snapshots` | 
[**get_all_volumes**](StorageApi.md#get_all_volumes) | **GET** `/api/2/volumes` | 
[**get_all_workspace_permissions**](StorageApi.md#get_all_workspace_permissions) | **GET** `/api/2/workspace-permissions` | 
[**get_all_workspaces**](StorageApi.md#get_all_workspaces) | **GET** `/api/2/workspaces` | 
[**get_file**](StorageApi.md#get_file) | **GET** `/api/2/files/{path}` | 
[**get_group_quota**](StorageApi.md#get_group_quota) | **GET** `/api/2/volumes/{id}/quotas/group/{group_id}` | 
[**get_my_workspaces**](StorageApi.md#get_my_workspaces) | **GET** `/api/2/workspaces/mine` | 
[**get_path_quota**](StorageApi.md#get_path_quota) | **GET** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
[**get_production**](StorageApi.md#get_production) | **GET** `/api/2/productions/{id}` | 
[**get_root_directory**](StorageApi.md#get_root_directory) | **GET** `/api/2/files` | 
[**get_samba_dfree_string**](StorageApi.md#get_samba_dfree_string) | **POST** `/api/2/private/dfree` | 
[**get_share**](StorageApi.md#get_share) | **GET** `/api/2/shares/{id}` | 
[**get_snapshot**](StorageApi.md#get_snapshot) | **GET** `/api/2/snapshots/{id}` | 
[**get_user_quota**](StorageApi.md#get_user_quota) | **GET** `/api/2/volumes/{id}/quotas/user/{user_id}` | 
[**get_volume**](StorageApi.md#get_volume) | **GET** `/api/2/volumes/{id}` | 
[**get_volume_active_connections**](StorageApi.md#get_volume_active_connections) | **GET** `/api/2/volumes/{id}/connections` | 
[**get_volume_file_size_distribution**](StorageApi.md#get_volume_file_size_distribution) | **GET** `/api/2/volumes/{id}/file-size-distribution` | 
[**get_volume_stats**](StorageApi.md#get_volume_stats) | **GET** `/api/2/volumes/{id}/stats` | 
[**get_workspace**](StorageApi.md#get_workspace) | **GET** `/api/2/workspaces/{id}` | 
[**get_workspace_permission**](StorageApi.md#get_workspace_permission) | **GET** `/api/2/workspace-permissions/{id}` | 
[**move_files**](StorageApi.md#move_files) | **POST** `/api/2/filesystem/move` | 
[**move_workspace**](StorageApi.md#move_workspace) | **POST** `/api/2/workspaces/{id}/move` | 
[**move_workspace_to_production**](StorageApi.md#move_workspace_to_production) | **POST** `/api/2/workspaces/{id}/move-to` | 
[**patch_file**](StorageApi.md#patch_file) | **PATCH** `/api/2/files/{path}` | 
[**patch_production**](StorageApi.md#patch_production) | **PATCH** `/api/2/productions/{id}` | 
[**patch_share**](StorageApi.md#patch_share) | **PATCH** `/api/2/shares/{id}` | 
[**patch_snapshot**](StorageApi.md#patch_snapshot) | **PATCH** `/api/2/snapshots/{id}` | 
[**patch_volume**](StorageApi.md#patch_volume) | **PATCH** `/api/2/volumes/{id}` | 
[**patch_workspace**](StorageApi.md#patch_workspace) | **PATCH** `/api/2/workspaces/{id}` | 
[**patch_workspace_permission**](StorageApi.md#patch_workspace_permission) | **PATCH** `/api/2/workspace-permissions/{id}` | 
[**record_storage_trace**](StorageApi.md#record_storage_trace) | **POST** `/api/2/filesystem/trace` | 
[**repair_workspace_permissions**](StorageApi.md#repair_workspace_permissions) | **POST** `/api/2/workspaces/{id}/repair-permissions` | 
[**share_to_home_workspace**](StorageApi.md#share_to_home_workspace) | **POST** `/api/2/share-to-home-workspace` | 
[**unbookmark_workspace**](StorageApi.md#unbookmark_workspace) | **DELETE** `/api/2/workspaces/{id}/bookmark` | 
[**unzip_file**](StorageApi.md#unzip_file) | **POST** `/api/2/filesystem/unzip` | 
[**update_group_quota**](StorageApi.md#update_group_quota) | **PUT** `/api/2/volumes/{id}/quotas/group/{group_id}` | 
[**update_path_quota**](StorageApi.md#update_path_quota) | **PUT** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
[**update_production**](StorageApi.md#update_production) | **PUT** `/api/2/productions/{id}` | 
[**update_share**](StorageApi.md#update_share) | **PUT** `/api/2/shares/{id}` | 
[**update_snapshot**](StorageApi.md#update_snapshot) | **PUT** `/api/2/snapshots/{id}` | 
[**update_user_quota**](StorageApi.md#update_user_quota) | **PUT** `/api/2/volumes/{id}/quotas/user/{user_id}` | 
[**update_volume**](StorageApi.md#update_volume) | **PUT** `/api/2/volumes/{id}` | 
[**update_workspace**](StorageApi.md#update_workspace) | **PUT** `/api/2/workspaces/{id}` | 
[**update_workspace_permission**](StorageApi.md#update_workspace_permission) | **PUT** `/api/2/workspace-permissions/{id}` | 
[**zip_files**](StorageApi.md#zip_files) | **POST** `/api/2/filesystem/zip` | 



***

# **apply_workspace_affinity**

    def apply_workspace_affinity(id)



### Required permissions    * User account permission: `projects:manage` 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.

    try:
        api_instance.apply_workspace_affinity(id)
    except ApiException as e:
        print("Exception when calling StorageApi->apply_workspace_affinity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **bookmark_workspace**

    def bookmark_workspace(id)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.

    try:
        api_instance.bookmark_workspace(id)
    except ApiException as e:
        print("Exception when calling StorageApi->bookmark_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **calculate_directory_size**

    def calculate_directory_size(path_input) -> FileSizeEndpointResponse 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    path_input = elements_sdk.PathInput() # PathInput | 

    try:
        api_response = api_instance.calculate_directory_size(path_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->calculate_directory_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_input** | [**PathInput**](PathInput.md)|  | 

### Return type

[**FileSizeEndpointResponse**](FileSizeEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **check_in_into_workspace**

    def check_in_into_workspace(id, workspace_check_in)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.
workspace_check_in = elements_sdk.WorkspaceCheckIn() # WorkspaceCheckIn | 

    try:
        api_instance.check_in_into_workspace(id, workspace_check_in)
    except ApiException as e:
        print("Exception when calling StorageApi->check_in_into_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **workspace_check_in** | [**WorkspaceCheckIn**](WorkspaceCheckIn.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **check_out_of_workspace**

    def check_out_of_workspace(id)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.

    try:
        api_instance.check_out_of_workspace(id)
    except ApiException as e:
        print("Exception when calling StorageApi->check_out_of_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **copy_files**

    def copy_files(file_copy_endpoint_request) -> TaskInfo 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    file_copy_endpoint_request = elements_sdk.FileCopyEndpointRequest() # FileCopyEndpointRequest | 

    try:
        api_response = api_instance.copy_files(file_copy_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->copy_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_copy_endpoint_request** | [**FileCopyEndpointRequest**](FileCopyEndpointRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_file**

    def create_file(filesystem_file) -> FilesystemFile 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    filesystem_file = elements_sdk.FilesystemFile() # FilesystemFile | 

    try:
        api_response = api_instance.create_file(filesystem_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filesystem_file** | [**FilesystemFile**](FilesystemFile.md)|  | 

### Return type

[**FilesystemFile**](FilesystemFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_path_quota**

    def create_path_quota(id, relative_path, create_path_quota_request)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
relative_path = 'relative_path_example' # str | 
create_path_quota_request = elements_sdk.CreatePathQuotaRequest() # CreatePathQuotaRequest | 

    try:
        api_instance.create_path_quota(id, relative_path, create_path_quota_request)
    except ApiException as e:
        print("Exception when calling StorageApi->create_path_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **relative_path** | **str**|  | 
 **create_path_quota_request** | [**CreatePathQuotaRequest**](CreatePathQuotaRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_production**

    def create_production(production) -> Production 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    production = elements_sdk.Production() # Production | 

    try:
        api_response = api_instance.create_production(production)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production** | [**Production**](Production.md)|  | 

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_share**

    def create_share(share) -> Share 



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    share = elements_sdk.Share() # Share | 

    try:
        api_response = api_instance.create_share(share)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share** | [**Share**](Share.md)|  | 

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_snapshot**

    def create_snapshot(snapshot) -> Snapshot 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    snapshot = elements_sdk.Snapshot() # Snapshot | 

    try:
        api_response = api_instance.create_snapshot(snapshot)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot** | [**Snapshot**](Snapshot.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_template_folder**

    def create_template_folder(create_template_folder_endpoint_request)



### Required permissions    * User account permission: `folder_templates:manage` 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    create_template_folder_endpoint_request = elements_sdk.CreateTemplateFolderEndpointRequest() # CreateTemplateFolderEndpointRequest | 

    try:
        api_instance.create_template_folder(create_template_folder_endpoint_request)
    except ApiException as e:
        print("Exception when calling StorageApi->create_template_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_folder_endpoint_request** | [**CreateTemplateFolderEndpointRequest**](CreateTemplateFolderEndpointRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_workspace**

    def create_workspace(workspace_detail) -> WorkspaceDetail 



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    workspace_detail = elements_sdk.WorkspaceDetail() # WorkspaceDetail | 

    try:
        api_response = api_instance.create_workspace(workspace_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_detail** | [**WorkspaceDetail**](WorkspaceDetail.md)|  | 

### Return type

[**WorkspaceDetail**](WorkspaceDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_workspace_permission**

    def create_workspace_permission(workspace_permission) -> WorkspacePermission 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    workspace_permission = elements_sdk.WorkspacePermission() # WorkspacePermission | 

    try:
        api_response = api_instance.create_workspace_permission(workspace_permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_permission** | [**WorkspacePermission**](WorkspacePermission.md)|  | 

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_file**

    def delete_file(path)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    path = 'path_example' # str | 

    try:
        api_instance.delete_file(path)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_files**

    def delete_files(file_delete_endpoint_request) -> TaskInfo 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    file_delete_endpoint_request = elements_sdk.FileDeleteEndpointRequest() # FileDeleteEndpointRequest | 

    try:
        api_response = api_instance.delete_files(file_delete_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_delete_endpoint_request** | [**FileDeleteEndpointRequest**](FileDeleteEndpointRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_path_quota**

    def delete_path_quota(id, relative_path)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
relative_path = 'relative_path_example' # str | 

    try:
        api_instance.delete_path_quota(id, relative_path)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_path_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **relative_path** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_production**

    def delete_production(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this production.

    try:
        api_instance.delete_production(id)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_share**

    def delete_share(id)



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this share.

    try:
        api_instance.delete_share(id)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_snapshot**

    def delete_snapshot(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this snapshot.

    try:
        api_instance.delete_snapshot(id)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_workspace**

    def delete_workspace(id)



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.

    try:
        api_instance.delete_workspace(id)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_workspace_permission**

    def delete_workspace_permission(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace permission.

    try:
        api_instance.delete_workspace_permission(id)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_deleted_workspaces**

    def get_all_deleted_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset) -> list[DeletedWorkspace] 



### Required permissions    * User account permission: `projects:view` 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    is_template = 'is_template_example' # str | Filter the returned list by `is_template`. (optional)
production = 'production_example' # str | Filter the returned list by `production`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
home_for = 'home_for_example' # str | Filter the returned list by `home_for`. (optional)
volume__type = 'volume__type_example' # str | Filter the returned list by `volume__type`. (optional)
production__name = 'production__name_example' # str | Filter the returned list by `production__name`. (optional)
production__active = 'production__active_example' # str | Filter the returned list by `production__active`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
is_external = 'is_external_example' # str | Filter the returned list by `is_external`. (optional)
active = 'active_example' # str | Filter the returned list by `active`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_deleted_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_deleted_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_template** | **str**| Filter the returned list by &#x60;is_template&#x60;. | [optional] 
 **production** | **str**| Filter the returned list by &#x60;production&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **home_for** | **str**| Filter the returned list by &#x60;home_for&#x60;. | [optional] 
 **volume__type** | **str**| Filter the returned list by &#x60;volume__type&#x60;. | [optional] 
 **production__name** | **str**| Filter the returned list by &#x60;production__name&#x60;. | [optional] 
 **production__active** | **str**| Filter the returned list by &#x60;production__active&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **is_external** | **str**| Filter the returned list by &#x60;is_external&#x60;. | [optional] 
 **active** | **str**| Filter the returned list by &#x60;active&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[DeletedWorkspace]**](DeletedWorkspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_productions**

    def get_all_productions(active=active, name=name, ordering=ordering, limit=limit, offset=offset, copy_template_content=copy_template_content, include_total_size=include_total_size) -> list[Production] 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    active = 'active_example' # str | Filter the returned list by `active`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
copy_template_content = True # bool |  (optional)
include_total_size = True # bool |  (optional)

    try:
        api_response = api_instance.get_all_productions(active=active, name=name, ordering=ordering, limit=limit, offset=offset, copy_template_content=copy_template_content, include_total_size=include_total_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_productions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **str**| Filter the returned list by &#x60;active&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **copy_template_content** | **bool**|  | [optional] 
 **include_total_size** | **bool**|  | [optional] 

### Return type

[**list[Production]**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_shares**

    def get_all_shares(ordering=ordering, limit=limit, offset=offset) -> list[Share] 



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_shares(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_shares: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Share]**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_snapshots**

    def get_all_snapshots(workspace=workspace, ordering=ordering, limit=limit, offset=offset) -> list[Snapshot] 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    workspace = 'workspace_example' # str | Filter the returned list by `workspace`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_snapshots(workspace=workspace, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Filter the returned list by &#x60;workspace&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Snapshot]**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_volumes**

    def get_all_volumes(is_default=is_default, type=type, use_for_homes=use_for_homes, use_for_workspaces=use_for_workspaces, name=name, display_name=display_name, visual_tag=visual_tag, ordering=ordering, limit=limit, offset=offset, include_status=include_status) -> list[Volume] 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    is_default = 'is_default_example' # str | Filter the returned list by `is_default`. (optional)
type = 'type_example' # str | Filter the returned list by `type`. (optional)
use_for_homes = 'use_for_homes_example' # str | Filter the returned list by `use_for_homes`. (optional)
use_for_workspaces = 'use_for_workspaces_example' # str | Filter the returned list by `use_for_workspaces`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
display_name = 'display_name_example' # str | Filter the returned list by `display_name`. (optional)
visual_tag = 'visual_tag_example' # str | Filter the returned list by `visual_tag`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
include_status = True # bool |  (optional)

    try:
        api_response = api_instance.get_all_volumes(is_default=is_default, type=type, use_for_homes=use_for_homes, use_for_workspaces=use_for_workspaces, name=name, display_name=display_name, visual_tag=visual_tag, ordering=ordering, limit=limit, offset=offset, include_status=include_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_volumes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_default** | **str**| Filter the returned list by &#x60;is_default&#x60;. | [optional] 
 **type** | **str**| Filter the returned list by &#x60;type&#x60;. | [optional] 
 **use_for_homes** | **str**| Filter the returned list by &#x60;use_for_homes&#x60;. | [optional] 
 **use_for_workspaces** | **str**| Filter the returned list by &#x60;use_for_workspaces&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **display_name** | **str**| Filter the returned list by &#x60;display_name&#x60;. | [optional] 
 **visual_tag** | **str**| Filter the returned list by &#x60;visual_tag&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **include_status** | **bool**|  | [optional] 

### Return type

[**list[Volume]**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_workspace_permissions**

    def get_all_workspace_permissions(workspace=workspace, user=user, group=group, ordering=ordering, limit=limit, offset=offset) -> list[WorkspacePermission] 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    workspace = 'workspace_example' # str | Filter the returned list by `workspace`. (optional)
user = 'user_example' # str | Filter the returned list by `user`. (optional)
group = 'group_example' # str | Filter the returned list by `group`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_workspace_permissions(workspace=workspace, user=user, group=group, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_workspace_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Filter the returned list by &#x60;workspace&#x60;. | [optional] 
 **user** | **str**| Filter the returned list by &#x60;user&#x60;. | [optional] 
 **group** | **str**| Filter the returned list by &#x60;group&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[WorkspacePermission]**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_workspaces**

    def get_all_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset, resolve_access_for=resolve_access_for, include_endpoints=include_endpoints, include_quotas=include_quotas) -> list[Workspace] 



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    is_template = 'is_template_example' # str | Filter the returned list by `is_template`. (optional)
production = 'production_example' # str | Filter the returned list by `production`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
home_for = 'home_for_example' # str | Filter the returned list by `home_for`. (optional)
volume__type = 'volume__type_example' # str | Filter the returned list by `volume__type`. (optional)
production__name = 'production__name_example' # str | Filter the returned list by `production__name`. (optional)
production__active = 'production__active_example' # str | Filter the returned list by `production__active`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
is_external = 'is_external_example' # str | Filter the returned list by `is_external`. (optional)
active = 'active_example' # str | Filter the returned list by `active`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
resolve_access_for = 56 # int |  (optional)
include_endpoints = True # bool |  (optional)
include_quotas = True # bool |  (optional)

    try:
        api_response = api_instance.get_all_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset, resolve_access_for=resolve_access_for, include_endpoints=include_endpoints, include_quotas=include_quotas)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_template** | **str**| Filter the returned list by &#x60;is_template&#x60;. | [optional] 
 **production** | **str**| Filter the returned list by &#x60;production&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **home_for** | **str**| Filter the returned list by &#x60;home_for&#x60;. | [optional] 
 **volume__type** | **str**| Filter the returned list by &#x60;volume__type&#x60;. | [optional] 
 **production__name** | **str**| Filter the returned list by &#x60;production__name&#x60;. | [optional] 
 **production__active** | **str**| Filter the returned list by &#x60;production__active&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **is_external** | **str**| Filter the returned list by &#x60;is_external&#x60;. | [optional] 
 **active** | **str**| Filter the returned list by &#x60;active&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **resolve_access_for** | **int**|  | [optional] 
 **include_endpoints** | **bool**|  | [optional] 
 **include_quotas** | **bool**|  | [optional] 

### Return type

[**list[Workspace]**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_file**

    def get_file(path, max_depth=max_depth, bundle=bundle) -> FilesystemFile 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    path = 'path_example' # str | 
max_depth = 56 # int |  (optional)
bundle = True # bool |  (optional)

    try:
        api_response = api_instance.get_file(path, max_depth=max_depth, bundle=bundle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **max_depth** | **int**|  | [optional] 
 **bundle** | **bool**|  | [optional] 

### Return type

[**FilesystemFile**](FilesystemFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_group_quota**

    def get_group_quota(group_id, id) -> Quota 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    group_id = 'group_id_example' # str | 
id = 56 # int | A unique integer value identifying this volume.

    try:
        api_response = api_instance.get_group_quota(group_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_group_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **id** | **int**| A unique integer value identifying this volume. | 

### Return type

[**Quota**](Quota.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_my_workspaces**

    def get_my_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset) -> list[Workspace] 



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    is_template = 'is_template_example' # str | Filter the returned list by `is_template`. (optional)
production = 'production_example' # str | Filter the returned list by `production`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
home_for = 'home_for_example' # str | Filter the returned list by `home_for`. (optional)
volume__type = 'volume__type_example' # str | Filter the returned list by `volume__type`. (optional)
production__name = 'production__name_example' # str | Filter the returned list by `production__name`. (optional)
production__active = 'production__active_example' # str | Filter the returned list by `production__active`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
is_external = 'is_external_example' # str | Filter the returned list by `is_external`. (optional)
active = 'active_example' # str | Filter the returned list by `active`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_my_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_my_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_template** | **str**| Filter the returned list by &#x60;is_template&#x60;. | [optional] 
 **production** | **str**| Filter the returned list by &#x60;production&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **home_for** | **str**| Filter the returned list by &#x60;home_for&#x60;. | [optional] 
 **volume__type** | **str**| Filter the returned list by &#x60;volume__type&#x60;. | [optional] 
 **production__name** | **str**| Filter the returned list by &#x60;production__name&#x60;. | [optional] 
 **production__active** | **str**| Filter the returned list by &#x60;production__active&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **is_external** | **str**| Filter the returned list by &#x60;is_external&#x60;. | [optional] 
 **active** | **str**| Filter the returned list by &#x60;active&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Workspace]**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_path_quota**

    def get_path_quota(id, relative_path) -> Quota 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
relative_path = 'relative_path_example' # str | 

    try:
        api_response = api_instance.get_path_quota(id, relative_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_path_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **relative_path** | **str**|  | 

### Return type

[**Quota**](Quota.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_production**

    def get_production(id, copy_template_content=copy_template_content, include_total_size=include_total_size) -> Production 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this production.
copy_template_content = True # bool |  (optional)
include_total_size = True # bool |  (optional)

    try:
        api_response = api_instance.get_production(id, copy_template_content=copy_template_content, include_total_size=include_total_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. | 
 **copy_template_content** | **bool**|  | [optional] 
 **include_total_size** | **bool**|  | [optional] 

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_root_directory**

    def get_root_directory(ordering=ordering, limit=limit, offset=offset)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_instance.get_root_directory(ordering=ordering, limit=limit, offset=offset)
    except ApiException as e:
        print("Exception when calling StorageApi->get_root_directory: %s\n" % e)
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


***

# **get_samba_dfree_string**

    def get_samba_dfree_string()



### Required permissions    * localhost only 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    
    try:
        api_instance.get_samba_dfree_string()
    except ApiException as e:
        print("Exception when calling StorageApi->get_samba_dfree_string: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_share**

    def get_share(id) -> Share 



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this share.

    try:
        api_response = api_instance.get_share(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. | 

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_snapshot**

    def get_snapshot(id) -> Snapshot 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this snapshot.

    try:
        api_response = api_instance.get_snapshot(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. | 

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_user_quota**

    def get_user_quota(id, user_id) -> Quota 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_user_quota(id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_user_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **user_id** | **str**|  | 

### Return type

[**Quota**](Quota.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_volume**

    def get_volume(id, include_status=include_status) -> Volume 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
include_status = True # bool |  (optional)

    try:
        api_response = api_instance.get_volume(id, include_status=include_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **include_status** | **bool**|  | [optional] 

### Return type

[**Volume**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_volume_active_connections**

    def get_volume_active_connections(id) -> StorNextConnections 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.

    try:
        api_response = api_instance.get_volume_active_connections(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_volume_active_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 

### Return type

[**StorNextConnections**](StorNextConnections.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_volume_file_size_distribution**

    def get_volume_file_size_distribution(id) -> FileSizeDistribution 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.

    try:
        api_response = api_instance.get_volume_file_size_distribution(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_volume_file_size_distribution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 

### Return type

[**FileSizeDistribution**](FileSizeDistribution.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_volume_stats**

    def get_volume_stats(id) -> VolumeStats 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.

    try:
        api_response = api_instance.get_volume_stats(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_volume_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 

### Return type

[**VolumeStats**](VolumeStats.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_workspace**

    def get_workspace(id) -> WorkspaceDetail 



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.

    try:
        api_response = api_instance.get_workspace(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

[**WorkspaceDetail**](WorkspaceDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_workspace_permission**

    def get_workspace_permission(id) -> WorkspacePermission 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace permission.

    try:
        api_response = api_instance.get_workspace_permission(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. | 

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **move_files**

    def move_files(file_move_endpoint_request) -> TaskInfo 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    file_move_endpoint_request = elements_sdk.FileMoveEndpointRequest() # FileMoveEndpointRequest | 

    try:
        api_response = api_instance.move_files(file_move_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->move_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_move_endpoint_request** | [**FileMoveEndpointRequest**](FileMoveEndpointRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **move_workspace**

    def move_workspace(id, move_workspace_request) -> TaskInfo 



### Required permissions    * User account permission: `projects:manage` 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.
move_workspace_request = elements_sdk.MoveWorkspaceRequest() # MoveWorkspaceRequest | 

    try:
        api_response = api_instance.move_workspace(id, move_workspace_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->move_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **move_workspace_request** | [**MoveWorkspaceRequest**](MoveWorkspaceRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **move_workspace_to_production**

    def move_workspace_to_production(id, workspace_move_to_request)



### Required permissions    * User account permission: `projects:manage` 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.
workspace_move_to_request = elements_sdk.WorkspaceMoveToRequest() # WorkspaceMoveToRequest | 

    try:
        api_instance.move_workspace_to_production(id, workspace_move_to_request)
    except ApiException as e:
        print("Exception when calling StorageApi->move_workspace_to_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **workspace_move_to_request** | [**WorkspaceMoveToRequest**](WorkspaceMoveToRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_file**

    def patch_file(path, file_partial_update, max_depth=max_depth, bundle=bundle) -> FilesystemFile 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    path = 'path_example' # str | 
file_partial_update = elements_sdk.FilePartialUpdate() # FilePartialUpdate | 
max_depth = 56 # int |  (optional)
bundle = True # bool |  (optional)

    try:
        api_response = api_instance.patch_file(path, file_partial_update, max_depth=max_depth, bundle=bundle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **file_partial_update** | [**FilePartialUpdate**](FilePartialUpdate.md)|  | 
 **max_depth** | **int**|  | [optional] 
 **bundle** | **bool**|  | [optional] 

### Return type

[**FilesystemFile**](FilesystemFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_production**

    def patch_production(id, production_partial_update) -> Production 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this production.
production_partial_update = elements_sdk.ProductionPartialUpdate() # ProductionPartialUpdate | 

    try:
        api_response = api_instance.patch_production(id, production_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. | 
 **production_partial_update** | [**ProductionPartialUpdate**](ProductionPartialUpdate.md)|  | 

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_share**

    def patch_share(id, share_partial_update) -> Share 



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this share.
share_partial_update = elements_sdk.SharePartialUpdate() # SharePartialUpdate | 

    try:
        api_response = api_instance.patch_share(id, share_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. | 
 **share_partial_update** | [**SharePartialUpdate**](SharePartialUpdate.md)|  | 

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_snapshot**

    def patch_snapshot(id, snapshot_partial_update) -> Snapshot 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this snapshot.
snapshot_partial_update = elements_sdk.SnapshotPartialUpdate() # SnapshotPartialUpdate | 

    try:
        api_response = api_instance.patch_snapshot(id, snapshot_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. | 
 **snapshot_partial_update** | [**SnapshotPartialUpdate**](SnapshotPartialUpdate.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_volume**

    def patch_volume(id, volume_partial_update) -> Volume 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
volume_partial_update = elements_sdk.VolumePartialUpdate() # VolumePartialUpdate | 

    try:
        api_response = api_instance.patch_volume(id, volume_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **volume_partial_update** | [**VolumePartialUpdate**](VolumePartialUpdate.md)|  | 

### Return type

[**Volume**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_workspace**

    def patch_workspace(id, workspace_detail_partial_update) -> WorkspaceDetail 



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.
workspace_detail_partial_update = elements_sdk.WorkspaceDetailPartialUpdate() # WorkspaceDetailPartialUpdate | 

    try:
        api_response = api_instance.patch_workspace(id, workspace_detail_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **workspace_detail_partial_update** | [**WorkspaceDetailPartialUpdate**](WorkspaceDetailPartialUpdate.md)|  | 

### Return type

[**WorkspaceDetail**](WorkspaceDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_workspace_permission**

    def patch_workspace_permission(id, workspace_permission_partial_update) -> WorkspacePermission 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace permission.
workspace_permission_partial_update = elements_sdk.WorkspacePermissionPartialUpdate() # WorkspacePermissionPartialUpdate | 

    try:
        api_response = api_instance.patch_workspace_permission(id, workspace_permission_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. | 
 **workspace_permission_partial_update** | [**WorkspacePermissionPartialUpdate**](WorkspacePermissionPartialUpdate.md)|  | 

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **record_storage_trace**

    def record_storage_trace(filesystem_trace_endpoint_request) -> FilesystemTraceEndpointResponse 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    filesystem_trace_endpoint_request = elements_sdk.FilesystemTraceEndpointRequest() # FilesystemTraceEndpointRequest | 

    try:
        api_response = api_instance.record_storage_trace(filesystem_trace_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->record_storage_trace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filesystem_trace_endpoint_request** | [**FilesystemTraceEndpointRequest**](FilesystemTraceEndpointRequest.md)|  | 

### Return type

[**FilesystemTraceEndpointResponse**](FilesystemTraceEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **repair_workspace_permissions**

    def repair_workspace_permissions(id) -> TaskInfo 



### Required permissions    * User account permission: `projects:manage` 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.

    try:
        api_response = api_instance.repair_workspace_permissions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->repair_workspace_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **share_to_home_workspace**

    def share_to_home_workspace(share_to_home_workspace_endpoint_request)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    share_to_home_workspace_endpoint_request = elements_sdk.ShareToHomeWorkspaceEndpointRequest() # ShareToHomeWorkspaceEndpointRequest | 

    try:
        api_instance.share_to_home_workspace(share_to_home_workspace_endpoint_request)
    except ApiException as e:
        print("Exception when calling StorageApi->share_to_home_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_to_home_workspace_endpoint_request** | [**ShareToHomeWorkspaceEndpointRequest**](ShareToHomeWorkspaceEndpointRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **unbookmark_workspace**

    def unbookmark_workspace(id)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.

    try:
        api_instance.unbookmark_workspace(id)
    except ApiException as e:
        print("Exception when calling StorageApi->unbookmark_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **unzip_file**

    def unzip_file(file_unzip_endpoint_request) -> TaskInfo 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    file_unzip_endpoint_request = elements_sdk.FileUnzipEndpointRequest() # FileUnzipEndpointRequest | 

    try:
        api_response = api_instance.unzip_file(file_unzip_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->unzip_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_unzip_endpoint_request** | [**FileUnzipEndpointRequest**](FileUnzipEndpointRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_group_quota**

    def update_group_quota(group_id, id, update_quota_request)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    group_id = 'group_id_example' # str | 
id = 56 # int | A unique integer value identifying this volume.
update_quota_request = elements_sdk.UpdateQuotaRequest() # UpdateQuotaRequest | 

    try:
        api_instance.update_group_quota(group_id, id, update_quota_request)
    except ApiException as e:
        print("Exception when calling StorageApi->update_group_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **id** | **int**| A unique integer value identifying this volume. | 
 **update_quota_request** | [**UpdateQuotaRequest**](UpdateQuotaRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_path_quota**

    def update_path_quota(id, relative_path, update_quota_request)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
relative_path = 'relative_path_example' # str | 
update_quota_request = elements_sdk.UpdateQuotaRequest() # UpdateQuotaRequest | 

    try:
        api_instance.update_path_quota(id, relative_path, update_quota_request)
    except ApiException as e:
        print("Exception when calling StorageApi->update_path_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **relative_path** | **str**|  | 
 **update_quota_request** | [**UpdateQuotaRequest**](UpdateQuotaRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_production**

    def update_production(id, production) -> Production 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this production.
production = elements_sdk.Production() # Production | 

    try:
        api_response = api_instance.update_production(id, production)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. | 
 **production** | [**Production**](Production.md)|  | 

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_share**

    def update_share(id, share) -> Share 



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this share.
share = elements_sdk.Share() # Share | 

    try:
        api_response = api_instance.update_share(id, share)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. | 
 **share** | [**Share**](Share.md)|  | 

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_snapshot**

    def update_snapshot(id, snapshot) -> Snapshot 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this snapshot.
snapshot = elements_sdk.Snapshot() # Snapshot | 

    try:
        api_response = api_instance.update_snapshot(id, snapshot)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. | 
 **snapshot** | [**Snapshot**](Snapshot.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_user_quota**

    def update_user_quota(id, user_id, update_quota_request)



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
user_id = 'user_id_example' # str | 
update_quota_request = elements_sdk.UpdateQuotaRequest() # UpdateQuotaRequest | 

    try:
        api_instance.update_user_quota(id, user_id, update_quota_request)
    except ApiException as e:
        print("Exception when calling StorageApi->update_user_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **user_id** | **str**|  | 
 **update_quota_request** | [**UpdateQuotaRequest**](UpdateQuotaRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_volume**

    def update_volume(id, volume) -> Volume 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this volume.
volume = elements_sdk.Volume() # Volume | 

    try:
        api_response = api_instance.update_volume(id, volume)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **volume** | [**Volume**](Volume.md)|  | 

### Return type

[**Volume**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_workspace**

    def update_workspace(id, workspace_detail) -> WorkspaceDetail 



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace.
workspace_detail = elements_sdk.WorkspaceDetail() # WorkspaceDetail | 

    try:
        api_response = api_instance.update_workspace(id, workspace_detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **workspace_detail** | [**WorkspaceDetail**](WorkspaceDetail.md)|  | 

### Return type

[**WorkspaceDetail**](WorkspaceDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_workspace_permission**

    def update_workspace_permission(id, workspace_permission) -> WorkspacePermission 



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    id = 56 # int | A unique integer value identifying this workspace permission.
workspace_permission = elements_sdk.WorkspacePermission() # WorkspacePermission | 

    try:
        api_response = api_instance.update_workspace_permission(id, workspace_permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. | 
 **workspace_permission** | [**WorkspacePermission**](WorkspacePermission.md)|  | 

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **zip_files**

    def zip_files(file_zip_endpoint_request) -> TaskInfo 



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StorageApi(api_client)
    file_zip_endpoint_request = elements_sdk.FileZipEndpointRequest() # FileZipEndpointRequest | 

    try:
        api_response = api_instance.zip_files(file_zip_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->zip_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_zip_endpoint_request** | [**FileZipEndpointRequest**](FileZipEndpointRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

