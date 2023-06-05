# elements_sdk.AutomationApi



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
[**get_task_log_v2**](AutomationApi.md#get_task_log_v2) | **GET** `/api/2/tasks/{id}/log-v2` | 
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


# **abort_task**
    def abort_task(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | A unique value identifying this task info.

    # example passing only required values which don't have defaults set
    try:
        api_instance.abort_task(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->abort_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_job**
    def Job create_job(job_update)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.job_update import JobUpdate
from elements_sdk.model.job import Job
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    job_update = JobUpdate(
        subtasks=[
            SubtaskReference(
                id=1,
            ),
        ],
        schedules=[
            ScheduleReference(
                id=1,
            ),
        ],
        allow_users=[
            ElementsUserReference(
                id=1,
            ),
        ],
        allow_groups=[
            ElementsGroupReference(
                id=1,
            ),
        ],
        variable_definitions=[
            {
                "key": "key_example",
            },
        ],
        media_roots=[
            1,
        ],
        special_type=2,
        name="name_example",
        description="description_example",
        enabled=True,
        allow_others_to_start=True,
        allow_client_to_start=True,
        show_as_button=True,
        input_type="path",
        hook="hook_example",
        webhook_secret="webhook_secret_example",
        security_context=1,
        part_of_workflow_for=1,
    ) # JobUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_job(job_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->create_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_update** | [**JobUpdate**](JobUpdate.md)|  |

### Return type

[**Job**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_schedule**
    def Schedule create_schedule(schedule_update)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.schedule import Schedule
from elements_sdk.model.schedule_update import ScheduleUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    schedule_update = ScheduleUpdate(
        variables={
            "key": "key_example",
        },
        type=1,
        enabled=True,
        last_run=dateutil_parser('1970-01-01T00:00:00.00Z'),
        every=-2147483648,
        period="minutes",
        crontab_day_of_month="crontab_day_of_month_example",
        crontab_day_of_week="crontab_day_of_week_example",
        crontab_hour="crontab_hour_example",
        crontab_minute="crontab_minute_example",
        crontab_month_of_year="crontab_month_of_year_example",
        job=1,
    ) # ScheduleUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_schedule(schedule_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->create_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_update** | [**ScheduleUpdate**](ScheduleUpdate.md)|  |

### Return type

[**Schedule**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_subtask**
    def Subtask create_subtask(subtask_update)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.subtask import Subtask
from elements_sdk.model.subtask_update import SubtaskUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    subtask_update = SubtaskUpdate(
        kwargs={
            "key": "key_example",
        },
        graph_layout={
            "key": "key_example",
        },
        trigger="trigger_example",
        name="name_example",
        noop_dont_save=True,
        no_concurrency=True,
        timeout=-2147483648,
        log_variable=True,
        task="task_example",
        condition_variable="condition_variable_example",
        condition_value="condition_value_example",
        sync=True,
        queue="queue_example",
        enqueue_at_front=True,
        parent=1,
        relative_to=1,
    ) # SubtaskUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_subtask(subtask_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->create_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subtask_update** | [**SubtaskUpdate**](SubtaskUpdate.md)|  |

### Return type

[**Subtask**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_finished_tasks**
    def delete_finished_tasks()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.delete_finished_tasks()
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->delete_finished_tasks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_job**
    def delete_job(id)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this job.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_job(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->delete_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_schedule**
    def delete_schedule(id)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this schedule.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_schedule(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->delete_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this schedule. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_subtask**
    def delete_subtask(id)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this subtask.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_subtask(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->delete_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subtask. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_task**
    def delete_task(id)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | A unique value identifying this task info.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_task(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->delete_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **download_all_task_logs**
    def download_all_task_logs()



### Required permissions    * User account permission: `tasks:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    job_instance = "job_instance_example" # str | Filter the returned list by `job_instance`. (optional)
    job_instance__in = "job_instance__in_example" # str | Multiple values may be separated by commas. (optional)
    subtask = 1 # int | Filter the returned list by `subtask`. (optional)
    state = "state_example" # str | Filter the returned list by `state`. (optional)
    state__in = 3.14 # float | Multiple values may be separated by commas. (optional)
    id = "id_example" # str | Filter the returned list by `id`. (optional)
    id__in = "id__in_example" # str | Multiple values may be separated by commas. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    task_name = "task_name_example" # str | Filter the returned list by `task_name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.download_all_task_logs(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->download_all_task_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional]
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional]
 **subtask** | **int**| Filter the returned list by &#x60;subtask&#x60;. | [optional]
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

# **download_task_log**
    def download_task_log(id)



### Required permissions    * User account permission: `tasks:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | A unique value identifying this task info.

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_task_log(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->download_task_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_job**
    def export_job(id)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this job.

    # example passing only required values which don't have defaults set
    try:
        api_instance.export_job(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->export_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_events**
    def [Event] get_all_events()



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.event import Event
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_events(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_all_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Event]**](Event.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_jobs**
    def [Job] get_all_jobs()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.job import Job
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    special_type = "special_type_example" # str | Filter the returned list by `special_type`. (optional)
    special_type__isnull = "special_type__isnull_example" # str | Filter the returned list by `special_type__isnull`. (optional)
    hook = "hook_example" # str | Filter the returned list by `hook`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_jobs(special_type=special_type, special_type__isnull=special_type__isnull, hook=hook, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

[**[Job]**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_schedules**
    def [Schedule] get_all_schedules()



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.schedule import Schedule
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    job = 1 # int | Filter the returned list by `job`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_schedules(job=job, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_all_schedules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **int**| Filter the returned list by &#x60;job&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Schedule]**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_subtasks**
    def [Subtask] get_all_subtasks()



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.subtask import Subtask
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    parent = 1 # int | Filter the returned list by `parent`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_subtasks(parent=parent, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_all_subtasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **int**| Filter the returned list by &#x60;parent&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Subtask]**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_task_queues**
    def [Queue] get_all_task_queues()



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.queue import Queue
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_task_queues(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_all_task_queues: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Queue]**](Queue.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_task_types**
    def [TaskType] get_all_task_types()



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.task_type import TaskType
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_task_types(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_all_task_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[TaskType]**](TaskType.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_tasks**
    def [TaskInfo] get_all_tasks()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
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
    api_instance = automation_api.AutomationApi(api_client)
    job_instance = "job_instance_example" # str | Filter the returned list by `job_instance`. (optional)
    job_instance__in = "job_instance__in_example" # str | Multiple values may be separated by commas. (optional)
    subtask = 1 # int | Filter the returned list by `subtask`. (optional)
    state = "state_example" # str | Filter the returned list by `state`. (optional)
    state__in = 3.14 # float | Multiple values may be separated by commas. (optional)
    id = "id_example" # str | Filter the returned list by `id`. (optional)
    id__in = "id__in_example" # str | Multiple values may be separated by commas. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    task_name = "task_name_example" # str | Filter the returned list by `task_name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    include_kwargs = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset, include_kwargs=include_kwargs)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_all_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional]
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional]
 **subtask** | **int**| Filter the returned list by &#x60;subtask&#x60;. | [optional]
 **state** | **str**| Filter the returned list by &#x60;state&#x60;. | [optional]
 **state__in** | **float**| Multiple values may be separated by commas. | [optional]
 **id** | **str**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **id__in** | **str**| Multiple values may be separated by commas. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **task_name** | **str**| Filter the returned list by &#x60;task_name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **include_kwargs** | **bool**|  | [optional]

### Return type

[**[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_event**
    def Event get_event(id)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.event import Event
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_event(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Event**](Event.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_finished_tasks**
    def [TaskInfo] get_finished_tasks()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
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
    api_instance = automation_api.AutomationApi(api_client)
    job_instance = "job_instance_example" # str | Filter the returned list by `job_instance`. (optional)
    job_instance__in = "job_instance__in_example" # str | Multiple values may be separated by commas. (optional)
    subtask = 1 # int | Filter the returned list by `subtask`. (optional)
    state = "state_example" # str | Filter the returned list by `state`. (optional)
    state__in = 3.14 # float | Multiple values may be separated by commas. (optional)
    id = "id_example" # str | Filter the returned list by `id`. (optional)
    id__in = "id__in_example" # str | Multiple values may be separated by commas. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    task_name = "task_name_example" # str | Filter the returned list by `task_name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_finished_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_finished_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional]
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional]
 **subtask** | **int**| Filter the returned list by &#x60;subtask&#x60;. | [optional]
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

[**[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_job**
    def Job get_job(id)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.job import Job
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this job.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_job(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. |

### Return type

[**Job**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_pending_tasks**
    def [TaskInfo] get_pending_tasks()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
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
    api_instance = automation_api.AutomationApi(api_client)
    job_instance = "job_instance_example" # str | Filter the returned list by `job_instance`. (optional)
    job_instance__in = "job_instance__in_example" # str | Multiple values may be separated by commas. (optional)
    subtask = 1 # int | Filter the returned list by `subtask`. (optional)
    state = "state_example" # str | Filter the returned list by `state`. (optional)
    state__in = 3.14 # float | Multiple values may be separated by commas. (optional)
    id = "id_example" # str | Filter the returned list by `id`. (optional)
    id__in = "id__in_example" # str | Multiple values may be separated by commas. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    task_name = "task_name_example" # str | Filter the returned list by `task_name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_pending_tasks(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_pending_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional]
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional]
 **subtask** | **int**| Filter the returned list by &#x60;subtask&#x60;. | [optional]
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

[**[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_python_environments**
    def [PythonEnvironment] get_python_environments()



### Required permissions    * User account permission: `tasks:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.python_environment import PythonEnvironment
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_python_environments()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_python_environments: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[PythonEnvironment]**](PythonEnvironment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_schedule**
    def Schedule get_schedule(id)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.schedule import Schedule
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this schedule.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_schedule(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this schedule. |

### Return type

[**Schedule**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_subtask**
    def Subtask get_subtask(id)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.subtask import Subtask
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this subtask.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_subtask(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subtask. |

### Return type

[**Subtask**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_task**
    def TaskInfo get_task(id)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | A unique value identifying this task info.
    include_kwargs = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_task(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_task: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_task(id, include_kwargs=include_kwargs)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. |
 **include_kwargs** | **bool**|  | [optional]

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_task_log**
    def TaskLog get_task_log(id)



### Required permissions    * User account permission: `tasks:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.task_log import TaskLog
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | A unique value identifying this task info.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_task_log(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_task_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. |

### Return type

[**TaskLog**](TaskLog.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_task_log_v2**
    def TaskLogV2 get_task_log_v2(id)



### Required permissions    * User account permission: `tasks:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | A unique value identifying this task info.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_task_log_v2(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_task_log_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. |

### Return type

[**TaskLogV2**](TaskLogV2.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_task_type**
    def TaskType get_task_type(type)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.task_type import TaskType
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    type = "o" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_task_type(type)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_task_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  |

### Return type

[**TaskType**](TaskType.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_tasks_summary**
    def TasksSummary get_tasks_summary()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.tasks_summary import TasksSummary
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    job_instance = "job_instance_example" # str | Filter the returned list by `job_instance`. (optional)
    job_instance__in = "job_instance__in_example" # str | Multiple values may be separated by commas. (optional)
    subtask = 1 # int | Filter the returned list by `subtask`. (optional)
    state = "state_example" # str | Filter the returned list by `state`. (optional)
    state__in = 3.14 # float | Multiple values may be separated by commas. (optional)
    id = "id_example" # str | Filter the returned list by `id`. (optional)
    id__in = "id__in_example" # str | Multiple values may be separated by commas. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    task_name = "task_name_example" # str | Filter the returned list by `task_name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_tasks_summary(job_instance=job_instance, job_instance__in=job_instance__in, subtask=subtask, state=state, state__in=state__in, id=id, id__in=id__in, name=name, task_name=task_name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->get_tasks_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | **str**| Filter the returned list by &#x60;job_instance&#x60;. | [optional]
 **job_instance__in** | **str**| Multiple values may be separated by commas. | [optional]
 **subtask** | **int**| Filter the returned list by &#x60;subtask&#x60;. | [optional]
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

# **import_job**
    def ImportJobResponse import_job(import_job_request)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.import_job_request import ImportJobRequest
from elements_sdk.model.import_job_response import ImportJobResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    import_job_request = ImportJobRequest(
        content="content_example",
        replace=True,
        rename="rename_example",
    ) # ImportJobRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.import_job(import_job_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->import_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_job_request** | [**ImportJobRequest**](ImportJobRequest.md)|  |

### Return type

[**ImportJobResponse**](ImportJobResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **kill_all_pending_tasks**
    def kill_all_pending_tasks()



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.kill_all_pending_tasks()
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->kill_all_pending_tasks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **kill_task**
    def kill_task(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | A unique value identifying this task info.

    # example passing only required values which don't have defaults set
    try:
        api_instance.kill_task(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->kill_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_job**
    def Job patch_job(id, job_partial_update)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.job_partial_update import JobPartialUpdate
from elements_sdk.model.job import Job
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this job.
    job_partial_update = JobPartialUpdate(
        subtasks=[
            SubtaskReference(
                id=1,
            ),
        ],
        schedules=[
            ScheduleReference(
                id=1,
            ),
        ],
        allow_users=[
            ElementsUserReference(
                id=1,
            ),
        ],
        allow_groups=[
            ElementsGroupReference(
                id=1,
            ),
        ],
        variable_definitions=[
            {
                "key": "key_example",
            },
        ],
        media_roots=[
            1,
        ],
        special_type=2,
        name="name_example",
        description="description_example",
        enabled=True,
        allow_others_to_start=True,
        allow_client_to_start=True,
        show_as_button=True,
        input_type="path",
        hook="hook_example",
        webhook_secret="webhook_secret_example",
        security_context=1,
        part_of_workflow_for=1,
    ) # JobPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_job(id, job_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **patch_schedule**
    def Schedule patch_schedule(id, schedule_partial_update)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.schedule import Schedule
from elements_sdk.model.schedule_partial_update import SchedulePartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this schedule.
    schedule_partial_update = SchedulePartialUpdate(
        variables={
            "key": "key_example",
        },
        type=1,
        enabled=True,
        last_run=dateutil_parser('1970-01-01T00:00:00.00Z'),
        every=-2147483648,
        period="minutes",
        crontab_day_of_month="crontab_day_of_month_example",
        crontab_day_of_week="crontab_day_of_week_example",
        crontab_hour="crontab_hour_example",
        crontab_minute="crontab_minute_example",
        crontab_month_of_year="crontab_month_of_year_example",
        job=1,
    ) # SchedulePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_schedule(id, schedule_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **patch_subtask**
    def Subtask patch_subtask(id, subtask_partial_update)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.subtask import Subtask
from elements_sdk.model.subtask_partial_update import SubtaskPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this subtask.
    subtask_partial_update = SubtaskPartialUpdate(
        kwargs={
            "key": "key_example",
        },
        graph_layout={
            "key": "key_example",
        },
        trigger="trigger_example",
        name="name_example",
        noop_dont_save=True,
        no_concurrency=True,
        timeout=-2147483648,
        log_variable=True,
        task="task_example",
        condition_variable="condition_variable_example",
        condition_value="condition_value_example",
        sync=True,
        queue="queue_example",
        enqueue_at_front=True,
        parent=1,
        relative_to=1,
    ) # SubtaskPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_subtask(id, subtask_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

# **restart_task**
    def TaskInfo restart_task(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | A unique value identifying this task info.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.restart_task(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->restart_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this task info. |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_job**
    def [TaskInfo] start_job(id, start_job_request)



### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.start_job_request import StartJobRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this job.
    start_job_request = StartJobRequest(
        variables={
            "key": "key_example",
        },
        secret="secret_example",
    ) # StartJobRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.start_job(id, start_job_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->start_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. |
 **start_job_request** | [**StartJobRequest**](StartJobRequest.md)|  |

### Return type

[**[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_task**
    def TaskInfo start_task(start_task_request)



### Required permissions    * User account permission: `tasks:manage` 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.start_task_request import StartTaskRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    start_task_request = StartTaskRequest(
        task_type="task_type_example",
        parameters={
            "key": "key_example",
        },
        sync=False,
    ) # StartTaskRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.start_task(start_task_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->start_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_task_request** | [**StartTaskRequest**](StartTaskRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_job**
    def Job update_job(id, job_update)



### Required permissions    * User account permission: `None` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.job_update import JobUpdate
from elements_sdk.model.job import Job
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this job.
    job_update = JobUpdate(
        subtasks=[
            SubtaskReference(
                id=1,
            ),
        ],
        schedules=[
            ScheduleReference(
                id=1,
            ),
        ],
        allow_users=[
            ElementsUserReference(
                id=1,
            ),
        ],
        allow_groups=[
            ElementsGroupReference(
                id=1,
            ),
        ],
        variable_definitions=[
            {
                "key": "key_example",
            },
        ],
        media_roots=[
            1,
        ],
        special_type=2,
        name="name_example",
        description="description_example",
        enabled=True,
        allow_others_to_start=True,
        allow_client_to_start=True,
        show_as_button=True,
        input_type="path",
        hook="hook_example",
        webhook_secret="webhook_secret_example",
        security_context=1,
        part_of_workflow_for=1,
    ) # JobUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_job(id, job_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->update_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job. |
 **job_update** | [**JobUpdate**](JobUpdate.md)|  |

### Return type

[**Job**](Job.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_schedule**
    def Schedule update_schedule(id, schedule_update)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.schedule import Schedule
from elements_sdk.model.schedule_update import ScheduleUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this schedule.
    schedule_update = ScheduleUpdate(
        variables={
            "key": "key_example",
        },
        type=1,
        enabled=True,
        last_run=dateutil_parser('1970-01-01T00:00:00.00Z'),
        every=-2147483648,
        period="minutes",
        crontab_day_of_month="crontab_day_of_month_example",
        crontab_day_of_week="crontab_day_of_week_example",
        crontab_hour="crontab_hour_example",
        crontab_minute="crontab_minute_example",
        crontab_month_of_year="crontab_month_of_year_example",
        job=1,
    ) # ScheduleUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_schedule(id, schedule_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->update_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this schedule. |
 **schedule_update** | [**ScheduleUpdate**](ScheduleUpdate.md)|  |

### Return type

[**Schedule**](Schedule.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_subtask**
    def Subtask update_subtask(id, subtask_update)



### Required permissions    * User account permission: `tasks:view` (read) / `tasks:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import automation_api
from elements_sdk.model.subtask import Subtask
from elements_sdk.model.subtask_update import SubtaskUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = automation_api.AutomationApi(api_client)
    id = 1 # int | A unique integer value identifying this subtask.
    subtask_update = SubtaskUpdate(
        kwargs={
            "key": "key_example",
        },
        graph_layout={
            "key": "key_example",
        },
        trigger="trigger_example",
        name="name_example",
        noop_dont_save=True,
        no_concurrency=True,
        timeout=-2147483648,
        log_variable=True,
        task="task_example",
        condition_variable="condition_variable_example",
        condition_value="condition_value_example",
        sync=True,
        queue="queue_example",
        enqueue_at_front=True,
        parent=1,
        relative_to=1,
    ) # SubtaskUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_subtask(id, subtask_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AutomationApi->update_subtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subtask. |
 **subtask_update** | [**SubtaskUpdate**](SubtaskUpdate.md)|  |

### Return type

[**Subtask**](Subtask.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

