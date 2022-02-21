# elements_sdk.StorageApi



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
[**create_volume**](StorageApi.md#create_volume) | **POST** `/api/2/volumes` | 
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


# **apply_workspace_affinity**
    def apply_workspace_affinity(id)



### Required permissions    * User account permission: `projects:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.

    # example passing only required values which don't have defaults set
    try:
        api_instance.apply_workspace_affinity(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->apply_workspace_affinity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **bookmark_workspace**
    def bookmark_workspace(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.

    # example passing only required values which don't have defaults set
    try:
        api_instance.bookmark_workspace(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->bookmark_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **calculate_directory_size**
    def FileSizeEndpointResponse calculate_directory_size(path_input)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.path_input import PathInput
from elements_sdk.model.file_size_endpoint_response import FileSizeEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    path_input = PathInput(
        input=[
            "input_example",
        ],
    ) # PathInput | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.calculate_directory_size(path_input)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->calculate_directory_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_input** | [**PathInput**](PathInput.md)|  |

### Return type

[**FileSizeEndpointResponse**](FileSizeEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **check_in_into_workspace**
    def check_in_into_workspace(id, workspace_check_in)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_check_in import WorkspaceCheckIn
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.
    workspace_check_in = WorkspaceCheckIn(
        mountpoint="mountpoint_example",
        protocol="protocol_example",
        address="address_example",
    ) # WorkspaceCheckIn | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.check_in_into_workspace(id, workspace_check_in)
    except elements_sdk.ApiException as e:
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

# **check_out_of_workspace**
    def check_out_of_workspace(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.

    # example passing only required values which don't have defaults set
    try:
        api_instance.check_out_of_workspace(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->check_out_of_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **copy_files**
    def TaskInfo copy_files(file_copy_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.file_copy_endpoint_request import FileCopyEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    file_copy_endpoint_request = FileCopyEndpointRequest(
        input=[
            "input_example",
        ],
        destination="destination_example",
        hardlink=True,
        sync=True,
        overwrite="overwrite_example",
        folders="merge",
    ) # FileCopyEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.copy_files(file_copy_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->copy_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_copy_endpoint_request** | [**FileCopyEndpointRequest**](FileCopyEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_file**
    def FilesystemFile create_file(file_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.file_update import FileUpdate
from elements_sdk.model.filesystem_file import FilesystemFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    file_update = FileUpdate(
        name="name_example",
        files=[
            BasicFile(
                name="name_example",
                files=[
                    {},
                ],
            ),
        ],
        parent="parent_example",
        mode="mode_example",
        uid=1,
        gid=1,
        user="user_example",
        group="group_example",
        recursive=True,
        affinity="affinity_example",
        mode_setuid=True,
        mode_setgid=True,
        mode_setvfx=True,
        mode_user_read=True,
        mode_user_write=True,
        mode_user_execute=True,
        mode_group_read=True,
        mode_group_write=True,
        mode_group_execute=True,
        mode_others_read=True,
        mode_others_write=True,
        mode_others_execute=True,
    ) # FileUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_file(file_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_update** | [**FileUpdate**](FileUpdate.md)|  |

### Return type

[**FilesystemFile**](FilesystemFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_path_quota**
    def create_path_quota(id, relative_path, create_path_quota_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.create_path_quota_request import CreatePathQuotaRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    relative_path = "relative_path_example" # str | 
    create_path_quota_request = CreatePathQuotaRequest(
        force_destroy_content=True,
    ) # CreatePathQuotaRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_path_quota(id, relative_path, create_path_quota_request)
    except elements_sdk.ApiException as e:
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

# **create_production**
    def Production create_production(production_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.production import Production
from elements_sdk.model.production_update import ProductionUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    production_update = ProductionUpdate(
        name="name_example",
        obscure_name=True,
        description="description_example",
        long_description="long_description_example",
        active=True,
        template=1,
        default_group=1,
    ) # ProductionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_production(production_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->create_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_update** | [**ProductionUpdate**](ProductionUpdate.md)|  |

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_share**
    def Share create_share(share_update)



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.share import Share
from elements_sdk.model.share_update import ShareUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    share_update = ShareUpdate(
        sharing_nfs_permissions=[
            NFSPermission(
                host="host_example",
                read_only=True,
                options="options_example",
            ),
        ],
        volume=VolumeReference(
            id=1,
            fs_properties=FSProperties(
                needs_ssh_connection=True,
                supports_directory_quotas=True,
                supports_soft_quotas=True,
                supports_user_quotas=True,
                supports_group_quotas=True,
                supports_xattrs=True,
                supports_snapshots=True,
                creating_directory_quota_destroys_content=True,
                removing_directory_quota_destroys_content=True,
            ),
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
                    supports_sharing_nfs_permissions=True,
                ),
            ),
            status=VolumeStatus(
                online=True,
                size_total=1,
                size_used=1,
                size_free=1,
                snfs=VolumeSNFSStatus(
                    stripe_groups=[
                        SNFSStripeGroup(
                            name="name_example",
                            status_tags=[
                                "status_tags_example",
                            ],
                            affinity="affinity_example",
                            size_total=1,
                            size_used=1,
                            size_free=1,
                        ),
                    ],
                ),
                lizardfs=VolumeLizardFSStatus(
                    master=StorageNodeMini(
                        id=1,
                        name="name_example",
                        address="address_example",
                        type=1,
                    ),
                    nodes=[
                        LizardFSNode(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            online=True,
                            version="version_example",
                            chunks=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            chunks_for_removal=1,
                            label="label_example",
                        ),
                    ],
                    disks=[
                        LizardFSDisk(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            mountpoint="mountpoint_example",
                            to_delete=True,
                            damaged=True,
                            scanning=True,
                            error_chunk=1,
                            error_timestamp=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            chunks=1,
                        ),
                    ],
                ),
                beegfs=VolumeBeeGFSStatus(
                    nodes=[
                        BeeGFSNode(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            roles=[
                                "roles_example",
                            ],
                            addresses=[
                                "addresses_example",
                            ],
                        ),
                    ],
                    targets=[
                        BeeGFSTarget(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            id=1,
                            host="host_example",
                            storage_pool=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            online=True,
                            consistent=True,
                            errors=[
                                "errors_example",
                            ],
                        ),
                    ],
                ),
            ),
        ),
        name="name_example",
        path="path_example",
        share_smb=True,
        share_nfs=True,
        share_afp=True,
        sharing_read_only=True,
        sharing_hidden=True,
        sharing_require_login=True,
        smb_extra_config="smb_extra_config_example",
        afp_extra_config="afp_extra_config_example",
        rw_access_group=1,
        ro_access_group=1,
    ) # ShareUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_share(share_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->create_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_update** | [**ShareUpdate**](ShareUpdate.md)|  |

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_snapshot**
    def Snapshot create_snapshot(snapshot_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.snapshot_update import SnapshotUpdate
from elements_sdk.model.snapshot import Snapshot
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    snapshot_update = SnapshotUpdate(
        workspace=1,
        name="name_example",
    ) # SnapshotUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_snapshot(snapshot_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->create_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_update** | [**SnapshotUpdate**](SnapshotUpdate.md)|  |

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_template_folder**
    def create_template_folder(create_template_folder_endpoint_request)



### Required permissions    * User account permission: `folder_templates:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.create_template_folder_endpoint_request import CreateTemplateFolderEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    create_template_folder_endpoint_request = CreateTemplateFolderEndpointRequest(
        group=1,
        template="template_example",
        path="path_example",
    ) # CreateTemplateFolderEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_template_folder(create_template_folder_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->create_template_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_folder_endpoint_request** | [**CreateTemplateFolderEndpointRequest**](CreateTemplateFolderEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_volume**
    def Volume create_volume(volume_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.volume import Volume
from elements_sdk.model.volume_update import VolumeUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    volume_update = VolumeUpdate(
        path="path_example",
        nodes=[
            1,
        ],
        display_name="display_name_example",
        visual_tag="visual_tag_example",
        is_default=True,
        use_for_homes=True,
        use_for_workspaces=True,
        type="generic",
        snm_enabled=True,
        snfs_name="snfs_name_example",
        simulated_quotas=True,
        cloud_account=1,
    ) # VolumeUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_volume(volume_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->create_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_update** | [**VolumeUpdate**](VolumeUpdate.md)|  |

### Return type

[**Volume**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_workspace**
    def WorkspaceDetail create_workspace(workspace_detail_update)



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_detail_update import WorkspaceDetailUpdate
from elements_sdk.model.workspace_detail import WorkspaceDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    workspace_detail_update = WorkspaceDetailUpdate(
        production=ProductionReference(
            id=1,
        ),
        volume=None,
        sharing_nfs_permissions=[
            NFSPermission(
                host="host_example",
                read_only=True,
                options="options_example",
            ),
        ],
        quota_size_hard=0,
        quota_size_soft=0,
        name="name_example",
        description="description_example",
        long_description="long_description_example",
        is_template=True,
        active=True,
        mac_protocol="smb",
        win_protocol="disk",
        win_drive="a",
        linux_protocol="smb",
        linux_mountpoint="linux_mountpoint_example",
        share_name="share_name_example",
        share_nfs=True,
        share_afp=True,
        sharing_hidden=True,
        sharing_require_login=True,
        sharing_read_only=True,
        sharing_allow_execute=True,
        enable_quota=True,
        affinity="affinity_example",
        emulate_avid=True,
        emulate_capture=True,
        emulate_preopen=True,
        emulate_ntfs_streams=True,
        emulate_recycle_bin=True,
        emulate_fruit=True,
        smb_extra_config="smb_extra_config_example",
        afp_extra_config="afp_extra_config_example",
        recycle_bin_exclude="recycle_bin_exclude_example",
        is_external=True,
        external_mac_url="external_mac_url_example",
        external_win_url="external_win_url_example",
        external_linux_url="external_linux_url_example",
        allow_symlinks=True,
        rw_permission_priority=True,
        template=1,
    ) # WorkspaceDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_workspace(workspace_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->create_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_detail_update** | [**WorkspaceDetailUpdate**](WorkspaceDetailUpdate.md)|  |

### Return type

[**WorkspaceDetail**](WorkspaceDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_workspace_permission**
    def WorkspacePermission create_workspace_permission(workspace_permission_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_permission_update import WorkspacePermissionUpdate
from elements_sdk.model.workspace_permission import WorkspacePermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    workspace_permission_update = WorkspacePermissionUpdate(
        user=None,
        group=None,
        read_only=True,
        workspace=1,
    ) # WorkspacePermissionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_workspace_permission(workspace_permission_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->create_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_permission_update** | [**WorkspacePermissionUpdate**](WorkspacePermissionUpdate.md)|  |

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_file**
    def delete_file(path)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    path = "/" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_file(path)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->delete_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_files**
    def TaskInfo delete_files(file_delete_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.file_delete_endpoint_request import FileDeleteEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    file_delete_endpoint_request = FileDeleteEndpointRequest(
        input=[
            "input_example",
        ],
        sync=True,
    ) # FileDeleteEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_files(file_delete_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->delete_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_delete_endpoint_request** | [**FileDeleteEndpointRequest**](FileDeleteEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_path_quota**
    def delete_path_quota(id, relative_path)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    relative_path = "relative_path_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_path_quota(id, relative_path)
    except elements_sdk.ApiException as e:
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

# **delete_production**
    def delete_production(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this production.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_production(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->delete_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_share**
    def delete_share(id)



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this share.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_share(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->delete_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_snapshot**
    def delete_snapshot(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this snapshot.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_snapshot(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->delete_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_workspace**
    def delete_workspace(id)



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_workspace(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->delete_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_workspace_permission**
    def delete_workspace_permission(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace permission.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_workspace_permission(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->delete_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_deleted_workspaces**
    def [DeletedWorkspace] get_all_deleted_workspaces()



### Required permissions    * User account permission: `projects:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.deleted_workspace import DeletedWorkspace
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    is_template = "is_template_example" # str | Filter the returned list by `is_template`. (optional)
    production = 3.14 # float | Filter the returned list by `production`. (optional)
    volume = 3.14 # float | Filter the returned list by `volume`. (optional)
    home_for = 3.14 # float | Filter the returned list by `home_for`. (optional)
    volume__type = "volume__type_example" # str | Filter the returned list by `volume__type`. (optional)
    production__name = "production__name_example" # str | Filter the returned list by `production__name`. (optional)
    production__active = "production__active_example" # str | Filter the returned list by `production__active`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    is_external = "is_external_example" # str | Filter the returned list by `is_external`. (optional)
    active = "active_example" # str | Filter the returned list by `active`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_deleted_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_all_deleted_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_template** | **str**| Filter the returned list by &#x60;is_template&#x60;. | [optional]
 **production** | **float**| Filter the returned list by &#x60;production&#x60;. | [optional]
 **volume** | **float**| Filter the returned list by &#x60;volume&#x60;. | [optional]
 **home_for** | **float**| Filter the returned list by &#x60;home_for&#x60;. | [optional]
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

[**[DeletedWorkspace]**](DeletedWorkspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_productions**
    def [Production] get_all_productions()



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.production import Production
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    active = "active_example" # str | Filter the returned list by `active`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    copy_template_content = True # bool |  (optional)
    include_total_size = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_productions(active=active, name=name, ordering=ordering, limit=limit, offset=offset, copy_template_content=copy_template_content, include_total_size=include_total_size)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

[**[Production]**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_shares**
    def [Share] get_all_shares()



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.share import Share
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_shares(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_all_shares: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Share]**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_snapshots**
    def [Snapshot] get_all_snapshots()



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.snapshot import Snapshot
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    workspace = 3.14 # float | Filter the returned list by `workspace`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_snapshots(workspace=workspace, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_all_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **float**| Filter the returned list by &#x60;workspace&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Snapshot]**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_volumes**
    def [Volume] get_all_volumes()



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.volume import Volume
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    is_default = "is_default_example" # str | Filter the returned list by `is_default`. (optional)
    type = "type_example" # str | Filter the returned list by `type`. (optional)
    use_for_homes = "use_for_homes_example" # str | Filter the returned list by `use_for_homes`. (optional)
    use_for_workspaces = "use_for_workspaces_example" # str | Filter the returned list by `use_for_workspaces`. (optional)
    display_name = "display_name_example" # str | Filter the returned list by `display_name`. (optional)
    visual_tag = "visual_tag_example" # str | Filter the returned list by `visual_tag`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    include_status = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_volumes(is_default=is_default, type=type, use_for_homes=use_for_homes, use_for_workspaces=use_for_workspaces, display_name=display_name, visual_tag=visual_tag, ordering=ordering, limit=limit, offset=offset, include_status=include_status)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_all_volumes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_default** | **str**| Filter the returned list by &#x60;is_default&#x60;. | [optional]
 **type** | **str**| Filter the returned list by &#x60;type&#x60;. | [optional]
 **use_for_homes** | **str**| Filter the returned list by &#x60;use_for_homes&#x60;. | [optional]
 **use_for_workspaces** | **str**| Filter the returned list by &#x60;use_for_workspaces&#x60;. | [optional]
 **display_name** | **str**| Filter the returned list by &#x60;display_name&#x60;. | [optional]
 **visual_tag** | **str**| Filter the returned list by &#x60;visual_tag&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **include_status** | **bool**|  | [optional]

### Return type

[**[Volume]**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_workspace_permissions**
    def [WorkspacePermission] get_all_workspace_permissions()



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_permission import WorkspacePermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    workspace = 3.14 # float | Filter the returned list by `workspace`. (optional)
    user = 3.14 # float | Filter the returned list by `user`. (optional)
    group = 3.14 # float | Filter the returned list by `group`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_workspace_permissions(workspace=workspace, user=user, group=group, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_all_workspace_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **float**| Filter the returned list by &#x60;workspace&#x60;. | [optional]
 **user** | **float**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **group** | **float**| Filter the returned list by &#x60;group&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[WorkspacePermission]**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_workspaces**
    def [Workspace] get_all_workspaces()



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace import Workspace
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    is_template = "is_template_example" # str | Filter the returned list by `is_template`. (optional)
    production = 3.14 # float | Filter the returned list by `production`. (optional)
    volume = 3.14 # float | Filter the returned list by `volume`. (optional)
    home_for = 3.14 # float | Filter the returned list by `home_for`. (optional)
    volume__type = "volume__type_example" # str | Filter the returned list by `volume__type`. (optional)
    production__name = "production__name_example" # str | Filter the returned list by `production__name`. (optional)
    production__active = "production__active_example" # str | Filter the returned list by `production__active`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    is_external = "is_external_example" # str | Filter the returned list by `is_external`. (optional)
    active = "active_example" # str | Filter the returned list by `active`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    full_path = "full_path_example" # str |  (optional)
    resolve_access_for = 1 # int |  (optional)
    include_endpoints = True # bool |  (optional)
    include_quotas = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset, full_path=full_path, resolve_access_for=resolve_access_for, include_endpoints=include_endpoints, include_quotas=include_quotas)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_all_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_template** | **str**| Filter the returned list by &#x60;is_template&#x60;. | [optional]
 **production** | **float**| Filter the returned list by &#x60;production&#x60;. | [optional]
 **volume** | **float**| Filter the returned list by &#x60;volume&#x60;. | [optional]
 **home_for** | **float**| Filter the returned list by &#x60;home_for&#x60;. | [optional]
 **volume__type** | **str**| Filter the returned list by &#x60;volume__type&#x60;. | [optional]
 **production__name** | **str**| Filter the returned list by &#x60;production__name&#x60;. | [optional]
 **production__active** | **str**| Filter the returned list by &#x60;production__active&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **is_external** | **str**| Filter the returned list by &#x60;is_external&#x60;. | [optional]
 **active** | **str**| Filter the returned list by &#x60;active&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **full_path** | **str**|  | [optional]
 **resolve_access_for** | **int**|  | [optional]
 **include_endpoints** | **bool**|  | [optional]
 **include_quotas** | **bool**|  | [optional]

### Return type

[**[Workspace]**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_file**
    def FilesystemFile get_file(path)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.filesystem_file import FilesystemFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    path = "/" # str | 
    max_depth = 1 # int |  (optional)
    bundle = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_file(path)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_file(path, max_depth=max_depth, bundle=bundle)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **get_group_quota**
    def Quota get_group_quota(group_id, id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.quota import Quota
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    group_id = "group_id_example" # str | 
    id = 1 # int | A unique integer value identifying this volume.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_group_quota(group_id, id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **get_my_workspaces**
    def [Workspace] get_my_workspaces()



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace import Workspace
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    is_template = "is_template_example" # str | Filter the returned list by `is_template`. (optional)
    production = 3.14 # float | Filter the returned list by `production`. (optional)
    volume = 3.14 # float | Filter the returned list by `volume`. (optional)
    home_for = 3.14 # float | Filter the returned list by `home_for`. (optional)
    volume__type = "volume__type_example" # str | Filter the returned list by `volume__type`. (optional)
    production__name = "production__name_example" # str | Filter the returned list by `production__name`. (optional)
    production__active = "production__active_example" # str | Filter the returned list by `production__active`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    is_external = "is_external_example" # str | Filter the returned list by `is_external`. (optional)
    active = "active_example" # str | Filter the returned list by `active`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_my_workspaces(is_template=is_template, production=production, volume=volume, home_for=home_for, volume__type=volume__type, production__name=production__name, production__active=production__active, name=name, is_external=is_external, active=active, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_my_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_template** | **str**| Filter the returned list by &#x60;is_template&#x60;. | [optional]
 **production** | **float**| Filter the returned list by &#x60;production&#x60;. | [optional]
 **volume** | **float**| Filter the returned list by &#x60;volume&#x60;. | [optional]
 **home_for** | **float**| Filter the returned list by &#x60;home_for&#x60;. | [optional]
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

[**[Workspace]**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_path_quota**
    def Quota get_path_quota(id, relative_path)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.quota import Quota
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    relative_path = "relative_path_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_path_quota(id, relative_path)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **get_production**
    def Production get_production(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.production import Production
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this production.
    copy_template_content = True # bool |  (optional)
    include_total_size = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_production(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_production: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_production(id, copy_template_content=copy_template_content, include_total_size=include_total_size)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **get_root_directory**
    def get_root_directory()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.filesystem_file import FilesystemFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_root_directory(ordering=ordering, limit=limit, offset=offset)
    except elements_sdk.ApiException as e:
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

# **get_samba_dfree_string**
    def get_samba_dfree_string()



### Required permissions    * localhost only 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_samba_dfree_string()
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_samba_dfree_string: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_share**
    def Share get_share(id)



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.share import Share
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this share.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_share(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. |

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_snapshot**
    def Snapshot get_snapshot(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.snapshot import Snapshot
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this snapshot.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_snapshot(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. |

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_user_quota**
    def Quota get_user_quota(id, user_id)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.quota import Quota
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    user_id = "user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_quota(id, user_id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **get_volume**
    def Volume get_volume(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.volume import Volume
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    include_status = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_volume(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_volume: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_volume(id, include_status=include_status)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **get_volume_active_connections**
    def StorNextConnections get_volume_active_connections(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.stor_next_connections import StorNextConnections
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_volume_active_connections(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_volume_active_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. |

### Return type

[**StorNextConnections**](StorNextConnections.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_volume_file_size_distribution**
    def FileSizeDistribution get_volume_file_size_distribution(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.file_size_distribution import FileSizeDistribution
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_volume_file_size_distribution(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_volume_file_size_distribution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. |

### Return type

[**FileSizeDistribution**](FileSizeDistribution.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_volume_stats**
    def VolumeStats get_volume_stats(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.volume_stats import VolumeStats
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_volume_stats(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_volume_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. |

### Return type

[**VolumeStats**](VolumeStats.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_workspace**
    def WorkspaceDetail get_workspace(id)



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_detail import WorkspaceDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_workspace(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. |

### Return type

[**WorkspaceDetail**](WorkspaceDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_workspace_permission**
    def WorkspacePermission get_workspace_permission(id)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_permission import WorkspacePermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace permission.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_workspace_permission(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->get_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. |

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **move_files**
    def TaskInfo move_files(file_move_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.file_move_endpoint_request import FileMoveEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    file_move_endpoint_request = FileMoveEndpointRequest(
        input=[
            "input_example",
        ],
        destination="destination_example",
        sync=True,
        overwrite="overwrite_example",
    ) # FileMoveEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.move_files(file_move_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->move_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_move_endpoint_request** | [**FileMoveEndpointRequest**](FileMoveEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **move_workspace**
    def TaskInfo move_workspace(id, move_workspace_request)



### Required permissions    * User account permission: `projects:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.move_workspace_request import MoveWorkspaceRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.
    move_workspace_request = MoveWorkspaceRequest(
        production=1,
        volume=1,
        directory="directory_example",
    ) # MoveWorkspaceRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.move_workspace(id, move_workspace_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **move_workspace_to_production**
    def move_workspace_to_production(id, workspace_move_to_request)



### Required permissions    * User account permission: `projects:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_move_to_request import WorkspaceMoveToRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.
    workspace_move_to_request = WorkspaceMoveToRequest(
        production=1,
    ) # WorkspaceMoveToRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.move_workspace_to_production(id, workspace_move_to_request)
    except elements_sdk.ApiException as e:
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

# **patch_file**
    def FilesystemFile patch_file(path, file_partial_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.filesystem_file import FilesystemFile
from elements_sdk.model.file_partial_update import FilePartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    path = "/" # str | 
    file_partial_update = FilePartialUpdate(
        name="name_example",
        files=[
            BasicFile(
                name="name_example",
                files=[
                    {},
                ],
            ),
        ],
        parent="parent_example",
        mode="mode_example",
        uid=1,
        gid=1,
        user="user_example",
        group="group_example",
        recursive=True,
        affinity="affinity_example",
        mode_setuid=True,
        mode_setgid=True,
        mode_setvfx=True,
        mode_user_read=True,
        mode_user_write=True,
        mode_user_execute=True,
        mode_group_read=True,
        mode_group_write=True,
        mode_group_execute=True,
        mode_others_read=True,
        mode_others_write=True,
        mode_others_execute=True,
    ) # FilePartialUpdate | 
    max_depth = 1 # int |  (optional)
    bundle = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_file(path, file_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->patch_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_file(path, file_partial_update, max_depth=max_depth, bundle=bundle)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **patch_production**
    def Production patch_production(id, production_partial_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.production import Production
from elements_sdk.model.production_partial_update import ProductionPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this production.
    production_partial_update = ProductionPartialUpdate(
        name="name_example",
        obscure_name=True,
        description="description_example",
        long_description="long_description_example",
        active=True,
        template=1,
        default_group=1,
    ) # ProductionPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_production(id, production_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **patch_share**
    def Share patch_share(id, share_partial_update)



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.share_partial_update import SharePartialUpdate
from elements_sdk.model.share import Share
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this share.
    share_partial_update = SharePartialUpdate(
        sharing_nfs_permissions=[
            NFSPermission(
                host="host_example",
                read_only=True,
                options="options_example",
            ),
        ],
        volume=VolumeReference(
            id=1,
            fs_properties=FSProperties(
                needs_ssh_connection=True,
                supports_directory_quotas=True,
                supports_soft_quotas=True,
                supports_user_quotas=True,
                supports_group_quotas=True,
                supports_xattrs=True,
                supports_snapshots=True,
                creating_directory_quota_destroys_content=True,
                removing_directory_quota_destroys_content=True,
            ),
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
                    supports_sharing_nfs_permissions=True,
                ),
            ),
            status=VolumeStatus(
                online=True,
                size_total=1,
                size_used=1,
                size_free=1,
                snfs=VolumeSNFSStatus(
                    stripe_groups=[
                        SNFSStripeGroup(
                            name="name_example",
                            status_tags=[
                                "status_tags_example",
                            ],
                            affinity="affinity_example",
                            size_total=1,
                            size_used=1,
                            size_free=1,
                        ),
                    ],
                ),
                lizardfs=VolumeLizardFSStatus(
                    master=StorageNodeMini(
                        id=1,
                        name="name_example",
                        address="address_example",
                        type=1,
                    ),
                    nodes=[
                        LizardFSNode(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            online=True,
                            version="version_example",
                            chunks=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            chunks_for_removal=1,
                            label="label_example",
                        ),
                    ],
                    disks=[
                        LizardFSDisk(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            mountpoint="mountpoint_example",
                            to_delete=True,
                            damaged=True,
                            scanning=True,
                            error_chunk=1,
                            error_timestamp=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            chunks=1,
                        ),
                    ],
                ),
                beegfs=VolumeBeeGFSStatus(
                    nodes=[
                        BeeGFSNode(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            roles=[
                                "roles_example",
                            ],
                            addresses=[
                                "addresses_example",
                            ],
                        ),
                    ],
                    targets=[
                        BeeGFSTarget(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            id=1,
                            host="host_example",
                            storage_pool=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            online=True,
                            consistent=True,
                            errors=[
                                "errors_example",
                            ],
                        ),
                    ],
                ),
            ),
        ),
        name="name_example",
        path="path_example",
        share_smb=True,
        share_nfs=True,
        share_afp=True,
        sharing_read_only=True,
        sharing_hidden=True,
        sharing_require_login=True,
        smb_extra_config="smb_extra_config_example",
        afp_extra_config="afp_extra_config_example",
        rw_access_group=1,
        ro_access_group=1,
    ) # SharePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_share(id, share_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **patch_snapshot**
    def Snapshot patch_snapshot(id, snapshot_partial_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.snapshot_partial_update import SnapshotPartialUpdate
from elements_sdk.model.snapshot import Snapshot
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this snapshot.
    snapshot_partial_update = SnapshotPartialUpdate(
        workspace=1,
        name="name_example",
    ) # SnapshotPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_snapshot(id, snapshot_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **patch_volume**
    def Volume patch_volume(id, volume_partial_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.volume_partial_update import VolumePartialUpdate
from elements_sdk.model.volume import Volume
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    volume_partial_update = VolumePartialUpdate(
        path="path_example",
        nodes=[
            1,
        ],
        display_name="display_name_example",
        visual_tag="visual_tag_example",
        is_default=True,
        use_for_homes=True,
        use_for_workspaces=True,
        type="generic",
        snm_enabled=True,
        snfs_name="snfs_name_example",
        simulated_quotas=True,
        cloud_account=1,
    ) # VolumePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_volume(id, volume_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **patch_workspace**
    def WorkspaceDetail patch_workspace(id, workspace_detail_partial_update)



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_detail import WorkspaceDetail
from elements_sdk.model.workspace_detail_partial_update import WorkspaceDetailPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.
    workspace_detail_partial_update = WorkspaceDetailPartialUpdate(
        production=ProductionReference(
            id=1,
        ),
        volume=None,
        sharing_nfs_permissions=[
            NFSPermission(
                host="host_example",
                read_only=True,
                options="options_example",
            ),
        ],
        quota_size_hard=0,
        quota_size_soft=0,
        name="name_example",
        description="description_example",
        long_description="long_description_example",
        is_template=True,
        active=True,
        mac_protocol="smb",
        win_protocol="disk",
        win_drive="a",
        linux_protocol="smb",
        linux_mountpoint="linux_mountpoint_example",
        share_name="share_name_example",
        share_nfs=True,
        share_afp=True,
        sharing_hidden=True,
        sharing_require_login=True,
        sharing_read_only=True,
        sharing_allow_execute=True,
        enable_quota=True,
        affinity="affinity_example",
        emulate_avid=True,
        emulate_capture=True,
        emulate_preopen=True,
        emulate_ntfs_streams=True,
        emulate_recycle_bin=True,
        emulate_fruit=True,
        smb_extra_config="smb_extra_config_example",
        afp_extra_config="afp_extra_config_example",
        recycle_bin_exclude="recycle_bin_exclude_example",
        is_external=True,
        external_mac_url="external_mac_url_example",
        external_win_url="external_win_url_example",
        external_linux_url="external_linux_url_example",
        allow_symlinks=True,
        rw_permission_priority=True,
        template=1,
    ) # WorkspaceDetailPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_workspace(id, workspace_detail_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **patch_workspace_permission**
    def WorkspacePermission patch_workspace_permission(id, workspace_permission_partial_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_permission_partial_update import WorkspacePermissionPartialUpdate
from elements_sdk.model.workspace_permission import WorkspacePermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace permission.
    workspace_permission_partial_update = WorkspacePermissionPartialUpdate(
        user=None,
        group=None,
        read_only=True,
        workspace=1,
    ) # WorkspacePermissionPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_workspace_permission(id, workspace_permission_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **record_storage_trace**
    def FilesystemTraceEndpointResponse record_storage_trace(filesystem_trace_endpoint_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.filesystem_trace_endpoint_response import FilesystemTraceEndpointResponse
from elements_sdk.model.filesystem_trace_endpoint_request import FilesystemTraceEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    filesystem_trace_endpoint_request = FilesystemTraceEndpointRequest(
        duration=1,
    ) # FilesystemTraceEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.record_storage_trace(filesystem_trace_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->record_storage_trace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filesystem_trace_endpoint_request** | [**FilesystemTraceEndpointRequest**](FilesystemTraceEndpointRequest.md)|  |

### Return type

[**FilesystemTraceEndpointResponse**](FilesystemTraceEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **repair_workspace_permissions**
    def TaskInfo repair_workspace_permissions(id)



### Required permissions    * User account permission: `projects:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.task_info import TaskInfo
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.repair_workspace_permissions(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->repair_workspace_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **share_to_home_workspace**
    def share_to_home_workspace(share_to_home_workspace_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.share_to_home_workspace_endpoint_request import ShareToHomeWorkspaceEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    share_to_home_workspace_endpoint_request = ShareToHomeWorkspaceEndpointRequest(
        paths=[
            "paths_example",
        ],
        bundles=[
            1,
        ],
        user=1,
        name="name_example",
    ) # ShareToHomeWorkspaceEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.share_to_home_workspace(share_to_home_workspace_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->share_to_home_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_to_home_workspace_endpoint_request** | [**ShareToHomeWorkspaceEndpointRequest**](ShareToHomeWorkspaceEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **unbookmark_workspace**
    def unbookmark_workspace(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.

    # example passing only required values which don't have defaults set
    try:
        api_instance.unbookmark_workspace(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->unbookmark_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **unzip_file**
    def TaskInfo unzip_file(file_unzip_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.file_unzip_endpoint_request import FileUnzipEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    file_unzip_endpoint_request = FileUnzipEndpointRequest(
        input="input_example",
        remove=True,
    ) # FileUnzipEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.unzip_file(file_unzip_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->unzip_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_unzip_endpoint_request** | [**FileUnzipEndpointRequest**](FileUnzipEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_group_quota**
    def update_group_quota(group_id, id, update_quota_request)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.update_quota_request import UpdateQuotaRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    group_id = "group_id_example" # str | 
    id = 1 # int | A unique integer value identifying this volume.
    update_quota_request = UpdateQuotaRequest(
        soft=1,
        hard=1,
    ) # UpdateQuotaRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_group_quota(group_id, id, update_quota_request)
    except elements_sdk.ApiException as e:
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

# **update_path_quota**
    def update_path_quota(id, relative_path, update_quota_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.update_quota_request import UpdateQuotaRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    relative_path = "relative_path_example" # str | 
    update_quota_request = UpdateQuotaRequest(
        soft=1,
        hard=1,
    ) # UpdateQuotaRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_path_quota(id, relative_path, update_quota_request)
    except elements_sdk.ApiException as e:
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

# **update_production**
    def Production update_production(id, production_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.production import Production
from elements_sdk.model.production_update import ProductionUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this production.
    production_update = ProductionUpdate(
        name="name_example",
        obscure_name=True,
        description="description_example",
        long_description="long_description_example",
        active=True,
        template=1,
        default_group=1,
    ) # ProductionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_production(id, production_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->update_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. |
 **production_update** | [**ProductionUpdate**](ProductionUpdate.md)|  |

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_share**
    def Share update_share(id, share_update)



### Required permissions    * User account permission: `shares:view` (read) / `shares:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.share import Share
from elements_sdk.model.share_update import ShareUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this share.
    share_update = ShareUpdate(
        sharing_nfs_permissions=[
            NFSPermission(
                host="host_example",
                read_only=True,
                options="options_example",
            ),
        ],
        volume=VolumeReference(
            id=1,
            fs_properties=FSProperties(
                needs_ssh_connection=True,
                supports_directory_quotas=True,
                supports_soft_quotas=True,
                supports_user_quotas=True,
                supports_group_quotas=True,
                supports_xattrs=True,
                supports_snapshots=True,
                creating_directory_quota_destroys_content=True,
                removing_directory_quota_destroys_content=True,
            ),
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
                    supports_sharing_nfs_permissions=True,
                ),
            ),
            status=VolumeStatus(
                online=True,
                size_total=1,
                size_used=1,
                size_free=1,
                snfs=VolumeSNFSStatus(
                    stripe_groups=[
                        SNFSStripeGroup(
                            name="name_example",
                            status_tags=[
                                "status_tags_example",
                            ],
                            affinity="affinity_example",
                            size_total=1,
                            size_used=1,
                            size_free=1,
                        ),
                    ],
                ),
                lizardfs=VolumeLizardFSStatus(
                    master=StorageNodeMini(
                        id=1,
                        name="name_example",
                        address="address_example",
                        type=1,
                    ),
                    nodes=[
                        LizardFSNode(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            online=True,
                            version="version_example",
                            chunks=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            chunks_for_removal=1,
                            label="label_example",
                        ),
                    ],
                    disks=[
                        LizardFSDisk(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            mountpoint="mountpoint_example",
                            to_delete=True,
                            damaged=True,
                            scanning=True,
                            error_chunk=1,
                            error_timestamp=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            chunks=1,
                        ),
                    ],
                ),
                beegfs=VolumeBeeGFSStatus(
                    nodes=[
                        BeeGFSNode(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            host="host_example",
                            roles=[
                                "roles_example",
                            ],
                            addresses=[
                                "addresses_example",
                            ],
                        ),
                    ],
                    targets=[
                        BeeGFSTarget(
                            node=StorageNodeMini(
                                id=1,
                                name="name_example",
                                address="address_example",
                                type=1,
                            ),
                            id=1,
                            host="host_example",
                            storage_pool=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            online=True,
                            consistent=True,
                            errors=[
                                "errors_example",
                            ],
                        ),
                    ],
                ),
            ),
        ),
        name="name_example",
        path="path_example",
        share_smb=True,
        share_nfs=True,
        share_afp=True,
        sharing_read_only=True,
        sharing_hidden=True,
        sharing_require_login=True,
        smb_extra_config="smb_extra_config_example",
        afp_extra_config="afp_extra_config_example",
        rw_access_group=1,
        ro_access_group=1,
    ) # ShareUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_share(id, share_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->update_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. |
 **share_update** | [**ShareUpdate**](ShareUpdate.md)|  |

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_snapshot**
    def Snapshot update_snapshot(id, snapshot_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.snapshot_update import SnapshotUpdate
from elements_sdk.model.snapshot import Snapshot
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this snapshot.
    snapshot_update = SnapshotUpdate(
        workspace=1,
        name="name_example",
    ) # SnapshotUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_snapshot(id, snapshot_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->update_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. |
 **snapshot_update** | [**SnapshotUpdate**](SnapshotUpdate.md)|  |

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_user_quota**
    def update_user_quota(id, user_id, update_quota_request)



### Required permissions    * User account permission: `users:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.update_quota_request import UpdateQuotaRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    user_id = "user_id_example" # str | 
    update_quota_request = UpdateQuotaRequest(
        soft=1,
        hard=1,
    ) # UpdateQuotaRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_user_quota(id, user_id, update_quota_request)
    except elements_sdk.ApiException as e:
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

# **update_volume**
    def Volume update_volume(id, volume_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.volume import Volume
from elements_sdk.model.volume_update import VolumeUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this volume.
    volume_update = VolumeUpdate(
        path="path_example",
        nodes=[
            1,
        ],
        display_name="display_name_example",
        visual_tag="visual_tag_example",
        is_default=True,
        use_for_homes=True,
        use_for_workspaces=True,
        type="generic",
        snm_enabled=True,
        snfs_name="snfs_name_example",
        simulated_quotas=True,
        cloud_account=1,
    ) # VolumeUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_volume(id, volume_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->update_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. |
 **volume_update** | [**VolumeUpdate**](VolumeUpdate.md)|  |

### Return type

[**Volume**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_workspace**
    def WorkspaceDetail update_workspace(id, workspace_detail_update)



### Required permissions    * User account permission: `None` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_detail_update import WorkspaceDetailUpdate
from elements_sdk.model.workspace_detail import WorkspaceDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace.
    workspace_detail_update = WorkspaceDetailUpdate(
        production=ProductionReference(
            id=1,
        ),
        volume=None,
        sharing_nfs_permissions=[
            NFSPermission(
                host="host_example",
                read_only=True,
                options="options_example",
            ),
        ],
        quota_size_hard=0,
        quota_size_soft=0,
        name="name_example",
        description="description_example",
        long_description="long_description_example",
        is_template=True,
        active=True,
        mac_protocol="smb",
        win_protocol="disk",
        win_drive="a",
        linux_protocol="smb",
        linux_mountpoint="linux_mountpoint_example",
        share_name="share_name_example",
        share_nfs=True,
        share_afp=True,
        sharing_hidden=True,
        sharing_require_login=True,
        sharing_read_only=True,
        sharing_allow_execute=True,
        enable_quota=True,
        affinity="affinity_example",
        emulate_avid=True,
        emulate_capture=True,
        emulate_preopen=True,
        emulate_ntfs_streams=True,
        emulate_recycle_bin=True,
        emulate_fruit=True,
        smb_extra_config="smb_extra_config_example",
        afp_extra_config="afp_extra_config_example",
        recycle_bin_exclude="recycle_bin_exclude_example",
        is_external=True,
        external_mac_url="external_mac_url_example",
        external_win_url="external_win_url_example",
        external_linux_url="external_linux_url_example",
        allow_symlinks=True,
        rw_permission_priority=True,
        template=1,
    ) # WorkspaceDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_workspace(id, workspace_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->update_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. |
 **workspace_detail_update** | [**WorkspaceDetailUpdate**](WorkspaceDetailUpdate.md)|  |

### Return type

[**WorkspaceDetail**](WorkspaceDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_workspace_permission**
    def WorkspacePermission update_workspace_permission(id, workspace_permission_update)



### Required permissions    * User account permission: `projects:view` (read) / `projects:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.workspace_permission_update import WorkspacePermissionUpdate
from elements_sdk.model.workspace_permission import WorkspacePermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    id = 1 # int | A unique integer value identifying this workspace permission.
    workspace_permission_update = WorkspacePermissionUpdate(
        user=None,
        group=None,
        read_only=True,
        workspace=1,
    ) # WorkspacePermissionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_workspace_permission(id, workspace_permission_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->update_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. |
 **workspace_permission_update** | [**WorkspacePermissionUpdate**](WorkspacePermissionUpdate.md)|  |

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **zip_files**
    def TaskInfo zip_files(file_zip_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import storage_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.file_zip_endpoint_request import FileZipEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = storage_api.StorageApi(api_client)
    file_zip_endpoint_request = FileZipEndpointRequest(
        input=[
            "input_example",
        ],
        path="path_example",
        name="name_example",
    ) # FileZipEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.zip_files(file_zip_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StorageApi->zip_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_zip_endpoint_request** | [**FileZipEndpointRequest**](FileZipEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

