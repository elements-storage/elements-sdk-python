# elements_sdk.AutomationApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_task**](AutomationApi.md#abort_task) | **POST** `/api/2/tasks/{id}/abort` | 
[**create_job**](AutomationApi.md#create_job) | **POST** `/api/2/jobs` | 
[**create_schedule**](AutomationApi.md#create_schedule) | **POST** `/api/2/schedules` | 
[**create_subtask**](AutomationApi.md#create_subtask) | **POST** `/api/2/subtasks` | 
[**delete_finished_tasks**](AutomationApi.md#delete_finished_tasks) | **DELETE** `/api/2/tasks/finished` | 
[**delete_job**](AutomationApi.md#delete_job) | **DELETE** `/api/2/jobs/{id}` | 
[**delete_schedule**](AutomationApi.md#delete_schedule) | **DELETE** `/api/2/schedules/{id}` | 
[**delete_subtask**](AutomationApi.md#delete_subtask) | **DELETE** `/api/2/subtasks/{id}` | 
[**delete_task**](AutomationApi.md#delete_task) | **DELETE** `/api/2/tasks/{id}` | 
[**download_all_task_logs**](AutomationApi.md#download_all_task_logs) | **GET** `/api/2/tasks/logs/download` | 
[**download_task_log**](AutomationApi.md#download_task_log) | **GET** `/api/2/tasks/{id}/log/download` | 
[**export_job**](AutomationApi.md#export_job) | **GET** `/api/2/jobs/{id}/export` | 
[**get_all_events**](AutomationApi.md#get_all_events) | **GET** `/api/2/events` | 
[**get_all_jobs**](AutomationApi.md#get_all_jobs) | **GET** `/api/2/jobs` | 
[**get_all_schedules**](AutomationApi.md#get_all_schedules) | **GET** `/api/2/schedules` | 
[**get_all_subtasks**](AutomationApi.md#get_all_subtasks) | **GET** `/api/2/subtasks` | 
[**get_all_task_queues**](AutomationApi.md#get_all_task_queues) | **GET** `/api/2/tasks/queues` | 
[**get_all_task_types**](AutomationApi.md#get_all_task_types) | **GET** `/api/2/tasks/types` | 
[**get_all_tasks**](AutomationApi.md#get_all_tasks) | **GET** `/api/2/tasks` | 
[**get_event**](AutomationApi.md#get_event) | **GET** `/api/2/events/{id}` | 
[**get_finished_tasks**](AutomationApi.md#get_finished_tasks) | **GET** `/api/2/tasks/finished` | 
[**get_job**](AutomationApi.md#get_job) | **GET** `/api/2/jobs/{id}` | 
[**get_pending_tasks**](AutomationApi.md#get_pending_tasks) | **GET** `/api/2/tasks/pending` | 
[**get_python_environments**](AutomationApi.md#get_python_environments) | **GET** `/api/2/python/environments` | 
[**get_schedule**](AutomationApi.md#get_schedule) | **GET** `/api/2/schedules/{id}` | 
[**get_subtask**](AutomationApi.md#get_subtask) | **GET** `/api/2/subtasks/{id}` | 
[**get_task**](AutomationApi.md#get_task) | **GET** `/api/2/tasks/{id}` | 
[**get_task_log**](AutomationApi.md#get_task_log) | **GET** `/api/2/tasks/{id}/log` | 
[**get_task_type**](AutomationApi.md#get_task_type) | **GET** `/api/2/tasks/types/{type}` | 
[**get_tasks_summary**](AutomationApi.md#get_tasks_summary) | **GET** `/api/2/tasks/summary` | 
[**import_job**](AutomationApi.md#import_job) | **POST** `/api/2/jobs/import` | 
[**kill_all_pending_tasks**](AutomationApi.md#kill_all_pending_tasks) | **DELETE** `/api/2/tasks/pending` | 
[**kill_task**](AutomationApi.md#kill_task) | **POST** `/api/2/tasks/{id}/kill` | 
[**patch_job**](AutomationApi.md#patch_job) | **PATCH** `/api/2/jobs/{id}` | 
[**patch_schedule**](AutomationApi.md#patch_schedule) | **PATCH** `/api/2/schedules/{id}` | 
[**patch_subtask**](AutomationApi.md#patch_subtask) | **PATCH** `/api/2/subtasks/{id}` | 
[**restart_task**](AutomationApi.md#restart_task) | **POST** `/api/2/tasks/{id}/restart` | 
[**start_job**](AutomationApi.md#start_job) | **POST** `/api/2/jobs/{id}/start` | 
[**start_task**](AutomationApi.md#start_task) | **POST** `/api/2/tasks/start` | 
[**update_job**](AutomationApi.md#update_job) | **PUT** `/api/2/jobs/{id}` | 
[**update_schedule**](AutomationApi.md#update_schedule) | **PUT** `/api/2/schedules/{id}` | 
[**update_subtask**](AutomationApi.md#update_subtask) | **PUT** `/api/2/subtasks/{id}` | 



***

# **abort_task**

    def abort_task(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 'id_example' # str | A unique value identifying this task info.

    try:
        api_instance.abort_task(id)
    except ApiException as e:
        print("Exception when calling AutomationApi->abort_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_job**

    def create_job(job) -> Job 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    job = elements_sdk.Job() # Job | 

    try:
        api_response = api_instance.create_job(job)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->create_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | [**Job**](Job.md)|  | 

### Return type

[**Job**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_schedule**

    def create_schedule(schedule) -> Schedule 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    schedule = elements_sdk.Schedule() # Schedule | 

    try:
        api_response = api_instance.create_schedule(schedule)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->create_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)|  | 

### Return type

[**Schedule**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_subtask**

    def create_subtask(subtask) -> Subtask 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    subtask = elements_sdk.Subtask() # Subtask | 

    try:
        api_response = api_instance.create_subtask(subtask)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->create_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subtask** | [**Subtask**](Subtask.md)|  | 

### Return type

[**Subtask**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_finished_tasks**

    def delete_finished_tasks()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    
    try:
        api_instance.delete_finished_tasks()
    except ApiException as e:
        print("Exception when calling AutomationApi->delete_finished_tasks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_job**

    def delete_job(id)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this job.

    try:
        api_instance.delete_job(id)
    except ApiException as e:
        print("Exception when calling AutomationApi->delete_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_schedule**

    def delete_schedule(id)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this schedule.

    try:
        api_instance.delete_schedule(id)
    except ApiException as e:
        print("Exception when calling AutomationApi->delete_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this schedule. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_subtask**

    def delete_subtask(id)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this subtask.

    try:
        api_instance.delete_subtask(id)
    except ApiException as e:
        print("Exception when calling AutomationApi->delete_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subtask. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_task**

    def delete_task(id)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 'id_example' # str | A unique value identifying this task info.

    try:
        api_instance.delete_task(id)
    except ApiException as e:
        print("Exception when calling AutomationApi->delete_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **download_all_task_logs**

    def download_all_task_logs(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: `tasks:view` 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    job_instance = 'job_instance_example' # str | Filter the returned list by `job_instance`. (optional)
job_instance__in = 'job_instance__in_example' # str | Multiple values may be separated by commas. (optional)
subtask = 'subtask_example' # str | Filter the returned list by `subtask`. (optional)
state = 'state_example' # str | Filter the returned list by `state`. (optional)
state__in = 3.4 # float | Multiple values may be separated by commas. (optional)
id = 'id_example' # str | Filter the returned list by `id`. (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
task_name = 'task_name_example' # str | Filter the returned list by `task_name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_instance.download_all_task_logs(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
    except ApiException as e:
        print("Exception when calling AutomationApi->download_all_task_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional] 
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **subtask** | **str**| Filter the returned list by &#x60;subtask&#x60;. | [optional] 
 **state** | **str**| Filter the returned list by &#x60;state&#x60;. | [optional] 
 **state__in** | **float**| Multiple values may be separated by commas. | [optional] 
 **id** | **str**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **task_name** | **str**| Filter the returned list by &#x60;task_name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **download_task_log**

    def download_task_log(id)



### Required permissions    * User account permission: `tasks:view` 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 'id_example' # str | A unique value identifying this task info.

    try:
        api_instance.download_task_log(id)
    except ApiException as e:
        print("Exception when calling AutomationApi->download_task_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **export_job**

    def export_job(id)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this job.

    try:
        api_instance.export_job(id)
    except ApiException as e:
        print("Exception when calling AutomationApi->export_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_events**

    def get_all_events(ordering=ordering, limit=limit, offset=offset) -> InlineResponse2002 



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
    api_instance = elements_sdk.AutomationApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_events(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_all_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_jobs**

    def get_all_jobs(special_type=special_type, special_type__isnull=special_type__isnull, hook=hook, name=name, ordering=ordering, limit=limit, offset=offset) -> list[Job] 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    special_type = 'special_type_example' # str | Filter the returned list by `special_type`. (optional)
special_type__isnull = 'special_type__isnull_example' # str | Filter the returned list by `special_type__isnull`. (optional)
hook = 'hook_example' # str | Filter the returned list by `hook`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_jobs(special_type=special_type, special_type__isnull=special_type__isnull, hook=hook, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_all_jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **special_type** | **str**| Filter the returned list by &#x60;special_type&#x60;. | [optional] 
 **special_type__isnull** | **str**| Filter the returned list by &#x60;special_type__isnull&#x60;. | [optional] 
 **hook** | **str**| Filter the returned list by &#x60;hook&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Job]**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_schedules**

    def get_all_schedules(job=job, ordering=ordering, limit=limit, offset=offset) -> list[Schedule] 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    job = 'job_example' # str | Filter the returned list by `job`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_schedules(job=job, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_all_schedules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Filter the returned list by &#x60;job&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Schedule]**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_subtasks**

    def get_all_subtasks(parent=parent, ordering=ordering, limit=limit, offset=offset) -> list[Subtask] 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    parent = 'parent_example' # str | Filter the returned list by `parent`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_subtasks(parent=parent, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_all_subtasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Filter the returned list by &#x60;parent&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Subtask]**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_task_queues**

    def get_all_task_queues(ordering=ordering, limit=limit, offset=offset) -> InlineResponse2003 



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
    api_instance = elements_sdk.AutomationApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_task_queues(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_all_task_queues: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_task_types**

    def get_all_task_types(ordering=ordering, limit=limit, offset=offset) -> InlineResponse2004 



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
    api_instance = elements_sdk.AutomationApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_task_types(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_all_task_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_tasks**

    def get_all_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset) -> list[TaskInfo] 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    job_instance = 'job_instance_example' # str | Filter the returned list by `job_instance`. (optional)
job_instance__in = 'job_instance__in_example' # str | Multiple values may be separated by commas. (optional)
subtask = 'subtask_example' # str | Filter the returned list by `subtask`. (optional)
state = 'state_example' # str | Filter the returned list by `state`. (optional)
state__in = 3.4 # float | Multiple values may be separated by commas. (optional)
id = 'id_example' # str | Filter the returned list by `id`. (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
task_name = 'task_name_example' # str | Filter the returned list by `task_name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_all_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional] 
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **subtask** | **str**| Filter the returned list by &#x60;subtask&#x60;. | [optional] 
 **state** | **str**| Filter the returned list by &#x60;state&#x60;. | [optional] 
 **state__in** | **float**| Multiple values may be separated by commas. | [optional] 
 **id** | **str**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **task_name** | **str**| Filter the returned list by &#x60;task_name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_event**

    def get_event(id) -> Event 



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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_event(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Event**](Event.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_finished_tasks**

    def get_finished_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset) -> list[TaskInfo] 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    job_instance = 'job_instance_example' # str | Filter the returned list by `job_instance`. (optional)
job_instance__in = 'job_instance__in_example' # str | Multiple values may be separated by commas. (optional)
subtask = 'subtask_example' # str | Filter the returned list by `subtask`. (optional)
state = 'state_example' # str | Filter the returned list by `state`. (optional)
state__in = 3.4 # float | Multiple values may be separated by commas. (optional)
id = 'id_example' # str | Filter the returned list by `id`. (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
task_name = 'task_name_example' # str | Filter the returned list by `task_name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_finished_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_finished_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional] 
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **subtask** | **str**| Filter the returned list by &#x60;subtask&#x60;. | [optional] 
 **state** | **str**| Filter the returned list by &#x60;state&#x60;. | [optional] 
 **state__in** | **float**| Multiple values may be separated by commas. | [optional] 
 **id** | **str**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **task_name** | **str**| Filter the returned list by &#x60;task_name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_job**

    def get_job(id) -> Job 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this job.

    try:
        api_response = api_instance.get_job(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. | 

### Return type

[**Job**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_pending_tasks**

    def get_pending_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset) -> list[TaskInfo] 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    job_instance = 'job_instance_example' # str | Filter the returned list by `job_instance`. (optional)
job_instance__in = 'job_instance__in_example' # str | Multiple values may be separated by commas. (optional)
subtask = 'subtask_example' # str | Filter the returned list by `subtask`. (optional)
state = 'state_example' # str | Filter the returned list by `state`. (optional)
state__in = 3.4 # float | Multiple values may be separated by commas. (optional)
id = 'id_example' # str | Filter the returned list by `id`. (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
task_name = 'task_name_example' # str | Filter the returned list by `task_name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_pending_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_pending_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional] 
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **subtask** | **str**| Filter the returned list by &#x60;subtask&#x60;. | [optional] 
 **state** | **str**| Filter the returned list by &#x60;state&#x60;. | [optional] 
 **state__in** | **float**| Multiple values may be separated by commas. | [optional] 
 **id** | **str**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **task_name** | **str**| Filter the returned list by &#x60;task_name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_python_environments**

    def get_python_environments() -> list[PythonEnvironment] 



### Required permissions    * User account permission: `tasks:manage` 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    
    try:
        api_response = api_instance.get_python_environments()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_python_environments: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**list[PythonEnvironment]**](PythonEnvironment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_schedule**

    def get_schedule(id) -> Schedule 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this schedule.

    try:
        api_response = api_instance.get_schedule(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this schedule. | 

### Return type

[**Schedule**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_subtask**

    def get_subtask(id) -> Subtask 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this subtask.

    try:
        api_response = api_instance.get_subtask(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subtask. | 

### Return type

[**Subtask**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_task**

    def get_task(id) -> TaskInfo 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 'id_example' # str | A unique value identifying this task info.

    try:
        api_response = api_instance.get_task(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_task_log**

    def get_task_log(id) -> TaskLog 



### Required permissions    * User account permission: `tasks:view` 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 'id_example' # str | A unique value identifying this task info.

    try:
        api_response = api_instance.get_task_log(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_task_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. | 

### Return type

[**TaskLog**](TaskLog.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_task_type**

    def get_task_type(type) -> TaskType 



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
    api_instance = elements_sdk.AutomationApi(api_client)
    type = 'type_example' # str | 

    try:
        api_response = api_instance.get_task_type(type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_task_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**TaskType**](TaskType.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_tasks_summary**

    def get_tasks_summary(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset) -> TasksSummary 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    job_instance = 'job_instance_example' # str | Filter the returned list by `job_instance`. (optional)
job_instance__in = 'job_instance__in_example' # str | Multiple values may be separated by commas. (optional)
subtask = 'subtask_example' # str | Filter the returned list by `subtask`. (optional)
state = 'state_example' # str | Filter the returned list by `state`. (optional)
state__in = 3.4 # float | Multiple values may be separated by commas. (optional)
id = 'id_example' # str | Filter the returned list by `id`. (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
task_name = 'task_name_example' # str | Filter the returned list by `task_name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_tasks_summary(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->get_tasks_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional] 
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **subtask** | **str**| Filter the returned list by &#x60;subtask&#x60;. | [optional] 
 **state** | **str**| Filter the returned list by &#x60;state&#x60;. | [optional] 
 **state__in** | **float**| Multiple values may be separated by commas. | [optional] 
 **id** | **str**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **task_name** | **str**| Filter the returned list by &#x60;task_name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**TasksSummary**](TasksSummary.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **import_job**

    def import_job(import_job_request) -> ImportJobResponse 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    import_job_request = elements_sdk.ImportJobRequest() # ImportJobRequest | 

    try:
        api_response = api_instance.import_job(import_job_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->import_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_job_request** | [**ImportJobRequest**](ImportJobRequest.md)|  | 

### Return type

[**ImportJobResponse**](ImportJobResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **kill_all_pending_tasks**

    def kill_all_pending_tasks()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    
    try:
        api_instance.kill_all_pending_tasks()
    except ApiException as e:
        print("Exception when calling AutomationApi->kill_all_pending_tasks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **kill_task**

    def kill_task(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 'id_example' # str | A unique value identifying this task info.

    try:
        api_instance.kill_task(id)
    except ApiException as e:
        print("Exception when calling AutomationApi->kill_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_job**

    def patch_job(id, job_partial_update) -> Job 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this job.
job_partial_update = elements_sdk.JobPartialUpdate() # JobPartialUpdate | 

    try:
        api_response = api_instance.patch_job(id, job_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->patch_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. | 
 **job_partial_update** | [**JobPartialUpdate**](JobPartialUpdate.md)|  | 

### Return type

[**Job**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_schedule**

    def patch_schedule(id, schedule_partial_update) -> Schedule 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this schedule.
schedule_partial_update = elements_sdk.SchedulePartialUpdate() # SchedulePartialUpdate | 

    try:
        api_response = api_instance.patch_schedule(id, schedule_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->patch_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this schedule. | 
 **schedule_partial_update** | [**SchedulePartialUpdate**](SchedulePartialUpdate.md)|  | 

### Return type

[**Schedule**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_subtask**

    def patch_subtask(id, subtask_partial_update) -> Subtask 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this subtask.
subtask_partial_update = elements_sdk.SubtaskPartialUpdate() # SubtaskPartialUpdate | 

    try:
        api_response = api_instance.patch_subtask(id, subtask_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->patch_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subtask. | 
 **subtask_partial_update** | [**SubtaskPartialUpdate**](SubtaskPartialUpdate.md)|  | 

### Return type

[**Subtask**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **restart_task**

    def restart_task(id) -> TaskInfo 



### Required permissions    * User account permission: `tasks:manage` 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 'id_example' # str | A unique value identifying this task info.

    try:
        api_response = api_instance.restart_task(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->restart_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_job**

    def start_job(id, start_job_request) -> list[TaskInfo] 



### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this job.
start_job_request = elements_sdk.StartJobRequest() # StartJobRequest | 

    try:
        api_response = api_instance.start_job(id, start_job_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->start_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. | 
 **start_job_request** | [**StartJobRequest**](StartJobRequest.md)|  | 

### Return type

[**list[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_task**

    def start_task(start_task_request) -> TaskInfo 



### Required permissions    * User account permission: `tasks:manage` 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    start_task_request = elements_sdk.StartTaskRequest() # StartTaskRequest | 

    try:
        api_response = api_instance.start_task(start_task_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->start_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_task_request** | [**StartTaskRequest**](StartTaskRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_job**

    def update_job(id, job) -> Job 



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this job.
job = elements_sdk.Job() # Job | 

    try:
        api_response = api_instance.update_job(id, job)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->update_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. | 
 **job** | [**Job**](Job.md)|  | 

### Return type

[**Job**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_schedule**

    def update_schedule(id, schedule) -> Schedule 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this schedule.
schedule = elements_sdk.Schedule() # Schedule | 

    try:
        api_response = api_instance.update_schedule(id, schedule)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->update_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this schedule. | 
 **schedule** | [**Schedule**](Schedule.md)|  | 

### Return type

[**Schedule**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_subtask**

    def update_subtask(id, subtask) -> Subtask 



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example

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
    api_instance = elements_sdk.AutomationApi(api_client)
    id = 56 # int | A unique integer value identifying this subtask.
subtask = elements_sdk.Subtask() # Subtask | 

    try:
        api_response = api_instance.update_subtask(id, subtask)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomationApi->update_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subtask. | 
 **subtask** | [**Subtask**](Subtask.md)|  | 

### Return type

[**Subtask**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

