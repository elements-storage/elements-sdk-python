# elements_sdk.StorageApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_workspace_affinity**](StorageApi.md#apply_workspace_affinity) | **POST** `/api/2/workspaces/{id}/apply-affinity` | 
[**bookmark_workspace**](StorageApi.md#bookmark_workspace) | **POST** `/api/2/workspaces/{id}/bookmark` | 
[**check_in_into_workspace**](StorageApi.md#check_in_into_workspace) | **POST** `/api/2/workspaces/{id}/check-in` | 
[**check_out_of_workspace**](StorageApi.md#check_out_of_workspace) | **POST** `/api/2/workspaces/{id}/check-out` | 
[**create_production**](StorageApi.md#create_production) | **POST** `/api/2/productions` | 
[**create_share**](StorageApi.md#create_share) | **POST** `/api/2/shares` | 
[**create_snapshot**](StorageApi.md#create_snapshot) | **POST** `/api/2/snapshots` | 
[**create_workspace**](StorageApi.md#create_workspace) | **POST** `/api/2/workspaces` | 
[**create_workspace_permission**](StorageApi.md#create_workspace_permission) | **POST** `/api/2/workspace-permissions` | 
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
[**get_my_workspaces**](StorageApi.md#get_my_workspaces) | **GET** `/api/2/workspaces/mine` | 
[**get_production**](StorageApi.md#get_production) | **GET** `/api/2/productions/{id}` | 
[**get_share**](StorageApi.md#get_share) | **GET** `/api/2/shares/{id}` | 
[**get_snapshot**](StorageApi.md#get_snapshot) | **GET** `/api/2/snapshots/{id}` | 
[**get_volume**](StorageApi.md#get_volume) | **GET** `/api/2/volumes/{id}` | 
[**get_volume_active_connections**](StorageApi.md#get_volume_active_connections) | **GET** `/api/2/volumes/{id}/connections` | 
[**get_volume_file_size_distribution**](StorageApi.md#get_volume_file_size_distribution) | **GET** `/api/2/volumes/{id}/file-size-distribution` | 
[**get_volume_stats**](StorageApi.md#get_volume_stats) | **GET** `/api/2/volumes/{id}/stats` | 
[**get_workspace**](StorageApi.md#get_workspace) | **GET** `/api/2/workspaces/{id}` | 
[**get_workspace_permission**](StorageApi.md#get_workspace_permission) | **GET** `/api/2/workspace-permissions/{id}` | 
[**move_workspace_to_production**](StorageApi.md#move_workspace_to_production) | **POST** `/api/2/workspaces/{id}/move-to` | 
[**patch_production**](StorageApi.md#patch_production) | **PATCH** `/api/2/productions/{id}` | 
[**patch_share**](StorageApi.md#patch_share) | **PATCH** `/api/2/shares/{id}` | 
[**patch_snapshot**](StorageApi.md#patch_snapshot) | **PATCH** `/api/2/snapshots/{id}` | 
[**patch_volume**](StorageApi.md#patch_volume) | **PATCH** `/api/2/volumes/{id}` | 
[**patch_workspace**](StorageApi.md#patch_workspace) | **PATCH** `/api/2/workspaces/{id}` | 
[**patch_workspace_permission**](StorageApi.md#patch_workspace_permission) | **PATCH** `/api/2/workspace-permissions/{id}` | 
[**repair_workspace_permissions**](StorageApi.md#repair_workspace_permissions) | **POST** `/api/2/workspaces/{id}/repair-permissions` | 
[**unbookmark_workspace**](StorageApi.md#unbookmark_workspace) | **DELETE** `/api/2/workspaces/{id}/bookmark` | 
[**update_production**](StorageApi.md#update_production) | **PUT** `/api/2/productions/{id}` | 
[**update_share**](StorageApi.md#update_share) | **PUT** `/api/2/shares/{id}` | 
[**update_snapshot**](StorageApi.md#update_snapshot) | **PUT** `/api/2/snapshots/{id}` | 
[**update_volume**](StorageApi.md#update_volume) | **PUT** `/api/2/volumes/{id}` | 
[**update_workspace**](StorageApi.md#update_workspace) | **PUT** `/api/2/workspaces/{id}` | 
[**update_workspace_permission**](StorageApi.md#update_workspace_permission) | **PUT** `/api/2/workspace-permissions/{id}` | 



***

# **apply_workspace_affinity**

    def apply_workspace_affinity(id) -> object 



### Required permissions    * User account permission: projects:manage 

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
        api_response = api_instance.apply_workspace_affinity(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->apply_workspace_affinity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **bookmark_workspace**

    def bookmark_workspace(id) -> object 



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
        api_response = api_instance.bookmark_workspace(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->bookmark_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **check_in_into_workspace**

    def check_in_into_workspace(id, data) -> object 



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
data = elements_sdk.WorkspaceCheckIn() # WorkspaceCheckIn | 

    try:
        api_response = api_instance.check_in_into_workspace(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->check_in_into_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **data** | [**WorkspaceCheckIn**](WorkspaceCheckIn.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **check_out_of_workspace**

    def check_out_of_workspace(id) -> object 



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
        api_response = api_instance.check_out_of_workspace(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->check_out_of_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_production**

    def create_production(data) -> Production 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
    data = elements_sdk.Production() # Production | 

    try:
        api_response = api_instance.create_production(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Production**](Production.md)|  | 

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_share**

    def create_share(data) -> Share 



### Required permissions    * User account permission: shares:view (read) / shares:manage (write) 

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
    data = elements_sdk.Share() # Share | 

    try:
        api_response = api_instance.create_share(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Share**](Share.md)|  | 

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_snapshot**

    def create_snapshot(data) -> Snapshot 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
    data = elements_sdk.Snapshot() # Snapshot | 

    try:
        api_response = api_instance.create_snapshot(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Snapshot**](Snapshot.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_workspace**

    def create_workspace(data) -> Workspace 



### Required permissions    * User account permission: None (read) / projects:manage (write) 

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
    data = elements_sdk.Workspace() # Workspace | 

    try:
        api_response = api_instance.create_workspace(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Workspace**](Workspace.md)|  | 

### Return type

[**Workspace**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_workspace_permission**

    def create_workspace_permission(data) -> WorkspacePermission 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
    data = elements_sdk.WorkspacePermission() # WorkspacePermission | 

    try:
        api_response = api_instance.create_workspace_permission(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WorkspacePermission**](WorkspacePermission.md)|  | 

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_production**

    def delete_production(id) -> object 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
        api_response = api_instance.delete_production(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_share**

    def delete_share(id) -> object 



### Required permissions    * User account permission: shares:view (read) / shares:manage (write) 

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
        api_response = api_instance.delete_share(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_snapshot**

    def delete_snapshot(id) -> object 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
        api_response = api_instance.delete_snapshot(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_workspace**

    def delete_workspace(id) -> object 



### Required permissions    * User account permission: None (read) / projects:manage (write) 

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
        api_response = api_instance.delete_workspace(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_workspace_permission**

    def delete_workspace_permission(id) -> object 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
        api_response = api_instance.delete_workspace_permission(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_deleted_workspaces**

    def get_all_deleted_workspaces(ordering=ordering, limit=limit, offset=offset) -> list[DeletedWorkspace] 



### Required permissions    * User account permission: projects:view 

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
        api_response = api_instance.get_all_deleted_workspaces(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_deleted_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[DeletedWorkspace]**](DeletedWorkspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_productions**

    def get_all_productions(active=active, name=name, ordering=ordering, limit=limit, offset=offset) -> list[Production] 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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

    try:
        api_response = api_instance.get_all_productions(active=active, name=name, ordering=ordering, limit=limit, offset=offset)
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

### Return type

[**list[Production]**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_shares**

    def get_all_shares(ordering=ordering, limit=limit, offset=offset) -> list[Share] 



### Required permissions    * User account permission: shares:view (read) / shares:manage (write) 

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



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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

    def get_all_volumes(is_default=is_default, type=type, use_for_homes=use_for_homes, use_for_workspaces=use_for_workspaces, ordering=ordering, limit=limit, offset=offset) -> list[Volume] 



### Required permissions    * User account permission: None (read) / system:admin-access (write) 

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
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_volumes(is_default=is_default, type=type, use_for_homes=use_for_homes, use_for_workspaces=use_for_workspaces, ordering=ordering, limit=limit, offset=offset)
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
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Volume]**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_workspace_permissions**

    def get_all_workspace_permissions(workspace=workspace, user=user, group=group, ordering=ordering, limit=limit, offset=offset) -> list[WorkspacePermission] 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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

    def get_all_workspaces(ordering=ordering, limit=limit, offset=offset, resolve_access_for=resolve_access_for, include_endpoints=include_endpoints, include_quotas=include_quotas) -> list[Workspace] 



### Required permissions    * User account permission: None (read) / projects:manage (write) 

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
resolve_access_for = 56 # int |  (optional)
include_endpoints = True # bool |  (optional)
include_quotas = True # bool |  (optional)

    try:
        api_response = api_instance.get_all_workspaces(ordering=ordering, limit=limit, offset=offset, resolve_access_for=resolve_access_for, include_endpoints=include_endpoints, include_quotas=include_quotas)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_all_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_my_workspaces**

    def get_my_workspaces(ordering=ordering, limit=limit, offset=offset) -> list[Workspace] 



### Required permissions    * User account permission: None (read) / projects:manage (write) 

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
        api_response = api_instance.get_my_workspaces(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_my_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Workspace]**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_production**

    def get_production(id) -> Production 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
        api_response = api_instance.get_production(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. | 

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_share**

    def get_share(id) -> Share 



### Required permissions    * User account permission: shares:view (read) / shares:manage (write) 

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



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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

# **get_volume**

    def get_volume(id) -> Volume 



### Required permissions    * User account permission: None (read) / system:admin-access (write) 

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
        api_response = api_instance.get_volume(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 

### Return type

[**Volume**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_volume_active_connections**

    def get_volume_active_connections(id) -> StorNextConnections 



### Required permissions    * User account permission: system:status:view 

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



### Required permissions    * User account permission: system:status:view 

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



### Required permissions    * User account permission: system:status:view 

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

    def get_workspace(id) -> Workspace 



### Required permissions    * User account permission: None (read) / projects:manage (write) 

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

[**Workspace**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_workspace_permission**

    def get_workspace_permission(id) -> WorkspacePermission 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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

# **move_workspace_to_production**

    def move_workspace_to_production(id, data) -> object 



### Required permissions    * User account permission: projects:manage 

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
data = elements_sdk.WorkspaceMoveToRequest() # WorkspaceMoveToRequest | 

    try:
        api_response = api_instance.move_workspace_to_production(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->move_workspace_to_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **data** | [**WorkspaceMoveToRequest**](WorkspaceMoveToRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_production**

    def patch_production(id, data) -> Production 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
data = elements_sdk.Production() # Production | 

    try:
        api_response = api_instance.patch_production(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. | 
 **data** | [**Production**](Production.md)|  | 

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_share**

    def patch_share(id, data) -> Share 



### Required permissions    * User account permission: shares:view (read) / shares:manage (write) 

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
data = elements_sdk.Share() # Share | 

    try:
        api_response = api_instance.patch_share(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. | 
 **data** | [**Share**](Share.md)|  | 

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_snapshot**

    def patch_snapshot(id, data) -> Snapshot 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
data = elements_sdk.Snapshot() # Snapshot | 

    try:
        api_response = api_instance.patch_snapshot(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. | 
 **data** | [**Snapshot**](Snapshot.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_volume**

    def patch_volume(id, data) -> Volume 



### Required permissions    * User account permission: None (read) / system:admin-access (write) 

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
data = elements_sdk.Volume() # Volume | 

    try:
        api_response = api_instance.patch_volume(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **data** | [**Volume**](Volume.md)|  | 

### Return type

[**Volume**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_workspace**

    def patch_workspace(id, data) -> Workspace 



### Required permissions    * User account permission: None (read) / projects:manage (write) 

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
data = elements_sdk.Workspace() # Workspace | 

    try:
        api_response = api_instance.patch_workspace(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **data** | [**Workspace**](Workspace.md)|  | 

### Return type

[**Workspace**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_workspace_permission**

    def patch_workspace_permission(id, data) -> WorkspacePermission 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
data = elements_sdk.WorkspacePermission() # WorkspacePermission | 

    try:
        api_response = api_instance.patch_workspace_permission(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->patch_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. | 
 **data** | [**WorkspacePermission**](WorkspacePermission.md)|  | 

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **repair_workspace_permissions**

    def repair_workspace_permissions(id) -> object 



### Required permissions    * User account permission: projects:manage 

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

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **unbookmark_workspace**

    def unbookmark_workspace(id) -> object 



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
        api_response = api_instance.unbookmark_workspace(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->unbookmark_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_production**

    def update_production(id, data) -> Production 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
data = elements_sdk.Production() # Production | 

    try:
        api_response = api_instance.update_production(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_production: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this production. | 
 **data** | [**Production**](Production.md)|  | 

### Return type

[**Production**](Production.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_share**

    def update_share(id, data) -> Share 



### Required permissions    * User account permission: shares:view (read) / shares:manage (write) 

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
data = elements_sdk.Share() # Share | 

    try:
        api_response = api_instance.update_share(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this share. | 
 **data** | [**Share**](Share.md)|  | 

### Return type

[**Share**](Share.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_snapshot**

    def update_snapshot(id, data) -> Snapshot 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
data = elements_sdk.Snapshot() # Snapshot | 

    try:
        api_response = api_instance.update_snapshot(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this snapshot. | 
 **data** | [**Snapshot**](Snapshot.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_volume**

    def update_volume(id, data) -> Volume 



### Required permissions    * User account permission: None (read) / system:admin-access (write) 

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
data = elements_sdk.Volume() # Volume | 

    try:
        api_response = api_instance.update_volume(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_volume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this volume. | 
 **data** | [**Volume**](Volume.md)|  | 

### Return type

[**Volume**](Volume.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_workspace**

    def update_workspace(id, data) -> Workspace 



### Required permissions    * User account permission: None (read) / projects:manage (write) 

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
data = elements_sdk.Workspace() # Workspace | 

    try:
        api_response = api_instance.update_workspace(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace. | 
 **data** | [**Workspace**](Workspace.md)|  | 

### Return type

[**Workspace**](Workspace.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_workspace_permission**

    def update_workspace_permission(id, data) -> WorkspacePermission 



### Required permissions    * User account permission: projects:view (read) / projects:manage (write) 

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
data = elements_sdk.WorkspacePermission() # WorkspacePermission | 

    try:
        api_response = api_instance.update_workspace_permission(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_workspace_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workspace permission. | 
 **data** | [**WorkspacePermission**](WorkspacePermission.md)|  | 

### Return type

[**WorkspacePermission**](WorkspacePermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

