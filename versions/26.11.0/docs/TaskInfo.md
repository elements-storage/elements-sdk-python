# TaskInfo

A record of a background (Automation) task, tracking its state, progress, timing, worker and result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | [readonly] 
**kwargs** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [readonly] 
**outputs** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [readonly] 
**subtask** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**worker** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**user** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**workstation** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**is_running** | **bool** | True when the task is in one of the following states: RUNNING (1), ABORTING (3). | [readonly] 
**is_finished** | **bool** | True when the task is in one of the following states: FINISHED (2), ABORTED (4), FAILED (5), WARNINGS (6), NOOP (7). | [readonly] 
**name** | **str, none_type** |  | 
**task_name** | **str, none_type** |  | 
**is_private** | **bool** | Private tasks are internal and hidden from the user-facing task list. | 
**worker_name** | **str, none_type** |  | 
**queue** | **str, none_type** | Name of the worker queue the task is assigned to. | 
**state** | **int** |  | 
**state_text** | **str, none_type** | Human-readable status or progress message for the current state. | 
**job_instance** | **str, none_type** | Groups tasks spawned by the same job execution | 
**started** | **datetime** |  | [readonly] 
**exception** | **str, none_type** | Error message if the task failed. | 
**traceback** | **str, none_type** | Python traceback captured if the task raised an unhandled error. | 
**related_bundle_id** | **int, none_type** | ID of the Media Library file bundle this task relates to, if any. | 
**related_proxy_id** | **int, none_type** | ID of the proxy this task relates to, if any. | 
**schedule** | **int, none_type** |  | 
**finished** | **datetime, none_type** |  | [optional] [readonly] 
**progress** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


