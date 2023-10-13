# elements_sdk.TapeArchiveApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_to_tape**](TapeArchiveApi.md#archive_to_tape) | **POST** `/api/2/archive/tape/archive` | 
[**cancel_all_tape_archive_jobs**](TapeArchiveApi.md#cancel_all_tape_archive_jobs) | **POST** `/api/2/archive/tape/jobs/cancel-all` | 
[**cancel_tape_archive_job**](TapeArchiveApi.md#cancel_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/cancel` | 
[**check_tape**](TapeArchiveApi.md#check_tape) | **POST** `/api/2/archive/tape/library/check` | 
[**create_tape**](TapeArchiveApi.md#create_tape) | **POST** `/api/2/archive/tape/tapes` | 
[**create_tape_group**](TapeArchiveApi.md#create_tape_group) | **POST** `/api/2/archive/tape/groups` | 
[**delete_tape**](TapeArchiveApi.md#delete_tape) | **DELETE** `/api/2/archive/tape/tapes/{id}` | 
[**delete_tape_archive_job**](TapeArchiveApi.md#delete_tape_archive_job) | **DELETE** `/api/2/archive/tape/jobs/{id}` | 
[**delete_tape_group**](TapeArchiveApi.md#delete_tape_group) | **DELETE** `/api/2/archive/tape/groups/{id}` | 
[**format_tape**](TapeArchiveApi.md#format_tape) | **POST** `/api/2/archive/tape/library/format` | 
[**get_all_archived_file_entries**](TapeArchiveApi.md#get_all_archived_file_entries) | **GET** `/api/2/archive/tape/files` | 
[**get_all_tape_archive_jobs**](TapeArchiveApi.md#get_all_tape_archive_jobs) | **GET** `/api/2/archive/tape/jobs` | 
[**get_all_tape_groups**](TapeArchiveApi.md#get_all_tape_groups) | **GET** `/api/2/archive/tape/groups` | 
[**get_all_tapes**](TapeArchiveApi.md#get_all_tapes) | **GET** `/api/2/archive/tape/tapes` | 
[**get_archived_file_entry**](TapeArchiveApi.md#get_archived_file_entry) | **GET** `/api/2/archive/tape/files/{id}` | 
[**get_tape**](TapeArchiveApi.md#get_tape) | **GET** `/api/2/archive/tape/tapes/{id}` | 
[**get_tape_archive_job**](TapeArchiveApi.md#get_tape_archive_job) | **GET** `/api/2/archive/tape/jobs/{id}` | 
[**get_tape_archive_job_sources**](TapeArchiveApi.md#get_tape_archive_job_sources) | **GET** `/api/2/archive/tape/jobs/{id}/sources` | 
[**get_tape_group**](TapeArchiveApi.md#get_tape_group) | **GET** `/api/2/archive/tape/groups/{id}` | 
[**get_tape_library_state**](TapeArchiveApi.md#get_tape_library_state) | **GET** `/api/2/archive/tape/library` | 
[**load_tape**](TapeArchiveApi.md#load_tape) | **POST** `/api/2/archive/tape/library/load` | 
[**move_tape**](TapeArchiveApi.md#move_tape) | **POST** `/api/2/archive/tape/library/move` | 
[**patch_tape**](TapeArchiveApi.md#patch_tape) | **PATCH** `/api/2/archive/tape/tapes/{id}` | 
[**patch_tape_group**](TapeArchiveApi.md#patch_tape_group) | **PATCH** `/api/2/archive/tape/groups/{id}` | 
[**pause_tape_archive_job**](TapeArchiveApi.md#pause_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/pause` | 
[**refresh_tape_library_state**](TapeArchiveApi.md#refresh_tape_library_state) | **POST** `/api/2/archive/tape/library/refresh` | 
[**reindex_tape**](TapeArchiveApi.md#reindex_tape) | **POST** `/api/2/archive/tape/library/reindex` | 
[**remove_finished_tape_archive_jobs**](TapeArchiveApi.md#remove_finished_tape_archive_jobs) | **POST** `/api/2/archive/tape/jobs/remove-finished` | 
[**restart_tape_archive_job**](TapeArchiveApi.md#restart_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/restart` | 
[**restore_from_tape**](TapeArchiveApi.md#restore_from_tape) | **POST** `/api/2/archive/tape/restore` | 
[**resume_tape_archive_job**](TapeArchiveApi.md#resume_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/resume` | 
[**search_tape_archive**](TapeArchiveApi.md#search_tape_archive) | **POST** `/api/2/archive/tape/search` | 
[**unload_tape**](TapeArchiveApi.md#unload_tape) | **POST** `/api/2/archive/tape/library/unload` | 
[**update_tape**](TapeArchiveApi.md#update_tape) | **PUT** `/api/2/archive/tape/tapes/{id}` | 
[**update_tape_group**](TapeArchiveApi.md#update_tape_group) | **PUT** `/api/2/archive/tape/groups/{id}` | 


# **archive_to_tape**
    def [TapeJob] archive_to_tape(archive_endpoint_request)



### Required permissions    * User account permission: `ltfs:backup`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.archive_endpoint_request import ArchiveEndpointRequest
from elements_sdk.model.tape_job import TapeJob
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    archive_endpoint_request = ArchiveEndpointRequest(
        source=[
            TapeJobSource(
                path="path_example",
                options={
                    "key": "key_example",
                },
                include="include_example",
            ),
        ],
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="name_example",
        group=1,
        group2=1,
        export=True,
        export2=True,
    ) # ArchiveEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.archive_to_tape(archive_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->archive_to_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_endpoint_request** | [**ArchiveEndpointRequest**](ArchiveEndpointRequest.md)|  |

### Return type

[**[TapeJob]**](TapeJob.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **cancel_all_tape_archive_jobs**
    def cancel_all_tape_archive_jobs()



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.cancel_all_tape_archive_jobs()
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->cancel_all_tape_archive_jobs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **cancel_tape_archive_job**
    def cancel_tape_archive_job(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.cancel_tape_archive_job(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->cancel_tape_archive_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **check_tape**
    def check_tape(tape_library_fsck_endpoint_request)



### Required permissions    * User account permission: `ltfs:manage`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_library_fsck_endpoint_request import TapeLibraryFsckEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    tape_library_fsck_endpoint_request = TapeLibraryFsckEndpointRequest(
        barcode="barcode_example",
    ) # TapeLibraryFsckEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.check_tape(tape_library_fsck_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->check_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_fsck_endpoint_request** | [**TapeLibraryFsckEndpointRequest**](TapeLibraryFsckEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_tape**
    def Tape create_tape(tape_update)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape import Tape
from elements_sdk.model.tape_update import TapeUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    tape_update = TapeUpdate(
        name="name_example",
        uuid="uuid_example",
        generation=-2147483648,
        custom_a="custom_a_example",
        custom_b="custom_b_example",
        custom_c="custom_c_example",
        custom_d="custom_d_example",
        free_space=-9223372036854776000,
        load_counter=-9223372036854776000,
        error_counter=-9223372036854776000,
        error_reason="error_reason_example",
        active=True,
        lto="5",
        group=1,
    ) # TapeUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_tape(tape_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->create_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_update** | [**TapeUpdate**](TapeUpdate.md)|  |

### Return type

[**Tape**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_tape_group**
    def TapeGroup create_tape_group(tape_group_update)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_group_update import TapeGroupUpdate
from elements_sdk.model.tape_group import TapeGroup
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    tape_group_update = TapeGroupUpdate(
        tapes=[
            TapeMiniReference(
                id=1,
            ),
        ],
        name="name_example",
    ) # TapeGroupUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_tape_group(tape_group_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->create_tape_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_group_update** | [**TapeGroupUpdate**](TapeGroupUpdate.md)|  |

### Return type

[**TapeGroup**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_tape**
    def delete_tape(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this tape.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tape(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->delete_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_tape_archive_job**
    def delete_tape_archive_job(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tape_archive_job(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->delete_tape_archive_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_tape_group**
    def delete_tape_group(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this tape group.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tape_group(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->delete_tape_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape group. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **format_tape**
    def format_tape(tape_library_format_endpoint_request)



### Required permissions    * User account permission: `ltfs:manage`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_library_format_endpoint_request import TapeLibraryFormatEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    tape_library_format_endpoint_request = TapeLibraryFormatEndpointRequest(
        barcode="barcode_example",
    ) # TapeLibraryFormatEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.format_tape(tape_library_format_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->format_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_format_endpoint_request** | [**TapeLibraryFormatEndpointRequest**](TapeLibraryFormatEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_archived_file_entries**
    def [TapeFile] get_all_archived_file_entries()



### Required permissions    * User account permission: `ltfs:search` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_file import TapeFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 3.14 # float | Filter the returned list by `id`. (optional)
    is_dir = "is_dir_example" # str | Filter the returned list by `is_dir`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    fullpath = "fullpath_example" # str | Filter the returned list by `fullpath`. (optional)
    parent = 1 # int | Filter the returned list by `parent`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_archived_file_entries(id=id, is_dir=is_dir, name=name, fullpath=fullpath, parent=parent, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_all_archived_file_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **fullpath** | **str**| Filter the returned list by &#x60;fullpath&#x60;. | [optional]
 **parent** | **int**| Filter the returned list by &#x60;parent&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[TapeFile]**](TapeFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_tape_archive_jobs**
    def [TapeJob] get_all_tape_archive_jobs()



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_job import TapeJob
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_tape_archive_jobs(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_all_tape_archive_jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[TapeJob]**](TapeJob.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_tape_groups**
    def [TapeGroup] get_all_tape_groups()



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_group import TapeGroup
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 3.14 # float | Filter the returned list by `id`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_tape_groups(id=id, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_all_tape_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[TapeGroup]**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_tapes**
    def [Tape] get_all_tapes()



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape import Tape
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 3.14 # float | Filter the returned list by `id`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    group = 1 # int | Filter the returned list by `group`. (optional)
    group__isnull = "group__isnull_example" # str | Filter the returned list by `group__isnull`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_tapes(id=id, name=name, group=group, group__isnull=group__isnull, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_all_tapes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **group** | **int**| Filter the returned list by &#x60;group&#x60;. | [optional]
 **group__isnull** | **str**| Filter the returned list by &#x60;group__isnull&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Tape]**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_archived_file_entry**
    def TapeFile get_archived_file_entry(id)



### Required permissions    * User account permission: `ltfs:search` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_file import TapeFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this Archived file entry.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_archived_file_entry(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_archived_file_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Archived file entry. |

### Return type

[**TapeFile**](TapeFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_tape**
    def Tape get_tape(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape import Tape
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this tape.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tape(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape. |

### Return type

[**Tape**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_tape_archive_job**
    def TapeJob get_tape_archive_job(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_job import TapeJob
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tape_archive_job(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_tape_archive_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**TapeJob**](TapeJob.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_tape_archive_job_sources**
    def [TapeJobSource] get_tape_archive_job_sources(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_job_source import TapeJobSource
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tape_archive_job_sources(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_tape_archive_job_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[TapeJobSource]**](TapeJobSource.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_tape_group**
    def TapeGroup get_tape_group(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_group import TapeGroup
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this tape group.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tape_group(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_tape_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape group. |

### Return type

[**TapeGroup**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_tape_library_state**
    def TapeLibraryEndpointResponse get_tape_library_state()



### Required permissions    * User account permission: `ltfs:manage`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_library_endpoint_response import TapeLibraryEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_tape_library_state()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->get_tape_library_state: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TapeLibraryEndpointResponse**](TapeLibraryEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **load_tape**
    def load_tape(tape_library_load_endpoint_request)



### Required permissions    * User account permission: `ltfs:manage`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_library_load_endpoint_request import TapeLibraryLoadEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    tape_library_load_endpoint_request = TapeLibraryLoadEndpointRequest(
        barcode="barcode_example",
    ) # TapeLibraryLoadEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.load_tape(tape_library_load_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->load_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_load_endpoint_request** | [**TapeLibraryLoadEndpointRequest**](TapeLibraryLoadEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **move_tape**
    def move_tape(tape_library_move_endpoint_request)



### Required permissions    * User account permission: `ltfs:manage`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_library_move_endpoint_request import TapeLibraryMoveEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    tape_library_move_endpoint_request = TapeLibraryMoveEndpointRequest(
        barcode="barcode_example",
        slot=1,
    ) # TapeLibraryMoveEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.move_tape(tape_library_move_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->move_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_move_endpoint_request** | [**TapeLibraryMoveEndpointRequest**](TapeLibraryMoveEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_tape**
    def Tape patch_tape(id, tape_partial_update)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape import Tape
from elements_sdk.model.tape_partial_update import TapePartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this tape.
    tape_partial_update = TapePartialUpdate(
        name="name_example",
        uuid="uuid_example",
        generation=-2147483648,
        custom_a="custom_a_example",
        custom_b="custom_b_example",
        custom_c="custom_c_example",
        custom_d="custom_d_example",
        free_space=-9223372036854776000,
        load_counter=-9223372036854776000,
        error_counter=-9223372036854776000,
        error_reason="error_reason_example",
        active=True,
        lto="5",
        group=1,
    ) # TapePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_tape(id, tape_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->patch_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape. |
 **tape_partial_update** | [**TapePartialUpdate**](TapePartialUpdate.md)|  |

### Return type

[**Tape**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_tape_group**
    def TapeGroup patch_tape_group(id, tape_group_partial_update)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_group import TapeGroup
from elements_sdk.model.tape_group_partial_update import TapeGroupPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this tape group.
    tape_group_partial_update = TapeGroupPartialUpdate(
        tapes=[
            TapeMiniReference(
                id=1,
            ),
        ],
        name="name_example",
    ) # TapeGroupPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_tape_group(id, tape_group_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->patch_tape_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape group. |
 **tape_group_partial_update** | [**TapeGroupPartialUpdate**](TapeGroupPartialUpdate.md)|  |

### Return type

[**TapeGroup**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **pause_tape_archive_job**
    def pause_tape_archive_job(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.pause_tape_archive_job(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->pause_tape_archive_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **refresh_tape_library_state**
    def refresh_tape_library_state()



### Required permissions    * User account permission: `ltfs:manage`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.refresh_tape_library_state()
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->refresh_tape_library_state: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **reindex_tape**
    def reindex_tape(tape_library_reindex_endpoint_request)



### Required permissions    * User account permission: `ltfs:manage`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_library_reindex_endpoint_request import TapeLibraryReindexEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    tape_library_reindex_endpoint_request = TapeLibraryReindexEndpointRequest(
        barcode="barcode_example",
    ) # TapeLibraryReindexEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.reindex_tape(tape_library_reindex_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->reindex_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_reindex_endpoint_request** | [**TapeLibraryReindexEndpointRequest**](TapeLibraryReindexEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **remove_finished_tape_archive_jobs**
    def remove_finished_tape_archive_jobs()



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.remove_finished_tape_archive_jobs()
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->remove_finished_tape_archive_jobs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **restart_tape_archive_job**
    def restart_tape_archive_job(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.restart_tape_archive_job(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->restart_tape_archive_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **restore_from_tape**
    def TapeJob restore_from_tape(restore_endpoint_request)



### Required permissions    * User account permission: `ltfs:restore`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.restore_endpoint_request import RestoreEndpointRequest
from elements_sdk.model.tape_job import TapeJob
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    restore_endpoint_request = RestoreEndpointRequest(
        name="name_example",
        source=[
            TapeJobSource(
                path="path_example",
                options={
                    "key": "key_example",
                },
                include="include_example",
            ),
        ],
        exclude=[
            "exclude_example",
        ],
        tape="tape_example",
        destination="destination_example",
        export=True,
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # RestoreEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.restore_from_tape(restore_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->restore_from_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_endpoint_request** | [**RestoreEndpointRequest**](RestoreEndpointRequest.md)|  |

### Return type

[**TapeJob**](TapeJob.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **resume_tape_archive_job**
    def resume_tape_archive_job(id)



### Required permissions    * User account permission: `None` (read) / `ltfs:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.resume_tape_archive_job(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->resume_tape_archive_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **search_tape_archive**
    def SearchEndpointResponse search_tape_archive(search_endpoint_request)



### Required permissions    * User account permission: `ltfs:search`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.search_endpoint_request import SearchEndpointRequest
from elements_sdk.model.search_endpoint_response import SearchEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    search_endpoint_request = SearchEndpointRequest(
        query="query_example",
        exclude="exclude_example",
        offset=1,
        limit=1,
        dirs_only=True,
        names_only=True,
        tapes=True,
    ) # SearchEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_tape_archive(search_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->search_tape_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_endpoint_request** | [**SearchEndpointRequest**](SearchEndpointRequest.md)|  |

### Return type

[**SearchEndpointResponse**](SearchEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **unload_tape**
    def unload_tape(tape_library_unload_endpoint_request)



### Required permissions    * User account permission: `ltfs:manage`   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_library_unload_endpoint_request import TapeLibraryUnloadEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    tape_library_unload_endpoint_request = TapeLibraryUnloadEndpointRequest(
        barcode="barcode_example",
    ) # TapeLibraryUnloadEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.unload_tape(tape_library_unload_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->unload_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_unload_endpoint_request** | [**TapeLibraryUnloadEndpointRequest**](TapeLibraryUnloadEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_tape**
    def Tape update_tape(id, tape_update)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape import Tape
from elements_sdk.model.tape_update import TapeUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this tape.
    tape_update = TapeUpdate(
        name="name_example",
        uuid="uuid_example",
        generation=-2147483648,
        custom_a="custom_a_example",
        custom_b="custom_b_example",
        custom_c="custom_c_example",
        custom_d="custom_d_example",
        free_space=-9223372036854776000,
        load_counter=-9223372036854776000,
        error_counter=-9223372036854776000,
        error_reason="error_reason_example",
        active=True,
        lto="5",
        group=1,
    ) # TapeUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_tape(id, tape_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->update_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape. |
 **tape_update** | [**TapeUpdate**](TapeUpdate.md)|  |

### Return type

[**Tape**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_tape_group**
    def TapeGroup update_tape_group(id, tape_group_update)



### Required permissions    * User account permission: `None` (read) / `ltfs:tapegroups:manage` (write)   * License component: ltfs 

### Example


```python
import elements_sdk
from elements_sdk.api import tape_archive_api
from elements_sdk.model.tape_group_update import TapeGroupUpdate
from elements_sdk.model.tape_group import TapeGroup
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = tape_archive_api.TapeArchiveApi(api_client)
    id = 1 # int | A unique integer value identifying this tape group.
    tape_group_update = TapeGroupUpdate(
        tapes=[
            TapeMiniReference(
                id=1,
            ),
        ],
        name="name_example",
    ) # TapeGroupUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_tape_group(id, tape_group_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling TapeArchiveApi->update_tape_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape group. |
 **tape_group_update** | [**TapeGroupUpdate**](TapeGroupUpdate.md)|  |

### Return type

[**TapeGroup**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

