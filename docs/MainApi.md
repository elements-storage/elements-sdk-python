# elements_sdk.MainApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_configuration**](MainApi.md#apply_configuration) | **POST** `/api/2/configuration/apply` | 
[**check_chunk_uploaded**](MainApi.md#check_chunk_uploaded) | **GET** `/api/2/uploads/chunk` | 
[**check_stor_next_license**](MainApi.md#check_stor_next_license) | **POST** `/api/2/stornext-license/check` | 
[**create_group**](MainApi.md#create_group) | **POST** `/api/2/groups` | 
[**create_home_workspace**](MainApi.md#create_home_workspace) | **POST** `/api/2/users/{id}/home` | 
[**create_user**](MainApi.md#create_user) | **POST** `/api/2/users` | 
[**create_workstation**](MainApi.md#create_workstation) | **POST** `/api/2/workstations` | 
[**delete_group**](MainApi.md#delete_group) | **DELETE** `/api/2/groups/{id}` | 
[**delete_home_workspace**](MainApi.md#delete_home_workspace) | **DELETE** `/api/2/users/{id}/home` | 
[**delete_user**](MainApi.md#delete_user) | **DELETE** `/api/2/users/{id}` | 
[**delete_workstation**](MainApi.md#delete_workstation) | **DELETE** `/api/2/workstations/{id}` | 
[**disable_user_totp**](MainApi.md#disable_user_totp) | **DELETE** `/api/2/users/{id}/totp` | 
[**enable_user_totp**](MainApi.md#enable_user_totp) | **POST** `/api/2/users/{id}/totp` | 
[**finish_upload**](MainApi.md#finish_upload) | **POST** `/api/2/uploads/finish` | 
[**fix_ldap_group_memberships**](MainApi.md#fix_ldap_group_memberships) | **POST** `/api/2/ldap-servers/{id}/fix-memberships` | 
[**get_all_downloads**](MainApi.md#get_all_downloads) | **GET** `/api/2/downloads` | 
[**get_all_groups**](MainApi.md#get_all_groups) | **GET** `/api/2/groups` | 
[**get_all_ldap_servers**](MainApi.md#get_all_ldap_servers) | **GET** `/api/2/ldap-servers` | 
[**get_all_storage_nodes**](MainApi.md#get_all_storage_nodes) | **GET** `/api/2/nodes` | 
[**get_all_users**](MainApi.md#get_all_users) | **GET** `/api/2/users` | 
[**get_all_workstations**](MainApi.md#get_all_workstations) | **GET** `/api/2/workstations` | 
[**get_client_download_file**](MainApi.md#get_client_download_file) | **GET** `/api/2/downloads/clients/{file}` | 
[**get_client_downloads**](MainApi.md#get_client_downloads) | **GET** `/api/2/downloads/clients` | 
[**get_current_workstation**](MainApi.md#get_current_workstation) | **GET** `/api/2/workstations/current` | 
[**get_download**](MainApi.md#get_download) | **GET** `/api/2/downloads/{id}` | 
[**get_download_file**](MainApi.md#get_download_file) | **GET** `/api/2/downloads/{id}/download` | 
[**get_download_icon**](MainApi.md#get_download_icon) | **GET** `/api/2/downloads/{id}/icon` | 
[**get_group**](MainApi.md#get_group) | **GET** `/api/2/groups/{id}` | 
[**get_home_workspace**](MainApi.md#get_home_workspace) | **GET** `/api/2/users/{id}/home` | 
[**get_ldap_server**](MainApi.md#get_ldap_server) | **GET** `/api/2/ldap-servers/{id}` | 
[**get_ldap_server_groups**](MainApi.md#get_ldap_server_groups) | **GET** `/api/2/ldap-servers/{id}/groups` | 
[**get_ldap_server_users**](MainApi.md#get_ldap_server_users) | **GET** `/api/2/ldap-servers/{id}/users` | 
[**get_node_ipmi_sensors**](MainApi.md#get_node_ipmi_sensors) | **GET** `/api/2/nodes/{id}/sensors` | 
[**get_node_stats**](MainApi.md#get_node_stats) | **GET** `/api/2/nodes/{id}/stats` | 
[**get_parameters**](MainApi.md#get_parameters) | **GET** `/api/2/parameters` | 
[**get_profile**](MainApi.md#get_profile) | **GET** `/api/2/users/me` | 
[**get_release_notes**](MainApi.md#get_release_notes) | **GET** `/api/2/release-notes` | 
[**get_stor_next_license**](MainApi.md#get_stor_next_license) | **GET** `/api/2/stornext-license` | 
[**get_storage_node**](MainApi.md#get_storage_node) | **GET** `/api/2/nodes/{id}` | 
[**get_system_info**](MainApi.md#get_system_info) | **GET** `/api/2/system/info` | 
[**get_user**](MainApi.md#get_user) | **GET** `/api/2/users/{id}` | 
[**get_workstation**](MainApi.md#get_workstation) | **GET** `/api/2/workstations/{id}` | 
[**install_stor_next_license**](MainApi.md#install_stor_next_license) | **POST** `/api/2/stornext-license` | 
[**patch_current_workstation**](MainApi.md#patch_current_workstation) | **PATCH** `/api/2/workstations/current` | 
[**patch_group**](MainApi.md#patch_group) | **PATCH** `/api/2/groups/{id}` | 
[**patch_user**](MainApi.md#patch_user) | **PATCH** `/api/2/users/{id}` | 
[**patch_workstation**](MainApi.md#patch_workstation) | **PATCH** `/api/2/workstations/{id}` | 
[**preview_user**](MainApi.md#preview_user) | **POST** `/api/2/users/preview` | 
[**register_upload**](MainApi.md#register_upload) | **POST** `/api/2/uploads/register` | 
[**reset_user_password**](MainApi.md#reset_user_password) | **POST** `/api/2/users/{id}/password/reset` | 
[**set_my_password**](MainApi.md#set_my_password) | **POST** `/api/2/users/me/password` | 
[**set_user_password**](MainApi.md#set_user_password) | **POST** `/api/2/users/{id}/password` | 
[**sync_ldap_group**](MainApi.md#sync_ldap_group) | **POST** `/api/2/groups/{id}/ldap-sync` | 
[**sync_ldap_users**](MainApi.md#sync_ldap_users) | **POST** `/api/2/ldap-servers/{id}/sync-users` | 
[**sync_user_totp**](MainApi.md#sync_user_totp) | **PUT** `/api/2/users/{id}/totp` | 
[**update_current_workstation**](MainApi.md#update_current_workstation) | **PUT** `/api/2/workstations/current` | 
[**update_group**](MainApi.md#update_group) | **PUT** `/api/2/groups/{id}` | 
[**update_parameters**](MainApi.md#update_parameters) | **PUT** `/api/2/parameters` | 
[**update_profile**](MainApi.md#update_profile) | **PUT** `/api/2/users/me` | 
[**update_user**](MainApi.md#update_user) | **PUT** `/api/2/users/{id}` | 
[**update_workstation**](MainApi.md#update_workstation) | **PUT** `/api/2/workstations/{id}` | 
[**upload_chunk**](MainApi.md#upload_chunk) | **POST** `/api/2/uploads/chunk` | 



***

# **apply_configuration**
> object apply_configuration()



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

configuration.host = "https://elements.local"

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

# **check_chunk_uploaded**
> object check_chunk_uploaded(upload_id=upload_id, chunk_number=chunk_number)



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

# **check_stor_next_license**
> list[StorNextLicenseCheckEndpointResponse] check_stor_next_license(data)



### Required permissions    * User account permission: maintenance:view   * License component: stornext_mdc 

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

# **create_group**
> ElementsGroupDetail create_group(data)



### Required permissions    * User account permission: users:view (read) / users:manage (write) 

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
> Workspace create_home_workspace(id, data)



### Required permissions    * User account permission: users:manage 

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

# **create_user**
> ElementsUserDetail create_user(data)



### Required permissions    * User account permission: None (read) / users:manage (write) 

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
> Workstation create_workstation(data)



### Required permissions    * Authenticated user   * <apps.main.api.workstation.AuthorizedWorkstation object at 0x7fe4489ef3c8> 

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

# **delete_group**
> object delete_group(id)



### Required permissions    * User account permission: users:view (read) / users:manage (write) 

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
> object delete_home_workspace(id)



### Required permissions    * User account permission: users:manage 

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

# **delete_user**
> object delete_user(id)



### Required permissions    * User account permission: None (read) / users:manage (write) 

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
> object delete_workstation(id)



### Required permissions    * Authenticated user   * <apps.main.api.workstation.AuthorizedWorkstation object at 0x7fe4489ef3c8> 

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
> object disable_user_totp(id)



### Required permissions    * User account permission: users:manage 

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
> object enable_user_totp(id, data)



### Required permissions    * User account permission: users:manage 

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
> object finish_upload(data)



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
> object fix_ldap_group_memberships(id)



### Required permissions    * User account permission: users:manage 

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

# **get_all_downloads**
> list[Download] get_all_downloads(ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: downloads:view 

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
> list[ElementsGroup] get_all_groups(ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: users:view (read) / users:manage (write) 

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
> list[LDAPServer] get_all_ldap_servers(ordering=ordering, limit=limit, offset=offset)



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

# **get_all_storage_nodes**
> list[StorageNode] get_all_storage_nodes(ordering=ordering, limit=limit, offset=offset)



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
    api_instance = elements_sdk.MainApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_storage_nodes(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_all_storage_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[StorageNode]**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_users**
> list[ElementsUser] get_all_users(username=username, home=home, ordering=ordering, limit=limit, offset=offset, include_allowed_fs_paths=include_allowed_fs_paths, include_client_sessions=include_client_sessions)



### Required permissions    * User account permission: None (read) / users:manage (write) 

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
> list[Workstation] get_all_workstations(ordering=ordering, limit=limit, offset=offset)



### Required permissions    * Authenticated user   * <apps.main.api.workstation.AuthorizedWorkstation object at 0x7fe4489ef3c8> 

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
> object get_client_download_file(file)



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

configuration.host = "https://elements.local"

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
> list[ClientsEndpointResponse] get_client_downloads()



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

configuration.host = "https://elements.local"

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
> Workstation get_current_workstation()



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
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_current_workstation()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_current_workstation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_download**
> Download get_download(id)



### Required permissions    * User account permission: downloads:view 

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

# **get_download_file**
> object get_download_file(id)



### Required permissions    * User account permission: downloads:view 

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
> object get_download_icon(id)



### Required permissions    * User account permission: downloads:view 

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
> ElementsGroupDetail get_group(id)



### Required permissions    * User account permission: users:view (read) / users:manage (write) 

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
> Workspace get_home_workspace(id)



### Required permissions    * User account permission: users:manage 

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

# **get_ldap_server**
> LDAPServer get_ldap_server(id)



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
> LDAPServerGroups get_ldap_server_groups(id)



### Required permissions    * User account permission: users:manage 

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
> LDAPServerUsers get_ldap_server_users(id)



### Required permissions    * User account permission: users:manage 

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

# **get_node_ipmi_sensors**
> Sensors get_node_ipmi_sensors(id)



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
> Stats get_node_stats(id)



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

# **get_parameters**
> Parameters get_parameters()



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

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_parameters()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_parameters: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**Parameters**](Parameters.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_profile**
> ElementsUserProfile get_profile()



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
    api_instance = elements_sdk.MainApi(api_client)
    
    try:
        api_response = api_instance.get_profile()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_profile: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**ElementsUserProfile**](ElementsUserProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_release_notes**
> list[ReleaseNotesEndpointResponse] get_release_notes()



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

# **get_stor_next_license**
> StorNextLicenseEndpointResponse get_stor_next_license()



### Required permissions    * User account permission: maintenance:view   * License component: stornext_mdc 

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
> StorageNode get_storage_node(id)



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
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Storage Node.

    try:
        api_response = api_instance.get_storage_node(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->get_storage_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Storage Node. | 

### Return type

[**StorageNode**](StorageNode.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_system_info**
> SystemInfoEndpointResponse get_system_info()



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

configuration.host = "https://elements.local"

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
> ElementsUserDetail get_user(id)



### Required permissions    * User account permission: None (read) / users:manage (write) 

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
> Workstation get_workstation(id)



### Required permissions    * Authenticated user   * <apps.main.api.workstation.AuthorizedWorkstation object at 0x7fe4489ef3c8> 

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
> StorNextLicenseEndpointResponse install_stor_next_license(data)



### Required permissions    * User account permission: maintenance:view   * License component: stornext_mdc 

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
> Workstation patch_current_workstation(data)



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
    api_instance = elements_sdk.MainApi(api_client)
    data = elements_sdk.Workstation() # Workstation | 

    try:
        api_response = api_instance.patch_current_workstation(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MainApi->patch_current_workstation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Workstation**](Workstation.md)|  | 

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_group**
> ElementsGroupDetail patch_group(id, data)



### Required permissions    * User account permission: users:view (read) / users:manage (write) 

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
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this Group.
data = elements_sdk.ElementsGroupDetail() # ElementsGroupDetail | 

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
 **data** | [**ElementsGroupDetail**](ElementsGroupDetail.md)|  | 

### Return type

[**ElementsGroupDetail**](ElementsGroupDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_user**
> ElementsUserDetail patch_user(id, data)



### Required permissions    * User account permission: None (read) / users:manage (write) 

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
    api_instance = elements_sdk.MainApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
data = elements_sdk.ElementsUserDetail() # ElementsUserDetail | 

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
 **data** | [**ElementsUserDetail**](ElementsUserDetail.md)|  | 

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_workstation**
> Workstation patch_workstation(id, data)



### Required permissions    * Authenticated user   * <apps.main.api.workstation.AuthorizedWorkstation object at 0x7fe4489ef3c8> 

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
    api_instance = elements_sdk.MainApi(api_client)
    id = 'id_example' # str | A unique value identifying this workstation.
data = elements_sdk.Workstation() # Workstation | 

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
 **data** | [**Workstation**](Workstation.md)|  | 

### Return type

[**Workstation**](Workstation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **preview_user**
> UserPreviewResponse preview_user(data)



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

# **register_upload**
> object register_upload(data)



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

# **reset_user_password**
> object reset_user_password(id, data)



### Required permissions    * User account permission: users:manage 

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

# **set_my_password**
> object set_my_password(data)



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
> object set_user_password(id, data)



### Required permissions    * User account permission: users:manage 

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

# **sync_ldap_group**
> object sync_ldap_group(id)



### Required permissions    * User account permission: users:manage 

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
> object sync_ldap_users(id)



### Required permissions    * User account permission: users:manage 

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

# **sync_user_totp**
> SyncTOTP sync_user_totp(id, data)



### Required permissions    * User account permission: users:manage 

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

# **update_current_workstation**
> Workstation update_current_workstation(data)



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

# **update_group**
> ElementsGroupDetail update_group(id, data)



### Required permissions    * User account permission: users:view (read) / users:manage (write) 

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

# **update_parameters**
> Parameters update_parameters(data)



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

configuration.host = "https://elements.local"

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
> ElementsUserProfile update_profile(data)



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

# **update_user**
> ElementsUserDetail update_user(id, data)



### Required permissions    * User account permission: None (read) / users:manage (write) 

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
> Workstation update_workstation(id, data)



### Required permissions    * Authenticated user   * <apps.main.api.workstation.AuthorizedWorkstation object at 0x7fe4489ef3c8> 

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
> object upload_chunk(data)



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

